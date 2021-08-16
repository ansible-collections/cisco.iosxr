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

from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.plugins.modules import iosxr_l2_interfaces
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import (
    set_module_args,
)
from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrL2InterfacesModule(TestIosxrModule):
    module = iosxr_l2_interfaces

    def setUp(self):
        super(TestIosxrL2InterfacesModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config"
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection"
        )
        self.get_resource_connection_facts = (
            self.mock_get_resource_connection_facts.start()
        )
        self.mock_get_os_version = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.l2_interfaces.l2_interfaces.get_os_version"
        )
        self.get_os_version = self.mock_get_os_version.start()
        self.get_os_version.return_value = "7.0.2"
        self.mock_get_os_version1 = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.l2_interfaces.l2_interfaces.get_os_version"
        )
        self.get_os_version1 = self.mock_get_os_version1.start()
        self.get_os_version1.return_value = "7.0.2"
        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.l2_interfaces.l2_interfaces.L2_InterfacesFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrL2InterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_get_os_version.stop()
        self.get_os_version1.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_l2_interface_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_l2_interfaces_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        l2transport=True,
                        l2protocol=[dict(cpsv="tunnel")],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/3.900",
                        encapsulation=dict(dot1q=20, second_dot1q=40),
                    ),
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_l2_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        l2transport=True,
                        l2protocol=[dict(cpsv="tunnel")],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/3.900",
                        encapsulation=dict(dot1q=20, second_dot1q=40),
                    ),
                ],
                state="merged",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/1",
            "l2transport l2protocol cpsv tunnel",
            "interface GigabitEthernet0/0/0/3.900",
            "encapsulation dot1q 20 second-dot1q 40",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l2_interfaces_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        l2transport=True,
                        l2protocol=[dict(cpsv="drop")],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/1",
            "l2transport l2protocol cpsv drop",
            "no l2transport",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l2_interfaces_deleted(self):
        self._prepare()
        set_module_args(dict(state="deleted"))

        commands = [
            "interface GigabitEthernet0/0/0/1",
            "no l2transport",
            "interface GigabitEthernet0/0/0/3.900",
            "no encapsulation dot1q",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l2_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        l2transport=True,
                        l2protocol=[dict(cpsv="tunnel")],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/3.900",
                        encapsulation=dict(dot1q=20, second_dot1q=40),
                    ),
                ],
                state="rendered",
            )
        )

        commands = [
            "interface GigabitEthernet0/0/0/1",
            "l2transport l2protocol cpsv tunnel",
            "interface GigabitEthernet0/0/0/3.900",
            "encapsulation dot1q 20 second-dot1q 40",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_l2_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="interface GigabitEthernet0/0/0/1\n l2transport\n  l2protocol cpsv tunnel\n  "
                "propagate remote-status\n !",
                state="parsed",
            )
        )
        result = self.execute_module(changed=False)
        print(result["parsed"])
        parsed_list = [
            {
                "name": "GigabitEthernet0/0/0/1",
                "l2transport": True,
                "l2protocol": [{"cpsv": "tunnel"}],
                "propagate": True,
            }
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_l2_interfaces_overridden(self):
        self.maxDiff = None
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/4",
                        l2transport=True,
                        l2protocol=[dict(cpsv="tunnel")],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/3.900",
                        encapsulation=dict(dot1q=40, second_dot1q=60),
                    ),
                ],
                state="overridden",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/4",
            "l2transport l2protocol cpsv tunnel",
            "interface GigabitEthernet0/0/0/3.900",
            "encapsulation dot1q 40 second-dot1q 60",
            "interface GigabitEthernet0/0/0/1",
            "no l2transport",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
