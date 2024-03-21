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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_vrfs
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrVrfsModule(TestIosxrModule):
    module = iosxr_vrfs

    def setUp(self):
        super(TestIosxrVrfsModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.vrfs.vrfs.VrfFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrVrfsModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_vrfs_merged_idempotent(self):
        run_cfg = dedent(
            """\
            vrf test
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 235
             description "this is sample vrf for feature testing"
             fallback-vrf "parsed-vrf"
             rd "2:3"
             remote-route-filtering disable
             vpn 23
             address-family ipv4 flowspec
              import route-policy rm-policy
              import from bridge-domain advertise-as-vpn
              import route-target
               10.1.2.3:300
            """
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
                        vpn="23",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="flowspec",
                                import_config=dict(
                                    route_policy="rm-policy",
                                    route_target="10.1.2.3:300",
                                    from_config=dict(bridge_domain=dict(advertise_as_vpn=True)),
                                ),
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_vrfs_merged(self):
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
                        vpn="2:3",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy",
                                    route_target="10.0.0.1:300",
                                    to=dict(
                                        default_vrf=dict(route_policy="rm-policy"),
                                        vrf=dict(allow_imported_vpn=True),
                                    ),
                                ),
                                import_config=dict(
                                    from_config=dict(
                                        bridge_domain=dict(advertise_as_vpn=True),
                                        default_vrf=dict(route_policy="test-policy"),
                                        vrf=dict(advertise_as_vpn=True),
                                    ),
                                    route_policy="test-policy",
                                    route_target="10.1.3.4:400",
                                ),
                                maximum=dict(prefix=100),
                            ),
                        ],
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
            "vpn id 2:3",
            "address-family ipv4 unicast",
            "export route-policy rm-policy",
            "export route-target 10.0.0.1:300",
            "export to default-vrf route-policy rm-policy",
            "export to vrf allow-imported-vpn",
            "import route-target 10.1.3.4:400",
            "import route-policy test-policy",
            "import from bridge-domain advertise-as-vpn",
            "import from default-vrf route-policy test-policy",
            "import from vrf advertise-as-vpn",
            "maximum prefix 100",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrfs_replaced(self):
        run_cfg = dedent(
            """\
            vrf VRF7
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 398
             description VRF7 description
             vpn id 4:5
             fallback-vrf replaced-vrf
             remote-route-filtering disable
             rd 67:9
             address-family ipv4 unicast
              import route-policy test-policy
              import from vrf advertise-as-vpn
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import route-target
               12.2.3.4:900
              !
              export route-policy rm-policy
              export to vrf allow-imported-vpn
              export to default-vrf route-policy rm-policy
              export route-target
               192.12.3.2:300
              !
              maximum prefix 200
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
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
                        vpn="4:5",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy",
                                    route_target="192.12.3.2:300",
                                    to=dict(
                                        default_vrf=dict(route_policy="rm-policy"),
                                        vrf=dict(allow_imported_vpn=True),
                                    ),
                                ),
                                import_config=dict(
                                    from_config=dict(
                                        bridge_domain=dict(advertise_as_vpn=True),
                                        default_vrf=dict(route_policy="test-policy"),
                                        vrf=dict(advertise_as_vpn=True),
                                    ),
                                    route_policy="test-policy",
                                    route_target="12.2.3.4:900",
                                ),
                                maximum=dict(prefix=200),
                            ),
                        ],
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
            "address-family ipv4 unicast",
            "export route-policy rm-policy",
            "export route-target 192.12.3.2:300",
            "export to default-vrf route-policy rm-policy",
            "export to vrf allow-imported-vpn",
            "import route-target 12.2.3.4:900",
            "import route-policy test-policy",
            "import from bridge-domain advertise-as-vpn",
            "import from default-vrf route-policy test-policy",
            "import from vrf advertise-as-vpn",
            "maximum prefix 200"
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrfs_replaced_idempotent(self):
        run_cfg = dedent(
            """\
            vrf VRF7
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 398
             description VRF7 description
             vpn id 4:5
             fallback-vrf replaced-vrf
             remote-route-filtering disable
             rd 67:9
             address-family ipv4 unicast
              import route-policy test-policy
              import from vrf advertise-as-vpn
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import route-target
               12.2.3.4:900
              !
              export route-policy rm-policy
              export to vrf allow-imported-vpn
              export to default-vrf route-policy rm-policy
              export route-target
               192.12.3.2:300
              !
              maximum prefix 200
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
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
                        vpn="4:5",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy",
                                    route_target="192.12.3.2:300",
                                    to=dict(
                                        default_vrf=dict(route_policy="rm-policy"),
                                        vrf=dict(allow_imported_vpn=True),
                                    ),
                                ),
                                import_config=dict(
                                    from_config=dict(
                                        bridge_domain=dict(advertise_as_vpn=True),
                                        default_vrf=dict(route_policy="test-policy"),
                                        vrf=dict(advertise_as_vpn=True),
                                    ),
                                    route_policy="test-policy",
                                    route_target="12.2.3.4:900",
                                ),
                                maximum=dict(prefix=200),
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_vrfs_deleted(self):
        run_cfg = dedent(
            """\
            vrf VRF7
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 398
             description VRF7 description
             vpn id 4:5
             fallback-vrf replaced-vrf
             remote-route-filtering disable
             rd 67:9
             address-family ipv4 unicast
              import route-policy test-policy
              import from vrf advertise-as-vpn
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import route-target
               12.2.3.4:900
              !
              export route-policy rm-policy
              export to vrf allow-imported-vpn
              export to default-vrf route-policy rm-policy
              export route-target
               192.12.3.2:300
              !
              maximum prefix 200
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(), state="deleted"))

        commands = ["no vrf VRF7", "no vrf VRF4"]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrfs_deleted_idempotent(self):
        run_cfg = dedent(
            """\
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=[], state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_iosxr_vrfs_rendered(self):
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
                        vpn="2:3",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy",
                                    route_target="10.0.0.1:300",
                                    to=dict(
                                        default_vrf=dict(route_policy="rm-policy"),
                                        vrf=dict(allow_imported_vpn=True),
                                    ),
                                ),
                                import_config=dict(
                                    from_config=dict(
                                        bridge_domain=dict(advertise_as_vpn=True),
                                        default_vrf=dict(route_policy="test-policy"),
                                        vrf=dict(advertise_as_vpn=True),
                                    ),
                                    route_policy="test-policy",
                                    route_target="10.1.3.4:400",
                                ),
                                maximum=dict(prefix=100),
                            ),
                        ],
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
            "vpn id 2:3",
            "address-family ipv4 unicast",
            "export route-policy rm-policy",
            "export route-target 10.0.0.1:300",
            "export to default-vrf route-policy rm-policy",
            "export to vrf allow-imported-vpn",
            "import route-target 10.1.3.4:400",
            "import route-policy test-policy",
            "import from bridge-domain advertise-as-vpn",
            "import from default-vrf route-policy test-policy",
            "import from vrf advertise-as-vpn",
            "maximum prefix 100",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_vrfs_parsed(self):
        run_cfg = dedent(
            """\
            vrf my_vrf
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 235
             description "this is sample vrf for feature testing"
             fallback-vrf "parsed-vrf"
             rd "2:3"
             remote-route-filtering disable
             vpn 23
             address-family ipv4 flowspec
              import route-policy rm-policy
              import from bridge-domain advertise-as-vpn
              import route-target
               10.1.2.3:300
            """,
        )
        set_module_args(dict(running_config=run_cfg, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "address_families": [
                    {
                        "afi": "ipv4",
                        "import_config": {
                            "from": {
                                "bridge_domain": {
                                    "advertise_as_vpn": "true"
                                }
                            },
                            "route_policy": "rm-policy",
                            "route_target": "10.1.2.3:300"
                        },
                        "safi": "flowspec"
                    }
                ],
                "description": "this is sample vrf for feature testing",
                "evpn_route_sync": 235,
                "fallback_vrf": "parsed-vrf",
                "mhost": {
                    "afi": "ipv4",
                    "default_interface": "Loopback0"
                },
                "name": "my_vrf",
                "rd": "2:3",
                "remote_route_filtering": {
                    "disable": "true"
                }
            }
        ]

        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_vrfs_overridden(self):
        """Unit test for overridden state"""

        run_cfg = dedent(
            """\
            vrf VRF6
             mhost ipv4 default-interface Loopback0
             evpn-route-sync 101
             description VRF6 Description
             vpn id 4:5
             fallback-vrf overridden-vrf
             remote-route-filtering disable
             rd 67:9
             address-family ipv4 unicast
              import route-policy test-policy
              import from vrf advertise-as-vpn
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import route-target
               10.1.3.4:900
              !
              export route-policy rm-policy1
              export to vrf allow-imported-vpn
              export to default-vrf route-policy rm-policy
              export route-target
               10.0.0.1:300
              !
              maximum prefix 500
            """,
        )

        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
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
                        vpn="4:5",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy1",
                                    route_target="10.0.0.1:300",
                                    to=dict(
                                        default_vrf=dict(route_policy="rm-policy"),
                                        vrf=dict(allow_imported_vpn=True),
                                    ),
                                ),
                                import_config=dict(
                                    from_config=dict(
                                        bridge_domain=dict(advertise_as_vpn=True),
                                        default_vrf=dict(route_policy="test-policy"),
                                        vrf=dict(advertise_as_vpn=True),
                                    ),
                                    route_policy="test-policy",
                                    route_target="10.1.3.4:900",
                                ),
                                maximum=dict(prefix=500),
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "vrf VRF6",
            "description VRF6 Description",
            "evpn-route-sync 101",
            "fallback-vrf overridden-vrf",
            "mhost ipv4 default-interface Loopback0",
            "rd 67:9",
            "remote-route-filtering disable",
            "vpn id 4:5",
            "address-family ipv4 unicast",
            "export route-policy rm-policy1",
            "export route-target 10.0.0.1:300",
            "export to default-vrf route-policy rm-policy",
            "export to vrf allow-imported-vpn",
            "import route-target 10.1.3.4:900",
            "import route-policy test-policy",
            "import from bridge-domain advertise-as-vpn",
            "import from default-vrf route-policy test-policy",
            "import from vrf advertise-as-vpn",
            "maximum prefix 500",
            "no vrf VRF4",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))
