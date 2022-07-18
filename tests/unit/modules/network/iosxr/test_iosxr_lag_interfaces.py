# (c) 2021 Red Hat Inc.
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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_lag_interfaces
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrLagInterfacesModule(TestIosxrModule):
    module = iosxr_lag_interfaces

    def setUp(self):
        super(TestIosxrLagInterfacesModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()
        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lag_interfaces.lag_interfaces.Lag_interfacesFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrLagInterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_lag_interface_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_lag_interfaces_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether10",
                        mode="active",
                        members=[
                            dict(
                                member="GigabitEthernet0/0/0/0",
                                mode="inherit",
                            ),
                            dict(
                                member="GigabitEthernet0/0/0/1",
                                mode="passive",
                            ),
                        ],
                        links=dict(max_active=10, min_active=2),
                    ),
                    dict(
                        name="Bundle-Ether11",
                        mode="active",
                        members=[
                            dict(
                                member="GigabitEthernet0/0/0/8",
                                mode="passive",
                            ),
                            dict(
                                member="GigabitEthernet0/0/0/9",
                                mode="passive",
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_lag_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether10",
                        mode="active",
                        members=[
                            dict(
                                member="GigabitEthernet0/0/0/0",
                                mode="inherit",
                            ),
                            dict(
                                member="GigabitEthernet0/0/0/1",
                                mode="passive",
                            ),
                        ],
                        links=dict(max_active=10, min_active=2),
                    ),
                    dict(
                        name="Bundle-Ether11",
                        mode="active",
                        members=[
                            dict(
                                member="GigabitEthernet0/0/0/8",
                                mode="passive",
                            ),
                            dict(
                                member="GigabitEthernet0/0/0/9",
                                mode="passive",
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface Bundle-Ether10",
            "bundle minimum-active links 2",
            "bundle maximum-active links 10",
            "lacp mode active",
            "interface GigabitEthernet0/0/0/1",
            "bundle id 10 mode passive",
            "interface GigabitEthernet0/0/0/0",
            "bundle id 10 mode inherit",
            "interface Bundle-Ether11",
            "lacp mode active",
            "interface GigabitEthernet0/0/0/8",
            "bundle id 11 mode passive",
            "interface GigabitEthernet0/0/0/9",
            "bundle id 11 mode passive",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lag_interfaces_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether10",
                        mode="passive",
                        members=[
                            dict(
                                member="GigabitEthernet0/0/0/0",
                                mode="passive",
                            ),
                        ],
                    ),
                    dict(name="Bundle-Ether12", mode="active"),
                ],
                state="replaced",
            ),
        )
        commands = [
            "interface Bundle-Ether10",
            "no bundle maximum-active links 10",
            "no bundle minimum-active links 2",
            "lacp mode passive",
            "interface GigabitEthernet0/0/0/1",
            "no bundle id",
            "interface GigabitEthernet0/0/0/0",
            "bundle id 10 mode passive",
            "interface Bundle-Ether12",
            "lacp mode active",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lag_interfaces_deleted(self):
        self._prepare()
        set_module_args(dict(state="deleted"))

        commands = [
            "interface Bundle-Ether10",
            "no bundle maximum-active links 10",
            "no bundle minimum-active links 2",
            "no lacp mode active",
            "interface GigabitEthernet0/0/0/0",
            "no bundle id",
            "interface GigabitEthernet0/0/0/1",
            "no bundle id",
            "interface Bundle-Ether11",
            "no lacp mode active",
            "interface GigabitEthernet0/0/0/8",
            "no bundle id",
            "interface GigabitEthernet0/0/0/9",
            "no bundle id",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lag_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether10",
                        mode="active",
                        members=[
                            dict(
                                member="GigabitEthernet0/0/0/0",
                                mode="passive",
                            ),
                            dict(
                                member="GigabitEthernet0/0/0/1",
                                mode="passive",
                            ),
                        ],
                        links=dict(max_active=10, min_active=2),
                    ),
                    dict(
                        name="Bundle-Ether11",
                        mode="active",
                        members=[
                            dict(
                                member="GigabitEthernet0/0/0/8",
                                mode="passive",
                            ),
                            dict(
                                member="GigabitEthernet0/0/0/9",
                                mode="passive",
                            ),
                        ],
                    ),
                ],
                state="rendered",
            ),
        )

        commands = [
            "interface Bundle-Ether10",
            "bundle minimum-active links 2",
            "bundle maximum-active links 10",
            "lacp mode active",
            "interface GigabitEthernet0/0/0/1",
            "bundle id 10 mode passive",
            "interface GigabitEthernet0/0/0/0",
            "bundle id 10 mode passive",
            "interface Bundle-Ether11",
            "lacp mode active",
            "interface GigabitEthernet0/0/0/8",
            "bundle id 11 mode passive",
            "interface GigabitEthernet0/0/0/9",
            "bundle id 11 mode passive",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_lag_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="interface Bundle-Ether10\r\n lacp mode active\r\n bundle maximum-active "
                "links 10\r\n bundle minimum-active links 2\r\n!\r\ninterface Bundle-Ether11"
                "\r\nlacp mode active\r\n!\r\ninterface GigabitEthernet0/0/0/0\r\n description "
                '"GigabitEthernet - 0"\r\n bundle id 10 mode inherit\r\n!\r\ninterface '
                "GigabitEthernet0/0/0/1"
                '\r\n description "GigabitEthernet - 2"\r\n  bundle id 10 mode passive\r\n!\r\n'
                'interface GigabitEthernet0/0/0/8\r\n description "GigabitEthernet - 8"'
                "\r\n bundle id 11 mode passive"
                "\r\n!\r\ninterface GigabitEthernet0/0/0/9\r\n description "
                '"GigabitEthernet - 9"\r\n bundle id 11 mode passive\r\n!',
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        print(result["parsed"])
        parsed_list = [
            {
                "links": {"max_active": 10, "min_active": 2},
                "members": [
                    {"member": "GigabitEthernet0/0/0/0", "mode": "inherit"},
                    {"member": "GigabitEthernet0/0/0/1", "mode": "passive"},
                ],
                "mode": "active",
                "name": "Bundle-Ether10",
            },
            {
                "members": [
                    {"member": "GigabitEthernet0/0/0/8", "mode": "passive"},
                    {"member": "GigabitEthernet0/0/0/9", "mode": "passive"},
                ],
                "mode": "active",
                "name": "Bundle-Ether11",
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_lag_interfaces_overridden(self):
        self.maxDiff = None
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether11",
                        mode="active",
                        members=[
                            dict(
                                member="GigabitEthernet0/0/0/0",
                                mode="active",
                            ),
                            dict(
                                member="GigabitEthernet0/0/0/1",
                                mode="active",
                            ),
                        ],
                        links=dict(max_active=10, min_active=5),
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "interface Bundle-Ether10",
            "no bundle maximum-active links 10",
            "no bundle minimum-active links 2",
            "no lacp mode active",
            "interface GigabitEthernet0/0/0/0",
            "no bundle id",
            "interface GigabitEthernet0/0/0/1",
            "no bundle id",
            "interface Bundle-Ether11",
            "bundle minimum-active links 5",
            "bundle maximum-active links 10",
            "interface GigabitEthernet0/0/0/8",
            "no bundle id",
            "interface GigabitEthernet0/0/0/9",
            "no bundle id",
            "interface GigabitEthernet0/0/0/0",
            "bundle id 11 mode active",
            "interface GigabitEthernet0/0/0/1",
            "bundle id 11 mode active",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
