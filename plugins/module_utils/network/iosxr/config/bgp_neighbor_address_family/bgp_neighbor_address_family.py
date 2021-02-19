#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr_bgp_neighbor_address_family config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module import (
    ResourceModule,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import (
    Facts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.bgp_neighbor_address_family import (
    Bgp_neighbor_address_familyTemplate,
)


class Bgp_neighbor_address_family(ResourceModule):
    """
    The iosxr_bgp_neighbor_address_family config class
    """

    def __init__(self, module):
        super(Bgp_neighbor_address_family, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="bgp_neighbor_address_family",
            tmplt=Bgp_neighbor_address_familyTemplate(),
        )
        self.parsers = [
            "router",
            "aigp",
            "allowas_in",
            "as_override",
            "bestpath_origin_as_allow_invalid",
            "capability_orf_prefix",
            "default_originate",
            "long_lived_graceful_restart_capable",
            "long_lived_graceful_restart_stale_time",
            "maximum_prefix",
            "multipath",
            "next_hop_self",
            "next_hop_unchanged",
            "optimal_route_reflection_group_name",
            "origin_as",
            "remove_private_AS",
            "route_reflector_client",
            "send_community_ebgp",
            "send_community_gshut_ebgp",
            "send_extended_community_ebgp",
            "send_multicast_attributes",
            "soft_reconfiguration",
            "weight",
            "site_of_origin",
            "validation"
        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            #import epdb; epdb.serve()
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
                    want, have and desired state.
                """

        for entry in self.want, self.have:
            self._bgp_list_to_dict(entry)

        # if state is deleted, clean up global params
        if self.state == "deleted":
            if not self.want or (
                    self.have.get("as_number") == self.want.get("as_number")
            ):
                self._compare(
                    want={"as_number": self.want.get("as_number")},
                    have=self.have,
                )

        else:
            wantd = self.want
            # if state is merged, merge want onto have and then compare
            # import epdb;epdb.serve()
            if self.state == "merged":
                wantd = dict_merge(self.have, self.want)

            self._compare(want=wantd, have=self.have)

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Bgp_global network resource.
        """

        self._compare_neighbors(want=want, have=have)
        if self.commands and "router bgp" not in self.commands[0]:
            self.commands.insert(
                0,
                self._tmplt.render(
                    {"as_number": want["as_number"]}, "router", False
                ),
            )

    def _compare_neighbors(self, want, have):
        """Leverages the base class `compare()` method and
                   populates the list of commands to be run by comparing
                   the `want` and `have` data with the `parsers` defined
                   for the Bgp_global neighbor resource.
                """
        want_nbr = want.get("neighbors", {})
        have_nbr = have.get("neighbors", {})
        vrf_want_have = []
        for name, entry in iteritems(want_nbr):
            have = have_nbr.pop(name, {})
            neighbor_address = entry.get("neighbor", "")
            self._compare_af(neighbor_address, want=entry, have=have)


        # for deleted and overridden state
        if self.state != "replaced":
            for name, entry in iteritems(have_nbr):
                neighbor_address = entry.get("neighbor", "")
                self._compare_af(neighbor_address, want={}, have=entry)

    def _compare_af(self, neighbor_address, want, have):
        """Custom handling of afs option
               :params want: the want BGP dictionary
               :params have: the have BGP dictionary
        """
        wafs = want.get("address_family", {})
        hafs = have.get("address_family", {})
        vrf_want_have = []
        begin_nbr = len(self.commands)
        for name, entry in iteritems(wafs):
            #import epdb;epdb.serve()
            begin = len(self.commands)
            af_have = hafs.pop(name, {})
            if entry.get("vrf"):
                vrf_want_have.append((entry, af_have))
            else:
                self.compare(parsers=self.parsers, want=entry, have=af_have)
                if len(self.commands) != begin:
                    self.commands.insert(
                        begin,
                        self._tmplt.render(
                            {"afi": entry.get("afi"), "safi": entry.get("safi")}, "address_family", False
                        ),
                    )
        if len(self.commands) != begin_nbr:
            self.commands.insert(
                begin_nbr,
                self._tmplt.render(
                    {"neighbor": neighbor_address}, "neighbor", False
                ),
        )
            # compare af under vrf separately to ensure correct generation of commands
        for waf, haf in vrf_want_have:
            begin = len(self.commands)
            self.compare(parsers=self.parsers, want=waf, have=haf)
            if len(self.commands) != begin:
                self.commands.insert(
                    begin,
                    self._tmplt.render(
                        {
                            "afi": waf.get("afi"),
                            "safi": waf.get("safi"),
                        },
                        "address_family", False,
                    ),
                )
                self.commands.insert(
                    begin,
                    self._tmplt.render(
                        {"neighbor": neighbor_address}, "neighbor", False),
                    ),
                self.commands.insert(
                     begin,
                    self._tmplt.render({"vrf": waf.get("vrf")}, "vrf", False),
                )

            # for deleted and overridden state
        if self.state != "replaced":
            for name, entry in iteritems(hafs):
                if "vrf" in entry:
                    self.addcmd({"vrf": entry.get("vrf")}, "vrf", False)
                self.addcmd({"neighbor": neighbor_address}, "neighbor", False)
                self.addcmd(
                    {
                        "afi": entry.get("afi"),
                        "safi": entry.get("safi"),
                     },
                    "address_family",
                    True,
                )

    def _bgp_list_to_dict(self, entry):
        """Convert list of items to dict of items
           for efficient diff calculation.
        :params entry: data dictionary
        """

        if "neighbors" in entry:
            entry["neighbors"] = {
                x["neighbor"]: x for x in entry.get("neighbors", [])
            }
            for neighbor, value in iteritems(entry["neighbors"]):
                if "address_family" in value:
                    entry["neighbors"][neighbor]["address_family"] = {
                        "address_family_" + x["afi"] + "_" + x["safi"] +"_vrf_" +x.get("vrf", ""): x for x in value.get("address_family", [])
                    }