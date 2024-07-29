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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_vrf_address_family
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrVrfAddressFamilyModule(TestIosxrModule):
    """Tests the iosxr_vrf_address_family module."""

    module = iosxr_vrf_address_family

    def setUp(self):
        """Setup for iosxr_vrf_address_family module tests."""
        super(TestIosxrVrfAddressFamilyModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.vrf_address_family.vrf_address_family."
            "Vrf_address_familyFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        """Tear down for iosxr_vrf_address_family module tests."""
        super(TestIosxrVrfAddressFamilyModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_vrf_address_family_merged_idempotent(self):
        """Test the idempotent nature of the iosxr_vrf_address_family module in merged state."""
        run_cfg = dedent(
            """\
            vrf test
             address-family ipv4 unicast
              export to default-vrf route-policy "rm-policy"
              export to vrf allow-imported-vpn
              export route-policy "export-policy"
              export route-target
               192.0.2.1:400
              import route-target
               192.0.2.2:200
              import route-policy "test-policy"
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy "new-policy"
              import from vrf advertise-as-vpn
              maximum prefix 23
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=[
                    dict(
                        name="test",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="export-policy",
                                    route_target="192.0.2.1:400",
                                    to=dict(
                                        default_vrf=dict(route_policy="rm-policy"),
                                        vrf=dict(allow_imported_vpn=True),
                                    ),
                                ),
                                import_config=dict(
                                    route_policy="test-policy",
                                    route_target="192.0.2.2:200",
                                    from_config=dict(
                                        bridge_domain=dict(advertise_as_vpn=True),
                                        default_vrf=dict(route_policy="new-policy"),
                                        vrf=dict(advertise_as_vpn=True),
                                    ),
                                ),
                                maximum=dict(prefix=23),
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_vrf_address_family_merged(self):
        """Test the merged state of the iosxr_vrf_address_family module."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy",
                                    route_target="192.0.2.1:400",
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
                                    route_target="192.0.2.6:200",
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
            "address-family ipv4 unicast",
            "export route-policy rm-policy",
            "export route-target 192.0.2.1:400",
            "export to default-vrf route-policy rm-policy",
            "export to vrf allow-imported-vpn",
            "import route-target 192.0.2.6:200",
            "import route-policy test-policy",
            "import from bridge-domain advertise-as-vpn",
            "import from default-vrf route-policy test-policy",
            "import from vrf advertise-as-vpn",
            "maximum prefix 100",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_address_family_replaced(self):
        """Test the replaced state of the iosxr_vrf_address_family module."""
        run_cfg = dedent(
            """\
            vrf VRF4
             address-family ipv4 unicast
              import route-policy test-policy
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import from vrf advertise-as-vpn
              import route-target
               192.0.2.6:200
              !
              export route-policy rm-policy
              export to vrf allow-imported-vpn
              export to default-vrf route-policy rm-policy
              export route-target
               192.0.2.1:400
              !
              maximum prefix 100
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF7",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy",
                                    route_target="192.0.2.2:400",
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
                                    route_target="192.0.2.4:400",
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
            "address-family ipv4 unicast",
            "export route-policy rm-policy",
            "export route-target 192.0.2.2:400",
            "export to default-vrf route-policy rm-policy",
            "export to vrf allow-imported-vpn",
            "import route-target 192.0.2.4:400",
            "import route-policy test-policy",
            "import from bridge-domain advertise-as-vpn",
            "import from default-vrf route-policy test-policy",
            "import from vrf advertise-as-vpn",
            "maximum prefix 200",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_address_family_replaced_idempotent(self):
        """Test the idempotent nature of the iosxr_vrf_address_family module in replaced state."""
        run_cfg = dedent(
            """\
            vrf VRF7
             address-family ipv4 unicast
              import route-policy test-policy
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import from vrf advertise-as-vpn
              import route-target
               192.0.2.4:400
              !
              export route-policy rm-policy
              export to vrf allow-imported-vpn
              export to default-vrf route-policy rm-policy
              export route-target
               192.0.2.2:400
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
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy",
                                    route_target="192.0.2.2:400",
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
                                    route_target="192.0.2.4:400",
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

    def test_iosxr_vrf_address_family_overridden(self):
        """Test the overridden state of the iosxr_vrf_address_family module."""
        run_cfg = dedent(
            """\
            vrf VRF7
             address-family ipv4 unicast
              import route-policy test-policy
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import from vrf advertise-as-vpn
              import route-target
               192.0.2.4:400
              !
              export route-policy rm-policy
              export to vrf allow-imported-vpn
              export to default-vrf route-policy rm-policy
              export route-target
               192.0.2.2:400
              !
              maximum prefix 200
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF6",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy1",
                                    route_target="192.0.2.8:200",
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
                                    route_target="192.0.2.2:200",
                                ),
                                maximum=dict(prefix=500),
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "vrf VRF7",
            "address-family ipv4 unicast",
            "no import route-policy test-policy",
            "no import from bridge-domain advertise-as-vpn",
            "no import from default-vrf route-policy test-policy",
            "no import from vrf advertise-as-vpn",
            "no import route-target 192.0.2.4:400",
            "no export route-policy rm-policy",
            "no export route-target 192.0.2.2:400",
            "no export to default-vrf route-policy rm-policy",
            "no export to vrf allow-imported-vpn",
            "no maximum prefix 200",
            "vrf VRF6",
            "address-family ipv4 unicast",
            "export route-policy rm-policy1",
            "export route-target 192.0.2.8:200",
            "export to default-vrf route-policy rm-policy",
            "export to vrf allow-imported-vpn",
            "import route-target 192.0.2.2:200",
            "import route-policy test-policy",
            "import from bridge-domain advertise-as-vpn",
            "import from default-vrf route-policy test-policy",
            "import from vrf advertise-as-vpn",
            "maximum prefix 500",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_address_family_overridden_idempotent(self):
        """Test the idempotent nature of the iosxr_vrf_address_family module in overridden state."""
        run_cfg = dedent(
            """\
            vrf VRF6
             address-family ipv4 unicast
              import route-policy test-policy
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import from vrf advertise-as-vpn
              import route-target
               192.0.2.2:200
              !
              export route-policy rm-policy1
              export to vrf allow-imported-vpn
              export to default-vrf route-policy rm-policy
              export route-target
               192.0.2.8:200
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
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy1",
                                    route_target="192.0.2.8:200",
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
                                    route_target="192.0.2.2:200",
                                ),
                                maximum=dict(prefix=500),
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_vrf_address_family_deleted(self):
        """Test the deleted state of the iosxr_vrf_address_family module."""
        run_cfg = dedent(
            """\
            vrf VRF7
             address-family ipv4 unicast
              import route-policy test-policy
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy test-policy
              import from vrf advertise-as-vpn
              import route-target
               192.0.2.2:200
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
                    ),
                ],
                state="deleted",
            ),
        )

        commands = [
            "vrf VRF7",
            "no address-family ipv4 unicast",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_vrf_address_family_deleted_idempotent(self):
        """Test the idempotent nature of the iosxr_vrf_address_family module in deleted state."""
        run_cfg = dedent(
            """\
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=[], state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_iosxr_vrf_address_family_rendered(self):
        """Test the rendered state of the iosxr_vrf_address_family module."""
        set_module_args(
            dict(
                config=[
                    dict(
                        name="VRF4",
                        address_families=[
                            dict(
                                afi="ipv4",
                                safi="unicast",
                                export=dict(
                                    route_policy="rm-policy",
                                    route_target="192.0.2.1:400",
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
                                    route_target="192.0.2.6:200",
                                ),
                                maximum=dict(prefix=100),
                            ),
                        ],
                    ),
                ],
                state="rendered",
            ),
        )
        commands = [
            "vrf VRF4",
            "address-family ipv4 unicast",
            "export route-policy rm-policy",
            "export route-target 192.0.2.1:400",
            "export to default-vrf route-policy rm-policy",
            "export to vrf allow-imported-vpn",
            "import route-target 192.0.2.6:200",
            "import route-policy test-policy",
            "import from bridge-domain advertise-as-vpn",
            "import from default-vrf route-policy test-policy",
            "import from vrf advertise-as-vpn",
            "maximum prefix 100",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_vrf_address_family_parsed(self):
        """Test the parsed state of the iosxr_vrf_address_family module."""
        run_cfg = dedent(
            """\
            vrf test
             address-family ipv4 unicast
              export to default-vrf route-policy "rm-policy"
              export to vrf allow-imported-vpn
              export route-policy "export-policy"
              export route-target
               192.0.2.1:400
              import route-target
               192.0.2.2:200
              import route-policy "test-policy"
              import from bridge-domain advertise-as-vpn
              import from default-vrf route-policy "new-policy"
              import from vrf advertise-as-vpn
              maximum prefix 23
            """,
        )
        set_module_args(dict(running_config=run_cfg, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "name": "test",
                "address_families": [
                    {
                        "afi": "ipv4",
                        "safi": "unicast",
                        "import_config": {
                            "route_policy": "test-policy",
                            "route_target": "192.0.2.2:200",
                            "from_config": {
                                "bridge_domain": {"advertise_as_vpn": True},
                                "default_vrf": {"route_policy": "new-policy"},
                                "vrf": {"advertise_as_vpn": True},
                            },
                        },
                        "export": {
                            "route_policy": "export-policy",
                            "route_target": "192.0.2.1:400",
                            "to": {
                                "default_vrf": {"route_policy": "rm-policy"},
                                "vrf": {"allow_imported_vpn": True},
                            },
                        },
                        "maximum": {"prefix": 23},
                    },
                ],
            },
        ]

        self.assertEqual(parsed_list, result["parsed"])
