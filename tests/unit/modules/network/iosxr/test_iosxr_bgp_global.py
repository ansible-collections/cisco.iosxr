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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_bgp_global
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrBgpGlobalModule(TestIosxrModule):
    module = iosxr_bgp_global

    def setUp(self):
        super(TestIosxrBgpGlobalModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.bgp_global.bgp_global."
            "Bgp_globalFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrBgpGlobalModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_bgp_global_merged_idempotent(self):
        run_cfg = dedent(
            """\
            router bgp 65536
              bgp confederation identifier 4
              bgp router-id 192.0.2.10
              bgp cluster-id 5
              default-metric 4
              socket send-buffer-size 4098
              bgp bestpath med confed
              socket receive-buffer-size 514
              neighbor 192.0.2.11
                remote-as 65537
                cluster-id 3
              neighbor 192.0.2.14
                remote-as 65538
                bfd fast-detect strict-mode
                bfd multiplier 6
                bfd minimum-interval 20
              vrf vrf1
                default-metric 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    default_metric=4,
                    socket=dict(
                        receive_buffer_size=514,
                        send_buffer_size=4098,
                    ),
                    bgp=dict(
                        confederation=dict(identifier=4),
                        bestpath=dict(med=dict(confed=True)),
                        cluster_id=5,
                        router_id="192.0.2.10",
                    ),
                    neighbors=[
                        dict(
                            neighbor="192.0.2.11",
                            cluster_id=3,
                            remote_as="65537",
                        ),
                        dict(
                            neighbor="192.0.2.14",
                            remote_as="65538",
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(strict_mode=True),
                            ),
                        ),
                    ],
                    vrfs=[dict(vrf="vrf1", default_metric=5)],
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_bgp_global_merged(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    default_metric=4,
                    socket=dict(
                        receive_buffer_size=514,
                        send_buffer_size=4098,
                    ),
                    bgp=dict(
                        confederation=dict(identifier=4),
                        bestpath=dict(med=dict(confed=True)),
                        cluster_id=5,
                        router_id="192.0.2.10",
                    ),
                    neighbors=[
                        dict(
                            neighbor="192.0.2.11",
                            cluster_id=3,
                            remote_as="65537",
                        ),
                        dict(
                            neighbor="192.0.2.14",
                            remote_as="65538",
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(strict_mode=True),
                            ),
                        ),
                    ],
                    vrfs=[dict(vrf="vrf1", default_metric=5)],
                ),
                state="merged",
            ),
        )
        commands = [
            "router bgp 65536",
            "bgp cluster-id 5",
            "bgp router-id 192.0.2.10",
            "bgp bestpath med confed",
            "bgp confederation identifier 4",
            "default-metric 4",
            "socket receive-buffer-size 514",
            "socket send-buffer-size 4098",
            "neighbor 192.0.2.11",
            "cluster-id 3",
            "remote-as 65537",
            "neighbor 192.0.2.14",
            "bfd fast-detect strict-mode",
            "bfd minimum-interval 20",
            "bfd multiplier 6",
            "remote-as 65538",
            "vrf vrf1",
            "default-metric 5",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_global_merged_remote_as_input_types(self):
        """remote_as may be int, str, or float in the module dict; CLI uses remote-as text (AAP-73646)."""
        base = dict(
            as_number="65536",
            default_metric=4,
            socket=dict(
                receive_buffer_size=514,
                send_buffer_size=4098,
            ),
            bgp=dict(
                confederation=dict(identifier=4),
                bestpath=dict(med=dict(confed=True)),
                cluster_id=5,
                router_id="192.0.2.10",
            ),
        )
        cases = [
            ([dict(neighbor="10.1.1.1", remote_as=65537)], "remote-as 65537"),
            ([dict(neighbor="10.1.1.2", remote_as="5467.8")], "remote-as 5467.8"),
            ([dict(neighbor="10.1.1.3", remote_as=5467.8)], "remote-as 5467.8"),
        ]
        for neighbors, needle in cases:
            set_module_args(dict(config=dict(**base, neighbors=neighbors), state="merged"))
            result = self.execute_module(changed=True)
            joined = " ".join(result["commands"])
            self.assertIn(needle, joined)

    def test_iosxr_bgp_global_merged_remote_as_vrf_input_types(self):
        """VRF neighbor remote_as accepts int, str, or float in module params (AAP-73646)."""
        base = dict(
            as_number="65536",
            bgp=dict(
                cluster_id=5,
                router_id="192.0.2.10",
            ),
            vrfs=[
                dict(
                    vrf="vrf_t",
                    neighbors=[
                        dict(neighbor="10.20.20.1", remote_as=65501),
                        dict(neighbor="10.20.20.2", remote_as="4394.9"),
                        dict(neighbor="10.20.20.3", remote_as=2.5),
                    ],
                ),
            ],
        )
        cases = ["remote-as 65501", "remote-as 4394.9", "remote-as 2.5"]
        set_module_args(dict(config=base, state="merged"))
        result = self.execute_module(changed=True)
        joined = "\n".join(result["commands"])
        for needle in cases:
            self.assertIn(needle, joined)

    def test_iosxr_bgp_global_merged_matches_integration_fixture_commands(self):
        """Keep integration merged.commands in sync with ResourceModule output."""
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    default_metric=4,
                    socket=dict(
                        receive_buffer_size=514,
                        send_buffer_size=4098,
                    ),
                    bgp=dict(
                        confederation=dict(identifier=4),
                        bestpath=dict(med=dict(confed=True)),
                        cluster_id=5,
                        router_id="192.0.2.10",
                    ),
                    neighbors=[
                        dict(
                            neighbor="192.0.2.11",
                            cluster_id=3,
                            remote_as="65537",
                        ),
                        dict(
                            neighbor="192.0.2.14",
                            remote_as="65538",
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(strict_mode=True),
                            ),
                        ),
                        dict(neighbor="203.0.113.10", remote_as="5467.8"),
                        dict(neighbor="203.0.113.11", remote_as=65001),
                        dict(neighbor="203.0.113.12", remote_as=4394.6),
                    ],
                    vrfs=[
                        dict(
                            vrf="vrf_asdot",
                            neighbors=[
                                dict(neighbor="198.51.100.100", remote_as=65540),
                                dict(neighbor="198.51.100.101", remote_as=2.5),
                                dict(neighbor="198.51.100.99", remote_as="1.0"),
                            ],
                        ),
                    ],
                ),
                state="merged",
            ),
        )
        result = self.execute_module(changed=True)
        expected = [
            "router bgp 65536",
            "bgp cluster-id 5",
            "bgp router-id 192.0.2.10",
            "bgp bestpath med confed",
            "bgp confederation identifier 4",
            "default-metric 4",
            "socket receive-buffer-size 514",
            "socket send-buffer-size 4098",
            "neighbor 192.0.2.11",
            "cluster-id 3",
            "remote-as 65537",
            "neighbor 192.0.2.14",
            "bfd fast-detect strict-mode",
            "bfd minimum-interval 20",
            "bfd multiplier 6",
            "remote-as 65538",
            "neighbor 203.0.113.10",
            "remote-as 5467.8",
            "neighbor 203.0.113.11",
            "remote-as 65001",
            "neighbor 203.0.113.12",
            "remote-as 4394.6",
            "vrf vrf_asdot",
            "neighbor 198.51.100.100",
            "remote-as 65540",
            "neighbor 198.51.100.101",
            "remote-as 2.5",
            "neighbor 198.51.100.99",
            "remote-as 1.0",
        ]
        self.assertEqual(sorted(result["commands"]), sorted(expected))

    def test_iosxr_bgp_global_replaced(self):
        run_cfg = dedent(
            """\
            router bgp 65536
              bgp confederation identifier 4
              bgp router-id 192.0.2.10
              bgp cluster-id 5
              default-metric 4
              socket send-buffer-size 4098
              bgp bestpath med confed
              socket receive-buffer-size 514
              neighbor 192.0.2.11
                remote-as 65537
                cluster-id 3
              neighbor 192.0.2.14
                remote-as 65538
                bfd fast-detect strict-mode
                bfd multiplier 6
                bfd minimum-interval 20
              vrf vrf1
                default-metric 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    default_metric=5,
                    socket=dict(
                        receive_buffer_size=514,
                        send_buffer_size=4098,
                    ),
                    bgp=dict(
                        confederation=dict(identifier=4),
                        bestpath=dict(med=dict(confed=True)),
                        cluster_id=5,
                        router_id="192.0.2.10",
                    ),
                    neighbors=[
                        dict(
                            neighbor="192.0.2.13",
                            remote_as="65538",
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(strict_mode=True),
                            ),
                            use=dict(
                                neighbor_group="test_ng",
                                session_group="test_sg",
                            ),
                            password=dict(
                                inheritance_disable="true",
                            ),
                            local_as=dict(
                                value="65539",
                                no_prepend=dict(
                                    set="true",
                                ),
                            ),
                        ),
                    ],
                    vrfs=[dict(vrf="vrf1", default_metric=5)],
                ),
                state="replaced",
            ),
        )
        commands = [
            "router bgp 65536",
            "no neighbor 192.0.2.11",
            "no neighbor 192.0.2.14",
            "default-metric 5",
            "neighbor 192.0.2.13",
            "bfd fast-detect strict-mode",
            "bfd minimum-interval 20",
            "bfd multiplier 6",
            "use session-group test_sg",
            "use neighbor-group test_ng",
            "local-as 65539 no-prepend",
            "password inheritance-disable",
            "remote-as 65538",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_global_replaced_idempotent(self):
        run_cfg = dedent(
            """\
            router bgp 65536
              bgp confederation identifier 4
              bgp router-id 192.0.2.10
              bgp cluster-id 5
              default-metric 4
              socket send-buffer-size 4098
              bgp bestpath med confed
              socket receive-buffer-size 514
              neighbor 192.0.2.11
                remote-as 65537
                cluster-id 3
              neighbor 192.0.2.14
                remote-as 65538
                bfd fast-detect strict-mode
                bfd multiplier 6
                bfd minimum-interval 20
                use session-group test_sg
                use neighbor-group test_ng
              vrf vrf1
                default-metric 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    default_metric=4,
                    socket=dict(
                        receive_buffer_size=514,
                        send_buffer_size=4098,
                    ),
                    bgp=dict(
                        confederation=dict(identifier=4),
                        bestpath=dict(med=dict(confed=True)),
                        cluster_id=5,
                        router_id="192.0.2.10",
                    ),
                    neighbors=[
                        dict(
                            neighbor="192.0.2.11",
                            cluster_id=3,
                            remote_as="65537",
                        ),
                        dict(
                            neighbor="192.0.2.14",
                            remote_as="65538",
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(strict_mode=True),
                            ),
                            use=dict(
                                neighbor_group="test_ng",
                                session_group="test_sg",
                            ),
                        ),
                    ],
                    vrfs=[dict(vrf="vrf1", default_metric=5)],
                ),
                state="replaced",
            ),
        )

        self.execute_module(changed=False, commands=[])

    def test_iosxr_bgp_global_deleted(self):
        run_cfg = dedent(
            """\
            router bgp 65536
              bgp confederation identifier 4
              bgp router-id 192.0.2.10
              bgp cluster-id 5
              default-metric 4
              socket send-buffer-size 4098
              bgp bestpath med confed
              socket receive-buffer-size 514
              neighbor 192.0.2.11
                remote-as 65537
                cluster-id 3
              neighbor 192.0.2.14
                remote-as 65538
                bfd fast-detect strict-mode
                bfd multiplier 6
                bfd minimum-interval 20
              vrf vrf1
                default-metric 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(as_number="65536"), state="deleted"))

        commands = [
            "router bgp 65536",
            "no bgp cluster-id 5",
            "no bgp router-id 192.0.2.10",
            "no bgp bestpath med confed",
            "no bgp confederation identifier 4",
            "no default-metric 4",
            "no socket receive-buffer-size 514",
            "no socket send-buffer-size 4098",
            "no neighbor 192.0.2.11",
            "no neighbor 192.0.2.14",
            "no vrf vrf1",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_global_deleted_idempotent(self):
        run_cfg = dedent(
            """\
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(config=dict(as_number="65536"), state="deleted"))

        result = self.execute_module(changed=False)
        self.assertEqual(result["commands"], [])

    def test_iosxr_bgp_global_rendered(self):
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    default_metric=4,
                    socket=dict(
                        receive_buffer_size=514,
                        send_buffer_size=4098,
                    ),
                    bgp=dict(
                        confederation=dict(identifier=4),
                        bestpath=dict(med=dict(confed=True)),
                        cluster_id=5,
                        router_id="192.0.2.10",
                    ),
                    neighbors=[
                        dict(
                            neighbor="192.0.2.11",
                            cluster_id=3,
                            remote_as="65537",
                        ),
                        dict(
                            neighbor="192.0.2.14",
                            remote_as="65538",
                            use=dict(
                                neighbor_group="test_nb",
                                session_group="test_sg",
                            ),
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(set=True),
                            ),
                        ),
                    ],
                    vrfs=[dict(vrf="vrf1", default_metric=5)],
                ),
                state="rendered",
            ),
        )

        commands = [
            "router bgp 65536",
            "bgp cluster-id 5",
            "bgp router-id 192.0.2.10",
            "bgp bestpath med confed",
            "bgp confederation identifier 4",
            "default-metric 4",
            "socket receive-buffer-size 514",
            "socket send-buffer-size 4098",
            "neighbor 192.0.2.11",
            "cluster-id 3",
            "remote-as 65537",
            "neighbor 192.0.2.14",
            "bfd fast-detect",
            "bfd minimum-interval 20",
            "bfd multiplier 6",
            "use neighbor-group test_nb",
            "use session-group test_sg",
            "remote-as 65538",
            "vrf vrf1",
            "default-metric 5",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_bgp_global_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="router bgp 65536\n bgp confederation identifier 4\n "
                "bgp router-id 192.0.2.10\n bgp cluster-id 5\n default-metric 4\n "
                "socket send-buffer-size 4098\n bgp bestpath med confed\n "
                "socket receive-buffer-size 514\n neighbor 192.0.2.11\n  "
                "local-as 4 no-prepend replace-as\n  "
                "password encrypted 15060E1F107B\n  remote-as 65537\n  "
                "cluster-id 3\n !\n neighbor 192.0.2.14\n  remote-as 65538\n  description test nbr description\n"
                " bfd fast-detect strict-mode\n "
                " bfd multiplier 6\n  bfd minimum-interval 20\n !\n!",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "as_number": "65536",
            "bgp": {
                "confederation": {"identifier": 4},
                "cluster_id": "5",
                "router_id": "192.0.2.10",
                "bestpath": {"med": {"confed": True}},
            },
            "default_metric": 4,
            "socket": {"send_buffer_size": 4098, "receive_buffer_size": 514},
            "neighbors": [
                {
                    "neighbor_address": "192.0.2.11",
                    "remote_as": "65537",
                    "cluster_id": "3",
                    "password": {"encrypted": "15060E1F107B"},
                    "local_as": {
                        "no_prepend": {"replace_as": {"set": True}},
                        "value": 4,
                    },
                },
                {
                    "neighbor_address": "192.0.2.14",
                    "remote_as": "65538",
                    "description": "test nbr description",
                },
            ],
            "bfd": {"multiplier": 6, "minimum_interval": 20},
        }

        self.assertEqual(parsed_list, result["parsed"])

    def test_iosxr_bgp_global_parsed_remote_as_asdot(self):
        """ASDOT/ASPLAIN remote-as must parse as strings for global and VRF neighbors (AAP-73646)."""
        self.maxDiff = None
        set_module_args(
            dict(
                running_config=(
                    "router bgp 65138\n bgp router-id 192.0.2.1\n neighbor 10.1.1.1\n"
                    "  remote-as 5467.8\n neighbor 10.1.1.2\n  remote-as 1.0\n"
                    " neighbor 10.1.1.3\n  remote-as 65535.65535\n"
                    " neighbor 10.5.5.5\n  remote-as 65001\n"
                    " vrf vrf1\n  neighbor 10.8.8.8\n   remote-as 65002\n"
                    "  neighbor 10.9.9.9\n   remote-as 4394.5\n !\n!"
                ),
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        expected = {
            "as_number": "65138",
            "bgp": {"router_id": "192.0.2.1"},
            "neighbors": [
                {"neighbor_address": "10.1.1.1", "remote_as": "5467.8"},
                {"neighbor_address": "10.1.1.2", "remote_as": "1.0"},
                {"neighbor_address": "10.1.1.3", "remote_as": "65535.65535"},
                {"neighbor_address": "10.5.5.5", "remote_as": "65001"},
            ],
            "vrfs": [
                {
                    "vrf": "vrf1",
                    "neighbors": [
                        {"neighbor_address": "10.8.8.8", "remote_as": "65002"},
                        {"neighbor_address": "10.9.9.9", "remote_as": "4394.5"},
                    ],
                },
            ],
        }
        self.assertEqual(expected, result["parsed"])

    def test_iosxr_bgp_global_purged(self):
        run_cfg = dedent(
            """\
            router bgp 65536
              bgp confederation identifier 4
              bgp router-id 192.0.2.10
              bgp cluster-id 5
              default-metric 4
              socket send-buffer-size 4098
              bgp bestpath med confed
              socket receive-buffer-size 514
              neighbor 192.0.2.11
                remote-as 65537
                cluster-id 3
              neighbor 192.0.2.14
                remote-as 65538
                bfd fast-detect strict-mode
                bfd multiplier 6
                bfd minimum-interval 20
              vrf vrf1
                default-metric 5
            """,
        )

        self.get_config.return_value = run_cfg

        set_module_args(dict(state="purged"))
        commands = ["no router bgp 65536"]

        result = self.execute_module(changed=True)
        self.assertEqual(set(result["commands"]), set(commands))

    def test_iosxr_bgp_global_ovrridden(self):
        run_cfg = dedent(
            """\
            router bgp 65536
              bgp confederation identifier 4
              bgp router-id 192.0.2.10
              bgp cluster-id 5
              default-metric 4
              socket send-buffer-size 4098
              bgp bestpath med confed
              socket receive-buffer-size 514
              neighbor 192.0.2.11
                remote-as 65537
                cluster-id 3
              neighbor 192.0.2.14
                remote-as 65538
                bfd fast-detect strict-mode
                bfd multiplier 6
                bfd minimum-interval 20
              vrf vrf1
                default-metric 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    default_metric=5,
                    socket=dict(
                        receive_buffer_size=514,
                        send_buffer_size=4098,
                    ),
                    bgp=dict(
                        confederation=dict(identifier=4),
                        bestpath=dict(med=dict(confed=True)),
                        cluster_id=5,
                        router_id="192.0.2.10",
                    ),
                    neighbors=[
                        dict(
                            neighbor="192.0.2.13",
                            remote_as="65538",
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(strict_mode=True),
                            ),
                            use=dict(
                                neighbor_group="test_ng",
                                session_group="test_sg",
                            ),
                            password=dict(
                                inheritance_disable="true",
                            ),
                            local_as=dict(
                                value="65539",
                                no_prepend=dict(
                                    set="true",
                                ),
                            ),
                        ),
                    ],
                    vrfs=[dict(vrf="vrf1", default_metric=5)],
                ),
                state="overridden",
            ),
        )
        commands = [
            "router bgp 65536",
            "no neighbor 192.0.2.11",
            "no neighbor 192.0.2.14",
            "default-metric 5",
            "neighbor 192.0.2.13",
            "bfd fast-detect strict-mode",
            "bfd minimum-interval 20",
            "bfd multiplier 6",
            "use session-group test_sg",
            "use neighbor-group test_ng",
            "local-as 65539 no-prepend",
            "password inheritance-disable",
            "remote-as 65538",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_bgp_global_overridden_idempotent(self):
        run_cfg = dedent(
            """\
            router bgp 65536
              bgp confederation identifier 4
              bgp router-id 192.0.2.10
              bgp cluster-id 5
              default-metric 4
              socket send-buffer-size 4098
              bgp bestpath med confed
              socket receive-buffer-size 514
              neighbor 192.0.2.11
                remote-as 65537
                cluster-id 3
              neighbor 192.0.2.14
                remote-as 65538
                bfd fast-detect strict-mode
                bfd multiplier 6
                bfd minimum-interval 20
                use session-group test_sg
                use neighbor-group test_ng
              vrf vrf1
                default-metric 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    as_number="65536",
                    default_metric=4,
                    socket=dict(
                        receive_buffer_size=514,
                        send_buffer_size=4098,
                    ),
                    bgp=dict(
                        confederation=dict(identifier=4),
                        bestpath=dict(med=dict(confed=True)),
                        cluster_id=5,
                        router_id="192.0.2.10",
                    ),
                    neighbors=[
                        dict(
                            neighbor="192.0.2.11",
                            cluster_id=3,
                            remote_as="65537",
                        ),
                        dict(
                            neighbor="192.0.2.14",
                            remote_as="65538",
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(strict_mode=True),
                            ),
                            use=dict(
                                neighbor_group="test_ng",
                                session_group="test_sg",
                            ),
                        ),
                    ],
                    vrfs=[dict(vrf="vrf1", default_metric=5)],
                ),
                state="overridden",
            ),
        )

        self.execute_module(changed=False, commands=[])
