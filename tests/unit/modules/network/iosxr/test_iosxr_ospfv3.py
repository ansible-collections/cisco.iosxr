#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest.mock import patch

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_ospfv3
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrOspfV3Module(TestIosxrModule):
    module = iosxr_ospfv3

    def setUp(self):
        super(TestIosxrOspfV3Module, self).setUp()

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
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.ospfv3.ospfv3."
            "Ospfv3Facts.get_ospfv3_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrOspfV3Module, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_ospfv3.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_ospfv3_merged(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="300",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = [
            "router ospfv3 300",
            "cost 2",
            "default-metric 10",
            "area 11 default-cost 5",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospfv3_merged_idempotent(self):
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

    def test_iosxr_ospfv3_replaced(self):
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
            "router ospfv3 30",
            "no default-metric 10",
            "router ospfv3 40",
            "cost 2",
            "default-metric 10",
            "area 11 default-cost 5",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospfv3_replaced_idempotent(self):
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

    def test_iosxr_ospfv3_overridden(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="40",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                        ),
                    ],
                ),
                state="overridden",
            ),
        )

        commands = [
            "no router ospfv3 30",
            "router ospfv3 40",
            "cost 2",
            "default-metric 10",
            "area 11 default-cost 5",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospfv3_overridden_idempotent(self):
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

    def test_iosxr_ospfv3_deleted(self):
        set_module_args(
            dict(
                config=dict(processes=[dict(process_id="30", cost=2)]),
                state="deleted",
            ),
        )
        commands = [
            "no router ospfv3 30",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospfv3_parsed(self):
        set_module_args(
            dict(
                running_config="router ospfv3 50\n cost 2\n area 11\n  default-cost 5\n !\n!",
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

    def test_iosxr_ospfv3_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    processes=[
                        dict(
                            process_id="60",
                            default_metric=10,
                            cost=2,
                            areas=[dict(area_id="11", default_cost=5)],
                        ),
                    ],
                ),
                state="rendered",
            ),
        )
        commands = [
            "area 11 default-cost 5",
            "cost 2",
            "default-metric 10",
            "router ospfv3 60",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), commands)
