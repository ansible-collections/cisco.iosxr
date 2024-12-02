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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_bgp_templates
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrBgptemplatesModule(TestIosxrModule):
    module = iosxr_bgp_templates

    def setUp(self):
        super(TestIosxrBgptemplatesModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.bgp_templates.bgp_templates."
            "Bgp_templatesFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrBgptemplatesModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_bgp_tmpl_merged_idempotent(self):
        run_cfg = dedent(
            """\
                router bgp 1
                 neighbor-group test
                  bfd fast-detect strict-mode
                  precedence critical
                  advertisement-interval 10
                  internal-vpn-client
                  address-family ipv4 unicast
                   advertise local-labeled-route
                  !
                 !
                 neighbor-group test1
                  bfd fast-detect
                  bfd minimum-interval 3
                  keychain test
                  ebgp-multihop 255
                  egress-engineering
                  precedence flash
                  graceful-maintenance
                   as-prepends 0
                  !
                  advertisement-interval 2
                  tcp mss inheritance-disable
                  local-as 6
                  password inheritance-disable
                  cluster-id 1
                  dmz-link-bandwidth
                  description test
                  ttl-security
                  local address inheritance-disable
                  update-source Loopback919
                  idle-watch-time 30
                  ignore-connected-check
                  session-open-mode both
                  send-buffer-size 4096
                  receive-buffer-size 512
                  internal-vpn-client
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   weight 0
                   send-community-ebgp
                   multipath
                   route-reflector-client
                   allowas-in 1
                   maximum-prefix 1 75
                   as-override
                   capability orf prefix send
                   send-extended-community-ebgp
                   default-originate
                   long-lived-graceful-restart capable
                   next-hop-self
                   send-community-gshut-ebgp inheritance-disable
                   soft-reconfiguration inbound
                   send-multicast-attributes disable
                   Signalling bgp disable
                   remove-private-AS inbound
                   update out originator-loopcheck disable
                   advertise local-labeled-route
                   next-hop-unchanged inheritance-disable
                  !
                 !

            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    neighbor=[
                        dict(
                            name="test",
                            bfd=dict(fast_detect=dict(strict_mode=True)),
                            advertisement_interval=10,
                            precedence="critical",
                            internal_vpn_client=True,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    advertise=dict(local_labeled_route=dict(set=True)),
                                ),
                            ],
                        ),
                        dict(
                            name="test1",
                            bfd=dict(
                                fast_detect=dict(set=True),
                                minimum_interval=3,
                            ),
                            keychain=dict(name="test"),
                            ebgp_multihop=dict(value=255),
                            egress_engineering=dict(set=True),
                            precedence="flash",
                            graceful_maintenance=dict(
                                as_prepends=dict(
                                    value="0",
                                ),
                                set=True,
                            ),
                            advertisement_interval=2,
                            tcp=dict(mss=dict(inheritance_disable=True)),
                            local_as=dict(value=6),
                            password=dict(inheritance_disable=True),
                            cluster_id=1,
                            dmz_link_bandwidth=dict(set=True),
                            description="test",
                            ttl_security=dict(set=True),
                            local_address_subnet="1.1.1.1/24",
                            update_source="Loopback919",
                            idle_watch_time=30,
                            ignore_connected_check=dict(set=True),
                            session_open_mode="both",
                            send_buffer_size=4096,
                            receive_buffer_size=512,
                            internal_vpn_client=True,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    origin_as=dict(validation=dict(disable=True)),
                                    bestpath_origin_as_allow_invalid=True,
                                    aigp=dict(set=True),
                                    weight=0,
                                    multipath=True,
                                    send_community_ebgp=dict(set=True),
                                    route_reflector_client=dict(set=True),
                                    allowas_in=dict(value=1),
                                    maximum_prefix=dict(
                                        max_limit=1,
                                        threshold_value=75,
                                    ),
                                    as_override=dict(set=True),
                                    capability_orf_prefix="send",
                                    send_extended_community_ebgp=dict(set=True),
                                    default_originate=dict(set=True),
                                    long_lived_graceful_restart=dict(
                                        capable=True,
                                    ),
                                    next_hop_self=dict(set=True),
                                    send_community_gshut_ebgp=dict(inheritance_disable=True),
                                    soft_reconfiguration=dict(inbound=dict(set=True)),
                                    send_multicast_attributes=dict(disable=True),
                                    signalling=dict(bgp_disable=True),
                                    remove_private_AS=dict(
                                        inbound=True,
                                    ),
                                    next_hop_unchanged=dict(inheritance_disable=True),
                                    advertise=dict(local_labeled_route=dict(set=True)),
                                    update=dict(
                                        out_originator_loopcheck_disable=True,
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_bgp_tmpl_merged(self):
        self.maxDiff = None
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    neighbor=[
                        dict(
                            name="test",
                            bfd=dict(fast_detect=dict(strict_mode=True)),
                            advertisement_interval=10,
                            precedence="critical",
                            internal_vpn_client=True,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    advertise=dict(local_labeled_route=dict(set=True)),
                                ),
                                dict(
                                    afi="vpnv4",
                                    safi="unicast",
                                ),
                                dict(
                                    afi="vpnv6",
                                    safi="unicast",
                                ),
                                dict(
                                    afi="link-state",
                                    safi="link-state",
                                ),
                                dict(
                                    afi="l2vpn",
                                    safi="evpn",
                                ),
                            ],
                        ),
                        dict(
                            name="test1",
                            bfd=dict(
                                fast_detect=dict(set=True),
                                minimum_interval=3,
                            ),
                            keychain=dict(name="test"),
                            ebgp_multihop=dict(value=255),
                            egress_engineering=dict(set=True),
                            precedence="flash",
                            graceful_maintenance=dict(
                                as_prepends=dict(
                                    value="0",
                                ),
                                set=True,
                            ),
                            advertisement_interval=2,
                            tcp=dict(mss=dict(inheritance_disable=True)),
                            local_as=dict(value=6),
                            password=dict(inheritance_disable=True),
                            cluster_id=1,
                            dmz_link_bandwidth=dict(set=True),
                            description="test",
                            ttl_security=dict(set=True),
                            local_address_subnet="1.1.1.1/24",
                            update_source="Loopback919",
                            idle_watch_time=30,
                            ignore_connected_check=dict(set=True),
                            session_open_mode="both",
                            send_buffer_size=4096,
                            receive_buffer_size=512,
                            internal_vpn_client=True,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    origin_as=dict(validation=dict(disable=True)),
                                    bestpath_origin_as_allow_invalid=True,
                                    aigp=dict(set=True),
                                    weight=0,
                                    multipath=True,
                                    send_community_ebgp=dict(set=True),
                                    route_reflector_client=dict(set=True),
                                    allowas_in=dict(value=1),
                                    maximum_prefix=dict(
                                        max_limit=1,
                                        threshold_value=75,
                                    ),
                                    as_override=dict(set=True),
                                    capability_orf_prefix="send",
                                    send_extended_community_ebgp=dict(set=True),
                                    default_originate=dict(set=True),
                                    long_lived_graceful_restart=dict(
                                        capable=True,
                                    ),
                                    next_hop_self=dict(set=True),
                                    send_community_gshut_ebgp=dict(inheritance_disable=True),
                                    soft_reconfiguration=dict(inbound=dict(set=True)),
                                    send_multicast_attributes=dict(disable=True),
                                    signalling=dict(bgp_disable=True),
                                    remove_private_AS=dict(
                                        inbound=True,
                                    ),
                                    next_hop_unchanged=dict(inheritance_disable=True),
                                    advertise=dict(local_labeled_route=dict(set=True)),
                                    update=dict(
                                        out_originator_loopcheck_disable=True,
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        commands = [
            "router bgp 1",
            "neighbor-group test",
            "advertisement-interval 10",
            "bfd fast-detect strict-mode",
            "internal-vpn-client",
            "precedence critical",
            "address-family vpnv4 unicast",
            "address-family vpnv6 unicast",
            "address-family link-state link-state",
            "address-family l2vpn evpn",
            "address-family ipv4 unicast",
            "advertise local-labeled-route",
            "neighbor-group test1",
            "advertisement-interval 2",
            "bfd fast-detect",
            "bfd minimum-interval 3",
            "dmz-link-bandwidth",
            "description test",
            "cluster-id 1",
            "ebgp-multihop 255",
            "egress-engineering",
            "idle-watch-time 30 ",
            "internal-vpn-client",
            "ignore-connected-check",
            "keychain test",
            "local-as 6",
            "password inheritance-disable",
            "precedence flash",
            "receive-buffer-size 512",
            "send-buffer-size 4096",
            "session-open-mode both",
            "tcp mss inheritance-disable",
            "update-source Loopback919",
            "ttl-security",
            "graceful-maintenance",
            "graceful-maintenance as-prepends 0",
            "address-family ipv4 unicast",
            "advertise local-labeled-route",
            "aigp",
            "allowas-in 1",
            "as-override",
            "bestpath origin-as allow invalid",
            "capability orf prefix send",
            "default-originate",
            "long-lived-graceful-restart capable",
            "maximum-prefix 1 75",
            "multipath",
            "next-hop-self",
            "next-hop-unchanged inheritance-disable",
            "origin-as validation disable",
            "remove-private-AS inbound",
            "route-reflector-client",
            "send-community-ebgp",
            "send-community-gshut-ebgp inheritance-disable",
            "send-extended-community-ebgp",
            "send-multicast-attributes disable",
            "soft-reconfiguration inbound",
            "weight 0",
            "signalling bgp disable ",
            "update out originator-loopcheck disable",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_tmpl_deleted(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                router bgp 1
                 neighbor-group test
                  bfd fast-detect strict-mode
                  precedence critical
                  advertisement-interval 10
                  internal-vpn-client
                  address-family ipv4 unicast
                   advertise local-labeled-route
                  !
                 !
                 neighbor-group test1
                  bfd fast-detect
                  bfd minimum-interval 3
                  keychain test
                  ebgp-multihop 255
                  egress-engineering
                  precedence flash
                  graceful-maintenance
                   as-prepends 0
                  !
                  advertisement-interval 2
                  tcp mss inheritance-disable
                  local-as 6
                  password inheritance-disable
                  cluster-id 1
                  dmz-link-bandwidth
                  description test
                  ttl-security
                  local address inheritance-disable
                  update-source Loopback919
                  idle-watch-time 30
                  ignore-connected-check
                  session-open-mode both
                  send-buffer-size 4096
                  receive-buffer-size 512
                  internal-vpn-client
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   weight 0
                   send-community-ebgp
                   multipath
                   route-reflector-client
                   allowas-in 1
                   maximum-prefix 1 75
                   as-override
                   capability orf prefix send
                   send-extended-community-ebgp
                   default-originate
                   long-lived-graceful-restart capable
                   next-hop-self
                   send-community-gshut-ebgp inheritance-disable
                   soft-reconfiguration inbound
                   send-multicast-attributes disable
                   Signalling bgp disable
                   remove-private-AS inbound
                   update out originator-loopcheck disable
                   advertise local-labeled-route
                   next-hop-unchanged inheritance-disable
                  !
                 !

                """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(), state="deleted"))
        commands = [
            "router bgp 1",
            "no neighbor-group test",
            "no neighbor-group test1",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_tmpl_deleted_idempotent(self):
        run_cfg = dedent(
            """\
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(as_number="1"), state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_iosxr_bgp_tmpl_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    neighbor=[
                        dict(
                            name="test",
                            bfd=dict(fast_detect=dict(strict_mode=True)),
                            advertisement_interval=10,
                            precedence="critical",
                            internal_vpn_client=True,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    advertise=dict(local_labeled_route=dict(set=True)),
                                ),
                            ],
                        ),
                        dict(
                            name="test1",
                            bfd=dict(
                                fast_detect=dict(set=True),
                                minimum_interval=3,
                            ),
                            keychain=dict(name="test"),
                            ebgp_multihop=dict(value=255),
                            egress_engineering=dict(set=True),
                            precedence="flash",
                            graceful_maintenance=dict(
                                as_prepends=dict(
                                    value="0",
                                ),
                                set=True,
                            ),
                            advertisement_interval=2,
                            tcp=dict(mss=dict(inheritance_disable=True)),
                            local_as=dict(no_prepend=dict(replace_as=dict(dual_as=True))),
                            password=dict(inheritance_disable=True),
                            cluster_id=1,
                            dmz_link_bandwidth=dict(set=True),
                            description="test",
                            ttl_security=dict(set=True),
                            local_address_subnet="1.1.1.1/24",
                            update_source="Loopback919",
                            idle_watch_time=30,
                            ignore_connected_check=dict(set=True),
                            session_open_mode="both",
                            send_buffer_size=4096,
                            receive_buffer_size=512,
                            internal_vpn_client=True,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    origin_as=dict(validation=dict(disable=True)),
                                    bestpath_origin_as_allow_invalid=True,
                                    aigp=dict(set=True),
                                    weight=0,
                                    multipath=True,
                                    send_community_ebgp=dict(set=True),
                                    route_reflector_client=dict(set=True),
                                    allowas_in=dict(value=1),
                                    maximum_prefix=dict(
                                        warning_only=True,
                                    ),
                                    as_override=dict(set=True),
                                    capability_orf_prefix="send",
                                    send_extended_community_ebgp=dict(set=True),
                                    default_originate=dict(set=True),
                                    long_lived_graceful_restart=dict(
                                        capable=True,
                                    ),
                                    next_hop_self=dict(set=True),
                                    send_community_gshut_ebgp=dict(inheritance_disable=True),
                                    soft_reconfiguration=dict(inbound=dict(always=True)),
                                    send_multicast_attributes=dict(disable=True),
                                    signalling=dict(bgp_disable=True),
                                    remove_private_AS=dict(
                                        inbound=True,
                                        entire_aspath=True,
                                        inheritance_disable=True,
                                    ),
                                    next_hop_unchanged=dict(multipath=True),
                                    advertise=dict(local_labeled_route=dict(set=True)),
                                    update=dict(
                                        out_originator_loopcheck_disable=True,
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
                state="rendered",
            ),
        )
        commands = [
            "router bgp 1",
            "neighbor-group test",
            "advertisement-interval 10",
            "bfd fast-detect strict-mode",
            "internal-vpn-client",
            "precedence critical",
            "address-family ipv4 unicast",
            "advertise local-labeled-route",
            "neighbor-group test1",
            "advertisement-interval 2",
            "bfd fast-detect",
            "bfd minimum-interval 3",
            "dmz-link-bandwidth",
            "description test",
            "cluster-id 1",
            "ebgp-multihop 255",
            "egress-engineering",
            "idle-watch-time 30 ",
            "internal-vpn-client",
            "ignore-connected-check",
            "keychain test",
            "local-as no-prepend replace-as dual-as",
            "password inheritance-disable",
            "precedence flash",
            "receive-buffer-size 512",
            "send-buffer-size 4096",
            "session-open-mode both",
            "tcp mss inheritance-disable",
            "update-source Loopback919",
            "ttl-security",
            "graceful-maintenance",
            "graceful-maintenance as-prepends 0",
            "address-family ipv4 unicast",
            "advertise local-labeled-route",
            "aigp",
            "allowas-in 1",
            "as-override",
            "bestpath origin-as allow invalid",
            "capability orf prefix send",
            "default-originate",
            "long-lived-graceful-restart capable",
            "maximum-prefix warning-only",
            "multipath",
            "next-hop-self",
            "next-hop-unchanged multipath",
            "origin-as validation disable",
            "remove-private-AS inbound entire-aspath inheritance-disable",
            "route-reflector-client",
            "send-community-ebgp",
            "send-community-gshut-ebgp inheritance-disable",
            "send-extended-community-ebgp",
            "send-multicast-attributes disable",
            "soft-reconfiguration inbound always",
            "weight 0",
            "signalling bgp disable ",
            "update out originator-loopcheck disable",
        ]

        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_bgp_tmpl_replaced(self):
        run_cfg = dedent(
            """\
                router bgp 1
                 neighbor-group test
                  bfd fast-detect strict-mode
                  precedence critical
                  advertisement-interval 10
                  internal-vpn-client
                  address-family ipv4 unicast
                   advertise local-labeled-route
                  !
                 !
                 neighbor-group test1
                  bfd fast-detect
                  bfd minimum-interval 3
                  keychain test
                  ebgp-multihop 255
                  egress-engineering
                  precedence flash
                  graceful-maintenance
                   as-prepends 0
                  !
                  advertisement-interval 2
                  tcp mss inheritance-disable
                  local-as 6
                  password inheritance-disable
                  cluster-id 1
                  dmz-link-bandwidth
                  description test
                  ttl-security
                  local address inheritance-disable
                  update-source Loopback919
                  idle-watch-time 30
                  ignore-connected-check
                  session-open-mode both
                  send-buffer-size 4096
                  receive-buffer-size 512
                  internal-vpn-client
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   weight 0
                   send-community-ebgp
                   multipath
                   route-reflector-client
                   allowas-in 1
                   maximum-prefix 1 75
                   as-override
                   capability orf prefix send
                   send-extended-community-ebgp
                   default-originate
                   long-lived-graceful-restart capable
                   next-hop-self
                   send-community-gshut-ebgp inheritance-disable
                   soft-reconfiguration inbound
                   send-multicast-attributes disable
                   Signalling bgp disable
                   remove-private-AS inbound
                   update out originator-loopcheck disable
                   advertise local-labeled-route
                   next-hop-unchanged inheritance-disable
                  !
                 !

            """,
        )
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    neighbor=[
                        dict(
                            name="test",
                            advertisement_interval=11,
                            internal_vpn_client=True,
                        ),
                        dict(
                            name="test1",
                            bfd=dict(
                                minimum_interval=4,
                            ),
                            ebgp_multihop=dict(value=254),
                            egress_engineering=dict(set=True),
                            precedence="critical",
                            graceful_maintenance=dict(
                                as_prepends=dict(
                                    value="4",
                                ),
                                set=True,
                            ),
                            advertisement_interval=3,
                            password=dict(encrypted="test"),
                            cluster_id=3,
                            description="test1",
                            ttl_security=dict(set=True),
                            local_address_subnet="1.1.1.2/24",
                            update_source="Loopback912",
                            idle_watch_time=34,
                            session_open_mode="active-only",
                            send_buffer_size=4097,
                            receive_buffer_size=513,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    weight=2,
                                    multipath=True,
                                    allowas_in=dict(value=2),
                                    maximum_prefix=dict(
                                        max_limit=1,
                                        threshold_value=75,
                                    ),
                                    soft_reconfiguration=dict(inbound=dict(always=True)),
                                    remove_private_AS=dict(
                                        inbound=True,
                                        entire_aspath=True,
                                        inheritance_disable=True,
                                    ),
                                    next_hop_unchanged=dict(multipath=True),
                                ),
                            ],
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        self.get_config.return_value = run_cfg

        commands = [
            "router bgp 1",
            "neighbor-group test",
            "no bfd fast-detect strict-mode",
            "no precedence critical",
            "advertisement-interval 11",
            "no address-family ipv4 unicast",
            "neighbor-group test1",
            "no bfd fast-detect",
            "no dmz-link-bandwidth",
            "no internal-vpn-client",
            "no ignore-connected-check",
            "no keychain test",
            "no local-as 6",
            "no local address inheritance-disable",
            "no password inheritance-disable",
            "no tcp mss inheritance-disable",
            "advertisement-interval 3",
            "bfd minimum-interval 4",
            "description test1",
            "cluster-id 3",
            "ebgp-multihop 254",
            "idle-watch-time 34 ",
            "password encrypted test",
            "precedence critical",
            "receive-buffer-size 513",
            "send-buffer-size 4097",
            "session-open-mode active-only",
            "update-source Loopback912",
            "graceful-maintenance as-prepends 4",
            "address-family ipv4 unicast",
            "no advertise local-labeled-route",
            "no aigp",
            "no as-override",
            "no bestpath origin-as allow invalid",
            "no capability orf prefix send",
            "no default-originate",
            "no long-lived-graceful-restart capable",
            "no next-hop-self",
            "no next-hop-unchanged inheritance-disable",
            "no origin-as validation disable",
            "no route-reflector-client",
            "no send-community-ebgp",
            "no send-community-gshut-ebgp inheritance-disable",
            "no send-extended-community-ebgp",
            "no send-multicast-attributes disable",
            "no signalling bgp disable ",
            "no update out originator-loopcheck disable",
            "allowas-in 2",
            "next-hop-unchanged multipath",
            "remove-private-AS inbound entire-aspath inheritance-disable",
            "soft-reconfiguration inbound always",
            "weight 2",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_tmpl_overridden(self):
        run_cfg = dedent(
            """\
                router bgp 1
                 neighbor-group test
                  bfd fast-detect strict-mode
                  precedence critical
                  advertisement-interval 10
                  internal-vpn-client
                  address-family ipv4 unicast
                   advertise local-labeled-route
                  !
                 !
                 neighbor-group test1
                  bfd fast-detect
                  bfd minimum-interval 3
                  keychain test
                  ebgp-multihop 255
                  egress-engineering
                  precedence flash
                  graceful-maintenance
                   as-prepends 0
                  !
                  advertisement-interval 2
                  tcp mss inheritance-disable
                  local-as 6
                  password inheritance-disable
                  cluster-id 1
                  dmz-link-bandwidth
                  description test
                  ttl-security
                  local address inheritance-disable
                  update-source Loopback919
                  idle-watch-time 30
                  ignore-connected-check
                  session-open-mode both
                  send-buffer-size 4096
                  receive-buffer-size 512
                  internal-vpn-client
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   weight 0
                   send-community-ebgp
                   multipath
                   route-reflector-client
                   allowas-in 1
                   maximum-prefix 1 75
                   as-override
                   capability orf prefix send
                   send-extended-community-ebgp
                   default-originate
                   long-lived-graceful-restart capable
                   next-hop-self
                   send-community-gshut-ebgp inheritance-disable
                   soft-reconfiguration inbound
                   send-multicast-attributes disable
                   Signalling bgp disable
                   remove-private-AS inbound
                   update out originator-loopcheck disable
                   advertise local-labeled-route
                   next-hop-unchanged inheritance-disable
                  !
                 !

            """,
        )
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    neighbor=[
                        dict(
                            name="test1",
                            bfd=dict(
                                minimum_interval=4,
                            ),
                            ebgp_multihop=dict(value=254),
                            egress_engineering=dict(set=True),
                            precedence="critical",
                            graceful_maintenance=dict(
                                as_prepends=dict(
                                    value="4",
                                ),
                                set=True,
                            ),
                            advertisement_interval=3,
                            password=dict(encrypted="test"),
                            cluster_id=3,
                            description="test1",
                            ttl_security=dict(set=True),
                            local_address_subnet="1.1.1.2/24",
                            update_source="Loopback912",
                            idle_watch_time=34,
                            session_open_mode="active-only",
                            send_buffer_size=4097,
                            receive_buffer_size=513,
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    weight=2,
                                    multipath=True,
                                    allowas_in=dict(value=2),
                                    maximum_prefix=dict(
                                        max_limit=1,
                                        threshold_value=75,
                                    ),
                                    soft_reconfiguration=dict(inbound=dict(always=True)),
                                    remove_private_AS=dict(
                                        inbound=True,
                                        entire_aspath=True,
                                        inheritance_disable=True,
                                    ),
                                    next_hop_unchanged=dict(multipath=True),
                                ),
                            ],
                        ),
                    ],
                ),
                state="overridden",
            ),
        )
        self.get_config.return_value = run_cfg
        commands = [
            "router bgp 1",
            "no neighbor-group test",
            "neighbor-group test1",
            "no bfd fast-detect",
            "no dmz-link-bandwidth",
            "no internal-vpn-client",
            "no ignore-connected-check",
            "no keychain test",
            "no local-as 6",
            "no local address inheritance-disable",
            "no password inheritance-disable",
            "no tcp mss inheritance-disable",
            "advertisement-interval 3",
            "bfd minimum-interval 4",
            "description test1",
            "cluster-id 3",
            "ebgp-multihop 254",
            "idle-watch-time 34 ",
            "password encrypted test",
            "precedence critical",
            "receive-buffer-size 513",
            "send-buffer-size 4097",
            "session-open-mode active-only",
            "update-source Loopback912",
            "graceful-maintenance as-prepends 4",
            "address-family ipv4 unicast",
            "no advertise local-labeled-route",
            "no aigp",
            "no as-override",
            "no bestpath origin-as allow invalid",
            "no capability orf prefix send",
            "no default-originate",
            "no long-lived-graceful-restart capable",
            "no next-hop-self",
            "no next-hop-unchanged inheritance-disable",
            "no origin-as validation disable",
            "no route-reflector-client",
            "no send-community-ebgp",
            "no send-community-gshut-ebgp inheritance-disable",
            "no send-extended-community-ebgp",
            "no send-multicast-attributes disable",
            "no signalling bgp disable ",
            "no update out originator-loopcheck disable",
            "allowas-in 2",
            "next-hop-unchanged multipath",
            "remove-private-AS inbound entire-aspath inheritance-disable",
            "soft-reconfiguration inbound always",
            "weight 2",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_tmpl_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="router bgp 1\n neighbor-group ********\n  "
                "bfd fast-detect strict-mode\n  update in filtering\n"
                "   message buffers 0 non-circular\n   logging disable\n"
                "  !\n  precedence critical\n  timers 0 3 3\n  "
                "advertisement-interval 10\n  maximum-peers 10\n  "
                "local-address-subnet 1.1.1.5/24\n  internal-vpn-client\n"
                "  address-family ipv4 unicast\n   advertise local-labeled-route\n"
                "  !\n !\n neighbor-group ********1\n  bfd fast-detect\n  "
                "update in filtering\n  !\n  bfd minimum-interval 3\n  "
                "capability additional-paths send disable\n  keychain ********\n"
                "  ebgp-multihop 255\n  egress-engineering\n  precedence flash\n  "
                "graceful-maintenance\n   as-prepends 0\n  !\n  advertisement-interval 2\n"
                "  tcp mss inheritance-disable\n  local-as 6\n  password inheritance-disable\n"
                "  shutdown inheritance-disable\n  maximum-peers 1\n  cluster-id 1\n"
                "  dmz-link-bandwidth\n  description ********\n  ttl-security\n  "
                "ebgp-recv-extcommunity-dmz\n  ebgp-send-extcommunity-dmz cumulative\n"
                "  local address inheritance-disable\n  update-source Loopback919\n  "
                "idle-watch-time 30\n  enforce-first-as\n  ignore-connected-check\n  "
                "session-open-mode both\n  send-buffer-size 4096\n  "
                "local-address-subnet 1.1.1.1/24\n  receive-buffer-size 512\n"
                "  internal-vpn-client\n  address-family ipv4 unicast\n   "
                "origin-as validation disable\n   bestpath origin-as allow invalid\n"
                "   weight 0\n   aigp send med\n   send-community-ebgp\n   multipath\n"
                "   route-reflector-client\n   allowas-in 1\n   "
                "encapsulation-type srv6\n   maximum-prefix 1 75\n   as-override\n   capability orf prefix send\n"
                "   send-extended-community-ebgp\n   default-originate\n   long-lived-graceful-restart capable\n"
                "   next-hop-self\n   send-community-gshut-ebgp inheritance-disable\n   soft-reconfiguration inbound\n"
                "   site-of-origin 1.1:1\n   send-multicast-attributes disable\n   Signalling bgp disable\n  "
                " remove-private-AS inbound\n   update out originator-loopcheck disable\n  "
                " advertise local-labeled-route\n   next-hop-unchanged inheritance-disable\n "
                "  cluster-id allow-equal disable\n  !       \n !        "
                "\n neighbor 1.1.1.1\n !        "
                "\n!",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "as_number": "1",
            "neighbor": [
                {
                    "name": "********",
                    "bfd": {"fast_detect": {"strict_mode": True}},
                    "update": {"in": {"filtering": {"logging": {"disable": True}}}},
                    "precedence": "critical",
                    "advertisement_interval": 10,
                    "maximum_peers": 10,
                    "internal_vpn_client": True,
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "safi": "unicast",
                            "advertise": {"local_labeled_route": {"set": True}},
                        },
                    ],
                },
                {
                    "name": "********1",
                    "bfd": {"fast_detect": {"set": True}, "minimum_interval": 3},
                    "capability": {"additional_paths": {"send": {"disable": True}}},
                    "keychain": {"name": "********"},
                    "ebgp_multihop": {"value": 255},
                    "egress_engineering": {"set": True},
                    "precedence": "flash",
                    "graceful_maintenance": {"set": True, "as_prepends": {"value": 0}},
                    "advertisement_interval": 2,
                    "tcp": {"mss": {"inheritance_disable": True}},
                    "local_as": {"value": 6},
                    "password": {"inheritance_disable": True},
                    "maximum_peers": 1,
                    "cluster_id": "1",
                    "dmz_link_bandwidth": {"set": True},
                    "description": "********",
                    "ttl_security": {"set": True},
                    "ebgp_recv_extcommunity_dmz": {"set": True},
                    "local": {"address": {"inheritance_disable": True}},
                    "update_source": "Loopback919",
                    "idle_watch_time": 30,
                    "ignore_connected_check": {"set": True},
                    "session_open_mode": "both",
                    "send_buffer_size": 4096,
                    "receive_buffer_size": 512,
                    "internal_vpn_client": True,
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "safi": "unicast",
                            "origin_as": {"validation": {"disable": True}},
                            "bestpath_origin_as_allow_invalid": True,
                            "weight": 0,
                            "aigp": {"send_med": {"set": True}},
                            "send_community_ebgp": {"set": True},
                            "multipath": True,
                            "route_reflector_client": {"set": True},
                            "allowas_in": {"value": 1},
                            "encapsulation_type_srv6": True,
                            "maximum_prefix": {"max_limit": 1, "threshold_value": 75},
                            "as_override": {"set": True},
                            "capability_orf_prefix": "send",
                            "send_extended_community_ebgp": {"set": True},
                            "default_originate": {"set": True},
                            "long_lived_graceful_restart": {"capable": True},
                            "next_hop_self": {"set": True},
                            "send_community_gshut_ebgp": {"inheritance_disable": True},
                            "soft_reconfiguration": {"inbound": {"set": True}},
                            "send_multicast_attributes": {"disable": True},
                            "signalling": {"bgp_disable": True},
                            "remove_private_AS": {"inbound": True},
                            "update": {"out_originator_loopcheck_disable": True},
                            "advertise": {"local_labeled_route": {"set": True}},
                            "next_hop_unchanged": {"inheritance_disable": True},
                        },
                    ],
                },
            ],
        }
        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_bgp_tmpl_gathered(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                router bgp 1
                 neighbor-group test
                  bfd fast-detect strict-mode
                  precedence critical
                  advertisement-interval 10
                  internal-vpn-client
                  address-family vpnv4 unicast
                  !
                  address-family vpnv6 unicast
                  !
                  address-family link-state link-state
                  !
                  address-family l2vpn evpn
                  !
                  address-family ipv4 unicast
                   advertise local-labeled-route
                  !
                 !
                 neighbor-group test1
                  bfd fast-detect
                  bfd minimum-interval 3
                  keychain test
                  ebgp-multihop 255
                  egress-engineering
                  precedence flash
                  graceful-maintenance
                   as-prepends 0
                  !
                  advertisement-interval 2
                  tcp mss inheritance-disable
                  local-as 6
                  password inheritance-disable
                  cluster-id 1
                  dmz-link-bandwidth
                  description test
                  ttl-security
                  local address inheritance-disable
                  update-source Loopback919
                  idle-watch-time 30
                  ignore-connected-check
                  session-open-mode both
                  send-buffer-size 4096
                  receive-buffer-size 512
                  internal-vpn-client
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   weight 0
                   send-community-ebgp
                   multipath
                   route-reflector-client
                   allowas-in 1
                   maximum-prefix 1 75
                   as-override
                   capability orf prefix send
                   send-extended-community-ebgp
                   default-originate
                   long-lived-graceful-restart capable
                   next-hop-self
                   send-community-gshut-ebgp inheritance-disable
                   soft-reconfiguration inbound
                   send-multicast-attributes disable
                   Signalling bgp disable
                   remove-private-AS inbound
                   update out originator-loopcheck disable
                   advertise local-labeled-route
                   next-hop-unchanged inheritance-disable
                  !
                 !

            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="gathered"))
        gathered = {
            "as_number": "1",
            "neighbor": [
                {
                    "name": "test",
                    "bfd": {"fast_detect": {"strict_mode": True}},
                    "precedence": "critical",
                    "advertisement_interval": 10,
                    "internal_vpn_client": True,
                    "address_family": [
                        {"afi": "vpnv4", "safi": "unicast"},
                        {"afi": "vpnv6", "safi": "unicast"},
                        {"afi": "link-state", "safi": "link-state"},
                        {"afi": "l2vpn", "safi": "evpn"},
                        {
                            "afi": "ipv4",
                            "safi": "unicast",
                            "advertise": {"local_labeled_route": {"set": True}},
                        },
                    ],
                },
                {
                    "name": "test1",
                    "bfd": {"fast_detect": {"set": True}, "minimum_interval": 3},
                    "keychain": {"name": "test"},
                    "ebgp_multihop": {"value": 255},
                    "egress_engineering": {"set": True},
                    "precedence": "flash",
                    "graceful_maintenance": {"set": True, "as_prepends": {"value": 0}},
                    "advertisement_interval": 2,
                    "tcp": {"mss": {"inheritance_disable": True}},
                    "local_as": {"value": 6},
                    "password": {"inheritance_disable": True},
                    "cluster_id": "1",
                    "dmz_link_bandwidth": {"set": True},
                    "description": "test",
                    "ttl_security": {"set": True},
                    "local": {"address": {"inheritance_disable": True}},
                    "update_source": "Loopback919",
                    "idle_watch_time": 30,
                    "ignore_connected_check": {"set": True},
                    "session_open_mode": "both",
                    "send_buffer_size": 4096,
                    "receive_buffer_size": 512,
                    "internal_vpn_client": True,
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "safi": "unicast",
                            "origin_as": {"validation": {"disable": True}},
                            "bestpath_origin_as_allow_invalid": True,
                            "aigp": {"set": True},
                            "weight": 0,
                            "send_community_ebgp": {"set": True},
                            "multipath": True,
                            "route_reflector_client": {"set": True},
                            "allowas_in": {"value": 1},
                            "maximum_prefix": {"max_limit": 1, "threshold_value": 75},
                            "as_override": {"set": True},
                            "capability_orf_prefix": "send",
                            "send_extended_community_ebgp": {"set": True},
                            "default_originate": {"set": True},
                            "long_lived_graceful_restart": {"capable": True},
                            "next_hop_self": {"set": True},
                            "send_community_gshut_ebgp": {"inheritance_disable": True},
                            "soft_reconfiguration": {"inbound": {"set": True}},
                            "send_multicast_attributes": {"disable": True},
                            "signalling": {"bgp_disable": True},
                            "remove_private_AS": {"inbound": True},
                            "update": {"out_originator_loopcheck_disable": True},
                            "advertise": {"local_labeled_route": {"set": True}},
                            "next_hop_unchanged": {"inheritance_disable": True},
                        },
                    ],
                },
            ],
        }
        result = self.execute_module(changed=False)
        self.assertEqual(gathered, result["gathered"])
