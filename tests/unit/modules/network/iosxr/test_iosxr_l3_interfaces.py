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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_l3_interfaces
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrL3InterfacesModule(TestIosxrModule):
    module = iosxr_l3_interfaces

    def setUp(self):
        super(TestIosxrL3InterfacesModule, self).setUp()

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
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.l3_interfaces.l3_interfaces.L3_InterfacesFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrL3InterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_l3_interface_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_l3_interfaces_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        ipv4=[dict(address="198.51.100.1/24")],
                        ipv6=[dict(address="2001:db8::/32")],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        ipv4=[
                            dict(address="192.0.2.1/24"),
                            dict(address="192.0.2.2/24", secondary=True),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_l3_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        ipv4=[dict(address="198.51.100.1/24")],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        ipv4=[
                            dict(address="192.0.2.1/24"),
                            dict(address="192.0.2.2/24", secondary=True),
                        ],
                        ipv6=[dict(address="2001:db8:0:3::/64")],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "ipv4 address 198.51.100.1 255.255.255.0",
            "interface GigabitEthernet0/0/0/1",
            "ipv4 address 192.0.2.2 255.255.255.0 secondary",
            "ipv4 address 192.0.2.1 255.255.255.0",
            "ipv6 address 2001:db8:0:3::/64",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        ipv4=[
                            dict(address="203.0.113.27/24"),
                            dict(address="203.0.114.1/24", secondary=True),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv6 address",
            "ipv4 address 203.0.113.27 255.255.255.0",
            "ipv4 address 203.0.114.1 255.255.255.0 secondary",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_deleted(self):
        self._prepare()
        set_module_args(dict(state="deleted"))

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no ipv6 address",
            "interface GigabitEthernet0/0/0/1",
            "no ipv4 address",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        ipv4=[dict(address="198.51.100.1/24")],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        ipv4=[
                            dict(address="192.0.2.1/24"),
                            dict(address="192.0.2.2/24", secondary=True),
                        ],
                        ipv6=[dict(address="2001:db8:0:3::/64")],
                    ),
                ],
                state="rendered",
            ),
        )

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "ipv4 address 198.51.100.1 255.255.255.0",
            "interface GigabitEthernet0/0/0/1",
            "ipv4 address 192.0.2.2 255.255.255.0 secondary",
            "ipv4 address 192.0.2.1 255.255.255.0",
            "ipv6 address 2001:db8:0:3::/64",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_l3_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="interface GigabitEthernet0/0/0/0\nipv4 address 198.51.100.1 255.255.255.0\n"
                "ipv6 address 2001:db8::/32\ninterface GigabitEthernet0/0/0/1\nipv4 address"
                " 192.0.2.1 255.255.255.0\nipv4 address 192.0.2.2 255.255.255.0 secondary\n",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        print(result["parsed"])
        parsed_list = [
            {
                "name": "GigabitEthernet0/0/0/0",
                "ipv4": [{"address": "198.51.100.1 255.255.255.0"}],
                "ipv6": [{"address": "2001:db8::/32"}],
            },
            {
                "name": "GigabitEthernet0/0/0/1",
                "ipv4": [
                    {"address": "192.0.2.1 255.255.255.0"},
                    {"address": "192.0.2.2 255.255.255.0", "secondary": True},
                ],
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_l3_interfaces_overridden(self):
        self.maxDiff = None
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        ipv4=[dict(address="198.51.102.1/24")],
                        ipv6=[dict(address="2001:db8:1::/64")],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no ipv6 address",
            "interface GigabitEthernet0/0/0/1",
            "no ipv4 address",
            "ipv4 address 198.51.102.1 255.255.255.0",
            "ipv6 address 2001:db8:1::/64",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
