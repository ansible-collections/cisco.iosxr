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

from unittest.mock import patch

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_lldp_interfaces
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrLldpInterfacesModule(TestIosxrModule):
    module = iosxr_lldp_interfaces

    def setUp(self):
        super(TestIosxrLldpInterfacesModule, self).setUp()

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
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lldp_interfaces.lldp_interfaces.Lldp_interfacesFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrLldpInterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_lldp_interfaces_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_lldp_interfaces_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(name="GigabitEthernet0/0/0/0", transmit=False),
                    dict(name="GigabitEthernet0/0/0/1", receive=False),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_lldp_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(name="GigabitEthernet0/0/0/0", transmit=False),
                    dict(name="GigabitEthernet0/0/0/1", receive=False),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "lldp transmit disable",
            "interface GigabitEthernet0/0/0/1",
            "lldp receive disable",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lldp_interfaces_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=[dict(name="GigabitEthernet0/0/0/1", transmit=False)],
                state="replaced",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/1",
            "no lldp receive disable",
            "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
            "lldp transmit disable",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lldp_interfaces_deleted(self):
        self._prepare()
        set_module_args(dict(state="deleted"))

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no lldp transmit disable",
            "no lldp destination mac-address ieee-nearest-bridge",
            "interface GigabitEthernet0/0/0/1",
            "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
            "no lldp receive disable",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lldp_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(name="GigabitEthernet0/0/0/0", transmit=False),
                    dict(name="GigabitEthernet0/0/0/1", receive=False),
                ],
                state="rendered",
            ),
        )

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "lldp transmit disable",
            "interface GigabitEthernet0/0/0/1",
            "lldp receive disable",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_lldp_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="interface TenGigE0/0/0/0\r\n ipv4 address 192.0.2.11 255.255.255.192\r\n!\r\ninterface preconfigure "
                "GigabitEthernet0/0/0/0\r\n lldp\r\n  transmit disable\r\n  destination mac-address\r\n   "
                "ieee-nearest-bridge\r\n  !\r\n !\r\n!\r\ninterface preconfigure GigabitEthernet0/0/0/1\r\n lldp\r\n  "
                "receive disable\r\n  destination mac-address\r\n   ieee-nearest-non-tmpr-bridge\r\n",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            {"name": "TenGigE0/0/0/0"},
            {
                "destination": {"mac_address": "ieee-nearest-bridge"},
                "name": "GigabitEthernet0/0/0/0",
                "transmit": False,
            },
            {
                "destination": {"mac_address": "ieee-nearest-non-tmpr-bridge"},
                "name": "GigabitEthernet0/0/0/1",
                "receive": False,
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_lldp_interfaces_overridden(self):
        self.maxDiff = None
        self._prepare()
        set_module_args(
            dict(
                config=[dict(name="GigabitEthernet0/0/0/0", transmit=False)],
                state="overridden",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/1",
            "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
            "no lldp receive disable",
            "interface GigabitEthernet0/0/0/0",
            "no lldp destination mac-address ieee-nearest-bridge",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
