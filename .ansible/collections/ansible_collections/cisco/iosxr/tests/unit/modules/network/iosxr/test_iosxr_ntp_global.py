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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_ntp_global
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrNtpGlobalModule(TestIosxrModule):
    module = iosxr_ntp_global

    def setUp(self):
        super(TestIosxrNtpGlobalModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.ntp_global.ntp_global."
            "Ntp_globalFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrNtpGlobalModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_ntp_global_merged_idempotent(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                ntp
                 max-associations 10
                 interface GigabitEthernet0/0/0/0 vrf siteB
                  multicast key 1
                 !
                 interface GigabitEthernet0/0/0/0
                  broadcast client
                  multicast client 224.0.0.8
                  multicast destination 224.0.0.8
                 !
                 authentication-key 1 md5 encrypted testkey
                 authentication-key 2 md5 encrypted 071B245F5A5B
                 authenticate
                 trusted-key 1
                 trusted-key 2
                 ipv4 dscp af11
                 ipv6 precedence routine
                 peer vrf siteC 192.0.2.1 iburst
                 server vrf siteD 192.0.2.2 burst
                 server 192.0.2.2 version 2 key 1 minpoll 4 maxpoll 5 prefer burst iburst source GigabitEthernet0/0/0/0
                 drift file apphost
                 drift aging time 0
                 master 1
                 access-group vrf siteA ipv4 peer PeerAcl2
                 access-group vrf siteA ipv4 serve ServeAcl2
                 access-group ipv4 peer PeerAcl1
                 access-group ipv4 serve ServeAcl1
                 access-group ipv4 serve-only ServeOnlyAcl1
                 access-group ipv4 query-only QueryOnlyAcl1
                 access-group ipv6 peer PeerAcl2
                 source vrf siteE GigabitEthernet0/0/0/0
                 source GigabitEthernet0/0/0/0
                 passive
                 broadcastdelay 1
                 update-calendar
                 log-internal-sync
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    access_group=dict(
                        ipv4=dict(
                            peer="PeerAcl1",
                            query_only="QueryOnlyAcl1",
                            serve="ServeAcl1",
                            serve_only="ServeOnlyAcl1",
                        ),
                        ipv6=dict(peer="PeerAcl2"),
                        vrfs=[
                            dict(
                                ipv4=dict(peer="PeerAcl2", serve="ServeAcl2"),
                                name="siteA",
                            ),
                        ],
                    ),
                    authenticate=True,
                    authentication_keys=[
                        dict(id=1, key="testkey", encryption=True),
                        dict(id=2, key="071B245F5A5B", encryption=True),
                    ],
                    broadcastdelay=1,
                    drift=dict(aging_time=0, file="apphost"),
                    interfaces=[
                        dict(
                            name="GigabitEthernet0/0/0/0",
                            multicast_client="224.0.0.8",
                            multicast_destination="224.0.0.8",
                            broadcast_client=True,
                        ),
                        dict(
                            name="GigabitEthernet0/0/0/0",
                            multicast_key=1,
                            vrf="siteB",
                        ),
                    ],
                    ipv4=dict(dscp="af11"),
                    ipv6=dict(precedence="routine"),
                    log_internal_sync=True,
                    master=dict(stratum=1),
                    max_associations=10,
                    passive=True,
                    peers=[dict(iburst=True, peer="192.0.2.1", vrf="siteC")],
                    servers=[
                        dict(burst=True, server="192.0.2.2", vrf="siteD"),
                        dict(
                            iburst=True,
                            burst=True,
                            server="192.0.2.2",
                            key_id=1,
                            maxpoll=5,
                            minpoll=4,
                            prefer=True,
                            source="GigabitEthernet0/0/0/0",
                            version=2,
                        ),
                    ],
                    source_interface="GigabitEthernet0/0/0/0",
                    source_vrfs=[
                        dict(name="GigabitEthernet0/0/0/0", vrf="siteE"),
                    ],
                    trusted_keys=[dict(key_id=1), dict(key_id=2)],
                    update_calendar=True,
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_ntp_global_merged(self):
        self.maxDiff = None
        set_module_args(
            dict(
                config=dict(
                    access_group=dict(
                        ipv4=dict(
                            peer="PeerAcl1",
                            query_only="QueryOnlyAcl1",
                            serve="ServeAcl1",
                            serve_only="ServeOnlyAcl1",
                        ),
                        ipv6=dict(peer="PeerAcl2"),
                        vrfs=[
                            dict(
                                ipv4=dict(peer="PeerAcl2", serve="ServeAcl2"),
                                name="siteA",
                            ),
                        ],
                    ),
                    authenticate=True,
                    authentication_keys=[
                        dict(id=1, key="testkey", encryption=True),
                        dict(id=2, key="071B245F5A5B", encryption=True),
                    ],
                    broadcastdelay=1,
                    drift=dict(aging_time=0, file="apphost"),
                    interfaces=[
                        dict(
                            name="GigabitEthernet0/0/0/0",
                            multicast_client="224.0.0.8",
                            multicast_destination="224.0.0.8",
                            broadcast_client=True,
                        ),
                        dict(
                            name="GigabitEthernet0/0/0/0",
                            multicast_key=1,
                            vrf="siteB",
                        ),
                    ],
                    ipv4=dict(dscp="af11"),
                    ipv6=dict(precedence="routine"),
                    log_internal_sync=True,
                    master=dict(stratum=1),
                    max_associations=10,
                    passive=True,
                    peers=[dict(iburst=True, peer="192.0.2.1", vrf="siteC")],
                    servers=[
                        dict(burst=True, server="192.0.2.2", vrf="siteD"),
                        dict(
                            iburst=True,
                            burst=True,
                            server="192.0.2.2",
                            key_id=1,
                            maxpoll=5,
                            minpoll=4,
                            prefer=True,
                            source="GigabitEthernet0/0/0/0",
                            version=2,
                        ),
                    ],
                    source_interface="GigabitEthernet0/0/0/0",
                    source_vrfs=[
                        dict(name="GigabitEthernet0/0/0/0", vrf="siteE"),
                    ],
                    trusted_keys=[dict(key_id=1), dict(key_id=2)],
                    update_calendar=True,
                ),
                state="merged",
            ),
        )
        commands = [
            "ntp authentication-key 1 md5 encrypted testkey",
            "ntp authentication-key 2 md5 encrypted 071B245F5A5B",
            "ntp peer vrf siteC 192.0.2.1 iburst",
            "ntp server vrf siteD 192.0.2.2 burst",
            "ntp server 192.0.2.2 burst iburst key 1 minpoll 4 maxpoll 5 prefer version 2 source GigabitEthernet0/0/0/0",
            "ntp trusted-key 1",
            "ntp trusted-key 2",
            "ntp interface GigabitEthernet0/0/0/0 broadcast client",
            "ntp interface GigabitEthernet0/0/0/0 multicast destination 224.0.0.8",
            "ntp interface GigabitEthernet0/0/0/0 multicast client 224.0.0.8",
            "ntp interface GigabitEthernet0/0/0/0 vrf siteB multicast key 1",
            "ntp vrf siteE source GigabitEthernet0/0/0/0",
            "ntp access-group vrf siteA ipv4 serve ServeAcl2",
            "ntp access-group vrf siteA ipv4 peer PeerAcl2",
            "ntp access-group ipv4 peer PeerAcl1",
            "ntp access-group ipv4 serve ServeAcl1",
            "ntp access-group ipv4 serve-only ServeOnlyAcl1",
            "ntp access-group ipv4 query-only QueryOnlyAcl1",
            "ntp access-group ipv6 peer PeerAcl2",
            "ntp authenticate",
            "ntp log-internal-sync",
            "ntp broadcastdelay 1",
            "ntp drift aging time 0",
            "ntp drift file apphost",
            "ntp ipv4 dscp af11",
            "ntp ipv6 precedence routine",
            "ntp max-associations 10",
            "ntp master 1",
            "ntp passive",
            "ntp update-calendar",
            "ntp source GigabitEthernet0/0/0/0",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ntp_global_deleted(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                ntp
                 max-associations 10
                 interface GigabitEthernet0/0/0/0 vrf siteB
                  multicast key 1
                 !
                 interface GigabitEthernet0/0/0/0
                  broadcast client
                  multicast client 224.0.0.8
                  multicast destination 224.0.0.8
                 !
                 authentication-key 1 md5 encrypted testkey
                 authentication-key 2 md5 encrypted 071B245F5A5B
                 authenticate
                 trusted-key 1
                 trusted-key 2
                 ipv4 dscp af11
                 ipv6 precedence routine
                 peer vrf siteC 192.0.2.1 iburst
                 server vrf siteD 192.0.2.2 burst
                 server 192.0.2.2 version 2 key 1 minpoll 4 maxpoll 5 prefer burst iburst source GigabitEthernet0/0/0/0
                 drift file apphost
                 drift aging time 0
                 master 1
                 access-group vrf siteA ipv4 peer PeerAcl3
                 access-group vrf siteA ipv4 serve ServeAcl2
                 access-group ipv4 peer PeerAcl1
                 access-group ipv4 serve ServeAcl1
                 access-group ipv4 serve-only ServeOnlyAcl1
                 access-group ipv4 query-only QueryOnlyAcl1
                 access-group ipv6 peer PeerAcl2
                 source vrf siteE GigabitEthernet0/0/0/0
                 source GigabitEthernet0/0/0/0
                 passive
                 broadcastdelay 1
                 update-calendar
                 log-internal-sync
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="deleted"))
        commands = [
            "no ntp authentication-key 1 md5 encrypted testkey",
            "no ntp authentication-key 2 md5 encrypted 071B245F5A5B",
            "no ntp peer vrf siteC 192.0.2.1 iburst",
            "no ntp server vrf siteD 192.0.2.2 burst",
            "no ntp server 192.0.2.2 burst iburst key 1 minpoll 4 maxpoll 5 prefer version 2 source GigabitEthernet0/0/0/0",
            "no ntp trusted-key 1",
            "no ntp trusted-key 2",
            "no ntp interface GigabitEthernet0/0/0/0 vrf siteB",
            "no ntp interface GigabitEthernet0/0/0/0",
            "no ntp vrf siteE source GigabitEthernet0/0/0/0",
            "no ntp access-group vrf siteA ipv4 serve ServeAcl2",
            "no ntp access-group vrf siteA ipv4 peer PeerAcl3",
            "no ntp access-group ipv4 peer PeerAcl1",
            "no ntp access-group ipv4 serve ServeAcl1",
            "no ntp access-group ipv4 serve-only ServeOnlyAcl1",
            "no ntp access-group ipv4 query-only QueryOnlyAcl1",
            "no ntp access-group ipv6 peer PeerAcl2",
            "no ntp authenticate",
            "no ntp log-internal-sync",
            "no ntp broadcastdelay 1",
            "no ntp drift aging time 0",
            "no ntp drift file apphost",
            "no ntp ipv4 dscp af11",
            "no ntp ipv6 precedence routine",
            "no ntp max-associations 10",
            "no ntp master 1",
            "no ntp passive",
            "no ntp update-calendar",
            "no ntp source GigabitEthernet0/0/0/0",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ntp_global_replaced(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                ntp
                 max-associations 10
                 interface GigabitEthernet0/0/0/0 vrf siteB
                  multicast key 1
                 !
                 interface GigabitEthernet0/0/0/0
                  broadcast client
                  multicast client 224.0.0.8
                  multicast destination 224.0.0.8
                 !
                 authentication-key 1 md5 encrypted testkey
                 authentication-key 2 md5 encrypted 071B245F5A5B
                 authenticate
                 trusted-key 1
                 trusted-key 2
                 ipv4 dscp af11
                 ipv6 precedence routine
                 peer vrf siteC 192.0.2.1 iburst
                 server vrf siteD 192.0.2.2 burst
                 server 192.0.2.2 version 2 key 1 minpoll 4 maxpoll 5 prefer burst iburst source GigabitEthernet0/0/0/0
                 drift file apphost
                 drift aging time 0
                 master 1
                 access-group vrf siteA ipv4 peer PeerAcl3
                 access-group vrf siteA ipv4 serve ServeAcl2
                 access-group ipv4 peer PeerAcl1
                 access-group ipv4 serve ServeAcl1
                 access-group ipv4 serve-only ServeOnlyAcl1
                 access-group ipv4 query-only QueryOnlyAcl1
                 access-group ipv6 peer PeerAcl2
                 source vrf siteE GigabitEthernet0/0/0/0
                 source GigabitEthernet0/0/0/0
                 passive
                 broadcastdelay 1
                 update-calendar
                 log-internal-sync
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    access_group=dict(
                        ipv4=dict(
                            peer="PeerAcl1",
                            query_only="QueryOnlyAcl2",
                            serve="ServeAcl1",
                            serve_only="ServeOnlyAcl1",
                        ),
                        ipv6=dict(peer="PeerAcl2"),
                        vrfs=[
                            dict(
                                ipv4=dict(peer="PeerAcl2", serve="ServeAcl2"),
                                name="siteA",
                            ),
                        ],
                    ),
                    authenticate=True,
                    authentication_keys=[
                        dict(id=1, key="testkey1", encryption=True),
                        dict(id=2, key="071B245F5A5B", encryption=True),
                    ],
                    broadcastdelay=1,
                    drift=dict(aging_time=0, file="apphost"),
                    interfaces=[
                        dict(
                            name="GigabitEthernet0/0/0/1",
                            multicast_client="224.0.0.8",
                            multicast_destination="224.0.0.8",
                            broadcast_client=True,
                        ),
                        dict(
                            name="GigabitEthernet0/0/0/0",
                            multicast_key=1,
                            vrf="siteB",
                        ),
                    ],
                    ipv4=dict(dscp="af12"),
                    ipv6=dict(precedence="routine"),
                    log_internal_sync=True,
                    master=dict(stratum=1),
                    max_associations=10,
                    passive=True,
                    peers=[dict(iburst=True, peer="192.0.2.1", vrf="siteC")],
                    servers=[
                        dict(burst=True, server="192.0.2.3", vrf="siteD"),
                        dict(
                            iburst=True,
                            burst=True,
                            server="192.0.2.2",
                            key_id=1,
                            maxpoll=5,
                            minpoll=4,
                            prefer=True,
                            source="GigabitEthernet0/0/0/1",
                            version=2,
                        ),
                    ],
                    source_interface="GigabitEthernet0/0/0/0",
                    source_vrfs=[
                        dict(name="GigabitEthernet0/0/0/0", vrf="siteE"),
                    ],
                    trusted_keys=[dict(key_id=1), dict(key_id=2)],
                    update_calendar=True,
                ),
                state="replaced",
            ),
        )
        commands = [
            "no ntp server vrf siteD 192.0.2.2 burst",
            "no ntp interface GigabitEthernet0/0/0/0",
            "ntp authentication-key 1 md5 encrypted testkey1",
            "ntp server vrf siteD 192.0.2.3 burst",
            "ntp server 192.0.2.2 burst iburst key 1 minpoll 4 maxpoll 5 prefer version 2 source GigabitEthernet0/0/0/1",
            "ntp interface GigabitEthernet0/0/0/1 broadcast client",
            "ntp interface GigabitEthernet0/0/0/1 multicast destination 224.0.0.8",
            "ntp interface GigabitEthernet0/0/0/1 multicast client 224.0.0.8",
            "ntp access-group ipv4 query-only QueryOnlyAcl2",
            "ntp access-group vrf siteA ipv4 peer PeerAcl2",
            "ntp access-group vrf siteA ipv4 serve ServeAcl2",
            "ntp ipv4 dscp af12",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_logging_global_rendered(self):
        self.maxDiff = None
        set_module_args(
            dict(
                config=dict(
                    access_group=dict(
                        ipv4=dict(
                            peer="PeerAcl1",
                            query_only="QueryOnlyAcl1",
                            serve="ServeAcl1",
                            serve_only="ServeOnlyAcl1",
                        ),
                        ipv6=dict(peer="PeerAcl2"),
                        vrfs=[
                            dict(
                                ipv4=dict(peer="PeerAcl2", serve="ServeAcl2"),
                                name="siteA",
                            ),
                        ],
                    ),
                    authenticate=True,
                    authentication_keys=[
                        dict(id=1, key="testkey", encryption=True),
                        dict(id=2, key="071B245F5A5B", encryption=True),
                    ],
                    broadcastdelay=1,
                    drift=dict(aging_time=0, file="apphost"),
                    interfaces=[
                        dict(
                            name="GigabitEthernet0/0/0/0",
                            multicast_client="224.0.0.8",
                            multicast_destination="224.0.0.8",
                            broadcast_client=True,
                        ),
                        dict(
                            name="GigabitEthernet0/0/0/0",
                            multicast_key=1,
                            vrf="siteB",
                        ),
                    ],
                    ipv4=dict(dscp="af11"),
                    ipv6=dict(precedence="routine"),
                    log_internal_sync=True,
                    master=dict(stratum=1),
                    max_associations=10,
                    passive=True,
                    peers=[dict(iburst=True, peer="192.0.2.1", vrf="siteC")],
                    servers=[
                        dict(burst=True, server="192.0.2.2", vrf="siteD"),
                        dict(
                            iburst=True,
                            burst=True,
                            server="192.0.2.2",
                            key_id=1,
                            maxpoll=5,
                            minpoll=4,
                            prefer=True,
                            source="GigabitEthernet0/0/0/0",
                            version=2,
                        ),
                    ],
                    source_interface="GigabitEthernet0/0/0/0",
                    source_vrfs=[
                        dict(name="GigabitEthernet0/0/0/0", vrf="siteE"),
                    ],
                    trusted_keys=[dict(key_id=1), dict(key_id=2)],
                    update_calendar=True,
                ),
                state="rendered",
            ),
        )
        commands = [
            "ntp authentication-key 1 md5 encrypted testkey",
            "ntp authentication-key 2 md5 encrypted 071B245F5A5B",
            "ntp peer vrf siteC 192.0.2.1 iburst",
            "ntp server vrf siteD 192.0.2.2 burst",
            "ntp server 192.0.2.2 burst iburst key 1 minpoll 4 maxpoll 5 prefer version 2 source GigabitEthernet0/0/0/0",
            "ntp trusted-key 1",
            "ntp trusted-key 2",
            "ntp interface GigabitEthernet0/0/0/0 broadcast client",
            "ntp interface GigabitEthernet0/0/0/0 multicast destination 224.0.0.8",
            "ntp interface GigabitEthernet0/0/0/0 multicast client 224.0.0.8",
            "ntp interface GigabitEthernet0/0/0/0 vrf siteB multicast key 1",
            "ntp vrf siteE source GigabitEthernet0/0/0/0",
            "ntp access-group vrf siteA ipv4 serve ServeAcl2",
            "ntp access-group vrf siteA ipv4 peer PeerAcl2",
            "ntp access-group ipv4 peer PeerAcl1",
            "ntp access-group ipv4 serve ServeAcl1",
            "ntp access-group ipv4 serve-only ServeOnlyAcl1",
            "ntp access-group ipv4 query-only QueryOnlyAcl1",
            "ntp access-group ipv6 peer PeerAcl2",
            "ntp authenticate",
            "ntp log-internal-sync",
            "ntp broadcastdelay 1",
            "ntp drift aging time 0",
            "ntp drift file apphost",
            "ntp ipv4 dscp af11",
            "ntp ipv6 precedence routine",
            "ntp max-associations 10",
            "ntp master 1",
            "ntp passive",
            "ntp update-calendar",
            "ntp source GigabitEthernet0/0/0/0",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_ntp_global_overridden(self):
        run_cfg = dedent(
            """\
                ntp
                 max-associations 10
                 interface GigabitEthernet0/0/0/0 vrf siteB
                  multicast key 1
                 !
                 interface GigabitEthernet0/0/0/0
                  broadcast client
                  multicast client 224.0.0.8
                  multicast destination 224.0.0.8
                 !
                 authentication-key 1 md5 encrypted testkey
                 authentication-key 2 md5 encrypted 071B245F5A5B
                 authenticate
                 trusted-key 1
                 trusted-key 2
                 ipv4 dscp af11
                 ipv6 precedence routine
                 peer vrf siteC 192.0.2.1 iburst
                 server vrf siteD 192.0.2.2 burst
                 server 192.0.2.2 version 2 key 1 minpoll 4 maxpoll 5 prefer burst iburst source GigabitEthernet0/0/0/0
                 drift file apphost
                 drift aging time 0
                 master 1
                 access-group vrf siteA ipv4 peer PeerAcl3
                 access-group vrf siteA ipv4 serve ServeAcl2
                 access-group ipv4 peer PeerAcl1
                 access-group ipv4 serve ServeAcl1
                 access-group ipv4 serve-only ServeOnlyAcl1
                 access-group ipv4 query-only QueryOnlyAcl1
                 access-group ipv6 peer PeerAcl2
                 source vrf siteE GigabitEthernet0/0/0/0
                 source GigabitEthernet0/0/0/0
                 passive
                 broadcastdelay 1
                 update-calendar
                 log-internal-sync
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    access_group=dict(
                        ipv4=dict(
                            peer="PeerAcl1",
                            query_only="QueryOnlyAcl2",
                            serve="ServeAcl1",
                            serve_only="ServeOnlyAcl1",
                        ),
                        ipv6=dict(peer="PeerAcl2"),
                        vrfs=[
                            dict(
                                ipv4=dict(peer="PeerAcl2", serve="ServeAcl2"),
                                name="siteA",
                            ),
                        ],
                    ),
                    authenticate=True,
                    authentication_keys=[
                        dict(id=1, key="testkey1", encryption=True),
                        dict(id=2, key="071B245F5A5B", encryption=True),
                    ],
                    broadcastdelay=1,
                    drift=dict(aging_time=0, file="apphost"),
                    interfaces=[
                        dict(
                            name="GigabitEthernet0/0/0/1",
                            multicast_client="224.0.0.8",
                            multicast_destination="224.0.0.8",
                            broadcast_client=True,
                        ),
                        dict(
                            name="GigabitEthernet0/0/0/0",
                            multicast_key=1,
                            vrf="siteB",
                        ),
                    ],
                    ipv4=dict(dscp="af12"),
                    ipv6=dict(precedence="routine"),
                    log_internal_sync=True,
                    master=dict(stratum=1),
                    max_associations=10,
                    passive=True,
                    peers=[dict(iburst=True, peer="192.0.2.1", vrf="siteC")],
                    servers=[
                        dict(burst=True, server="192.0.2.3", vrf="siteD"),
                        dict(
                            iburst=True,
                            burst=True,
                            server="192.0.2.2",
                            key_id=1,
                            maxpoll=5,
                            minpoll=4,
                            prefer=True,
                            source="GigabitEthernet0/0/0/1",
                            version=2,
                        ),
                    ],
                    source_interface="GigabitEthernet0/0/0/0",
                    source_vrfs=[
                        dict(name="GigabitEthernet0/0/0/0", vrf="siteE"),
                    ],
                    trusted_keys=[dict(key_id=1), dict(key_id=2)],
                    update_calendar=True,
                ),
                state="overridden",
            ),
        )
        commands = [
            "no ntp server vrf siteD 192.0.2.2 burst",
            "no ntp interface GigabitEthernet0/0/0/0",
            "ntp authentication-key 1 md5 encrypted testkey1",
            "ntp server vrf siteD 192.0.2.3 burst",
            "ntp server 192.0.2.2 burst iburst key 1 minpoll 4 maxpoll 5 prefer version 2 source GigabitEthernet0/0/0/1",
            "ntp interface GigabitEthernet0/0/0/1 broadcast client",
            "ntp interface GigabitEthernet0/0/0/1 multicast destination 224.0.0.8",
            "ntp interface GigabitEthernet0/0/0/1 multicast client 224.0.0.8",
            "ntp access-group ipv4 query-only QueryOnlyAcl2",
            "ntp access-group vrf siteA ipv4 peer PeerAcl2",
            "ntp access-group vrf siteA ipv4 serve ServeAcl2",
            "ntp ipv4 dscp af12",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_ntp_global_gathered(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                ntp
                 max-associations 10
                 interface GigabitEthernet0/0/0/0
                  broadcast client
                  multicast client 224.0.0.8
                  multicast destination 224.0.0.8
                 !
                 authentication-key 1 md5 encrypted testkey
                 authentication-key 2 md5 encrypted 071B245F5A5B
                 authenticate
                 trusted-key 1
                 trusted-key 2
                 ipv4 dscp af11
                 ipv6 precedence routine
                 peer vrf siteC 192.0.2.1 iburst
                 server 192.0.2.2 version 2 key 1 minpoll 4 maxpoll 5 prefer burst iburst source GigabitEthernet0/0/0/0
                 drift file apphost
                 drift aging time 0
                 master 1
                 access-group vrf siteA ipv4 peer PeerAcl3
                 access-group vrf siteA ipv4 serve ServeAcl2
                 access-group ipv4 peer PeerAcl1
                 access-group ipv4 serve ServeAcl1
                 access-group ipv4 serve-only ServeOnlyAcl1
                 access-group ipv4 query-only QueryOnlyAcl1
                 access-group ipv6 peer PeerAcl2
                 source vrf siteE GigabitEthernet0/0/0/0
                 source GigabitEthernet0/0/0/0
                 passive
                 broadcastdelay 1
                 update-calendar
                 log-internal-sync
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="gathered"))
        gathered = {
            "max_associations": 10,
            "interfaces": [
                {
                    "name": "GigabitEthernet0/0/0/0",
                    "broadcast_client": True,
                    "multicast_client": "224.0.0.8",
                    "multicast_destination": "224.0.0.8",
                },
            ],
            "authentication_keys": [
                {"id": 1, "key": "testkey", "encryption": True},
                {"id": 2, "key": "071B245F5A5B", "encryption": True},
            ],
            "authenticate": True,
            "trusted_keys": [{"key_id": 1}, {"key_id": 2}],
            "ipv4": {"dscp": "af11"},
            "ipv6": {"precedence": "routine"},
            "peers": [{"peer": "192.0.2.1", "vrf": "siteC", "iburst": True}],
            "servers": [
                {
                    "server": "192.0.2.2",
                    "burst": True,
                    "iburst": True,
                    "key_id": 1,
                    "minpoll": 4,
                    "maxpoll": 5,
                    "prefer": True,
                    "version": 2,
                    "source": "GigabitEthernet0/0/0/0",
                },
            ],
            "drift": {"file": "apphost", "aging_time": 0},
            "master": {"stratum": 1},
            "access_group": {
                "vrfs": [
                    {
                        "name": "siteA",
                        "ipv4": {"peer": "PeerAcl3", "serve": "ServeAcl2"},
                    },
                ],
                "ipv4": {
                    "peer": "PeerAcl1",
                    "serve": "ServeAcl1",
                    "serve_only": "ServeOnlyAcl1",
                    "query_only": "QueryOnlyAcl1",
                },
                "ipv6": {"peer": "PeerAcl2"},
            },
            "source_vrfs": [
                {"name": "GigabitEthernet0/0/0/0", "vrf": "siteE"},
            ],
            "source_interface": "GigabitEthernet0/0/0/0",
            "passive": True,
            "broadcastdelay": 1,
            "update_calendar": True,
            "log_internal_sync": True,
        }
        result = self.execute_module(changed=False)
        self.assertEqual(gathered, result["gathered"])

    def test_iosxr_ntp_global_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="ntp\n max-associations 10\n interface GigabitEthernet0/0/0/0\n  broadcast client\n"
                "  multicast client 224.0.0.8\n  multicast destination 224.0.0.8\n !\n "
                "authentication-key 1 md5 encrypted testkey\n authentication-key 2 md5 "
                "encrypted 071B245F5A5B\n authenticate\n trusted-key 1\n trusted-key 2\n ipv4 dscp "
                "af11\n ipv6 precedence routine\n peer vrf siteC 192.0.2.1 iburst\n"
                " server 192.0.2.2 version 2 key 1 minpoll 4 maxpoll 5 prefer "
                "burst iburst source GigabitEthernet0/0/0/0\n drift file apphost\n drift aging time 0\n"
                " master 1\n access-group vrf siteA ipv4 peer PeerAcl3\n access-group vrf siteA "
                "ipv4 serve  ServeAcl2\n access-group ipv4 peer PeerAcl1\n access-group ipv4 serve "
                "ServeAcl1\n access-group ipv4 serve-only ServeOnlyAcl1\n access-group ipv4 "
                "query-only QueryOnlyAcl1\n access-group ipv6 peer PeerAcl2\n source vrf siteE "
                "GigabitEthernet0/0/0/0\n source GigabitEthernet0/0/0/0\n"
                " passive\n broadcastdelay "
                "1\n update-calendar\n log-internal-sync\n!",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "max_associations": 10,
            "interfaces": [
                {
                    "name": "GigabitEthernet0/0/0/0",
                    "broadcast_client": True,
                    "multicast_client": "224.0.0.8",
                    "multicast_destination": "224.0.0.8",
                },
            ],
            "authentication_keys": [
                {"id": 1, "key": "testkey", "encryption": True},
                {"id": 2, "key": "071B245F5A5B", "encryption": True},
            ],
            "authenticate": True,
            "trusted_keys": [{"key_id": 1}, {"key_id": 2}],
            "ipv4": {"dscp": "af11"},
            "ipv6": {"precedence": "routine"},
            "peers": [{"peer": "192.0.2.1", "vrf": "siteC", "iburst": True}],
            "servers": [
                {
                    "server": "192.0.2.2",
                    "burst": True,
                    "iburst": True,
                    "key_id": 1,
                    "minpoll": 4,
                    "maxpoll": 5,
                    "prefer": True,
                    "version": 2,
                    "source": "GigabitEthernet0/0/0/0",
                },
            ],
            "drift": {"file": "apphost", "aging_time": 0},
            "master": {"stratum": 1},
            "access_group": {
                "vrfs": [{"name": "siteA", "ipv4": {"peer": "PeerAcl3"}}],
                "ipv4": {
                    "peer": "PeerAcl1",
                    "serve": "ServeAcl1",
                    "serve_only": "ServeOnlyAcl1",
                    "query_only": "QueryOnlyAcl1",
                },
                "ipv6": {"peer": "PeerAcl2"},
            },
            "source_vrfs": [
                {"name": "GigabitEthernet0/0/0/0", "vrf": "siteE"},
            ],
            "source_interface": "GigabitEthernet0/0/0/0",
            "passive": True,
            "broadcastdelay": 1,
            "update_calendar": True,
            "log_internal_sync": True,
        }
        self.assertEqual(parsed_list, result["parsed"])
