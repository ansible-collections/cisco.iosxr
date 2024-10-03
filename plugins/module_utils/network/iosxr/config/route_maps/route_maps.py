#
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The iosxr_route_maps config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
    ResourceModule,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import Facts
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.route_maps import (
    Route_mapsTemplate,
)


class Route_maps(ResourceModule):
    """
    The iosxr_route_maps config class
    """

    def __init__(self, module):
        super(Route_maps, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="route_maps",
            tmplt=Route_mapsTemplate(),
        )
        self.parsers = [
            "add.eigrp_metric",
            "add.rip_metric",
            "apply",
            "drop",
            "pass",
            "prepend",
            "suppress_route",
            "unsuppress_route",
            "remove",
            "set.administrative_distance",
            "set.aigp_metric",
            "set.attribute_set",
            "set.c_multicast_routing",
            "set.community",
            "set.core_tree",
            "set.dampening",
            "set.downstream_core_tree",
            "set.eigrp_metric",
            "set.fallback_vrf_lookup",
            "set.flow_tag",
            "set.forward_class",
            "set.ip_precedence",
            "set.isis_metric",
            "set.label",
            "set.label_index",
            "set.label_mode",
            "set.large_community",
            "set.level",
            "set.load_balance",
            "set.lsm_root",
            "set.metric_type",
            "set.mpls",
            "set.next_hop",
            "set.origin",
            "set.ospf_metric",
            "set.path_color",
            "set.qos_group",
            "set.rib_metric",
            "set.rip_metric",
            "set.rip_tag",
            "set.rt_set",
            "set.s_pmsi",
            "set.spf_priority",
            "set.static_p2mp_te",
            "set.tag",
            "set.traffic_index",
            "set.upstream_core_tree",
            "set.vpn_distinguisher",
            "set.weight",
        ]

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """Generate configuration commands to send based on
        want, have and desired state.
        """
        wantd = self._route_maps_list_to_dict(self.want)
        haved = self._route_maps_list_to_dict(self.have)
        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {k: v for k, v in iteritems(haved) if k in wantd or not wantd}
            wantd = {}

        # remove superfluous config for overridden and deleted
        if self.state in ["overridden", "deleted"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    self._compare(want={}, have=have, policy_name=k)

        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}), policy_name=k)

    def _compare(self, want, have, policy_name):
        """Leverages the base class `compare()` method and
        populates the list of commands to be run by comparing
        the `want` and `have` data with the `parsers` defined
        for the Route_maps network resource.
        """
        order_list = [
            "global",
            "if_",
            "elseif_",
            "elseHas_global_",
            "elseHas_if_",
            "elseHas_elseif_",
            "elseHas_else_",
        ]  # to maintain the sanity of how commands are generated
        begin = len(self.commands)

        for check_cond in order_list:
            w_res = {key: val for key, val in want.items() if key.startswith(check_cond)}

            for w_condition, w_policy_config in w_res.items():
                h_policy_config = have.pop(w_condition, {})
                if w_policy_config != h_policy_config:
                    render_condition = {
                        "condition": w_policy_config.pop("condition", ""),
                        "condition_type": w_policy_config.pop("conf_type"),
                    }
                    if render_condition.get("condition_type") != "global":
                        self.addcmd(render_condition, "condition", negate=False)
                    self.compare(parsers=self.parsers, want=w_policy_config, have=h_policy_config)

        if len(self.commands) != begin:
            self.commands.insert(begin, f"route-policy {policy_name}")

    def _route_maps_list_to_dict(self, data):
        temp_rmap_list = dict()

        def process_apply(apply_conf):
            rm_apply = {}
            for apply_config in apply_conf:
                rm_apply[apply_config.get("route_policy")] = apply_config
            return rm_apply

        for rmap in data:
            temp_rmap = dict()
            rmap_name = ""
            for cond, rm_conf in rmap.items():
                if cond == "name":
                    rmap_name = rm_conf
                    temp_rmap["name"] = rmap_name
                elif cond in ["if", "global"]:
                    if rm_conf.get("apply"):
                        rm_conf["apply"] = process_apply(rm_conf.get("apply"))
                    rm_conf["conf_type"] = cond
                    if cond == "global":
                        temp_rmap[cond] = rm_conf
                    else:
                        temp_rmap[
                            cond + "_" + (rm_conf.get("condition").replace(" ", "_"))
                        ] = rm_conf
                elif cond == "elseif":
                    for elif_config in rm_conf:
                        if elif_config.get("apply"):
                            elif_config["apply"] = process_apply(elif_config.get("apply"))
                        elif_config["conf_type"] = cond
                        temp_rmap[
                            cond + "_" + (elif_config.get("condition").replace(" ", "_"))
                        ] = elif_config
                elif (
                    cond == "else"
                ):  # wanted to do recursion but the overall performance is better this way
                    for else_cond, else_rm_conf in rm_conf.items():
                        if else_cond in ["if", "global", "else"]:
                            if else_rm_conf.get("apply"):
                                else_rm_conf["apply"] = process_apply(else_rm_conf.get("apply"))
                            else_rm_conf["conf_type"] = else_cond
                            if else_cond in ["global", "else"]:
                                temp_rmap["elseHas_" + else_cond + "_"] = else_rm_conf
                            else:
                                temp_rmap[
                                    "elseHas_"
                                    + else_cond
                                    + "_"
                                    + (else_rm_conf.get("condition").replace(" ", "_"))
                                ] = else_rm_conf
                        elif else_cond == "elseif":
                            for elif_config in else_rm_conf:
                                if elif_config.get("apply"):
                                    elif_config["apply"] = process_apply(elif_config.get("apply"))
                                elif_config["conf_type"] = "elseif"
                                temp_rmap[
                                    "elseHas_"
                                    + else_cond
                                    + "_"
                                    + (elif_config.get("condition").replace(" ", "_"))
                                ] = elif_config
            if temp_rmap:
                temp_rmap_list[rmap_name] = temp_rmap
        return temp_rmap_list
