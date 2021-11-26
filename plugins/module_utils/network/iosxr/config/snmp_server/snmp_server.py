#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr_snmp_server config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
    dict_diff,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import (
    Facts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.snmp_server import (
    Snmp_serverTemplate,
)


class Snmp_server(ResourceModule):
    """
    The iosxr_snmp_server config class
    """

    def __init__(self, module):
        super(Snmp_server, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="snmp_server",
            tmplt=Snmp_serverTemplate(),
        )
        self.parsers = [
            "chassis_id",
            "correlator.buffer_size",
            "contact",
            "ifindex",
            "ipv4.dscp",
            "ipv6.dscp",
            "ipv4.precedence",
            "ipv6.precedence",
            "location",
            "logging_threshold_oid_processing",
            "logging_threshold_pdu_processing",
            "mib_bulkstat_max_procmem_size",
            "mroutemib_send_all_vrf",
            "oid_poll_stats",
            "overload_control",
            "packetsize",
            "queue_length",
            "throttle_time",
            "trap_source",
            "trap_timeout",
        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """
        wantd = self.list_to_dict(self.want)
        haved = self.list_to_dict(self.have)

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            wantd = {}

        self._compare(want=wantd, have=haved)
        if self.state in ["overridden", "replaced"]:
            self.commands = [
                each for each in self.commands if "no" in each
            ] + [each for each in self.commands if "no" not in each]

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Logging_global network resource.
        """
        self.compare(parsers=self.parsers, want=want, have=have)
        self._compare_lists(want, have)
        self._compare_complex_dict(want, have)
        self._compare_vrfs(want, have)

    def _remove_snmp_server(self, begin):
        for i in range(begin, len(self.commands)):
            self.commands[i] = self.commands[i].replace("snmp-server ", "")

    def _compare_vrfs(self, want, have):
        wvrfs = want.get("vrfs", {})
        hvrfs = have.get("vrfs", {})
        for name, entry in iteritems(wvrfs):
            begin = len(self.commands)
            vrf_have = hvrfs.pop(name, {})
            self._compare_lists(want=entry, have=vrf_have)
            if len(self.commands) != begin:
                self._remove_snmp_server(begin)
                self.commands.insert(
                    begin,
                    self._tmplt.render(
                        {"vrf": entry.get("vrf")}, "vrfs", False
                    ),
                )
        # cleanup remaining VRFs
        # but do not negate it entirely
        # instead remove only those attributes
        # that this module manages
        for name, entry in iteritems(hvrfs):
            self.addcmd(entry, "vrfs", True)

    def _compare_complex_dict(self, want, have):
        """
            Handles dict attributes from config_data
        """
        for x in [
            "inform",
            "ifmib",
            "drop",
            "traps",
            "notification_log_mib",
            "timeouts",
            "trap",
        ]:
            wantx = want.get(x, {})
            havex = have.get(x, {})
            updates = dict_diff(havex, wantx)
            updates = {x: updates}
            self.addcmd(updates, x)

            if havex:
                self.addcmd({x: havex}, x, negate=True)

    def _compare_lists(self, want, have):
        """
            Handles list attributes from config_data
        """
        for x in [
            "community",
            "community_map",
            "correlator.rule_sets",
            "correlator.rules",
            "context",
            "groups",
            "hosts",
            "interfaces",
            "mib_object_lists",
            "mib_schema",
            "mib_bulkstat_transfer_ids",
            "users",
            "targets",
        ]:

            wantx = want.get(x, {})
            havex = have.get(x, {})
            if "." in x:
                complex_parser = x.split(".")
                wantx = want.get(complex_parser[0], {}).get(
                    complex_parser[1], {}
                )
                havex = have.get(complex_parser[0], {}).get(
                    complex_parser[1], {}
                )

            if x in [
                "interfaces",
                "correlator.rules",
                "mib_schema",
                "mib_bulkstat_transfer_ids",
            ]:
                # handling complex parsers for replaced and overridden state

                for key, wentry in iteritems(wantx):
                    hentry = havex.pop(key, {})
                    updates = dict_diff(hentry, wentry)
                    if updates and x in [
                        "interfaces",
                        "mib_schema",
                        "mib_bulkstat_transfer_ids",
                    ]:
                        updates.update(name=wentry["name"])
                        self.addcmd(updates, x)
                    elif updates and x == "correlator.rules":
                        updates.update(rule_name=wentry["rule_name"])
                        self.addcmd(updates, x)
            else:
                for key, wentry in iteritems(wantx):
                    hentry = havex.pop(key, {})
                    if wentry != hentry:
                        self.addcmd(wentry, x)

            for key, hentry in iteritems(havex):
                self.addcmd(hentry, x, negate=True)

    def list_to_dict(self, config):

        data = deepcopy(config)

        if data.get("vrfs"):
            for x in data["vrfs"]:
                if "context" in x:
                    x["context"] = {y: {"name": y} for y in x["context"]}
                if "hosts" in x:
                    x["hosts"] = {
                        y["host"]
                        + y.get("version", "")
                        + y.get("community", ""): y
                        for y in x["hosts"]
                    }

        pkey = {
            "community": "name",
            "community_map": "name",
            "interfaces": "name",
            "mib_schema": "name",
            "groups": "group",
            "mib_bulkstat_transfer_ids": "name",
            "users": "user",
            "vrfs": "vrf",
        }
        for k in pkey.keys():
            if k in data:
                data[k] = {i[pkey[k]]: i for i in data[k]}

        if "correlator" in data:
            if "rules" in data["correlator"]:
                data["correlator"]["rules"] = {
                    x["rule_name"]: x for x in data["correlator"]["rules"]
                }
            if "rule_sets" in data["correlator"]:
                data["correlator"]["rule_sets"] = {
                    x["name"]: x for x in data["correlator"]["rule_sets"]
                }

        if "context" in data:
            data["context"] = {x: {"name": x} for x in data["context"]}
        if "mib_object_lists" in data:
            data["mib_object_lists"] = {
                x: {"mib_object": x} for x in data["mib_object_lists"]
            }
        if "targets" in data:
            data["targets"] = {
                x["name"] + x.get("vrf", "") + x.get("host", ""): x
                for x in data["targets"]
            }
        if "hosts" in data:
            data["hosts"] = {
                x["host"] + x.get("version", "") + x.get("community", ""): x
                for x in data["hosts"]
            }

        # if "hosts" in data:
        #     data["hosts"] = {x["host"]: x for x in data["hosts"]}
        # if "interfaces" in data:
        #     data["interfaces"] = {x["name"]: x for x in data["interfaces"]}
        # if "mib_object_lists" in data:
        #     data["mib_object_lists"] = {x: {"mib_object": x} for x in data["mib_object_lists"]}
        # if "mib_schema" in data:
        #     data["mib_schema"] = {x["name"]: x for x in data["mib_schema"]}
        # if "mib_bulkstat_transfer_ids" in data:
        #     data["mib_bulkstat_transfer_ids"] = {x["name"]: x for x in data["mib_bulkstat_transfer_ids"]}

        return data
