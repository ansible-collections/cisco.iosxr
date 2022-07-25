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
# (c) 2016 Red Hat Inc.
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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_banner
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrBannerModule(TestIosxrModule):

    module = iosxr_banner

    def setUp(self):
        super(TestIosxrBannerModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.modules.iosxr_banner.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.cisco.iosxr.plugins.modules.iosxr_banner.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_is_cliconf = patch(
            "ansible_collections.cisco.iosxr.plugins.modules.iosxr_banner.is_cliconf",
        )
        self.is_cliconf = self.mock_is_cliconf.start()

    def tearDown(self):
        super(TestIosxrBannerModule, self).tearDown()

        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_is_cliconf.stop()

    def load_fixtures(self, commands=None):
        self.get_config.return_value = load_fixture("iosxr_banner_config.cfg")
        self.load_config.return_value = dict(diff=None, session="session")
        self.is_cliconf.return_value = True

    def test_iosxr_banner_login_create(self):
        set_module_args(dict(banner="login", text="test\nbanner\nstring"))
        commands = ["banner login test\nbanner\nstring"]
        self.execute_module(changed=True, commands=commands)

    def test_iosxr_banner_login_remove(self):
        set_module_args(dict(banner="login", state="absent"))
        commands = ["no banner login"]
        self.execute_module(changed=True, commands=commands)

    def test_iosxr_banner_fail_create(self):
        set_module_args(dict(banner="exec1", text="test\nbanner\nstring"))
        result = self.execute_module(failed=True, changed=True)
        self.assertEqual(
            result["msg"],
            "value of banner must be one of: login, motd, got: exec1",
        )

    def test_iosxr_banner_exec1_fail_remove(self):
        set_module_args(dict(banner="exec1", state="absent"))
        result = self.execute_module(failed=True, changed=True)
        self.assertIn(
            result["msg"],
            "value of banner must be one of: login, motd, got: exec1",
        )

    def test_iosxr_banner_motd_create(self):
        set_module_args(dict(banner="motd", text="test\nbanner\nstring"))
        commands = ["banner motd test\nbanner\nstring"]
        self.execute_module(changed=True, commands=commands)

    def test_iosxr_banner_motd_remove(self):
        set_module_args(dict(banner="motd", state="absent"))
        commands = ["no banner motd"]
        self.execute_module(changed=True, commands=commands)
