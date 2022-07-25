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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_bgp_global
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
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
                            bfd=dict(
                                multiplier=6,
                                minimum_interval=20,
                                fast_detect=dict(strict_mode=True),
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
            "bfd fast-detect strict-mode",
            "bfd minimum-interval 20",
            "bfd multiplier 6",
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
                "socket receive-buffer-size 514\n neighbor 192.0.2.11\n  remote-as 65537\n  "
                "cluster-id 3\n !\n neighbor 192.0.2.14\n  remote-as 65538\n "
                " bfd fast-detect strict-mode\n "
                " bfd multiplier 6\n  bfd minimum-interval 20\n !\n!",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "as_number": "65536",
            "bgp": {
                "bestpath": {"med": {"confed": True}},
                "cluster_id": "5",
                "confederation": {"identifier": 4},
                "router_id": "192.0.2.10",
            },
            "default_metric": 4,
            "neighbors": [
                {
                    "cluster_id": "3",
                    "neighbor_address": "192.0.2.11",
                    "remote_as": 65537,
                },
                {
                    "bfd": {
                        "fast_detect": {"strict_mode": True},
                        "minimum_interval": 20,
                        "multiplier": 6,
                    },
                    "neighbor_address": "192.0.2.14",
                    "remote_as": 65538,
                },
            ],
            "socket": {"receive_buffer_size": 514, "send_buffer_size": 4098},
        }

        self.assertEqual(parsed_list, result["parsed"])

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
