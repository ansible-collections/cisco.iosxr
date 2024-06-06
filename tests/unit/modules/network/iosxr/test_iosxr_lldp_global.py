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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_lldp_global
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrLldpModule(TestIosxrModule):
    module = iosxr_lldp_global

    def setUp(self):
        super(TestIosxrLldpModule, self).setUp()

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
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lldp_global.lldp_global.Lldp_globalFacts.get_config",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrLldpModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_lldp_global_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_lldp_global_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=dict(
                    holdtime=100,
                    reinit=2,
                    timer=3000,
                    subinterfaces=True,
                    tlv_select=dict(
                        management_address=False,
                        system_description=False,
                    ),
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_lldp_global_merged(self):
        set_module_args(
            dict(
                config=dict(
                    holdtime=100,
                    reinit=2,
                    timer=3000,
                    subinterfaces=True,
                    tlv_select=dict(
                        management_address=False,
                        system_description=False,
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "lldp reinit 2",
            "lldp holdtime 100",
            "lldp timer 3000",
            "lldp subinterfaces enable",
            "lldp tlv-select system-description disable",
            "lldp tlv-select management-address disable",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lldp_global_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=dict(
                    holdtime=100,
                    tlv_select=dict(
                        management_address=False,
                        system_description=False,
                        port_description=False,
                    ),
                ),
                state="replaced",
            ),
        )
        commands = [
            "no lldp reinit 2",
            "no lldp subinterfaces enable",
            "no lldp timer 3000",
            "lldp tlv-select port-description disable",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lldp_global_deleted(self):
        self._prepare()
        set_module_args(dict(state="deleted"))

        commands = [
            "no lldp holdtime 100",
            "no lldp reinit 2",
            "no lldp subinterfaces enable",
            "no lldp timer 3000",
            "no lldp tlv-select management-address disable",
            "no lldp tlv-select system-description disable",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_lldp_global_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    holdtime=100,
                    reinit=2,
                    timer=3000,
                    subinterfaces=True,
                    tlv_select=dict(
                        management_address=False,
                        system_description=False,
                    ),
                ),
                state="rendered",
            ),
        )

        commands = [
            "lldp reinit 2",
            "lldp holdtime 100",
            "lldp timer 3000",
            "lldp subinterfaces enable",
            "lldp tlv-select system-description disable",
            "lldp tlv-select management-address disable",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_lag_interfaces_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="lldp reinit 2\nlldp holdtime 100\nlldp timer 3000\nlldp subinterfaces\
                     enable\nlldp tlv-select system-description disable\nlldp tlv-select management-address\
                 disable\n",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "holdtime": 100,
            "reinit": 2,
            "timer": 3000,
            "tlv_select": {"system_description": False},
        }
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_lldp_global_overridden(self):
        self._prepare()
        set_module_args(
            dict(
                config=dict(
                    holdtime=100,
                    tlv_select=dict(
                        management_address=False,
                        system_description=False,
                        port_description=False,
                    ),
                ),
                state="overridden",
            ),
        )
        commands = [
            "no lldp reinit 2",
            "no lldp subinterfaces enable",
            "no lldp timer 3000",
            "lldp tlv-select port-description disable",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
