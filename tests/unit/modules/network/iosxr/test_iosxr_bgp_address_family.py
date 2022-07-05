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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_bgp_address_family
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrBgpGlobalModule(TestIosxrModule):
    module = iosxr_bgp_address_family

    def setUp(self):
        super(TestIosxrBgpGlobalModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base.get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.bgp_address_family.bgp_address_family.Bgp_address_familyFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrBgpGlobalModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_bgp_address_family_merged_idempotent(self):
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
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_bgp_address_family_merged(self):
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
                state="merged",
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
