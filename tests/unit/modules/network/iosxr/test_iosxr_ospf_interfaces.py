#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.plugins.modules import (
    iosxr_ospf_interfaces,
)
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import (
    set_module_args,
)
from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrOspf_InterfacesModule(TestIosxrModule):
    module = iosxr_ospf_interfaces

    def setUp(self):
        super(TestIosxrOspf_InterfacesModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config"
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config"
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base."
            "get_resource_connection"
        )
        self.get_resource_connection_config = (
            self.mock_get_resource_connection_config.start()
        )

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module."
            "get_resource_connection"
        )
        self.get_resource_connection_facts = (
            self.mock_get_resource_connection_facts.start()
        )

        self.mock_edit_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.providers.providers.CliProvider.edit_config"
        )
        self.edit_config = self.mock_edit_config.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.ospf_interfaces.ospf_interfaces."
            "Ospf_interfacesFacts.get_ospf_interfaces"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrOspf_InterfacesModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_edit_config.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(self, commands=None):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_ospf_interfaces.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_ospf_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        type="gigabitethernet",
                        address_family=[
                            dict(
                                afi="ipv4",
                                processes=[
                                    dict(
                                        process_id="LAB1",
                                        area=dict(area_id="0.0.0.3"),
                                    )
                                ],
                                cost=10,
                                authentication=dict(
                                    message_digest=dict(keychain="iosxr")
                                ),
                            )
                        ],
                    )
                ],
                state="merged",
            )
        )
        commands = [
            "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 cost 10",
            "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 authentication message-digest",
            "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 authentication message-digest keychain iosxr",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospf_interfaces_merged_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        type="gigabitethernet",
                        address_family=[
                            dict(
                                afi="ipv4",
                                processes=[
                                    dict(
                                        process_id="LAB3",
                                        area=dict(area_id="0.0.0.3"),
                                    )
                                ],
                                cost=20,
                                authentication=dict(
                                    message_digest=dict(keychain="cisco")
                                ),
                            )
                        ],
                    )
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_ospf_interfaces_replaced(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        type="gigabitethernet",
                        address_family=[
                            dict(
                                afi="ipv4",
                                processes=[
                                    dict(
                                        process_id="LAB3",
                                        area=dict(area_id="0.0.0.3"),
                                    )
                                ],
                                cost=40,
                                authentication=dict(
                                    message_digest=dict(keychain="ciscoiosxr")
                                ),
                            )
                        ],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 cost 40",
            "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 authentication message-digest",
            "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 authentication message-digest keychain ciscoiosxr",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospf_interfaces_replaced_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        type="gigabitethernet",
                        address_family=[
                            dict(
                                afi="ipv4",
                                processes=[
                                    dict(
                                        process_id="LAB3",
                                        area=dict(area_id="0.0.0.3"),
                                    )
                                ],
                                cost=20,
                                authentication=dict(
                                    message_digest=dict(keychain="cisco")
                                ),
                            )
                        ],
                    )
                ],
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_ospf_interfaces_overridden(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/4",
                        type="gigabitethernet",
                        address_family=[
                            dict(
                                afi="ipv4",
                                processes=[
                                    dict(
                                        process_id="LAB4",
                                        area=dict(area_id="0.0.0.4"),
                                    )
                                ],
                                cost=40,
                                authentication=dict(
                                    message_digest=dict(keychain="iosxr")
                                ),
                            )
                        ],
                    )
                ],
                state="overridden",
            )
        )

        commands = [
            "no router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0",
            "router ospf LAB4 area 0.0.0.4 interface GigabitEthernet 0/0/0/4 cost 40",
            "router ospf LAB4 area 0.0.0.4 interface GigabitEthernet 0/0/0/4 authentication message-digest",
            "router ospf LAB4 area 0.0.0.4 interface GigabitEthernet 0/0/0/4 authentication message-digest keychain iosxr",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospf_interfaces_overridden_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        type="gigabitethernet",
                        address_family=[
                            dict(
                                afi="ipv4",
                                processes=[
                                    dict(
                                        process_id="LAB3",
                                        area=dict(area_id="0.0.0.3"),
                                    )
                                ],
                                cost=20,
                                authentication=dict(
                                    message_digest=dict(keychain="cisco")
                                ),
                            )
                        ],
                    )
                ],
                state="overridden",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_ospf_interfaces_deleted(self):
        set_module_args(
            dict(
                config=[
                    dict(name="GigabitEthernet0/0/0/0", type="gigabitethernet")
                ],
                state="deleted",
            )
        )
        commands = [
            "no router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0"
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ospf_interfaces_deleted_idempotent(self):
        set_module_args(
            dict(
                config=[
                    dict(name="GigabitEthernet0/0/0/1", type="gigabitethernet")
                ],
                state="deleted",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_ospf_interfaces_parsed(self):
        set_module_args(
            dict(
                running_config="router ospf LAB3\n area 0.0.0.3\n  interface GigabitEthernet0/0/0/0\n   cost 20\n  !\n !\n!",
                state="parsed",
            )
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            dict(
                name="GigabitEthernet0/0/0/0",
                type="gigabitethernet",
                address_family=[
                    dict(
                        afi="ipv4",
                        processes=[
                            dict(
                                process_id="LAB3", area=dict(area_id="0.0.0.3")
                            )
                        ],
                        cost=20,
                    )
                ],
            )
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_ospf_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        type="gigabitethernet",
                        address_family=[
                            dict(
                                afi="ipv4",
                                processes=[
                                    dict(
                                        process_id="LAB1",
                                        area=dict(area_id="0.0.0.3"),
                                    )
                                ],
                                cost=10,
                                authentication=dict(
                                    message_digest=dict(keychain="iosxr")
                                ),
                            )
                        ],
                    )
                ],
                state="rendered",
            )
        )
        commands = [
            "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 cost 10",
            "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 authentication message-digest",
            "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 authentication message-digest keychain iosxr",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))
