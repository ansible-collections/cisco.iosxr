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
    iosxr_acl_interfaces,
)
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import (
    set_module_args,
)
from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrAclInterfacesModule(TestIosxrModule):
    module = iosxr_acl_interfaces

    def setUp(self):
        super(TestIosxrAclInterfacesModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection"
        )
        self.get_resource_connection = (
            self.mock_get_resource_connection.start()
        )

        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.acl_interfaces.acl_interfaces.Acl_interfacesFacts.get_config"
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrAclInterfacesModule, self).tearDown()
        self.get_resource_connection.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_acl_interfaces_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_acl_interfaces_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        access_groups=[
                            dict(
                                afi="ipv4",
                                acls=[
                                    dict(name="acl_1", direction="in"),
                                    dict(name="acl_2", direction="out"),
                                ],
                            ),
                            dict(
                                afi="ipv6",
                                acls=[
                                    dict(name="acl6_1", direction="in"),
                                    dict(name="acl6_2", direction="out"),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        access_groups=[
                            dict(
                                afi="ipv4",
                                acls=[dict(name="acl_1", direction="out")],
                            )
                        ],
                    ),
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_acl_interfaces_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        access_groups=[
                            dict(
                                afi="ipv4",
                                acls=[
                                    dict(name="acl_1", direction="in"),
                                    dict(name="acl_2", direction="out"),
                                ],
                            ),
                            dict(
                                afi="ipv6",
                                acls=[
                                    dict(name="acl6_1", direction="in"),
                                    dict(name="acl6_2", direction="out"),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        access_groups=[
                            dict(
                                afi="ipv4",
                                acls=[dict(name="acl_1", direction="in")],
                            )
                        ],
                    ),
                ],
                state="merged",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "ipv4 access-group acl_1 ingress",
            "ipv4 access-group acl_2 egress",
            "ipv6 access-group acl6_1 ingress",
            "ipv6 access-group acl6_2 egress",
            "interface GigabitEthernet0/0/0/1",
            "ipv4 access-group acl_1 ingress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_acl_interfaces_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        access_groups=[
                            dict(
                                afi="ipv6",
                                acls=[dict(name="acl6_3", direction="in")],
                            )
                        ],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 access-group acl_1 ingress",
            "no ipv4 access-group acl_2 egress",
            "no ipv6 access-group acl6_2 egress",
            "ipv6 access-group acl6_3 ingress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_acl_interfaces_deleted(self):
        self._prepare()
        set_module_args(dict(state="deleted"))

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 access-group acl_1 ingress",
            "no ipv4 access-group acl_2 egress",
            "no ipv6 access-group acl6_1 ingress",
            "no ipv6 access-group acl6_2 egress",
            "interface GigabitEthernet0/0/0/1",
            "no ipv4 access-group acl_1 egress",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_acl_interfaces_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        access_groups=[
                            dict(
                                afi="ipv4",
                                acls=[
                                    dict(name="acl_1", direction="in"),
                                    dict(name="acl_2", direction="out"),
                                ],
                            ),
                            dict(
                                afi="ipv6",
                                acls=[
                                    dict(name="acl6_1", direction="in"),
                                    dict(name="acl6_2", direction="out"),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        access_groups=[
                            dict(
                                afi="ipv4",
                                acls=[dict(name="acl_1", direction="in")],
                            )
                        ],
                    ),
                ],
                state="rendered",
            )
        )

        commands = [
            "interface GigabitEthernet0/0/0/0",
            "ipv4 access-group acl_1 ingress",
            "ipv4 access-group acl_2 egress",
            "ipv6 access-group acl6_1 ingress",
            "ipv6 access-group acl6_2 egress",
            "interface GigabitEthernet0/0/0/1",
            "ipv4 access-group acl_1 ingress",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_acl_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="interface GigabitEthernet0/0/0/0\r\n shutdown\r\n ipv4 access-group acl_1 ingress\r\n"
                " ipv4 access-group acl_2 egress\r\n ipv6 access-group acl6_1 ingress\r\n ipv6 "
                "access-group acl6_2 egress\r\n!\r\ninterface GigabitEthernet0/0/0/1\r\n "
                "shutdown\r\n ipv4 access-group acl_1 egress\r\n!",
                state="parsed",
            )
        )
        result = self.execute_module(changed=False)
        print(result["parsed"])
        parsed_list = [
            {
                "name": "GigabitEthernet0/0/0/0",
                "access_groups": [
                    {
                        "afi": "ipv4",
                        "acls": [
                            {"name": "acl_1", "direction": "in"},
                            {"name": "acl_2", "direction": "out"},
                        ],
                    },
                    {
                        "afi": "ipv6",
                        "acls": [
                            {"name": "acl6_1", "direction": "in"},
                            {"name": "acl6_2", "direction": "out"},
                        ],
                    },
                ],
            },
            {
                "name": "GigabitEthernet0/0/0/1",
                "access_groups": [
                    {
                        "afi": "ipv4",
                        "acls": [{"name": "acl_1", "direction": "out"}],
                    }
                ],
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_acl_interfaces_overridden(self):
        self.maxDiff = None
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        name="GigabitEthernet0/0/0/0",
                        access_groups=[
                            dict(
                                afi="ipv6",
                                acls=[dict(name="acl6_3", direction="in")],
                            )
                        ],
                    ),
                    dict(
                        name="GigabitEthernet0/0/0/1",
                        access_groups=[
                            dict(
                                afi="ipv4",
                                acls=[dict(name="acl_2", direction="in")],
                            ),
                            dict(
                                afi="ipv6",
                                acls=[dict(name="acl6_3", direction="out")],
                            ),
                        ],
                    ),
                ],
                state="overridden",
            )
        )
        commands = [
            "interface GigabitEthernet0/0/0/0",
            "no ipv4 access-group acl_1 ingress",
            "no ipv4 access-group acl_2 egress",
            "no ipv6 access-group acl6_2 egress",
            "ipv6 access-group acl6_3 ingress",
            "interface GigabitEthernet0/0/0/1",
            "no ipv4 access-group acl_1 egress",
            "ipv4 access-group acl_2 ingress",
            "ipv6 access-group acl6_3 egress",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
