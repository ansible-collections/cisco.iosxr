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
from unittest.mock import patch

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_hostname
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrHostnameModule(TestIosxrModule):
    module = iosxr_hostname

    def setUp(self):
        super(TestIosxrHostnameModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.hostname.hostname."
            "HostnameFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrHostnameModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_hostname_merged_idempotent(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                hostname iosxr1
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(hostname="iosxr1"), state="merged"))
        self.execute_module(changed=False, commands=[])

    def test_iosxr_hostname_merged(self):
        self.maxDiff = None
        set_module_args(dict(config=dict(hostname="iosxr1"), state="merged"))
        commands = ["hostname iosxr1"]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_hostname_deleted(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                hostname iosxr1
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="deleted"))
        commands = ["no hostname iosxr1"]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_hostname_rendered(self):
        self.maxDiff = None
        set_module_args(dict(config=dict(hostname="iosxr1"), state="rendered"))
        commands = ["hostname iosxr1"]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_hostname_gathered(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                hostname iosxr1
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="gathered"))
        gathered = {"hostname": "iosxr1"}
        result = self.execute_module(changed=False)
        self.assertEqual(gathered, result["gathered"])

    def test_iosxr_hostname_parsed(self):
        self.maxDiff = None
        set_module_args(dict(running_config="hostname iosxr1", state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {"hostname": "iosxr1"}
        self.assertEqual(parsed_list, result["parsed"])
