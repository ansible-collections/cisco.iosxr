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

from textwrap import dedent
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.plugins.modules import iosxr_prefix_lists
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import (
    set_module_args,
)
from .iosxr_module import TestIosxrModule


class TestIosxrPrefixListsModule(TestIosxrModule):
    module = iosxr_prefix_lists

    def setUp(self):
        super(TestIosxrPrefixListsModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection"
        )
        self.get_resource_connection = (
            self.mock_get_resource_connection.start()
        )

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.prefix_lists.prefix_lists."
            "Prefix_listsFacts.get_config"
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrPrefixListsModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_prefix_lists_merged_idempotent(self):
        run_cfg = dedent(
            """ipv6 prefix-list test2\n 4 remark test\n!
            \nipv4 prefix-list test1\n 3 remark test1\n 2 permit 10.0.0.0/24\n!
            """
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="test2",
                                entries=[
                                    dict(
                                        sequence=4,
                                        action="remark",
                                        description="test",
                                    )
                                ],
                            )
                        ],
                    ),
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="test1",
                                entries=[
                                    dict(
                                        sequence=3,
                                        action="remark",
                                        description="test1",
                                    ),
                                    dict(
                                        sequence=2,
                                        action="permit",
                                        prefix="10.0.0.0/24",
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_prefix_lists_merged(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="test2",
                                entries=[
                                    dict(
                                        sequence=4,
                                        action="remark",
                                        description="test",
                                    )
                                ],
                            )
                        ],
                    ),
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="test1",
                                entries=[
                                    dict(
                                        sequence=3,
                                        action="remark",
                                        description="test1",
                                    ),
                                    dict(
                                        sequence=2,
                                        action="permit",
                                        prefix="10.0.0.0/24",
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
                state="merged",
            )
        )
        commands = [
            "ipv6 prefix-list test2 4 remark test",
            "ipv4 prefix-list test1 2 permit 10.0.0.0/24",
            "ipv4 prefix-list test1 3 remark test1",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_prefix_lists_replaced(self):
        run_cfg = dedent(
            """ipv6 prefix-list test2\n 4 remark test\n!
            \nipv4 prefix-list test1\n 3 remark test1\n 2 permit 10.0.0.0/24\n!"""
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="test2",
                                entries=[
                                    dict(
                                        sequence=2,
                                        action="permit",
                                        prefix="10.0.0.0/24",
                                    )
                                ],
                            ),
                            dict(
                                name="test1",
                                entries=[
                                    dict(
                                        sequence=2,
                                        action="permit",
                                        prefix="10.0.0.0/24",
                                    )
                                ],
                            ),
                        ],
                    )
                ],
                state="replaced",
            )
        )
        commands = [
            "no ipv4 prefix-list test1 3 remark test1",
            "ipv4 prefix-list test2 2 permit 10.0.0.0/24",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_prefix_lists_replaced_idempotent(self):
        run_cfg = dedent(
            """ipv6 prefix-list test2\n 4 remark test\n!
            \nipv4 prefix-list test1\n 3 remark test1\n 2 permit 10.0.0.0/24\n!"""
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="test2",
                                entries=[
                                    dict(
                                        sequence=4,
                                        action="remark",
                                        description="test",
                                    )
                                ],
                            )
                        ],
                    ),
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="test1",
                                entries=[
                                    dict(
                                        sequence=3,
                                        action="remark",
                                        description="test1",
                                    ),
                                    dict(
                                        sequence=2,
                                        action="permit",
                                        prefix="10.0.0.0/24",
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
                state="replaced",
            )
        )

        self.execute_module(changed=False, commands=[])

    def test_iosxr_prefix_list_deleted(self):
        run_cfg = dedent(
            """ipv6 prefix-list test2\n 4 remark test\n!
            \nipv4 prefix-list test1\n 3 remark test1\n 2 permit 10.0.0.0/24\n!"""
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="deleted"))

        commands = ["no ipv4 prefix-list test1", "no ipv6 prefix-list test2"]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_prefix_list_deleted_idempotent(self):
        run_cfg = dedent(
            """\
            """
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=[], state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_iosxr_prefix_list_rendered(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv6",
                        prefix_lists=[
                            dict(
                                name="test2",
                                entries=[
                                    dict(
                                        sequence=4,
                                        action="remark",
                                        description="test",
                                    )
                                ],
                            )
                        ],
                    ),
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="test1",
                                entries=[
                                    dict(
                                        sequence=3,
                                        action="remark",
                                        description="test1",
                                    ),
                                    dict(
                                        sequence=2,
                                        action="permit",
                                        prefix="10.0.0.0/24",
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
                state="rendered",
            )
        )

        commands = [
            "ipv6 prefix-list test2 4 remark test",
            "ipv4 prefix-list test1 2 permit 10.0.0.0/24",
            "ipv4 prefix-list test1 3 remark test1",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_prefix_list_parsed(self):
        set_module_args(
            dict(
                running_config="ipv4 prefix-list test1\n 3 remark test1\n!",
                state="parsed",
            )
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "afi": "ipv4",
                "prefix_lists": [
                    {
                        "name": "test1",
                        "entries": [
                            {
                                "sequence": 3,
                                "action": "remark",
                                "description": "test1",
                            }
                        ],
                    }
                ],
            }
        ]

        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_prefix_list_overridden(self):
        run_cfg = dedent(
            """ipv6 prefix-list test2\n 4 remark test\n!
            \nipv4 prefix-list test1\n 3 remark test1\n 2 permit 10.0.0.0/24\n!
            """
        )

        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        prefix_lists=[
                            dict(
                                name="test2",
                                entries=[
                                    dict(
                                        sequence=2,
                                        action="permit",
                                        prefix="10.0.0.0/24",
                                    )
                                ],
                            ),
                            dict(
                                name="test1",
                                entries=[
                                    dict(
                                        sequence=2,
                                        action="permit",
                                        prefix="10.0.0.0/24",
                                    )
                                ],
                            ),
                        ],
                    )
                ],
                state="overridden",
            )
        )
        commands = [
            "no ipv4 prefix-list test1 3 remark test1",
            "ipv4 prefix-list test2 2 permit 10.0.0.0/24",
            "no ipv6 prefix-list test2",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))
