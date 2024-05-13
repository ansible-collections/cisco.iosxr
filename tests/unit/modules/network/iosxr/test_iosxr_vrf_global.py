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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_vrf_global
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrVrfGlobalModule(TestIosxrModule):
    """Tests the iosxr_vrf_global module."""

    module = iosxr_vrf_global

    def setUp(self):
        """Setup for iosxr_vrfs module tests."""
        super(TestIosxrVrfGlobalModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.vrf_global.vrf_global."
            "Vrf_globalFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        """Tear down for iosxr_vrfs module tests."""
        super(TestIosxrVrfGlobalModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_vrf_global_merged_idempotent(self):
        """Test the idempotent nature of the iosxr_vrf_global module in merged state."""
        run_cfg = dedent(
            """\
            vrf test
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 235
             description "this is sample vrf for feature testing"
             fallback-vrf "parsed-vrf"
             rd "2:3"
             remote-route-filtering disable
             vpn id 23
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    dict(
                        name="test",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        evpn_route_sync=235,
                        description="this is sample vrf for feature testing",
                        fallback_vrf="parsed-vrf",
                        rd="2:3",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="23"),
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_vrf_global_merged(self):
        """Test the merged state of the iosxr_vrf_global module."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        description="VRF4 Description",
                        evpn_route_sync=793,
                        fallback_vrf="parsed-vrf",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        rd="3:4",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="23"),
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "vrf VRF4",
            "description VRF4 Description",
            "evpn-route-sync 793",
            "fallback-vrf parsed-vrf",
            "mhost ipv4 default-interface Loopback0",
            "rd 3:4",
            "remote-route-filtering disable",
            "vpn id 23",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_global_replaced(self):
        """Test the replaced state of the iosxr_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf VRF4
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 793
             description VRF4 description
             vpn id 23
             fallback-vrf parsed-vrf
             remote-route-filtering disable
             rd 3:4
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        description="VRF4 description",
                        evpn_route_sync=793,
                        fallback_vrf="parsed-vrf",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        rd="3:4",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="23"),
                    ),
                    dict(
                        name="VRF7",
                        description="VRF7 description",
                        evpn_route_sync=398,
                        fallback_vrf="replaced-vrf",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        rd="67:9",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="4:5"),
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "vrf VRF7",
            "description VRF7 description",
            "evpn-route-sync 398",
            "fallback-vrf replaced-vrf",
            "mhost ipv4 default-interface Loopback0",
            "rd 67:9",
            "remote-route-filtering disable",
            "vpn id 4:5",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_global_replaced_idempotent(self):
        """Test the idempotent nature of the iosxr_vrf_global module in replaced state."""
        run_cfg = dedent(
            """\
            vrf VRF4
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 793
             description VRF4 description
             vpn id 23
             fallback-vrf parsed-vrf
             remote-route-filtering disable
             rd 3:4
            vrf VRF7
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 398
             description VRF7 description
             vpn id 4:5
             fallback-vrf replaced-vrf
             remote-route-filtering disable
             rd 67:9
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        description="VRF4 description",
                        evpn_route_sync=793,
                        fallback_vrf="parsed-vrf",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        rd="3:4",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="23"),
                    ),
                    dict(
                        name="VRF7",
                        description="VRF7 description",
                        evpn_route_sync=398,
                        fallback_vrf="replaced-vrf",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        rd="67:9",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="4:5"),
                    ),
                ],
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_vrf_global_overridden(self):
        """Test the overridden state of the iosxr_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf VRF4
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 793
             description VRF4 description
             vpn id 2:3
             fallback-vrf merged-vrf
             remote-route-filtering disable
             rd 3:4
            vrf VRF7
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 398
             description VRF7 description
             vpn id 4:5
             fallback-vrf replaced-vrf
             remote-route-filtering disable
             rd 6:9
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                    ),
                    dict(
                        name="VRF6",
                        description="VRF6 description",
                        evpn_route_sync=101,
                        fallback_vrf="overridden-vrf",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        rd="9:8",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="23:3"),
                    ),
                    dict(
                        name="VRF7",
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "vrf VRF4",
            "no description VRF4 description",
            "no evpn-route-sync 793",
            "no fallback-vrf merged-vrf",
            "no mhost ipv4 default-interface Loopback0",
            "no rd 3:4",
            "no remote-route-filtering disable",
            "no vpn id 2:3",
            "vrf VRF7",
            "no description VRF7 description",
            "no evpn-route-sync 398",
            "no fallback-vrf replaced-vrf",
            "no mhost ipv4 default-interface Loopback0",
            "no rd 6:9",
            "no remote-route-filtering disable",
            "no vpn id 4:5",
            "vrf VRF6",
            "description VRF6 description",
            "evpn-route-sync 101",
            "fallback-vrf overridden-vrf",
            "mhost ipv4 default-interface Loopback0",
            "rd 9:8",
            "remote-route-filtering disable",
            "vpn id 23:3",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_global_overridden_idempotent(self):
        """Test the idempotent nature of the iosxr_vrf_global module in overridden state."""
        run_cfg = dedent(
            """\
            vrf VRF4
            vrf VRF6
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 101
             description VRF6 description
             vpn id 4:5
             fallback-vrf overridden-vrf
             remote-route-filtering disable
             rd 67:9
            vrf VRF7
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                    ),
                    dict(
                        name="VRF6",
                        description="VRF6 description",
                        evpn_route_sync=101,
                        fallback_vrf="overridden-vrf",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        rd="67:9",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="4:5"),
                    ),
                    dict(
                        name="VRF7",
                    ),
                ],
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_vrf_global_deleted(self):
        """Test the deleted state of the iosxr_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf VRF4
            vrf VRF6
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 101
             description VRF6 description
             vpn id 23:3
             fallback-vrf overridden-vrf
             remote-route-filtering disable
             rd 9:8
            vrf VRF7
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                    ),
                    dict(
                        name="VRF6",
                    ),
                    dict(
                        name="VRF7",
                    ),
                ],
                state="deleted",
            ),
        )

        commands = [
            "vrf VRF6",
            "no description VRF6 description",
            "no evpn-route-sync 101",
            "no fallback-vrf overridden-vrf",
            "no mhost ipv4 default-interface Loopback0",
            "no rd 9:8",
            "no remote-route-filtering disable",
            "no vpn id 23:3",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_global_deleted_idempotent(self):
        """Test the idempotent nature of the iosxr_vrf_global module in deleted state."""
        run_cfg = dedent(
            """\
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=[], state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_ios_vrf_global_purged(self):
        """Test the purged state of the iosxr_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf VRF4
            vrf VRF6
            vrf VRF7
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="purged"))
        commands = [
            "no vrf VRF4",
            "no vrf VRF6",
            "no vrf VRF7",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_global_rendered(self):
        """Test the rendered state of the iosxr_vrf_global module."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        description="VRF4 Description",
                        evpn_route_sync=793,
                        fallback_vrf="rendered-vrf",
                        mhost=dict(
                            afi="ipv4",
                            default_interface="Loopback0",
                        ),
                        rd="3:4",
                        remote_route_filtering=dict(disable=True),
                        vpn=dict(id="2:3"),
                    ),
                ],
                state="rendered",
            ),
        )
        commands = [
            "vrf VRF4",
            "description VRF4 Description",
            "evpn-route-sync 793",
            "fallback-vrf rendered-vrf",
            "mhost ipv4 default-interface Loopback0",
            "rd 3:4",
            "remote-route-filtering disable",
            "vpn id 2:3",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_vrf_global_parsed(self):
        """Test the parsed state of the iosxr_vrf_global module."""
        run_cfg = dedent(
            """\
            vrf my_vrf
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 235
             description "this is sample vrf for feature testing"
             fallback-vrf "parsed-vrf"
             rd "2:3"
             remote-route-filtering disable
            """,
        )
        set_module_args(dict(running_config=run_cfg, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "name": "my_vrf",
                "mhost": {
                    "afi": "ipv4",
                    "default_interface": "Loopback0",
                },
                "evpn_route_sync": 235,
                "description": "this is sample vrf for feature testing",
                "fallback_vrf": "parsed-vrf",
                "rd": "2:3",
                "remote_route_filtering": {
                    "disable": True,
                },
            },
        ]

        self.assertEqual(parsed_list, result["parsed"])
