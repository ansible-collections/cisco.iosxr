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

    def test_iosxr_bgp_address_family_replaced(self):
        run_cfg = dedent(
            """\
            router bgp 65536
             address-family ipv4 unicast
              bgp attribute-download
              advertise best-external
              dynamic-med interval 10
              bgp scan-time 20
              redistribute connected metric 10
              redistribute isis test3 metric 4
              redistribute application test1 metric 10
              allocate-label all
            address-family ipv4 mvpn
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    address_family=[
                        dict(
                            afi="ipv4",
                            safi="unicast",
                            dynamic_med=4,
                            redistribute=[
                                dict(
                                    protocol="application",
                                    id="test1",
                                    metric=10,
                                ),
                                dict(protocol="connected", metric=10),
                                dict(protocol="isis", id="test3", metric=4),
                            ],
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        commands = [
            "router bgp 65536",
            "address-family ipv4 unicast",
            "no advertise best-external",
            "no allocate-label all",
            "no bgp attribute-download",
            "no bgp scan-time 20",
            "dynamic-med interval 4",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_address_family_replaced_idempotent(self):
        run_cfg = dedent(
            """\
            router bgp 65536
             address-family ipv4 unicast
              dynamic-med interval 4
              redistribute connected metric 10
              redistribute isis test3 metric 4
              redistribute application test1 metric 10
            address-family ipv4 mvpn
            """,
        )
        self.get_config.return_value = run_cfg

        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    address_family=[
                        dict(
                            afi="ipv4",
                            safi="unicast",
                            dynamic_med=4,
                            redistribute=[
                                dict(
                                    protocol="application",
                                    id="test1",
                                    metric=10,
                                ),
                                dict(protocol="connected", metric=10),
                                dict(protocol="isis", id="test3", metric=4),
                            ],
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_bgp_address_family_deleted(self):
        run_cfg = dedent(
            """\
            router bgp 65536
             address-family ipv4 unicast
              bgp attribute-download
              advertise best-external
              dynamic-med interval 10
              bgp scan-time 20
              redistribute connected metric 10
              redistribute isis test3 metric 4
              redistribute application test1 metric 10
              allocate-label all
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(), state="deleted"))

        commands = ["router bgp 65536", "no address-family ipv4 unicast"]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_address_family_deleted1(self):
        run_cfg = dedent(
            """\
            router bgp 65536
             address-family ipv6 unicast
              dynamic-med interval 4
             address-family ipv4 unicast
              bgp attribute-download
              advertise best-external
              dynamic-med interval 10
              bgp scan-time 20
              redistribute connected metric 10
              redistribute isis test3 metric 4
              redistribute application test1 metric 10
              allocate-label all
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number=65536,
                    address_family=[
                        dict(afi="ipv6", safi="unicast", dynamic_med=4),
                    ],
                ),
                state="deleted",
            ),
        )
        commands = ["router bgp 65536", "no address-family ipv6 unicast"]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_address_family_deleted_idempotent(self):
        run_cfg = dedent(
            """\
            "router bgp 65536"
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(as_number="65536"), state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_iosxr_bgp_address_family_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    address_family=[
                        dict(
                            afi="ipv4",
                            safi="unicast",
                            dynamic_med=10,
                            redistribute=[
                                dict(
                                    protocol="application",
                                    id="test1",
                                    metric=10,
                                ),
                                dict(protocol="connected", metric=10),
                                dict(protocol="isis", id="test3", metric=4),
                            ],
                            bgp=dict(scan_time=20, attribute_download=True),
                            advertise_best_external=True,
                            allocate_label=dict(all=True),
                        ),
                    ],
                ),
                state="rendered",
            ),
        )
        commands = [
            "router bgp 65536",
            "address-family ipv4 unicast",
            "advertise best-external",
            "allocate-label all",
            "bgp attribute-download",
            "bgp scan-time 20",
            "dynamic-med interval 10",
            "redistribute application test1 metric 10",
            "redistribute connected metric 10",
            "redistribute isis test3 metric 4",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_bgp_address_family_parsed(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
            router bgp 65536
             address-family ipv4 unicast
              bgp attribute-download
              advertise best-external
              dynamic-med interval 10
              bgp scan-time 20
              redistribute application test1 metric 10
              allocate-label all
            """,
        )
        set_module_args(dict(running_config=run_cfg, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = {
            "address_family": [
                {
                    "advertise_best_external": True,
                    "safi": "unicast",
                    "afi": "ipv4",
                    "allocate_label": {"all": True},
                    "bgp": {"attribute_download": True, "scan_time": 20},
                    "dynamic_med": 10,
                    "redistribute": [
                        {
                            "protocol": "application",
                            "metric": 10,
                            "id": "test1",
                        },
                    ],
                },
            ],
            "as_number": "65536",
        }

        self.assertEqual(parsed_list, result["parsed"])
