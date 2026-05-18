#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_ospfv2
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrOspfV2Module(TestIosxrModule):
    module = iosxr_ospfv2

    def setUp(self):
        super(TestIosxrOspfV2Module, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base."
            "get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.ospfv2.ospfv2."
            "Ospfv2Facts.get_ospfv2_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrOspfV2Module, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_ospfv2.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_ospfv2_merged(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="300",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                            log_adjacency_changes=dict(set=True),
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = [
            "router ospf 300",
            "cost 2",
            "default-metric 10",
            "area 11 default-cost 5",
            "log adjacency changes",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospfv2_merged_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="30",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_ospfv2_replaced(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="30",
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                        ),
                        dict(
                            process_id="40",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        commands = [
            "router ospf 30",
            "no default-metric 10",
            "router ospf 40",
            "cost 2",
            "default-metric 10",
            "area 11 default-cost 5",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospfv2_replaced_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="30",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_ospfv2_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="40",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                            log_adjacency_changes=dict(set=True),
                        ),
                    ],
                ),
                state="overridden",
            ),
        )

        commands = [
            "router ospf 30",
            "no cost 2",
            "no default-metric 10",
            "no area 11 default-cost 5",
            "router ospf 40",
            "cost 2",
            "default-metric 10",
            "area 11 default-cost 5",
            "log adjacency changes",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospfv2_overridden_idempotent(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="30",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                        ),
                    ],
                ),
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_ospfv2_deleted(self):
        set_module_args(
            dict(
                config=dict(processes=[dict(process_id="30", cost=2)]),
                state="deleted",
            ),
        )
        commands = [
            "router ospf 30",
            "no cost 2",
            "no default-metric 10",
            "no area 11 default-cost 5",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospfv2_parsed(self):
        set_module_args(
            dict(
                running_config="router ospf 50\n cost 2\n area 11\n  default-cost 5\n !\n!",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "processes": [
                dict(
                    process_id="50",
                    cost=2,
                    areas=[dict(area_id="11", default_cost=5)],
                ),
            ],
        }
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_ospfv2_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="60",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                            log_adjacency_changes=dict(set=True),
                        ),
                    ],
                ),
                state="rendered",
            ),
        )
        commands = [
            "area 11 default-cost 5",
            "cost 2",
            "log adjacency changes",
            "default-metric 10",
            "router ospf 60",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_ospfv2_max_metric_router_lsa_basic(self):
        """Test basic max-metric router-lsa configuration."""
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="100",
                            max_metric=dict(
                                router_lsa=dict(set=True),
                            ),
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = ["router ospf 100", "max-metric router-lsa"]
        result = self.execute_module(changed=True)
        self.assertEqual(result["commands"], commands)

    def test_iosxr_ospfv2_max_metric_external_lsa_set(self):
        """Test max-metric router-lsa with external-lsa set."""
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="100",
                            max_metric=dict(
                                router_lsa=dict(
                                    external_lsa=dict(set=True),
                                ),
                            ),
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = ["router ospf 100", "max-metric router-lsa external-lsa"]
        result = self.execute_module(changed=True)
        self.assertEqual(result["commands"], commands)

    def test_iosxr_ospfv2_max_metric_external_lsa_value(self):
        """Test max-metric router-lsa with external-lsa max_metric_value."""
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="100",
                            max_metric=dict(
                                router_lsa=dict(
                                    external_lsa=dict(max_metric_value=100),
                                ),
                            ),
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = ["router ospf 100", "max-metric router-lsa external-lsa 100"]
        result = self.execute_module(changed=True)
        self.assertEqual(result["commands"], commands)

    def test_iosxr_ospfv2_max_metric_summary_lsa_value(self):
        """Test max-metric router-lsa with summary-lsa max_metric_value."""
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="100",
                            max_metric=dict(
                                router_lsa=dict(
                                    summary_lsa=dict(max_metric_value=200),
                                ),
                            ),
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = ["router ospf 100", "max-metric router-lsa summary-lsa 200"]
        result = self.execute_module(changed=True)
        self.assertEqual(result["commands"], commands)

    def test_iosxr_ospfv2_max_metric_on_startup_wait_period(self):
        """Test max-metric router-lsa on-startup with wait_period."""
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="100",
                            max_metric=dict(
                                router_lsa=dict(
                                    on_startup=dict(wait_period=300),
                                ),
                            ),
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = ["router ospf 100", "max-metric router-lsa on-startup 300"]
        result = self.execute_module(changed=True)
        self.assertEqual(result["commands"], commands)

    def test_iosxr_ospfv2_max_metric_complex_combination(self):
        """Test max-metric with multiple options combined."""
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="100",
                            max_metric=dict(
                                router_lsa=dict(
                                    on_startup=dict(wait_period=300),
                                    external_lsa=dict(max_metric_value=150),
                                    include_stub=True,
                                    summary_lsa=dict(max_metric_value=250),
                                ),
                            ),
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = [
            "router ospf 100",
            "max-metric router-lsa on-startup 300 external-lsa 150 include-stub summary-lsa 250",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(result["commands"], commands)

    def test_iosxr_ospfv2_max_metric_parsed(self):
        """Test parsing max-metric configuration."""
        set_module_args(
            dict(
                running_config="""router ospf 100
 max-metric router-lsa on-startup 300 external-lsa 150 include-stub summary-lsa 250
!""",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "processes": [
                {
                    "process_id": "100",
                    "max_metric": {
                        "router_lsa": {
                            "set": True,
                            "on_startup": {"wait_period": 300},
                            "external_lsa": {"max_metric_value": 150},
                            "include_stub": True,
                            "summary_lsa": {"max_metric_value": 250},
                        },
                    },
                },
            ],
        }
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_ospfv2_max_metric_deleted(self):
        """Test deleting max-metric configuration."""
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="30",
                            max_metric=dict(
                                router_lsa=dict(
                                    external_lsa=dict(max_metric_value=100),
                                ),
                            ),
                        ),
                    ],
                ),
                state="deleted",
            ),
        )
        commands = [
            "router ospf 30",
            "no cost 2",
            "no default-metric 10",
            "no area 11 default-cost 5",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(result["commands"], commands)

    def test_iosxr_ospfv2_max_metric_rendered(self):
        """Test rendering max-metric configuration."""
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="100",
                            max_metric=dict(
                                router_lsa=dict(
                                    on_startup=dict(wait_for_bgp=True),
                                    external_lsa=dict(max_metric_value=150),
                                    summary_lsa=dict(set=True),
                                ),
                            ),
                        ),
                    ],
                ),
                state="rendered",
            ),
        )
        commands = [
            "router ospf 100",
            "max-metric router-lsa on-startup wait-for-bgp external-lsa 150 summary-lsa",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(result["rendered"], commands)
