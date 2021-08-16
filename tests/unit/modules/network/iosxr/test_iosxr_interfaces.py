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
from ansible_collections.cisco.iosxr.plugins.modules import iosxr_interfaces
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import (
    set_module_args,
)
from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrInterfacesModule(TestIosxrModule):
    module = iosxr_interfaces

    def setUp(self):
        super(TestIosxrInterfacesModule, self).setUp()

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

        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.interfaces.interfaces.InterfacesFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrInterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_interface_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_interfaces_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        description="Configured and Merged by Ansible-Network",
                        mtu=110,
                        enabled=True,
                        duplex="half",
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        description="Configured and Merged by Ansible-Network",
                        mtu=2800,
                        speed=100,
                    ),
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        description="Configured and Merged by Ansible-Network",
                        mtu=110,
                        enabled=True,
                        duplex="half",
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        description="Configured and Merged by Ansible-Network",
                        mtu=2800,
                        enabled=False,
                        duplex="full",
                        speed=100,
                    ),
                ],
                state="merged",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "description Configured and Merged by Ansible-Network",
            "mtu 110",
            "duplex half",
            "no shutdown",
            "interface GigabitEthernet0/0/0/1",
            "description Configured and Merged by Ansible-Network",
            "mtu 2800",
            "speed 100",
            "duplex full",
            "shutdown",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_interfaces_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        description="Configured and Replaced by Ansible-Network",
                        mtu=110,
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        description="Configured and Replaced by Ansible-Network",
                        speed=100,
                    ),
                ],
                state="replaced",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "description Configured and Replaced by Ansible-Network",
            "no duplex",
            "interface GigabitEthernet0/0/0/1",
            "description Configured and Replaced by Ansible-Network",
            "no mtu",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_interfaces_deleted(self):
        self._prepare()
        set_module_args(dict(state="deleted"))

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no description",
            "no mtu",
            "no duplex",
            "interface GigabitEthernet0/0/0/1",
            "no description",
            "no speed",
            "no mtu",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        description="Configured and Merged by Ansible-Network",
                        mtu=110,
                        enabled=True,
                        duplex="half",
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        description="Configured and Merged by Ansible-Network",
                        mtu=2800,
                        enabled=False,
                        duplex="full",
                        speed=100,
                    ),
                ],
                state="rendered",
            )
        )

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "description Configured and Merged by Ansible-Network",
            "mtu 110",
            "duplex half",
            "no shutdown",
            "interface GigabitEthernet0/0/0/1",
            "description Configured and Merged by Ansible-Network",
            "mtu 2800",
            "speed 100",
            "duplex full",
            "shutdown",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="interface GigabitEthernet0/0/0/0\n description Configured and Merged by Ansible-Network\n "
                "mtu 110\n duplex half\ninterface GigabitEthernet0/0/0/1\n "
                "description Configured and Merged by Ansible-Network\n no shutdown\n mtu 2800\n speed 100",
                state="parsed",
            )
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "description": "Configured and Merged by Ansible-Network",
                "duplex": "half",
                "enabled": True,
                "mtu": 110,
                "name": "GigabitEthernet0/0/0/0",
            },
            {
                "description": "Configured and Merged by Ansible-Network",
                "enabled": True,
                "mtu": 2800,
                "name": "GigabitEthernet0/0/0/1",
                "speed": 100,
            },
        ]

        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_interfaces_overridden(self):
        self.maxDiff = None
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        description="Configured and Overridden by Ansible-Network",
                        mtu=2000,
                        enabled=False,
                        duplex="full",
                        speed=100,
                    )
                ],
                state="overridden",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no description",
            "no mtu",
            "no duplex",
            "interface GigabitEthernet0/0/0/1",
            "description Configured and Overridden by Ansible-Network",
            "mtu 2000",
            "duplex full",
            "shutdown",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
