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
from ansible_collections.cisco.iosxr.plugins.modules import (
    iosxr_bgp_neighbor_address_family,
)
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import (
    set_module_args,
)
from .iosxr_module import TestIosxrModule


class TestIosxrBgpNeighborAddressFamilyModule(TestIosxrModule):
    module = iosxr_bgp_neighbor_address_family

    def setUp(self):
        super(TestIosxrBgpNeighborAddressFamilyModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection"
        )
        self.get_resource_connection = (
            self.mock_get_resource_connection.start()
        )

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.bgp_neighbor_address_family.bgp_neighbor_address_family."
            "Bgp_neighbor_address_familyFacts.get_config"
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrBgpNeighborAddressFamilyModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_bgp_nbr_af_merged_idempotent(self):
        run_cfg = dedent(
            """\
                router bgp 1
                 bgp router-id 1.2.3.4
                 neighbor 1.1.1.1
                  remote-as 5
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   aigp send med
                   send-community-ebgp
                   multipath
                   allowas-in 4
                   maximum-prefix 10 20 restart 10
                   as-override
                   capability orf prefix both
                   send-extended-community-ebgp
                   default-originate
                   next-hop-self
                   send-community-gshut-ebgp
                   soft-reconfiguration inbound
                   send-multicast-attributes
                   remove-private-AS inbound entire-aspath
                   route-policy test1 in
                   route-policy test1 out
                   next-hop-unchanged multipath
                 vrf vrf1
                  rd auto
                  address-family ipv4 unicast
                  neighbor 1.2.1.2
                   remote-as 5
                   address-family ipv4 unicast
                    multipath
                    capability orf prefix both
                    default-originate
            """
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            neighbors=[
                                dict(
                                    neighbor_address="1.2.1.2",
                                    address_family=[
                                        dict(
                                            afi="ipv4",
                                            safi="unicast",
                                            multipath=True,
                                            default_originate=dict(set=True),
                                            capability_orf_prefix="both",
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="1.1.1.1",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    multipath=True,
                                    default_originate=dict(set=True),
                                    capability_orf_prefix="both",
                                    send_multicast_attributes=dict(set=True),
                                    soft_reconfiguration=dict(
                                        inbound=dict(set=True)
                                    ),
                                    send_community_gshut_ebgp=dict(set=True),
                                    send_extended_community_ebgp=dict(
                                        set=True
                                    ),
                                    send_community_ebgp=dict(set=True),
                                    origin_as=dict(
                                        validation=dict(disable=True)
                                    ),
                                    remove_private_AS=dict(
                                        set=True,
                                        inbound=True,
                                        entire_aspath=True,
                                    ),
                                    route_policy=dict(
                                        inbound="test1", outbound="test1"
                                    ),
                                    maximum_prefix=dict(
                                        max_limit=10,
                                        threshold_value=20,
                                        restart=10,
                                    ),
                                    next_hop_self=dict(set=True),
                                    next_hop_unchanged=dict(multipath=True),
                                    aigp=dict(
                                        set=True, send_med=dict(set=True)
                                    ),
                                    as_override=dict(set=True),
                                    allowas_in=dict(value=4),
                                    bestpath_origin_as_allow_invalid=True,
                                    long_lived_graceful_restart=dict(
                                        stale_time=dict(send=20, accept=30)
                                    ),
                                )
                            ],
                        )
                    ],
                ),
                state="merged",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_bgp_nbr_af_merged(self):
        self.maxDiff = None
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            neighbors=[
                                dict(
                                    neighbor_address="1.2.1.2",
                                    address_family=[
                                        dict(
                                            afi="ipv4",
                                            safi="unicast",
                                            multipath=True,
                                            default_originate=dict(set=True),
                                            capability_orf_prefix="both",
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="1.1.1.1",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    multipath=True,
                                    default_originate=dict(set=True),
                                    capability_orf_prefix="both",
                                    send_multicast_attributes=dict(set=True),
                                    soft_reconfiguration=dict(
                                        inbound=dict(set=True)
                                    ),
                                    send_community_gshut_ebgp=dict(set=True),
                                    send_extended_community_ebgp=dict(
                                        set=True
                                    ),
                                    send_community_ebgp=dict(set=True),
                                    origin_as=dict(
                                        validation=dict(disable=True)
                                    ),
                                    remove_private_AS=dict(
                                        set=True,
                                        inbound=True,
                                        entire_aspath=True,
                                    ),
                                    route_policy=dict(
                                        inbound="test1", outbound="test1"
                                    ),
                                    maximum_prefix=dict(
                                        max_limit=10,
                                        threshold_value=20,
                                        restart=10,
                                    ),
                                    next_hop_self=dict(set=True),
                                    next_hop_unchanged=dict(multipath=True),
                                    aigp=dict(
                                        set=True, send_med=dict(set=True)
                                    ),
                                    as_override=dict(set=True),
                                    bestpath_origin_as_allow_invalid=True,
                                    long_lived_graceful_restart=dict(
                                        stale_time=dict(send=20, accept=30)
                                    ),
                                )
                            ],
                        )
                    ],
                ),
                state="merged",
            )
        )
        commands = [
            "router bgp 1",
            "neighbor 1.1.1.1",
            "address-family ipv4 unicast",
            "aigp",
            "aigp send med",
            "as-override",
            "bestpath origin-as allow invalid",
            "capability orf prefix both",
            "default-originate",
            "maximum-prefix 10 20 restart 10",
            "multipath",
            "next-hop-self",
            "next-hop-unchanged multipath",
            "origin-as validation disable",
            "remove-private-AS inbound entire-aspath",
            "route-policy test1 in",
            "route-policy test1 out",
            "send-community-ebgp",
            "send-community-gshut-ebgp",
            "send-extended-community-ebgp",
            "send-multicast-attributes",
            "soft-reconfiguration inbound",
            "vrf vrf1",
            "neighbor 1.2.1.2",
            "address-family ipv4 unicast",
            "capability orf prefix both",
            "default-originate",
            "multipath",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_nbr_af_replaced(self):
        run_cfg = dedent(
            """\
                router bgp 1
                 bgp router-id 1.2.3.4
                 neighbor 1.1.1.1
                  remote-as 5
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   aigp send med
                   send-community-ebgp
                   multipath
                   allowas-in 4
                   maximum-prefix 10 20 restart 10
                   as-override
                   capability orf prefix both
                   send-extended-community-ebgp
                   default-originate
                   next-hop-self
                   send-community-gshut-ebgp
                   soft-reconfiguration inbound
                   send-multicast-attributes
                   remove-private-AS inbound entire-aspath
                   next-hop-unchanged multipath
                 vrf vrf1
                  rd auto
                  address-family ipv4 unicast
                  neighbor 1.2.1.2
                   remote-as 5
                   address-family ipv4 unicast
                    multipath
                    capability orf prefix both
                    default-originate
                    route-policy test2 in
                    route-policy test2 out
            """
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            neighbors=[
                                dict(
                                    neighbor_address="1.2.1.2",
                                    address_family=[
                                        dict(
                                            afi="ipv4",
                                            safi="unicast",
                                            multipath=True,
                                            default_originate=dict(set=True),
                                            route_policy=dict(
                                                inbound="test1",
                                                outbound="test1",
                                            ),
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                ),
                state="replaced",
            )
        )
        commands = [
            "router bgp 1",
            "vrf vrf1",
            "neighbor 1.2.1.2",
            "address-family ipv4 unicast",
            "no capability orf prefix both",
            "route-policy test1 in",
            "route-policy test1 out",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_nbr_af_replaced_idempotent(self):
        run_cfg = dedent(
            """\
                router bgp 1
                 bgp router-id 1.2.3.4
                 neighbor 1.1.1.1
                  remote-as 5
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   aigp send med
                   send-community-ebgp
                   multipath
                   allowas-in 4
                   maximum-prefix 10 20 restart 10
                   as-override
                   capability orf prefix both
                   send-extended-community-ebgp
                   default-originate
                   next-hop-self
                   send-community-gshut-ebgp
                   soft-reconfiguration inbound
                   send-multicast-attributes
                   remove-private-AS inbound entire-aspath
                   next-hop-unchanged multipath
                 vrf vrf1
                  rd auto
                  address-family ipv4 unicast
                  neighbor 1.2.1.2
                   remote-as 5
                   address-family ipv4 unicast
                    multipath
                    capability orf prefix both
                    default-originate
            """
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            neighbors=[
                                dict(
                                    neighbor_address="1.2.1.2",
                                    address_family=[
                                        dict(
                                            afi="ipv4",
                                            safi="unicast",
                                            multipath=True,
                                            default_originate=dict(set=True),
                                            capability_orf_prefix="both",
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                ),
                state="replaced",
            )
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_bgp_nbr_af_deleted(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                    router bgp 1
                     bgp router-id 1.2.3.4
                     neighbor 1.1.1.1
                      remote-as 5
                      address-family ipv4 unicast
                       origin-as validation disable
                       bestpath origin-as allow invalid
                       aigp
                       aigp send med
                       send-community-ebgp
                       multipath
                       allowas-in 4
                       maximum-prefix 10 20 restart 10
                       as-override
                       capability orf prefix both
                       send-extended-community-ebgp
                       default-originate
                       next-hop-self
                       send-community-gshut-ebgp
                       soft-reconfiguration inbound
                       send-multicast-attributes
                       remove-private-AS inbound entire-aspath
                       next-hop-unchanged multipath
                     vrf vrf1
                      rd auto
                      address-family ipv4 unicast
                      neighbor 1.2.1.2
                       remote-as 5
                       address-family ipv4 unicast
                        multipath
                        capability orf prefix both
                        default-originate
                """
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(), state="deleted"))
        commands = [
            "router bgp 1",
            "neighbor 1.1.1.1",
            "no address-family ipv4 unicast",
            "vrf vrf1",
            "neighbor 1.2.1.2",
            "no address-family ipv4 unicast",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_nbr_af_deleted_idempotent(self):
        run_cfg = dedent(
            """\
            """
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(as_number="1"), state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_iosxr_bgp_nbr_af_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            neighbors=[
                                dict(
                                    neighbor_address="1.2.1.2",
                                    address_family=[
                                        dict(
                                            afi="ipv4",
                                            safi="unicast",
                                            multipath=True,
                                            default_originate=dict(set=True),
                                            capability_orf_prefix="both",
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                    neighbors=[
                        dict(
                            neighbor_address="1.1.1.1",
                            address_family=[
                                dict(
                                    afi="ipv4",
                                    safi="unicast",
                                    multipath=True,
                                    default_originate=dict(set=True),
                                    capability_orf_prefix="both",
                                    send_multicast_attributes=dict(set=True),
                                    soft_reconfiguration=dict(
                                        inbound=dict(set=True)
                                    ),
                                    send_community_gshut_ebgp=dict(set=True),
                                    send_extended_community_ebgp=dict(
                                        set=True
                                    ),
                                    send_community_ebgp=dict(set=True),
                                    origin_as=dict(
                                        validation=dict(disable=True)
                                    ),
                                    remove_private_AS=dict(
                                        set=True,
                                        inbound=True,
                                        entire_aspath=True,
                                    ),
                                    maximum_prefix=dict(
                                        max_limit=10,
                                        threshold_value=20,
                                        restart=10,
                                    ),
                                    next_hop_self=dict(set=True),
                                    next_hop_unchanged=dict(multipath=True),
                                    aigp=dict(
                                        set=True, send_med=dict(set=True)
                                    ),
                                    as_override=dict(set=True),
                                    allowas_in=dict(value=4),
                                    bestpath_origin_as_allow_invalid=True,
                                    long_lived_graceful_restart=dict(
                                        stale_time=dict(send=20, accept=30)
                                    ),
                                )
                            ],
                        )
                    ],
                ),
                state="rendered",
            )
        )
        commands = [
            "router bgp 1",
            "neighbor 1.1.1.1",
            "address-family ipv4 unicast",
            "aigp",
            "aigp send med",
            "allowas-in 4",
            "as-override",
            "bestpath origin-as allow invalid",
            "capability orf prefix both",
            "default-originate",
            "maximum-prefix 10 20 restart 10",
            "multipath",
            "next-hop-self",
            "next-hop-unchanged multipath",
            "origin-as validation disable",
            "remove-private-AS inbound entire-aspath",
            "send-community-ebgp",
            "send-community-gshut-ebgp",
            "send-extended-community-ebgp",
            "send-multicast-attributes",
            "soft-reconfiguration inbound",
            "vrf vrf1",
            "neighbor 1.2.1.2",
            "address-family ipv4 unicast",
            "capability orf prefix both",
            "default-originate",
            "multipath",
        ]

        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_bgp_global_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="router bgp 1\n bgp router-id 1.2.1.3\n neighbor 1.1.1.1\n  "
                "remote-as 6\n  address-family ipv4 unicast\n   origin-as validation disable\n   "
                "bestpath origin-as allow invalid\n   weight 0\n   send-community-ebgp\n  "
                " multipath\n   allowas-in 3\n   maximum-prefix 1 1 discard-extra-paths\n"
                "   capability orf prefix both\n   "
                "send-extended-community-ebgp\n   long-lived-graceful-restart capable\n"
                "   next-hop-self\n   "
                "remove-private-AS\n   send-community-gshut-ebgp inheritance-disable\n "
                "  send-multicast-attributes\n   "
                "remove-private-AS inbound entire-aspath\n   "
                "next-hop-unchanged multipath\n  !\n  "
                "!\n !",
                state="parsed",
            )
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "as_number": "1",
            "neighbors": [
                {
                    "address_family": [
                        {
                            "afi": "ipv4",
                            "allowas_in": {"value": 3},
                            "bestpath_origin_as_allow_invalid": True,
                            "capability_orf_prefix": "both",
                            "long_lived_graceful_restart": {"capable": True},
                            "multipath": True,
                            "next_hop_self": {"set": True},
                            "next_hop_unchanged": {"multipath": True},
                            "origin_as": {"validation": {"disable": True}},
                            "remove_private_AS": {
                                "entire_aspath": True,
                                "inbound": True,
                                "set": True,
                            },
                            "safi": "unicast",
                            "send_community_ebgp": {"set": True},
                            "send_community_gshut_ebgp": {
                                "inheritance_disable": True
                            },
                            "send_extended_community_ebgp": {"set": True},
                            "send_multicast_attributes": {"set": True},
                            "weight": 0,
                        }
                    ],
                    "neighbor_address": "1.1.1.1",
                }
            ],
        }

        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_bgp_nbr_af_overridden(self):
        run_cfg = dedent(
            """\
                router bgp 1
                 bgp router-id 1.2.3.4
                 neighbor 1.1.1.1
                  remote-as 5
                  address-family ipv4 unicast
                   origin-as validation disable
                   bestpath origin-as allow invalid
                   aigp
                   aigp send med
                   send-community-ebgp
                   multipath
                   allowas-in 4
                   maximum-prefix 10 20 restart 10
                   as-override
                   capability orf prefix both
                   send-extended-community-ebgp
                   default-originate
                   next-hop-self
                   send-community-gshut-ebgp
                   soft-reconfiguration inbound
                   send-multicast-attributes
                   remove-private-AS inbound entire-aspath
                   next-hop-unchanged multipath
                 vrf vrf1
                  rd auto
                  address-family ipv4 unicast
                  neighbor 1.2.1.2
                   remote-as 5
                   address-family ipv4 unicast
                    multipath
                    capability orf prefix both
                    default-originate
                    route-policy test2 in
                    route-policy test2 out
            """
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="1",
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            neighbors=[
                                dict(
                                    neighbor_address="1.2.1.2",
                                    address_family=[
                                        dict(
                                            afi="ipv4",
                                            safi="unicast",
                                            multipath=True,
                                            default_originate=dict(set=True),
                                        )
                                    ],
                                )
                            ],
                        )
                    ],
                ),
                state="overridden",
            )
        )
        commands = [
            "router bgp 1",
            "vrf vrf1",
            "neighbor 1.2.1.2",
            "address-family ipv4 unicast",
            "no capability orf prefix both",
            "no route-policy test2 in",
            "no route-policy test2 out",
            "neighbor 1.1.1.1",
            "no address-family ipv4 unicast",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))
