# (c) 2024 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent
from unittest.mock import patch

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_route_maps
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrRouteMapsModule(TestIosxrModule):
    module = iosxr_route_maps

    def setUp(self):
        super(TestIosxrRouteMapsModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.route_maps.route_maps."
            "Route_mapsFacts.get_policynames",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_get_config_data = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.route_maps.route_maps."
            "Route_mapsFacts.get_policydata",
        )
        self.get_config_data = self.mock_get_config_data.start()

    def tearDown(self):
        super(TestIosxrRouteMapsModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()
        self.get_config_data.stop()

    def test_iosxr_route_maps_merged_simple(self):
        self.maxDiff = None
        self.get_config.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
            """,
        )
        self.get_config_data.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
              set ospf-metric 232
              prepend as-path most-recent 22
              if destination in DEFAULT then
                set qos-group 2
                set spf-priority critical
                set upstream-core-tree ingress-replication
              elseif destination in TEST-EXTERNAL-CONDITION0 then
                add eigrp-metric 22 223 23 223 232
                remove as-path private-as entire-aspath
              elseif destination in TEST-EXTERNAL-CONDITION1 then
                set tag 2323
                apply DUMMY-RMP-1
                apply DUMMY-RMP-2
                apply DUMMY-RMP-3
                set weight 23
              else
                set ospf-metric 232
                set qos-group 2
                set rip-tag 2
                set rt-set route-limit 22
                if destination in TEST-INTERNAL-IFCONDITION then
                  unsuppress-route
                elseif destination in TEST-INTERNAL_ELIFCONDITION then
                  pass
                  apply DUMMY-RMP-4
                  set administrative-distance 22
                elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then
                  apply DUMMY-RMP-3
                else
                  set ospf-metric 232
                  set qos-group 2
                  set rip-tag 2
                  set rt-set route-limit 22
                  set s-pmsi star-g
                endif
               endif
            end-policy
            """,
        )
        set_module_args(
            dict(
                config=[
                    {
                        "else_section": {
                            "else_section": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                    "s_pmsi": True,
                                },
                            },
                            "elseif_section": [
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-4"}],
                                    "condition": "destination in TEST-INTERNAL_ELIFCONDITION",
                                    "pass": True,
                                    "set": {"administrative_distance": 22},
                                },
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-3"}],
                                    "condition": "destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT",
                                },
                            ],
                            "global": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                },
                            },
                            "if_section": {
                                "condition": "destination in TEST-INTERNAL-IFCONDITION",
                                "unsuppress_route": True,
                            },
                        },
                        "elseif_section": [
                            {
                                "add": {
                                    "eigrp_metric": {
                                        "bandwidth": 22,
                                        "delay": 223,
                                        "effective_bandwith": 223,
                                        "max_transmission": 232,
                                        "reliability": 23,
                                    },
                                },
                                "condition": "destination in TEST-EXTERNAL-CONDITION0",
                                "remove": {"entire_aspath": True, "set": True},
                            },
                            {
                                "apply": [
                                    {"route_policy": "DUMMY-RMP-1"},
                                    {"route_policy": "DUMMY-RMP-2"},
                                    {"route_policy": "DUMMY-RMP-3"},
                                ],
                                "condition": "destination in TEST-EXTERNAL-CONDITION1",
                                "set": {"tag": 2323, "weight": 23},
                            },
                        ],
                        "global": {"set": {"ospf_metric": 232}},
                        "if_section": {
                            "condition": "destination in DEFAULT",
                            "set": {
                                "qos_group": 2,
                                "spf_priority": {"critical": True},
                                "upstream_core_tree": {"ingress_replication": True},
                            },
                        },
                        "name": "TEST_ROUTE_POLICY_COMPLEX",
                    },
                    {
                        "else_section": {
                            "else_section": {"drop": True},
                            "if_section": {
                                "condition": "as-path in (ios-regex '_8888_')",
                                "pass": True,
                            },
                        },
                        "if_section": {"condition": "destination in TESTROUTES", "drop": True},
                        "name": "TEST_ROUTE_POLICY_BIT_SIMPLE",
                    },
                    {
                        "else_section": {
                            "global": {
                                "pass": True,
                                "set": {
                                    "community": {"additive": True, "community_name": "(24680:1)"},
                                },
                            },
                        },
                        "if_section": {
                            "condition": "destination in ILOVEROUTEPOLICY",
                            "drop": True,
                        },
                        "name": "TEST_ROUTE_POLICY_SUPER_SIMPLE",
                    },
                ],
                state="merged",
            ),
        )
        result = self.execute_module(changed=True)

        commands = [
            "route-policy TEST_ROUTE_POLICY_BIT_SIMPLE",
            "if destination in TESTROUTES then",
            "drop",
            "else",
            "if as-path in (ios-regex '_8888_') then",
            "pass",
            "else",
            "drop",
            "endif",
            "endif",
            "end-policy",
            "route-policy TEST_ROUTE_POLICY_SUPER_SIMPLE",
            "if destination in ILOVEROUTEPOLICY then",
            "drop",
            "else",
            "pass",
            "set community (24680:1) additive",
            "endif",
            "end-policy",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_route_maps_merged_complex(self):
        self.maxDiff = None
        self.get_config.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
            """,
        )
        self.get_config_data.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
              set ospf-metric 232
              prepend as-path most-recent 22
              if destination in DEFAULT then
                set qos-group 2
                set spf-priority critical
                set upstream-core-tree ingress-replication
              elseif destination in TEST-EXTERNAL-CONDITION0 then
                add eigrp-metric 22 223 23 223 232
                remove as-path private-as entire-aspath
              elseif destination in TEST-EXTERNAL-CONDITION1 then
                set tag 2323
                apply DUMMY-RMP-1
                apply DUMMY-RMP-2
                apply DUMMY-RMP-3
                set weight 23
              else
                set ospf-metric 232
                set qos-group 2
                set rip-tag 2
                set rt-set route-limit 22
                if destination in TEST-INTERNAL-IFCONDITION then
                  unsuppress-route
                elseif destination in TEST-INTERNAL_ELIFCONDITION then
                  pass
                  apply DUMMY-RMP-4
                  set administrative-distance 22
                elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then
                  apply DUMMY-RMP-3
                else
                  set ospf-metric 232
                  set qos-group 2
                  set rip-tag 2
                  set rt-set route-limit 22
                  set s-pmsi star-g
                endif
               endif
            end-policy
            """,
        )
        set_module_args(
            dict(
                config=[
                    {
                        "else_section": {
                            "else_section": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                    "s_pmsi": True,
                                },
                            },
                            "elseif_section": [
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-4"}],
                                    "condition": "destination in TEST-INTERNAL_ELIFCONDITION",
                                    "pass": True,
                                    "set": {"administrative_distance": 22},
                                },
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-3"}],
                                    "condition": "destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT",
                                },
                            ],
                            "global": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                },
                            },
                            "if_section": {
                                "condition": "destination in TEST-INTERNAL-IFCONDITION",
                                "unsuppress_route": True,
                            },
                        },
                        "elseif_section": [
                            {
                                "add": {
                                    "eigrp_metric": {
                                        "bandwidth": 22,
                                        "delay": 223,
                                        "effective_bandwith": 223,
                                        "max_transmission": 232,
                                        "reliability": 23,
                                    },
                                },
                                "condition": "destination in TEST-EXTERNAL-CONDITION0",
                                "remove": {"entire_aspath": True, "set": True},
                            },
                            {
                                "apply": [
                                    {"route_policy": "DUMMY-RMP-1"},
                                    {"route_policy": "DUMMY-RMP-2"},
                                    {"route_policy": "DUMMY-RMP-3"},
                                ],
                                "condition": "destination in TEST-EXTERNAL-CONDITION1",
                                "set": {"tag": 2323, "weight": 23},
                            },
                        ],
                        "global": {"set": {"ospf_metric": 232}},
                        "if_section": {
                            "condition": "destination in DEFAULT",
                            "set": {
                                "qos_group": 2,
                                "spf_priority": {"critical": True},
                                "upstream_core_tree": {"ingress_replication": True},
                            },
                        },
                        "name": "APPLY_TEST_ROUTE_POLICY_COMPLEX",
                    },
                    {
                        "else_section": {
                            "else_section": {"drop": True},
                            "if_section": {
                                "condition": "as-path in (ios-regex '_8888_')",
                                "pass": True,
                            },
                        },
                        "if_section": {"condition": "destination in TESTROUTES", "drop": True},
                        "name": "TEST_ROUTE_POLICY_BIT_SIMPLE",
                    },
                    {
                        "else_section": {
                            "global": {
                                "pass": True,
                                "set": {
                                    "community": {"additive": True, "community_name": "(24680:1)"},
                                },
                            },
                        },
                        "if_section": {
                            "condition": "destination in ILOVEROUTEPOLICY",
                            "drop": True,
                        },
                        "name": "TEST_ROUTE_POLICY_SUPER_SIMPLE",
                    },
                ],
                state="merged",
            ),
        )
        result = self.execute_module(changed=True)

        commands = [
            "route-policy TEST_ROUTE_POLICY_SUPER_SIMPLE",
            "if destination in ILOVEROUTEPOLICY then",
            "drop",
            "else",
            "pass",
            "set community (24680:1) additive",
            "endif",
            "end-policy",
            "route-policy TEST_ROUTE_POLICY_BIT_SIMPLE",
            "if destination in TESTROUTES then",
            "drop",
            "else",
            "if as-path in (ios-regex '_8888_') then",
            "pass",
            "else",
            "drop",
            "endif",
            "endif",
            "end-policy",
            "route-policy APPLY_TEST_ROUTE_POLICY_COMPLEX",
            "if destination in DEFAULT then",
            "set spf-priority critical high medium",
            "set upstream-core-tree ingress-replication mldp p2mp-te sr-p2mp",
            "elseif destination in TEST-EXTERNAL-CONDITION0 then",
            "add eigrp-metric 22 223 23 223 232",
            "remove as-path private-as entire-aspath",
            "elseif destination in TEST-EXTERNAL-CONDITION1 then",
            "apply DUMMY-RMP-1",
            "apply DUMMY-RMP-2",
            "apply DUMMY-RMP-3",
            "set tag 2323",
            "set weight 23",
            "else",
            "if destination in TEST-INTERNAL-IFCONDITION then",
            "unsuppress-route",
            "elseif destination in TEST-INTERNAL_ELIFCONDITION then",
            "apply DUMMY-RMP-4",
            "pass",
            "set administrative-distance 22",
            "elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then",
            "apply DUMMY-RMP-3",
            "else",
            "set s-pmsi star-g",
            "endif",
            "endif",
            "end-policy",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_route_maps_overridden(self):
        self.maxDiff = None
        self.get_config.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
            """,
        )
        self.get_config_data.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
              set ospf-metric 232
              prepend as-path most-recent 22
              if destination in DEFAULT then
                set qos-group 2
                set spf-priority critical
                set upstream-core-tree ingress-replication
              elseif destination in TEST-EXTERNAL-CONDITION0 then
                add eigrp-metric 22 223 23 223 232
                remove as-path private-as entire-aspath
              elseif destination in TEST-EXTERNAL-CONDITION1 then
                set tag 2323
                apply DUMMY-RMP-1
                apply DUMMY-RMP-2
                apply DUMMY-RMP-3
                set weight 23
              else
                set ospf-metric 232
                set qos-group 2
                set rip-tag 2
                set rt-set route-limit 22
                if destination in TEST-INTERNAL-IFCONDITION then
                  unsuppress-route
                elseif destination in TEST-INTERNAL_ELIFCONDITION then
                  pass
                  apply DUMMY-RMP-4
                  set administrative-distance 22
                elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then
                  apply DUMMY-RMP-3
                else
                  set ospf-metric 232
                  set qos-group 2
                  set rip-tag 2
                  set rt-set route-limit 22
                  set s-pmsi star-g
                endif
               endif
            end-policy
            """,
        )
        set_module_args(
            dict(
                config=[
                    {
                        "else_section": {
                            "else_section": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                    "s_pmsi": True,
                                },
                            },
                            "elseif_section": [
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-4"}],
                                    "condition": "destination in TEST-INTERNAL_ELIFCONDITION",
                                    "pass": True,
                                    "set": {"administrative_distance": 22},
                                },
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-3"}],
                                    "condition": "destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT",
                                },
                            ],
                            "global": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                },
                            },
                            "if_section": {
                                "condition": "destination in TEST-INTERNAL-IFCONDITION",
                                "unsuppress_route": True,
                            },
                        },
                        "elseif_section": [
                            {
                                "add": {
                                    "eigrp_metric": {
                                        "bandwidth": 22,
                                        "delay": 223,
                                        "effective_bandwith": 223,
                                        "max_transmission": 232,
                                        "reliability": 23,
                                    },
                                },
                                "condition": "destination in TEST-EXTERNAL-CONDITION0",
                                "remove": {"entire_aspath": True, "set": True},
                            },
                            {
                                "apply": [
                                    {"route_policy": "DUMMY-RMP-1"},
                                    {"route_policy": "DUMMY-RMP-2"},
                                    {"route_policy": "DUMMY-RMP-3"},
                                ],
                                "condition": "destination in TEST-EXTERNAL-CONDITION1",
                                "set": {"tag": 2323, "weight": 23},
                            },
                        ],
                        "global": {"set": {"ospf_metric": 232}},
                        "if_section": {
                            "condition": "destination in DEFAULT",
                            "set": {
                                "qos_group": 2,
                                "spf_priority": {"critical": True},
                                "upstream_core_tree": {"ingress_replication": True},
                            },
                        },
                        "name": "APPLY_TEST_ROUTE_POLICY_COMPLEX",
                    },
                    {
                        "else_section": {
                            "else_section": {"drop": True},
                            "if_section": {"condition": "as-path in 15446", "pass": True},
                        },
                        "if_section": {"condition": "destination in TESTROUTES", "drop": True},
                        "name": "TEST_ROUTE_POLICY_BIT_SIMPLE",
                    },
                    {
                        "else_section": {
                            "global": {
                                "pass": True,
                                "set": {
                                    "community": {"additive": True, "community_name": "(24680:1)"},
                                },
                            },
                        },
                        "if_section": {
                            "condition": "destination in ILOVEROUTEPOLICY",
                            "drop": True,
                        },
                        "name": "TEST_ROUTE_POLICY_SUPER_SIMPLE",
                    },
                ],
                state="overridden",
            ),
        )
        result = self.execute_module(changed=True)

        commands = [
            "route-policy APPLY_TEST_ROUTE_POLICY_COMPLEX",
            "if destination in DEFAULT then",
            "set spf-priority critical high medium",
            "set upstream-core-tree ingress-replication mldp p2mp-te sr-p2mp",
            "elseif destination in TEST-EXTERNAL-CONDITION0 then",
            "add eigrp-metric 22 223 23 223 232",
            "remove as-path private-as entire-aspath",
            "elseif destination in TEST-EXTERNAL-CONDITION1 then",
            "apply DUMMY-RMP-1",
            "apply DUMMY-RMP-2",
            "apply DUMMY-RMP-3",
            "set tag 2323",
            "set weight 23",
            "else",
            "if destination in TEST-INTERNAL-IFCONDITION then",
            "unsuppress-route",
            "elseif destination in TEST-INTERNAL_ELIFCONDITION then",
            "apply DUMMY-RMP-4",
            "pass",
            "set administrative-distance 22",
            "elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then",
            "apply DUMMY-RMP-3",
            "else",
            "set s-pmsi star-g",
            "endif",
            "endif",
            "end-policy",
            "route-policy TEST_ROUTE_POLICY_BIT_SIMPLE",
            "if destination in TESTROUTES then",
            "drop",
            "else",
            "if as-path in 15446 then",
            "pass",
            "else",
            "drop",
            "endif",
            "endif",
            "end-policy",
            "route-policy TEST_ROUTE_POLICY_SUPER_SIMPLE",
            "if destination in ILOVEROUTEPOLICY then",
            "drop",
            "else",
            "pass",
            "set community (24680:1) additive",
            "endif",
            "end-policy",
            "no route-policy TEST_ROUTE_POLICY_COMPLEX",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_route_maps_replaced(self):
        self.maxDiff = None
        self.get_config.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
            """,
        )
        self.get_config_data.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
              set ospf-metric 232
              prepend as-path most-recent 22
              if destination in DEFAULT then
                set qos-group 2
                set spf-priority critical
                set upstream-core-tree ingress-replication
              elseif destination in TEST-EXTERNAL-CONDITION0 then
                add eigrp-metric 22 223 23 223 232
                remove as-path private-as entire-aspath
              elseif destination in TEST-EXTERNAL-CONDITION1 then
                set tag 2323
                apply DUMMY-RMP-1
                apply DUMMY-RMP-2
                apply DUMMY-RMP-3
                set weight 23
              else
                set ospf-metric 232
                set qos-group 2
                set rip-tag 2
                set rt-set route-limit 22
                if destination in TEST-INTERNAL-IFCONDITION then
                  unsuppress-route
                elseif destination in TEST-INTERNAL_ELIFCONDITION then
                  pass
                  apply DUMMY-RMP-4
                  set administrative-distance 22
                elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then
                  apply DUMMY-RMP-3
                else
                  set ospf-metric 232
                  set qos-group 2
                  set rip-tag 2
                  set rt-set route-limit 22
                  set s-pmsi star-g
                endif
               endif
            end-policy
            """,
        )
        set_module_args(
            dict(
                config=[
                    {
                        "else_section": {
                            "else_section": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                    "s_pmsi": True,
                                },
                            },
                            "elseif_section": [
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-4"}],
                                    "condition": "destination in TEST-INTERNAL_ELIFCONDITION",
                                    "pass": True,
                                    "set": {"administrative_distance": 22},
                                },
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-3"}],
                                    "condition": "destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT",
                                },
                            ],
                            "global": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                },
                            },
                            "if_section": {
                                "condition": "destination in TEST-INTERNAL-IFCONDITION",
                                "unsuppress_route": True,
                            },
                        },
                        "elseif_section": [
                            {
                                "add": {
                                    "eigrp_metric": {
                                        "bandwidth": 22,
                                        "delay": 223,
                                        "effective_bandwith": 223,
                                        "max_transmission": 232,
                                        "reliability": 23,
                                    },
                                },
                                "condition": "destination in TEST-EXTERNAL-CONDITION0",
                                "remove": {"entire_aspath": True, "set": True},
                            },
                            {
                                "apply": [
                                    {"route_policy": "DUMMY-RMP-1"},
                                    {"route_policy": "DUMMY-RMP-2"},
                                    {"route_policy": "DUMMY-RMP-3"},
                                ],
                                "condition": "destination in TEST-EXTERNAL-CONDITION1",
                                "set": {"tag": 2323, "weight": 23},
                            },
                        ],
                        "global": {"set": {"ospf_metric": 232}},
                        "if_section": {
                            "condition": "destination in DEFAULT",
                            "set": {
                                "qos_group": 2,
                                "spf_priority": {"critical": True},
                                "upstream_core_tree": {"ingress_replication": True},
                            },
                        },
                        "name": "APPLY_TEST_ROUTE_POLICY_COMPLEX",
                    },
                    {
                        "else_section": {
                            "else_section": {"drop": True},
                            "if_section": {"condition": "as-path in 15446", "pass": True},
                        },
                        "if_section": {"condition": "destination in TESTROUTES", "drop": True},
                        "name": "TEST_ROUTE_POLICY_BIT_SIMPLE",
                    },
                    {
                        "else_section": {
                            "global": {
                                "pass": True,
                                "set": {
                                    "community": {"additive": True, "community_name": "(24680:1)"},
                                },
                            },
                        },
                        "if_section": {
                            "condition": "destination in ILOVEROUTEPOLICY",
                            "drop": True,
                        },
                        "name": "TEST_ROUTE_POLICY_SUPER_SIMPLE",
                    },
                ],
                state="replaced",
            ),
        )
        result = self.execute_module(changed=True)

        commands = [
            "route-policy APPLY_TEST_ROUTE_POLICY_COMPLEX",
            "if destination in DEFAULT then",
            "set spf-priority critical high medium",
            "set upstream-core-tree ingress-replication mldp p2mp-te sr-p2mp",
            "elseif destination in TEST-EXTERNAL-CONDITION0 then",
            "add eigrp-metric 22 223 23 223 232",
            "remove as-path private-as entire-aspath",
            "elseif destination in TEST-EXTERNAL-CONDITION1 then",
            "apply DUMMY-RMP-1",
            "apply DUMMY-RMP-2",
            "apply DUMMY-RMP-3",
            "set tag 2323",
            "set weight 23",
            "else",
            "if destination in TEST-INTERNAL-IFCONDITION then",
            "unsuppress-route",
            "elseif destination in TEST-INTERNAL_ELIFCONDITION then",
            "apply DUMMY-RMP-4",
            "pass",
            "set administrative-distance 22",
            "elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then",
            "apply DUMMY-RMP-3",
            "else",
            "set s-pmsi star-g",
            "endif",
            "endif",
            "end-policy",
            "route-policy TEST_ROUTE_POLICY_BIT_SIMPLE",
            "if destination in TESTROUTES then",
            "drop",
            "else",
            "if as-path in 15446 then",
            "pass",
            "else",
            "drop",
            "endif",
            "endif",
            "end-policy",
            "route-policy TEST_ROUTE_POLICY_SUPER_SIMPLE",
            "if destination in ILOVEROUTEPOLICY then",
            "drop",
            "else",
            "pass",
            "set community (24680:1) additive",
            "endif",
            "end-policy",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_route_maps_purged_safe(self):
        self.maxDiff = None
        self.get_config.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
            """,
        )
        self.get_config_data.return_value = dedent(
            """\
            route-policy TEST_ROUTE_POLICY_COMPLEX
              set ospf-metric 232
              prepend as-path most-recent 22
              if destination in DEFAULT then
                set qos-group 2
                set spf-priority critical
                set upstream-core-tree ingress-replication
              elseif destination in TEST-EXTERNAL-CONDITION0 then
                add eigrp-metric 22 223 23 223 232
                remove as-path private-as entire-aspath
              elseif destination in TEST-EXTERNAL-CONDITION1 then
                set tag 2323
                apply DUMMY-RMP-1
                apply DUMMY-RMP-2
                apply DUMMY-RMP-3
                set weight 23
              else
                set ospf-metric 232
                set qos-group 2
                set rip-tag 2
                set rt-set route-limit 22
                if destination in TEST-INTERNAL-IFCONDITION then
                  unsuppress-route
                elseif destination in TEST-INTERNAL_ELIFCONDITION then
                  pass
                  apply DUMMY-RMP-4
                  set administrative-distance 22
                elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then
                  apply DUMMY-RMP-3
                else
                  set ospf-metric 232
                  set qos-group 2
                  set rip-tag 2
                  set rt-set route-limit 22
                  set s-pmsi star-g
                endif
               endif
            end-policy
            """,
        )
        set_module_args(
            dict(
                config=[
                    {
                        "else_section": {
                            "else_section": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                    "s_pmsi": True,
                                },
                            },
                            "elseif_section": [
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-4"}],
                                    "condition": "destination in TEST-INTERNAL_ELIFCONDITION",
                                    "pass": True,
                                    "set": {"administrative_distance": 22},
                                },
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-3"}],
                                    "condition": "destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT",
                                },
                            ],
                            "global": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                },
                            },
                            "if_section": {
                                "condition": "destination in TEST-INTERNAL-IFCONDITION",
                                "unsuppress_route": True,
                            },
                        },
                        "elseif_section": [
                            {
                                "add": {
                                    "eigrp_metric": {
                                        "bandwidth": 22,
                                        "delay": 223,
                                        "effective_bandwith": 223,
                                        "max_transmission": 232,
                                        "reliability": 23,
                                    },
                                },
                                "condition": "destination in TEST-EXTERNAL-CONDITION0",
                                "remove": {"entire_aspath": True, "set": True},
                            },
                            {
                                "apply": [
                                    {"route_policy": "DUMMY-RMP-1"},
                                    {"route_policy": "DUMMY-RMP-2"},
                                    {"route_policy": "DUMMY-RMP-3"},
                                ],
                                "condition": "destination in TEST-EXTERNAL-CONDITION1",
                                "set": {"tag": 2323, "weight": 23},
                            },
                        ],
                        "global": {"set": {"ospf_metric": 232}},
                        "if_section": {
                            "condition": "destination in DEFAULT",
                            "set": {
                                "qos_group": 2,
                                "spf_priority": {"critical": True},
                                "upstream_core_tree": {"ingress_replication": True},
                            },
                        },
                        "name": "APPLY_TEST_ROUTE_POLICY_COMPLEX",
                    },
                    {
                        "else_section": {
                            "else_section": {"drop": True},
                            "if_section": {"condition": "as-path in 15446", "pass": True},
                        },
                        "if_section": {"condition": "destination in TESTROUTES", "drop": True},
                        "name": "TEST_ROUTE_POLICY_BIT_SIMPLE",
                    },
                    {
                        "else_section": {
                            "global": {
                                "pass": True,
                                "set": {
                                    "community": {"additive": True, "community_name": "(24680:1)"},
                                },
                            },
                        },
                        "if_section": {
                            "condition": "destination in ILOVEROUTEPOLICY",
                            "drop": True,
                        },
                        "name": "TEST_ROUTE_POLICY_SUPER_SIMPLE",
                    },
                ],
                state="purged",
            ),
        )
        self.execute_module(changed=False)

    def test_iosxr_route_maps_purged(self):
        self.maxDiff = None
        self.get_config.return_value = dedent(
            """\
            route-policy APPLY_TEST_ROUTE_POLICY_COMPLEX
            """,
        )
        self.get_config_data.return_value = dedent(
            """\
            route-policy APPLY_TEST_ROUTE_POLICY_COMPLEX
              set ospf-metric 232
              prepend as-path most-recent 22
              if destination in DEFAULT then
                set qos-group 2
                set spf-priority critical
                set upstream-core-tree ingress-replication
              elseif destination in TEST-EXTERNAL-CONDITION0 then
                add eigrp-metric 22 223 23 223 232
                remove as-path private-as entire-aspath
              elseif destination in TEST-EXTERNAL-CONDITION1 then
                set tag 2323
                apply DUMMY-RMP-1
                apply DUMMY-RMP-2
                apply DUMMY-RMP-3
                set weight 23
              else
                set ospf-metric 232
                set qos-group 2
                set rip-tag 2
                set rt-set route-limit 22
                if destination in TEST-INTERNAL-IFCONDITION then
                  unsuppress-route
                elseif destination in TEST-INTERNAL_ELIFCONDITION then
                  pass
                  apply DUMMY-RMP-4
                  set administrative-distance 22
                elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then
                  apply DUMMY-RMP-3
                else
                  set ospf-metric 232
                  set qos-group 2
                  set rip-tag 2
                  set rt-set route-limit 22
                  set s-pmsi star-g
                endif
               endif
            end-policy
            """,
        )
        set_module_args(
            dict(
                config=[
                    {
                        "else_section": {
                            "else_section": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                    "s_pmsi": True,
                                },
                            },
                            "elseif_section": [
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-4"}],
                                    "condition": "destination in TEST-INTERNAL_ELIFCONDITION",
                                    "pass": True,
                                    "set": {"administrative_distance": 22},
                                },
                                {
                                    "apply": [{"route_policy": "DUMMY-RMP-3"}],
                                    "condition": "destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT",
                                },
                            ],
                            "global": {
                                "set": {
                                    "ospf_metric": 232,
                                    "qos_group": 2,
                                    "rip_tag": 2,
                                    "rt_set": 22,
                                },
                            },
                            "if_section": {
                                "condition": "destination in TEST-INTERNAL-IFCONDITION",
                                "unsuppress_route": True,
                            },
                        },
                        "elseif_section": [
                            {
                                "add": {
                                    "eigrp_metric": {
                                        "bandwidth": 22,
                                        "delay": 223,
                                        "effective_bandwith": 223,
                                        "max_transmission": 232,
                                        "reliability": 23,
                                    },
                                },
                                "condition": "destination in TEST-EXTERNAL-CONDITION0",
                                "remove": {"entire_aspath": True, "set": True},
                            },
                            {
                                "apply": [
                                    {"route_policy": "DUMMY-RMP-1"},
                                    {"route_policy": "DUMMY-RMP-2"},
                                    {"route_policy": "DUMMY-RMP-3"},
                                ],
                                "condition": "destination in TEST-EXTERNAL-CONDITION1",
                                "set": {"tag": 2323, "weight": 23},
                            },
                        ],
                        "global": {"set": {"ospf_metric": 232}},
                        "if_section": {
                            "condition": "destination in DEFAULT",
                            "set": {
                                "qos_group": 2,
                                "spf_priority": {"critical": True},
                                "upstream_core_tree": {"ingress_replication": True},
                            },
                        },
                        "name": "APPLY_TEST_ROUTE_POLICY_COMPLEX",
                    },
                    {
                        "else_section": {
                            "else_section": {"drop": True},
                            "if_section": {"condition": "as-path in 15446", "pass": True},
                        },
                        "if_section": {"condition": "destination in TESTROUTES", "drop": True},
                        "name": "TEST_ROUTE_POLICY_BIT_SIMPLE",
                    },
                    {
                        "else_section": {
                            "global": {
                                "pass": True,
                                "set": {
                                    "community": {"additive": True, "community_name": "(24680:1)"},
                                },
                            },
                        },
                        "if_section": {
                            "condition": "destination in ILOVEROUTEPOLICY",
                            "drop": True,
                        },
                        "name": "TEST_ROUTE_POLICY_SUPER_SIMPLE",
                    },
                ],
                state="purged",
            ),
        )
        result = self.execute_module(changed=True)

        commands = [
            "no route-policy APPLY_TEST_ROUTE_POLICY_COMPLEX",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_route_maps_parsed(self):
        set_module_args(
            dict(
                running_config=dedent(
                    """\
                    route-policy APPLY_TEST_ROUTE_POLICY_COMPLEX
                      set ospf-metric 232
                      prepend as-path most-recent 22
                      if destination in DEFAULT then
                        set qos-group 2
                        set spf-priority critical
                        set upstream-core-tree ingress-replication
                      elseif destination in TEST-EXTERNAL-CONDITION0 then
                        add eigrp-metric 22 223 23 223 232
                        remove as-path private-as entire-aspath
                      elseif destination in TEST-EXTERNAL-CONDITION1 then
                        set tag 2323
                        apply DUMMY-RMP-1
                        apply DUMMY-RMP-2
                        apply DUMMY-RMP-3
                        set weight 23
                      else
                        set ospf-metric 232
                        set qos-group 2
                        set rip-tag 2
                        set rt-set route-limit 22
                        if destination in TEST-INTERNAL-IFCONDITION then
                          unsuppress-route
                        elseif destination in TEST-INTERNAL_ELIFCONDITION then
                          pass
                          apply DUMMY-RMP-4
                          set administrative-distance 22
                        elseif destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT then
                          apply DUMMY-RMP-3
                        else
                          set ospf-metric 232
                          set qos-group 2
                          set rip-tag 2
                          set rt-set route-limit 22
                          set s-pmsi star-g
                        endif
                       endif
                    end-policy
                    """,
                ),
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "name": "APPLY_TEST_ROUTE_POLICY_COMPLEX",
                "if_section": {
                    "set": {
                        "qos_group": 2,
                        "spf_priority": {"critical": True},
                        "upstream_core_tree": {"ingress_replication": True},
                    },
                    "condition": "destination in DEFAULT",
                },
                "global": {"set": {"ospf_metric": 232}},
                "elseif_section": [
                    {
                        "add": {
                            "eigrp_metric": {
                                "bandwidth": 22,
                                "delay": 223,
                                "reliability": 23,
                                "effective_bandwith": 223,
                                "max_transmission": 232,
                            },
                        },
                        "remove": {"set": True, "entire_aspath": True},
                        "condition": "destination in TEST-EXTERNAL-CONDITION0",
                    },
                    {
                        "set": {"tag": 2323, "weight": 23},
                        "apply": [
                            {"route_policy": "DUMMY-RMP-1"},
                            {"route_policy": "DUMMY-RMP-2"},
                            {"route_policy": "DUMMY-RMP-3"},
                        ],
                        "condition": "destination in TEST-EXTERNAL-CONDITION1",
                    },
                ],
                "else_section": {
                    "global": {
                        "set": {"ospf_metric": 232, "qos_group": 2, "rip_tag": 2, "rt_set": 22},
                    },
                    "if_section": {
                        "unsuppress_route": True,
                        "condition": "destination in TEST-INTERNAL-IFCONDITION",
                    },
                    "else_section": {
                        "set": {
                            "ospf_metric": 232,
                            "qos_group": 2,
                            "rip_tag": 2,
                            "rt_set": 22,
                            "s_pmsi": True,
                        },
                    },
                    "elseif_section": [
                        {
                            "pass": True,
                            "apply": [{"route_policy": "DUMMY-RMP-4"}],
                            "set": {"administrative_distance": 22},
                            "condition": "destination in TEST-INTERNAL_ELIFCONDITION",
                        },
                        {
                            "apply": [{"route_policy": "DUMMY-RMP-3"}],
                            "condition": "destination in TEST-INTERNAL-DIFFERENT or destination in DEFAULT",
                        },
                    ],
                },
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_route_maps_parsed_local_pref(self):
        set_module_args(
            dict(
                running_config=dedent(
                    """\
                    route-policy APPLY_TEST_ROUTE_POLICY_COMPLEX
                      set ospf-metric 232
                      set local-preference +100
                      set local-preference -200
                      set local-preference *600
                      set local-preference +900
                   """,
                ),
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "name": "APPLY_TEST_ROUTE_POLICY_COMPLEX",
                "global": {
                    "set": {
                        "ospf_metric": 232,
                        "local_preference": [
                            {"increment": True, "metric_number": 100},
                            {"decrement": True, "metric_number": 200},
                            {"multiply": True, "metric_number": 600},
                            {"increment": True, "metric_number": 900},
                        ],
                    },
                },
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])
