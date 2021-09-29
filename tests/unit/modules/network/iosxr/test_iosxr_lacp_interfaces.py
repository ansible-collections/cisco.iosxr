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
from ansible_collections.cisco.iosxr.plugins.modules import (
    iosxr_lacp_interfaces,
)
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import (
    set_module_args,
)
from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrLacpInterfacesModule(TestIosxrModule):
    module = iosxr_lacp_interfaces

    def setUp(self):
        super(TestIosxrLacpInterfacesModule, self).setUp()

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
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lacp_interfaces.lacp_interfaces.Lacp_interfacesFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrLacpInterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_lacp_interfaces_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_lacp_interfaces_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether10",
                        churn_logging="actor",
                        collector_max_delay=100,
                        switchover_suppress_flaps=500,
                    ),
                    dict(
                        name="Bundle-Ether11",
                        system=dict(mac="00c2.4c00.bd15"),
                    ),
                    dict(name="GigabitEthernet0/0/0/1", period=200),
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_lacp_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether10",
                        churn_logging="actor",
                        collector_max_delay=100,
                        switchover_suppress_flaps=500,
                    ),
                    dict(
                        name="Bundle-Ether11",
                        system=dict(mac="00c2.4c00.bd15"),
                    ),
                    dict(name="GigabitEthernet0/0/0/1", period=100),
                ],
                state="merged",
            )
        )
        commands = [
            "interface Bundle-Ether10",
            "lacp churn logging actor",
            "lacp switchover suppress-flaps 500",
            "lacp collector-max-delay 100",
            "interface Bundle-Ether11",
            "lacp system mac 00c2.4c00.bd15",
            "interface GigabitEthernet0/0/0/1",
            "lacp period 100",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lacp_interfaces_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(name="Bundle-Ether10", churn_logging="partner"),
                    dict(name="GigabitEthernet0/0/0/1", period=300),
                ],
                state="replaced",
            )
        )
        commands = [
            "interface Bundle-Ether10",
            "no lacp switchover suppress-flaps 500",
            "no lacp collector-max-delay 100",
            "lacp churn logging partner",
            "interface GigabitEthernet0/0/0/1",
            "lacp period 300",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lacp_interfaces_deleted(self):
        self._prepare()
        set_module_args(dict(state="deleted"))

        commands = [
            "interface Bundle-Ether10",
            "no lacp switchover suppress-flaps 500",
            "no lacp collector-max-delay 100",
            "no lacp churn logging actor",
            "interface Bundle-Ether11",
            "no lacp system mac 00c2.4c00.bd15",
            "interface GigabitEthernet0/0/0/1",
            "no lacp period 200",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lag_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether10",
                        churn_logging="actor",
                        collector_max_delay=100,
                        switchover_suppress_flaps=500,
                    ),
                    dict(
                        name="Bundle-Ether11",
                        system=dict(mac="00c2.4c00.bd15"),
                    ),
                    dict(name="GigabitEthernet0/0/0/1", period=100),
                ],
                state="rendered",
            )
        )

        commands = [
            "interface Bundle-Ether10",
            "lacp churn logging actor",
            "lacp switchover suppress-flaps 500",
            "lacp collector-max-delay 100",
            "interface Bundle-Ether11",
            "lacp system mac 00c2.4c00.bd15",
            "interface GigabitEthernet0/0/0/1",
            "lacp period 100",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_lacp_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="interface Bundle-Ether10\r\n lacp churn logging actor\r\n lacp"
                " switchover suppress-flaps 500\r\n "
                "lacp collector-max-delay 100\r\n!\r\ninterface "
                "Bundle-Ether11\r\n lacp system mac 00c2.4c00.bd15\r"
                "\n!\r\ninterface MgmtEth0/RP0/CPU0/0\r\n ipv4 address"
                " 192.0.2.11 255.255.255.0\r\n!\r\ninterface "
                "GigabitEthernet0/0/0/1\r\n lacp period 200\r\n!",
                state="parsed",
            )
        )
        result = self.execute_module(changed=False)
        print(result["parsed"])
        parsed_list = [
            {
                "churn_logging": "actor",
                "collector_max_delay": 100,
                "name": "Bundle-Ether10",
                "switchover_suppress_flaps": 500,
            },
            {"name": "Bundle-Ether11", "system": {"mac": "00c2.4c00.bd15"}},
            {"name": "GigabitEthernet0/0/0/1", "period": 200},
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_lag_interfaces_overridden(self):
        self.maxDiff = None
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether12",
                        churn_logging="both",
                        collector_max_delay=100,
                        switchover_suppress_flaps=500,
                    ),
                    dict(name="GigabitEthernet0/0/0/1", period=300),
                ],
                state="overridden",
            )
        )
        commands = [
            "interface Bundle-Ether10",
            "no lacp switchover suppress-flaps 500",
            "no lacp collector-max-delay 100",
            "no lacp churn logging actor",
            "interface Bundle-Ether11",
            "no lacp system mac 00c2.4c00.bd15",
            "interface Bundle-Ether12",
            "lacp churn logging both",
            "lacp collector-max-delay 100",
            "lacp switchover suppress-flaps 500",
            "interface GigabitEthernet0/0/0/1",
            "lacp period 300",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
