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

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent
from unittest.mock import patch

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_vrf_interfaces
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrVrfInterfacesModule(TestIosxrModule):
    module = iosxr_vrf_interfaces

    def setUp(self):
        super(TestIosxrVrfInterfacesModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.vrf_interfaces.vrf_interfaces."
            "Vrf_interfacesFacts.get_device_data",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrVrfInterfacesModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_vrf_interfaces_merged_idempotent(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                interface Loopback888
                 description test for ansible
                 shutdown
                !
                interface Loopback999
                !
                interface MgmtEth0/RP0/CPU0/0
                 ipv4 address dhcp
                !
                interface GigabitEthernet0/0/0/0
                 description this is interface0
                 cdp
                !
                interface GigabitEthernet0/0/0/1
                 vrf testvrf1
                 shutdown
                !
                interface GigabitEthernet0/0/0/2
                 vrf testvrf_12
                 shutdown
                !
                interface preconfigure GigabitEthernet0/0/0/7
                 description test interface
                 ipv4 address 172.31.1.1 255.255.255.0
                !
                interface preconfigure TenGigE0/0/0/0
                 service-policy output mypolicy
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    {"name": "Loopback888"},
                    {"name": "Loopback999"},
                    {"name": "MgmtEth0/RP0/CPU0/0"},
                    {"name": "GigabitEthernet0/0/0/0"},
                    {"name": "GigabitEthernet0/0/0/1", "vrf_name": "testvrf1"},
                    {"name": "GigabitEthernet0/0/0/2", "vrf_name": "testvrf_12"},
                    {"name": "GigabitEthernet0/0/0/7"},
                    {"name": "TenGigE0/0/0/0"},
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_vrf_interfaces_merged(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                interface Loopback888
                 description test for ansible
                 shutdown
                !
                interface Loopback999
                !
                interface MgmtEth0/RP0/CPU0/0
                 ipv4 address dhcp
                !
                interface GigabitEthernet0/0/0/0
                 description this is interface0
                 cdp
                !
                interface GigabitEthernet0/0/0/1
                 vrf testvrf1
                 shutdown
                !
                interface GigabitEthernet0/0/0/2
                 vrf testvrf_12
                 shutdown
                !
                interface preconfigure GigabitEthernet0/0/0/7
                 description test interface
                 ipv4 address 172.31.1.1 255.255.255.0
                !
                interface preconfigure TenGigE0/0/0/0
                 service-policy output mypolicy
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    {"name": "Loopback888"},
                    {"name": "Loopback999"},
                    {"name": "MgmtEth0/RP0/CPU0/0"},
                    {"name": "GigabitEthernet0/0/0/0"},
                    {"name": "GigabitEthernet0/0/0/1", "vrf_name": "testvrf1"},
                    {"name": "GigabitEthernet0/0/0/2", "vrf_name": "testvrf_12"},
                    {"name": "GigabitEthernet0/0/0/7"},
                    {"name": "TenGigE0/0/0/0", "vrf_name": "testvrf_12"},
                ],
                state="merged",
            ),
        )
        commands = [
            "interface TenGigE0/0/0/0",
            "vrf testvrf_12",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_interfaces_replaced(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                interface Loopback888
                 description test for ansible
                 shutdown
                !
                interface Loopback999
                !
                interface MgmtEth0/RP0/CPU0/0
                 ipv4 address dhcp
                !
                interface GigabitEthernet0/0/0/0
                 description this is interface0
                 cdp
                !
                interface GigabitEthernet0/0/0/1
                 vrf testvrf1
                 shutdown
                !
                interface GigabitEthernet0/0/0/2
                 vrf testvrf_12
                 shutdown
                !
                interface preconfigure GigabitEthernet0/0/0/7
                 description test interface
                 ipv4 address 172.31.1.1 255.255.255.0
                !
                interface preconfigure TenGigE0/0/0/0
                 service-policy output mypolicy
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    {"name": "Loopback888"},
                    {"name": "Loopback999"},
                    {"name": "MgmtEth0/RP0/CPU0/0"},
                    {"name": "GigabitEthernet0/0/0/0"},
                    {"name": "GigabitEthernet0/0/0/1", "vrf_name": "testvrf_replaced"},
                    {"name": "GigabitEthernet0/0/0/2", "vrf_name": "testvrf_12"},
                    {"name": "GigabitEthernet0/0/0/7"},
                    {"name": "TenGigE0/0/0/0", "vrf_name": "testvrf_12"},
                ],
                state="replaced",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/1",
            "vrf testvrf_replaced",
            "interface TenGigE0/0/0/0",
            "vrf testvrf_12",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_interfaces_overridden(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                interface Loopback888
                 description test for ansible
                 shutdown
                !
                interface Loopback999
                !
                interface MgmtEth0/RP0/CPU0/0
                 ipv4 address dhcp
                !
                interface GigabitEthernet0/0/0/0
                 description this is interface0
                 cdp
                !
                interface GigabitEthernet0/0/0/1
                 vrf testvrf1
                 shutdown
                !
                interface GigabitEthernet0/0/0/2
                 vrf testvrf_12
                 shutdown
                !
                interface preconfigure GigabitEthernet0/0/0/7
                 description test interface
                 ipv4 address 172.31.1.1 255.255.255.0
                !
                interface preconfigure TenGigE0/0/0/0
                 service-policy output mypolicy
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    {"name": "Loopback888"},
                    {"name": "Loopback999"},
                    {"name": "MgmtEth0/RP0/CPU0/0"},
                    {"name": "GigabitEthernet0/0/0/0"},
                    {"name": "GigabitEthernet0/0/0/1"},
                    {"name": "GigabitEthernet0/0/0/2"},
                    {"name": "GigabitEthernet0/0/0/7"},
                    {"name": "TenGigE0/0/0/0", "vrf_name": "testvrf_12"},
                ],
                state="overridden",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/1",
            "no vrf testvrf1",
            "interface GigabitEthernet0/0/0/2",
            "no vrf testvrf_12",
            "interface TenGigE0/0/0/0",
            "vrf testvrf_12",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_interfaces_deleted(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                interface Loopback888
                 description test for ansible
                 shutdown
                !
                interface Loopback999
                !
                interface MgmtEth0/RP0/CPU0/0
                 ipv4 address dhcp
                !
                interface GigabitEthernet0/0/0/0
                 description this is interface0
                 cdp
                !
                interface GigabitEthernet0/0/0/1
                 vrf testvrf1
                 shutdown
                !
                interface GigabitEthernet0/0/0/2
                 vrf testvrf_12
                 shutdown
                !
                interface preconfigure GigabitEthernet0/0/0/7
                 description test interface
                 ipv4 address 172.31.1.1 255.255.255.0
                !
                interface preconfigure TenGigE0/0/0/0
                 service-policy output mypolicy
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    {"name": "Loopback888"},
                    {"name": "Loopback999"},
                    {"name": "MgmtEth0/RP0/CPU0/0"},
                    {"name": "GigabitEthernet0/0/0/0"},
                    {"name": "GigabitEthernet0/0/0/1", "vrf_name": "testvrf_replaced"},
                    {"name": "GigabitEthernet0/0/0/2", "vrf_name": "testvrf_12"},
                    {"name": "GigabitEthernet0/0/0/7"},
                    {"name": "TenGigE0/0/0/0", "vrf_name": "testvrf_12"},
                ],
                state="deleted",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/1",
            "no vrf testvrf1",
            "interface GigabitEthernet0/0/0/2",
            "no vrf testvrf_12",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_interfaces_parsed(self):
        set_module_args(
            dict(
                running_config=dedent(
                    """\
                        interface Loopback888
                         description test for ansible
                         shutdown
                        !
                        interface Loopback999
                        !
                        interface MgmtEth0/RP0/CPU0/0
                         ipv4 address dhcp
                        !
                        interface GigabitEthernet0/0/0/0
                         description this is interface0
                         cdp
                        !
                        interface GigabitEthernet0/0/0/1
                         vrf testvrf1
                         shutdown
                        !
                        interface GigabitEthernet0/0/0/2
                         vrf testvrf_12
                         shutdown
                        !
                        interface preconfigure GigabitEthernet0/0/0/7
                         description test interface
                         ipv4 address 172.31.1.1 255.255.255.0
                        !
                        interface preconfigure TenGigE0/0/0/0
                         service-policy output mypolicy
                        !
                    """,
                ),
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            {"name": "Loopback888"},
            {"name": "Loopback999"},
            {"name": "MgmtEth0/RP0/CPU0/0"},
            {"name": "GigabitEthernet0/0/0/0"},
            {"name": "GigabitEthernet0/0/0/1", "vrf_name": "testvrf1"},
            {"name": "GigabitEthernet0/0/0/2", "vrf_name": "testvrf_12"},
            {"name": "GigabitEthernet0/0/0/7"},
            {"name": "TenGigE0/0/0/0"},
        ]
        self.assertEqual(parsed_list, result["parsed"])
