#
# (c) 2020 Red Hat Inc.
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
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type

from os import path
from unittest import TestCase
from unittest.mock import MagicMock

from ansible.module_utils._text import to_bytes, to_text

from ansible_collections.cisco.iosxr.plugins.cliconf import iosxr


class TestPluginCLIConfIOSXR(TestCase):
    """Test class for IOSXR CLI Conf Methods"""

    def setUp(self):
        self._mock_connection = MagicMock()
        self._prepare()
        self._cliconf = iosxr.Cliconf(self._mock_connection)
        self.maxDiff = None

    def _prepare(self, platform="iosxr"):
        b_FIXTURE_DIR = b"%s/fixtures/cliconf/%s" % (
            to_bytes(
                path.dirname(path.abspath(__file__)),
                errors="surrogate_or_strict",
            ),
            to_bytes(platform),
        )

        def _connection_side_effect(*args, **kwargs):
            try:
                if args:
                    value = args[0]
                else:
                    value = kwargs.get("command")
                if b"|" in value:
                    value = value.replace(b"|", b"")
                fixture_path = path.abspath(
                    b"%s/%s" % (b_FIXTURE_DIR, b"_".join(value.split(b" "))),
                )
                with open(fixture_path, "rb") as file_desc:
                    return to_text(file_desc.read())
            except (OSError, IOError):
                if args:
                    value = args[0]
                    return value
                elif kwargs.get("command"):
                    value = kwargs.get("command")
                    return value
                return "NO-OP"

        self._mock_connection.send.side_effect = _connection_side_effect

    def tearDown(self):
        pass

    def test_get_device_info_iosxr(self):
        """Test get_device_info for nxos"""
        device_info = self._cliconf.get_device_info()

        mock_device_info = {
            "network_os_image": "bootflash:disk0/xrvr-os-mbi-6.0.0/mbixrvr-rp.vm",
            "network_os_version": "6.0.0[Default]",
            "network_os": "iosxr",
            "network_os_hostname": "iosxr01",
            "network_os_model": "IOS XRv",
        }

        self.assertEqual(device_info, mock_device_info)

    def test_get_command_output_iosxr(self):
        """Test _get_command_with_output for iosxr"""
        self._prepare()
        cmd = self._cliconf.get_command_output("show running-config hostname")

        self.assertEqual(cmd, "hostname iosxr01")
