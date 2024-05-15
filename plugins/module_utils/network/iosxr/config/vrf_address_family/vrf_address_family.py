#
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr_vrf_address_family config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""
import q
from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import (
    Facts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.vrf_address_family import (
    Vrf_address_familyTemplate,
)


class Vrf_address_family(ResourceModule):
    """
    The iosxr_vrf_address_family config class
    """

    def __init__(self, module):
        super(Vrf_address_family, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="vrf_address_family",
            tmplt=Vrf_address_familyTemplate(),
        )
        self.parsers = [
            "address_family",
            "export.route_policy",
            "export.route_target",
            "export.to.default_vrf.route_policy",
            "export.to.vrf.allow_imported_vpn",
            "import_config.route_target",
            "import_config.route_policy",
            "import_config.from_config.bridge_domain.advertise_as_vpn",
            "import_config.from_config.default_vrf.route_policy",
            "import_config.from_config.vrf.advertise_as_vpn",
            "maximum.prefix",
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
        wantd = self.want
        haved = self.have

        wantd = self._vrf_list_to_dict(wantd)
        haved = self._vrf_list_to_dict(haved)

        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            to_del = {"address_families": self._set_to_delete(haved, wantd)}
            haved.update(to_del)

            wantd = {"name": haved.get("name")}

        self._compare(want=wantd, have=haved)

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Vrf_address_family network resource.
        """
        self._compare_vrf(want=want, have=have)

    def _compare_vrf(self, want, have):
        """Custom handling of vrfs option
        :params want: the want VRF dictionary
        :params have: the have VRF dictionary
        """

        for name, entry in iteritems(want):
            begin = len(self.commands)
            vrf_have = have.pop(name, {})

            self.compare(parsers=self.parsers, want=entry, have=vrf_have)
            self._compare_af(entry, vrf_have)
            if len(self.commands) != begin:
                self.commands.insert(begin, "vrf {0}".format(name))

        # for deleted and overridden state
        if self.state != "replaced":
            begin = len(self.commands)
            for name, entry in iteritems(have):
                self.commands.insert(begin, "no vrf {0}".format(name))

    def _compare_af(self, want, have):
        """Custom handling of afs option
        :params want: the want VRF dictionary
        :params have: the have VRF dictionary
        """
        wafs = want.get("address_families", {})
        hafs = have.get("address_families", {})
        for name, entry in iteritems(wafs):
            begin = len(self.commands)
            af_have = hafs.pop(name, {})

            self.compare(parsers=self.parsers, want=entry, have=af_have)
            if len(self.commands) != begin:
                self.commands.insert(
                    begin,
                    self._tmplt.render(
                        {
                            "afi": entry.get("afi"),
                            "safi": entry.get("safi"),
                        },
                        "address_family",
                        False,
                    ),
                )

        # for deleted and overridden state
        if self.state != "replaced":
            for name, entry in iteritems(hafs):
                self.addcmd(
                    {"afi": entry.get("afi"), "safi": entry.get("safi")},
                    "address_family",
                    True,
                )

    def _vrf_list_to_dict(self, entry):
        """Convert list of items to dict of items
           for efficient diff calculation.
        :params entry: data dictionary
        """

        for vrf in entry:
            if "address_families" in vrf:
                vrf["address_families"] = {
                    (x["afi"], x.get("safi")): x for x in vrf["address_families"]
                }

        entry = {x["name"]: x for x in entry}
        return entry

    def _get_config(self):
        return self._connection.get("show running-config vrf")

    def _set_to_delete(self, haved, wantd):
        afs_to_del = {}
        h_addrs = haved.get("address_families", {})
        w_addrs = wantd.get("address_families", {})
        for af, h_addr in iteritems(h_addrs):
            if af in w_addrs:
                afs_to_del[af] = h_addr
        return afs_to_del
