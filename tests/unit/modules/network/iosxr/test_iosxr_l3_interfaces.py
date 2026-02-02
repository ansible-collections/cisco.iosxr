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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_l3_interfaces
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

    def _prepare(self, l3_interface_config):
        def load_from_file(*args, **kwargs):
            return load_fixture(l3_interface_config)

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_l3_interfaces_merged_idempotent(self):
        self._prepare("iosxr_l3_interface_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        ipv4=[dict(address="198.51.100.1/24")],
                        ipv6=[dict(address="2001:db8::/32")],
                        carrier_delay={"up": 100},
                        dampening={
                            "enabled": True,
                            "half_life": 10,
                            "reuse_threshold": 750,
                            "suppress_threshold": 3000,
                            "max_suppress_time": 60,
                            "restart_penalty": 1000,
                        },
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
                        carrier_delay={"down": 50},
                        dampening={
                            "enabled": True,
                            "half_life": 10,
                            "reuse_threshold": 750,
                        },
                        load_interval=30,
                        flow_control="ingress",
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
            "carrier-delay down 50",
            "dampening 10 750",
            "load-interval 30",
            "flow-control ingress",
            "ipv4 address 198.51.100.1 255.255.255.0",
            "interface GigabitEthernet0/0/0/1",
            "ipv4 address 192.0.2.2 255.255.255.0 secondary",
            "ipv4 address 192.0.2.1 255.255.255.0",
            "ipv6 address 2001:db8:0:3::/64",
        ]
        result = self.execute_module(changed=True)
        print(sorted(result["commands"]))
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_replaced(self):
        self._prepare("iosxr_l3_interface_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        ipv4=[
                            dict(address="203.0.113.27/24"),
                            dict(address="203.0.114.1/24", secondary=True),
                        ],
                        carrier_delay={"down": 100},
                        dampening={
                            "enabled": True,
                            "half_life": 20,
                            "reuse_threshold": 800,
                            "suppress_threshold": 3500,
                            "max_suppress_time": 120,
                            "restart_penalty": 1000,
                        },
                        load_interval=60,
                        flow_control="egress",
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv6 address",
            "no ipv4 address",
            "no carrier-delay",
            "no dampening",
            "ipv4 address 203.0.113.27 255.255.255.0",
            "ipv4 address 203.0.114.1 255.255.255.0 secondary",
            "carrier-delay down 100",
            "dampening 20 800 3500 120 1000",
            "load-interval 60",
            "flow-control egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_deleted(self):
        self._prepare("iosxr_l3_interface_config.cfg")
        set_module_args(dict(state="deleted"))

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no ipv6 address",
            "no carrier-delay",
            "no dampening",
            "interface GigabitEthernet0/0/0/1",
            "no ipv4 address",
        ]
        result = self.execute_module(changed=True)
        print(result["commands"])
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
                        carrier_delay={"up": 100},
                        dampening={
                            "enabled": True,
                            "half_life": 10,
                            "reuse_threshold": 750,
                            "suppress_threshold": 3000,
                            "max_suppress_time": 60,
                            "restart_penalty": 1000,
                        },
                        load_interval=30,
                        flow_control="ingress",
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
            "carrier-delay up 100",
            "dampening 10 750 3000 60 1000",
            "load-interval 30",
            "flow-control ingress",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_l3_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="interface GigabitEthernet0/0/0/0\nipv4 address 198.51.100.1 255.255.255.0\ncarrier-delay up 2 down 10\ndampening 3\n"
                "\nload-interval 4\nipv6 address 2001:db8::/32\ninterface GigabitEthernet0/0/0/1\nipv4 address"
                " 192.0.2.1 255.255.255.0\nipv4 address 192.0.2.2 255.255.255.0 secondary\nflow-control bidirectional\n",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "name": "GigabitEthernet0/0/0/0",
                "ipv4": [{"address": "198.51.100.1/24"}],
                "ipv6": [{"address": "2001:db8::/32"}],
                "carrier_delay": {"up": 2, "down": 10},
                "dampening": {
                    "enabled": True,
                    "half_life": 3,
                },
                "load_interval": 4,
            },
            {
                "name": "GigabitEthernet0/0/0/1",
                "ipv4": [
                    {"address": "192.0.2.1/24"},
                    {"address": "192.0.2.2/24", "secondary": True},
                ],
                "flow_control": "bidirectional",
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_l3_interfaces_overridden(self):
        self.maxDiff = None
        self._prepare("iosxr_l3_interface_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        ipv4=[dict(address="198.51.102.1/24")],
                        ipv6=[dict(address="2001:db8:1::/64")],
                        flow_control="bidirectional",
                        load_interval=120,
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no ipv6 address",
            "no carrier-delay",
            "no dampening",
            "interface GigabitEthernet0/0/0/1",
            "no ipv4 address",
            "ipv4 address 198.51.102.1 255.255.255.0",
            "ipv6 address 2001:db8:1::/64",
            "flow-control bidirectional",
            "load-interval 120",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_3_interfaces_gathered(self):
        self._prepare("iosxr_interface_gathered.cfg")
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered = [
            {"name": "GigabitEthernet0/0/0/5", "ipv4": [{"address": "10.255.2.9/30"}]},
            {"name": "GigabitEthernet0/0/0/6", "ipv4": [{"address": "10.255.2.17/30"}]},
        ]
        self.assertEqual(gathered, result["gathered"])

    def test_iosxr_l3_interfaces_flow_merged(self):
        self._prepare("iosxr_l3_interface_flow_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "MONITOR-A",
                                    "sampler": "SAMPLER-1",
                                    "direction": "ingress",
                                }
                            ],
                            "ipv6": [
                                {
                                    "monitor": "MONITOR-B",
                                    "sampler": "SAMPLER-2",
                                    "direction": "egress",
                                }
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_l3_interfaces_flow_merged_idempotent(self):
        self._prepare("iosxr_l3_interface_flow_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "MONITOR-A",
                                    "sampler": "SAMPLER-1",
                                    "direction": "ingress",
                                },
                            ],
                            "ipv6": [
                                {
                                    "monitor": "MONITOR-B",
                                    "sampler": "SAMPLER-2",
                                    "direction": "egress",
                                },
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_l3_interfaces_flow_replaced(self):
        self._prepare("iosxr_l3_interface_flow_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "MONITOR-REPLACED",
                                    "sampler": "SAMPLER-REPLACED",
                                    "direction": "egress",
                                },
                            ],
                        },
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no flow ipv6 monitor MONITOR-B sampler SAMPLER-2 egress",
            "no flow ipv4 monitor MONITOR-A sampler SAMPLER-1 ingress",
            "flow ipv4 monitor MONITOR-REPLACED sampler SAMPLER-REPLACED egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_deleted(self):
        """Test flow parameter in deleted state"""
        self._prepare("iosxr_l3_interface_flow_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                    ),
                ],
                state="deleted",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no flow ipv4 monitor MONITOR-A sampler SAMPLER-1 ingress",
            "no flow ipv6 monitor MONITOR-B sampler SAMPLER-2 egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_overridden(self):
        self._prepare("iosxr_l3_interface_flow_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "OVERRIDE-MONITOR",
                                    "sampler": "OVERRIDE-SAMPLER",
                                    "direction": "ingress",
                                },
                            ],
                        },
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no flow ipv4 monitor MONITOR-A sampler SAMPLER-1 ingress",
            "no flow ipv6 monitor MONITOR-B sampler SAMPLER-2 egress",
            "interface GigabitEthernet0/0/0/1",
            "no ipv4 address",
            "flow ipv4 monitor OVERRIDE-MONITOR sampler OVERRIDE-SAMPLER ingress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_gathered_bidirectional(self):
        """Test gathered state: gather config with bidirectional flow"""
        self._prepare("iosxr_l3_interface_flow_gathered_bidirectional.cfg")
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gathered = [
            {
                "name": "Bundle-Ether90.3201",
                "ipv4": [{"address": "10.176.248.168/31"}],
                "load_interval": 30,
                "flow": {
                    "ipv4": [
                        {
                            "monitor": "FlowMap-IPv4",
                            "sampler": "NETFLOW_1in2000",
                            "direction": "ingress",
                        },
                        {
                            "monitor": "FlowMap-IPv4",
                            "sampler": "NETFLOW_1in2000",
                            "direction": "egress",
                        },
                    ],
                },
            },
            {
                "name": "Bundle-Ether90.3202",
                "ipv4": [{"address": "10.176.248.172/31"}],
                "ipv6": [{"address": "fd10:0:4620:4001::2/127"}],
                "load_interval": 30,
                "flow": {
                    "ipv4": [
                        {
                            "monitor": "FlowMap-IPv4",
                            "sampler": "NETFLOW_1in2000",
                            "direction": "ingress",
                        },
                        {
                            "monitor": "FlowMap-IPv4",
                            "sampler": "NETFLOW_1in2000",
                            "direction": "egress",
                        },
                    ],
                    "ipv6": [
                        {
                            "monitor": "FlowMap-IPv6",
                            "sampler": "NETFLOW_1in2000",
                            "direction": "ingress",
                        },
                        {
                            "monitor": "FlowMap-IPv6",
                            "sampler": "NETFLOW_1in2000",
                            "direction": "egress",
                        },
                    ],
                },
            },
        ]
        self.assertEqual(gathered, result["gathered"])

    def test_iosxr_l3_interfaces_flow_bidirectional_merged(self):
        """Test bidirectional flow in merged state - should add both ingress and egress"""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "MONITOR-BIDIR",
                                    "sampler": "SAMPLER-BIDIR",
                                    "direction": "bidirectional",
                                },
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "flow ipv4 monitor MONITOR-BIDIR sampler SAMPLER-BIDIR ingress",
            "flow ipv4 monitor MONITOR-BIDIR sampler SAMPLER-BIDIR egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_bidirectional_both_protocols(self):
        """Test bidirectional flow for both IPv4 and IPv6"""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "FlowMap-IPv4",
                                    "sampler": "NETFLOW_1in2000",
                                    "direction": "bidirectional",
                                },
                            ],
                            "ipv6": [
                                {
                                    "monitor": "FlowMap-IPv6",
                                    "sampler": "NETFLOW_1in2000",
                                    "direction": "bidirectional",
                                },
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "flow ipv4 monitor FlowMap-IPv4 sampler NETFLOW_1in2000 ingress",
            "flow ipv4 monitor FlowMap-IPv4 sampler NETFLOW_1in2000 egress",
            "flow ipv6 monitor FlowMap-IPv6 sampler NETFLOW_1in2000 ingress",
            "flow ipv6 monitor FlowMap-IPv6 sampler NETFLOW_1in2000 egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_bidirectional_replaced(self):
        self._prepare("iosxr_l3_interface_flow_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "NEW-MONITOR",
                                    "sampler": "NEW-SAMPLER",
                                    "direction": "bidirectional",
                                },
                            ],
                        },
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no flow ipv4 monitor MONITOR-A sampler SAMPLER-1 ingress",
            "no flow ipv6 monitor MONITOR-B sampler SAMPLER-2 egress",
            "flow ipv4 monitor NEW-MONITOR sampler NEW-SAMPLER ingress",
            "flow ipv4 monitor NEW-MONITOR sampler NEW-SAMPLER egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_bidirectional_idempotent(self):
        """Test bidirectional is idempotent when both ingress and egress already exist"""
        self._prepare("iosxr_l3_interface_flow_gathered_bidirectional.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether90.3201",
                        ipv4=[{"address": "10.176.248.168/31"}],
                        load_interval=30,
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "FlowMap-IPv4",
                                    "sampler": "NETFLOW_1in2000",
                                    "direction": "bidirectional",
                                },
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        result = self.execute_module(changed=False, commands=[])

    def test_iosxr_l3_interfaces_flow_mixed_directions(self):
        """Test mixing bidirectional with explicit directions"""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "MONITOR-BIDIR",
                                    "sampler": "SAMPLER-1",
                                    "direction": "bidirectional",
                                },
                            ],
                            "ipv6": [
                                {
                                    "monitor": "MONITOR-IPV6",
                                    "sampler": "SAMPLER-2",
                                    "direction": "ingress",
                                },
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "flow ipv4 monitor MONITOR-BIDIR sampler SAMPLER-1 ingress",
            "flow ipv4 monitor MONITOR-BIDIR sampler SAMPLER-1 egress",
            "flow ipv6 monitor MONITOR-IPV6 sampler SAMPLER-2 ingress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_bidirectional_partial_update(self):
        """Test bidirectional when only one direction exists - should add missing direction"""
        self._prepare("iosxr_l3_interface_flow_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        ipv4=[{"address": "198.51.100.1/24"}],
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "MONITOR-A",
                                    "sampler": "SAMPLER-1",
                                    "direction": "bidirectional",
                                },
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "flow ipv4 monitor MONITOR-A sampler SAMPLER-1 egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_bidirectional_overridden(self):
        """Test bidirectional in overridden state"""
        self._prepare("iosxr_l3_interface_flow_config.cfg")
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "OVERRIDE-BIDIR",
                                    "sampler": "OVERRIDE-SAMPLER",
                                    "direction": "bidirectional",
                                },
                            ],
                        },
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 address",
            "no flow ipv4 monitor MONITOR-A sampler SAMPLER-1 ingress",
            "no flow ipv6 monitor MONITOR-B sampler SAMPLER-2 egress",
            "interface GigabitEthernet0/0/0/1",
            "no ipv4 address",
            "flow ipv4 monitor OVERRIDE-BIDIR sampler OVERRIDE-SAMPLER ingress",
            "flow ipv4 monitor OVERRIDE-BIDIR sampler OVERRIDE-SAMPLER egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_bidirectional_multiple_monitors(self):
        """Test multiple flow monitors with bidirectional and explicit directions"""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "MONITOR-1",
                                    "sampler": "SAMPLER-1",
                                    "direction": "bidirectional",
                                },
                                {
                                    "monitor": "MONITOR-2",
                                    "sampler": "SAMPLER-2",
                                    "direction": "ingress",
                                },
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "flow ipv4 monitor MONITOR-1 sampler SAMPLER-1 ingress",
            "flow ipv4 monitor MONITOR-1 sampler SAMPLER-1 egress",
            "flow ipv4 monitor MONITOR-2 sampler SAMPLER-2 ingress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_bidirectional_rendered(self):
        """Test bidirectional in rendered state"""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        ipv4=[{"address": "192.0.2.1/24"}],
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "FlowMap-IPv4",
                                    "sampler": "NETFLOW_1in2000",
                                    "direction": "bidirectional",
                                },
                            ],
                        },
                    ),
                ],
                state="rendered",
            ),
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "ipv4 address 192.0.2.1 255.255.255.0",
            "flow ipv4 monitor FlowMap-IPv4 sampler NETFLOW_1in2000 ingress",
            "flow ipv4 monitor FlowMap-IPv4 sampler NETFLOW_1in2000 egress",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_l3_interfaces_flow_bidirectional_real_world_scenario(self):
        """Test real-world scenario from GitHub issue with bidirectional"""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Bundle-Ether90.3202",
                        ipv4=[{"address": "10.176.248.172/31"}],
                        ipv6=[{"address": "fd10:0:4620:4001::2/127"}],
                        load_interval=30,
                        flow={
                            "ipv4": [
                                {
                                    "monitor": "FlowMap-IPv4",
                                    "sampler": "NETFLOW_1in2000",
                                    "direction": "bidirectional",
                                },
                            ],
                            "ipv6": [
                                {
                                    "monitor": "FlowMap-IPv6",
                                    "sampler": "NETFLOW_1in2000",
                                    "direction": "bidirectional",
                                },
                            ],
                        },
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "interface Bundle-Ether90.3202",
            "ipv4 address 10.176.248.172 255.255.255.254",
            "ipv6 address fd10:0:4620:4001::2/127",
            "load-interval 30",
            "flow ipv4 monitor FlowMap-IPv4 sampler NETFLOW_1in2000 ingress",
            "flow ipv4 monitor FlowMap-IPv4 sampler NETFLOW_1in2000 egress",
            "flow ipv6 monitor FlowMap-IPv6 sampler NETFLOW_1in2000 ingress",
            "flow ipv6 monitor FlowMap-IPv6 sampler NETFLOW_1in2000 egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
