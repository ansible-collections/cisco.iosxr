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

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_snmp_server
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrSnmpServerModule(TestIosxrModule):
    module = iosxr_snmp_server

    def setUp(self):
        super(TestIosxrSnmpServerModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.snmp_server.snmp_server."
            "Snmp_serverFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrSnmpServerModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_snmp_server_merged_idempotent(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                snmp-server vrf vrf1
                 host 1.1.1.1 traps test1
                !
                snmp-server drop report acl IPv4 test1
                snmp-server drop unknown-user
                snmp-server ipv4 dscp af11
                snmp-server ipv6 precedence routine
                snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2 v4acl
                snmp-server community test2 RW SystemOwner IPv4 test IPv6 test1
                snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1
                snmp-server queue-length 2
                snmp-server trap-timeout 3
                snmp-server trap throttle-time 12
                snmp-server traps rf
                snmp-server traps bfd
                snmp-server traps bgp cbgp2
                snmp-server traps pim neighbor-change
                snmp-server traps pim invalid-message-received
                snmp-server traps pim rp-mapping-change
                snmp-server traps pim interface-state-change
                snmp-server traps copy-complete
                snmp-server traps hsrp
                snmp-server traps ipsla
                snmp-server traps msdp peer-state-change
                snmp-server traps snmp linkup
                snmp-server traps snmp linkdown
                snmp-server traps snmp coldstart
                snmp-server traps snmp warmstart
                snmp-server traps snmp authentication
                snmp-server traps vrrp events
                snmp-server traps flash removal
                snmp-server traps flash insertion
                snmp-server traps ipsec tunnel stop
                snmp-server traps ipsec tunnel start
                snmp-server traps power
                snmp-server traps config
                snmp-server traps entity
                snmp-server traps sensor
                snmp-server traps selective-vrf-download role-change
                snmp-server traps syslog
                snmp-server traps system
                snmp-server traps ospf lsa lsa-maxage
                snmp-server traps ospf lsa lsa-originate
                snmp-server traps ospf errors bad-packet
                snmp-server traps ospf errors authentication-failure
                snmp-server traps ospf errors config-error
                snmp-server traps ospf errors virt-bad-packet
                snmp-server traps ospf errors virt-authentication-failure
                snmp-server traps ospf errors virt-config-error
                snmp-server traps ospf retransmit packets
                snmp-server traps ospf retransmit virt-packets
                snmp-server traps ospf state-change if-state-change
                snmp-server traps ospf state-change neighbor-state-change
                snmp-server traps ospf state-change virtif-state-change
                snmp-server traps ospf state-change virtneighbor-state-change
                snmp-server traps rsvp all
                snmp-server traps rsvp new-flow
                snmp-server traps rsvp lost-flow
                snmp-server traps l2tun sessions
                snmp-server traps l2tun tunnel-up
                snmp-server traps l2tun tunnel-down
                snmp-server traps vpls all
                snmp-server traps vpls status
                snmp-server traps vpls full-clear
                snmp-server traps vpls full-raise
                snmp-server traps bulkstat collection
                snmp-server traps diameter peerup
                snmp-server traps diameter peerdown
                snmp-server traps diameter protocolerror
                snmp-server traps diameter permanentfail
                snmp-server traps diameter transientfail
                snmp-server traps l2vpn all
                snmp-server traps l2vpn vc-up
                snmp-server traps l2vpn vc-down
                snmp-server traps bridgemib
                snmp-server traps ospfv3 errors bad-packet
                snmp-server traps ospfv3 errors config-error
                snmp-server traps ospfv3 errors virt-config-error
                snmp-server traps ospfv3 state-change neighbor-state-change
                snmp-server traps ospfv3 state-change virtif-state-change
                snmp-server traps ospfv3 state-change virtneighbor-state-change
                snmp-server traps ospfv3 state-change restart-status-change
                snmp-server traps ospfv3 state-change restart-helper-status-change
                snmp-server traps ospfv3 state-change restart-virtual-helper-status-change
                snmp-server traps subscriber session-agg node
                snmp-server traps subscriber session-agg access-interface
                snmp-server traps addrpool low
                snmp-server traps addrpool high
                snmp-server traps cisco-entity-ext
                snmp-server traps entity-state operstatus
                snmp-server traps entity-state switchover
                snmp-server traps entity-redundancy all
                snmp-server traps entity-redundancy status
                snmp-server traps entity-redundancy switchover
                snmp-server chassis-id test2
                snmp-server contact t1
                snmp-server location test1
                snmp-server target list test host 1.1.1.2
                snmp-server target list test2 vrf vrf2
                snmp-server context c1
                snmp-server context c2
                snmp-server logging threshold oid-processing 1
                snmp-server logging threshold pdu-processing 1
                snmp-server mib bulkstat max-procmem-size 101
                snmp-server mib bulkstat object-list test1
                !
                snmp-server mib bulkstat schema mib1
                 object-list test1
                 poll-interval 1
                !
                snmp-server mib bulkstat transfer-id test2
                 retry 1
                 buffer-size 1024
                 enable
                 format schemaASCII
                 retain 1
                 schema test2
                !
                snmp-server timeouts duplicate 0
                snmp-server timeouts inQdrop 0
                snmp-server timeouts subagent 1
                snmp-server timeouts pdu stats 1
                snmp-server timeouts threshold 0
                snmp-server packetsize 490
                snmp-server correlator rule rule1
                 timeout 5
                !
                snmp-server correlator ruleset rule1
                !
                snmp-server correlator buffer-size 1024
                snmp-server trap-source GigabitEthernet0/0/0/2
                snmp-server throttle-time 60
                snmp-server community-map cm1 context c1 security-name s1 target-list t1
                snmp-server inform retries 7
                snmp-server overload-control 4 6
                snmp-server ifmib internal cache max-duration 4
                snmp-server mroutemib send-all-vrf
                snmp-server notification-log-mib size 5
                snmp-server notification-log-mib GlobalSize 5
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            hosts=[
                                dict(
                                    community="test1",
                                    host="1.1.1.1",
                                    traps=True,
                                ),
                            ],
                        ),
                    ],
                    users=[
                        dict(
                            Ipv4_acl="test1",
                            Ipv6_acl="test2",
                            group="test2",
                            user="u1",
                            v4_acl="v4acl",
                        ),
                    ],
                    timeouts=dict(
                        duplicate=0,
                        inQdrop=0,
                        pdu_stats=1,
                        subagent=1,
                        threshold=0,
                    ),
                    trap=dict(throttle_time=12),
                    targets=[
                        dict(name="test2", vrf="vrf2"),
                        dict(host="1.1.1.2", name="test"),
                    ],
                    ifmib=dict(internal_cache_max_duration=4),
                    inform=dict(retries=7),
                    chassis_id="test2",
                    packetsize=490,
                    queue_length=2,
                    throttle_time=60,
                    trap_source="GigabitEthernet0/0/0/2",
                    trap_timeout=3,
                    context=["c1", "c2"],
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[dict(name="rule1")],
                        rules=[dict(rule_name="rule1", timeout=5)],
                    ),
                    communities=[
                        dict(
                            name="test2",
                            rw=True,
                            systemowner=True,
                            acl_v4="test",
                            acl_v6="test1",
                        ),
                    ],
                    community_maps=[
                        dict(
                            name="cm1",
                            context="c1",
                            target_list="t1",
                            security_name="s1",
                        ),
                    ],
                    drop=dict(report_IPv4="test1", unknown_user=True),
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    groups=[
                        dict(
                            Ipv4_acl="test",
                            Ipv6_acl="test1",
                            context="test3",
                            group="g2",
                            read="test1",
                            version="v1",
                            write="test2",
                        ),
                    ],
                    location="test1",
                    logging_threshold_oid_processing=1,
                    logging_threshold_pdu_processing=1,
                    mib_bulkstat_max_procmem_size=101,
                    mroutemib_send_all_vrf=True,
                    mib_object_lists=["test1"],
                    overload_control=dict(
                        overload_drop_time=4,
                        overload_throttle_rate=6,
                    ),
                    mib_schema=[
                        dict(
                            name="mib1",
                            object_list="test1",
                            poll_interval=1,
                        ),
                    ],
                    notification_log_mib=dict(GlobalSize=5, size=5),
                    mib_bulkstat_transfer_ids=[
                        dict(
                            buffer_size=1024,
                            enable=True,
                            format_schemaASCI=True,
                            name="test2",
                            retain=1,
                            retry=1,
                            schema="test2",
                        ),
                    ],
                    traps=dict(
                        diameter=dict(
                            peerdown=True,
                            peerup=True,
                            permanentfail=True,
                            protocolerror=True,
                            transientfail=True,
                        ),
                        entity=True,
                        entity_redundancy=dict(
                            all=True,
                            status=True,
                            switchover=True,
                        ),
                        entity_state=dict(operstatus=True, switchover=True),
                        flash=dict(insertion=True, removal=True),
                        hsrp=True,
                        ipsla=True,
                        ipsec=dict(start=True, stop=True),
                        bridgemib=True,
                        bulkstat_collection=True,
                        cisco_entity_ext=True,
                        config=True,
                        copy_complete=True,
                        addrpool=dict(high=True, low=True),
                        bfd=True,
                        bgp=dict(cbgp2=True),
                        l2tun=dict(
                            sessions=True,
                            tunnel_down=True,
                            tunnel_up=True,
                        ),
                        l2vpn=dict(all=True, vc_down=True, vc_up=True),
                        msdp_peer_state_change=True,
                        ospf=dict(
                            errors=dict(
                                authentication_failure=True,
                                bad_packet=True,
                                config_error=True,
                                virt_authentication_failure=True,
                                virt_bad_packet=True,
                                virt_config_error=True,
                            ),
                            lsa=dict(lsa_maxage=True, lsa_originate=True),
                            retransmit=dict(packets=True, virt_packets=True),
                            state_change=dict(
                                if_state_change=True,
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                            ),
                        ),
                        ospfv3=dict(
                            errors=dict(
                                bad_packet=True,
                                config_error=True,
                                virt_config_error=True,
                            ),
                            state_change=dict(
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                                restart_helper_status_change=True,
                                restart_status_change=True,
                                restart_virtual_helper_status_change=True,
                            ),
                        ),
                        pim=dict(
                            interface_state_change=True,
                            invalid_message_received=True,
                            neighbor_change=True,
                            rp_mapping_change=True,
                        ),
                        power=True,
                        rf=True,
                        rsvp=dict(all=True, lost_flow=True, new_flow=True),
                        selective_vrf_download_role_change=True,
                        sensor=True,
                        snmp=dict(
                            authentication=True,
                            coldstart=True,
                            linkdown=True,
                            linkup=True,
                            warmstart=True,
                        ),
                        subscriber=dict(
                            session_agg_access_interface=True,
                            session_agg_node=True,
                        ),
                        syslog=True,
                        system=True,
                        vpls=dict(
                            all=True,
                            full_clear=True,
                            full_raise=True,
                            status=True,
                        ),
                        vrrp_events=True,
                    ),
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_snmp_server_merged(self):
        self.maxDiff = None

        set_module_args(
            dict(
                config=dict(
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            hosts=[
                                dict(
                                    community="test1",
                                    host="1.1.1.1",
                                    traps=True,
                                ),
                            ],
                        ),
                    ],
                    users=[
                        dict(
                            Ipv4_acl="test1",
                            Ipv6_acl="test2",
                            group="test2",
                            user="u1",
                            v4_acl="v4acl",
                            SystemOwner=True,
                        ),
                    ],
                    timeouts=dict(
                        duplicate=0,
                        inQdrop=0,
                        pdu_stats=1,
                        subagent=1,
                        threshold=0,
                    ),
                    trap=dict(throttle_time=12, link_ietf=True),
                    targets=[
                        dict(name="test2", vrf="vrf2"),
                        dict(host="1.1.1.2", name="test"),
                    ],
                    ifmib=dict(internal_cache_max_duration=4),
                    inform=dict(retries=7),
                    chassis_id="test2",
                    packetsize=490,
                    queue_length=2,
                    throttle_time=60,
                    trap_source="GigabitEthernet0/0/0/2",
                    trap_timeout=3,
                    context=["c1", "c2"],
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[dict(name="rule1")],
                        rules=[dict(rule_name="rule1", timeout=5)],
                    ),
                    communities=[
                        dict(
                            name="test2",
                            ro=True,
                            sdrowner=True,
                            acl_v4="test",
                            acl_v6="test1",
                        ),
                    ],
                    community_maps=[
                        dict(
                            name="cm1",
                            context="c1",
                            target_list="t1",
                            security_name="s1",
                        ),
                    ],
                    drop=dict(report_IPv4="test1", unknown_user=True),
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    groups=[
                        dict(
                            Ipv4_acl="test",
                            Ipv6_acl="test1",
                            context="test3",
                            group="g2",
                            read="test1",
                            version="v1",
                            write="test2",
                        ),
                    ],
                    interfaces=[dict(name=" GigabitEthernet0/0/0/2")],
                    location="test1",
                    logging_threshold_oid_processing=1,
                    logging_threshold_pdu_processing=1,
                    mib_bulkstat_max_procmem_size=101,
                    mroutemib_send_all_vrf=True,
                    mib_object_lists=["test1"],
                    overload_control=dict(
                        overload_drop_time=4,
                        overload_throttle_rate=6,
                    ),
                    mib_schema=[
                        dict(
                            name="mib1",
                            object_list="test1",
                            poll_interval=1,
                        ),
                    ],
                    notification_log_mib=dict(GlobalSize=5, size=5),
                    mib_bulkstat_transfer_ids=[
                        dict(
                            buffer_size=1024,
                            enable=True,
                            format_schemaASCI=True,
                            name="test2",
                            retain=1,
                            retry=1,
                            schema="test2",
                        ),
                    ],
                    traps=dict(
                        diameter=dict(
                            peerdown=True,
                            peerup=True,
                            permanentfail=True,
                            protocolerror=True,
                            transientfail=True,
                        ),
                        entity=True,
                        entity_redundancy=dict(
                            all=True,
                            status=True,
                            switchover=True,
                        ),
                        entity_state=dict(operstatus=True, switchover=True),
                        flash=dict(insertion=True, removal=True),
                        hsrp=True,
                        ipsla=True,
                        ipsec=dict(start=True, stop=True),
                        bridgemib=True,
                        bulkstat_collection=True,
                        cisco_entity_ext=True,
                        config=True,
                        copy_complete=True,
                        addrpool=dict(high=True, low=True),
                        bfd=True,
                        bgp=dict(cbgp2=True),
                        l2tun=dict(
                            sessions=True,
                            tunnel_down=True,
                            tunnel_up=True,
                        ),
                        l2vpn=dict(all=True, vc_down=True, vc_up=True),
                        msdp_peer_state_change=True,
                        ospf=dict(
                            errors=dict(
                                authentication_failure=True,
                                bad_packet=True,
                                config_error=True,
                                virt_authentication_failure=True,
                                virt_bad_packet=True,
                                virt_config_error=True,
                            ),
                            lsa=dict(lsa_maxage=True, lsa_originate=True),
                            retransmit=dict(packets=True, virt_packets=True),
                            state_change=dict(
                                if_state_change=True,
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                            ),
                        ),
                        ospfv3=dict(
                            errors=dict(
                                bad_packet=True,
                                config_error=True,
                                virt_config_error=True,
                            ),
                            state_change=dict(
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                                restart_helper_status_change=True,
                                restart_status_change=True,
                                restart_virtual_helper_status_change=True,
                            ),
                        ),
                        pim=dict(
                            interface_state_change=True,
                            invalid_message_received=True,
                            neighbor_change=True,
                            rp_mapping_change=True,
                        ),
                        power=True,
                        rf=True,
                        rsvp=dict(all=True, lost_flow=True, new_flow=True),
                        selective_vrf_download_role_change=True,
                        sensor=True,
                        snmp=dict(
                            authentication=True,
                            coldstart=True,
                            linkdown=True,
                            linkup=True,
                            warmstart=True,
                        ),
                        subscriber=dict(
                            session_agg_access_interface=True,
                            session_agg_node=True,
                        ),
                        syslog=True,
                        system=True,
                        vpls=dict(
                            all=True,
                            full_clear=True,
                            full_raise=True,
                            status=True,
                        ),
                        vrrp_events=True,
                        isis=dict(
                            adjacency_change=True,
                            area_mismatch=True,
                            attempt_to_exceed_max_sequence=True,
                            authentication_failure=True,
                            authentication_type_failure=True,
                            corrupted_lsp_detected=True,
                            database_overload=True,
                            id_len_mismatch=True,
                            lsp_error_detected=True,
                            lsp_too_large_to_propagate=True,
                            manual_address_drops=True,
                            max_area_addresses_mismatch=True,
                            orig_lsp_buff_size_mismatch=True,
                            own_lsp_purge=True,
                            protocols_supported_mismatch=True,
                            rejected_adjacency=True,
                            sequence_number_skip=True,
                            version_skew=True,
                        ),
                    ),
                ),
                state="merged",
            ),
        )
        commands = [
            "snmp-server chassis-id test2",
            "snmp-server correlator buffer-size 1024",
            "snmp-server ipv4 dscp af11",
            "snmp-server ipv6 precedence routine",
            "snmp-server location test1",
            "snmp-server logging threshold oid-processing 1",
            "snmp-server logging threshold pdu-processing 1",
            "snmp-server mib bulkstat max-procmem-size 101",
            "snmp-server mroutemib send-all-vrf",
            "snmp-server overload-control 4 6",
            "snmp-server packetsize 490",
            "snmp-server queue-length 2",
            "snmp-server throttle-time 60",
            "snmp-server trap-source GigabitEthernet0/0/0/2",
            "snmp-server trap-timeout 3",
            "snmp-server drop report acl IPv4 test1",
            "snmp-server drop unknown-user",
            "snmp-server ifmib internal cache max-duration 4",
            "snmp-server inform retries 7",
            "snmp-server notification-log-mib size 5",
            "snmp-server notification-log-mib GlobalSize 5",
            "snmp-server trap link ietf",
            "snmp-server trap throttle-time 12",
            "snmp-server timeouts threshold 0",
            "snmp-server timeouts pdu stats 1",
            "snmp-server timeouts subagent 1",
            "snmp-server timeouts inQdrop 0",
            "snmp-server timeouts duplicate 0",
            "snmp-server traps addrpool low",
            "snmp-server traps addrpool high",
            "snmp-server traps bfd",
            "snmp-server traps bgp cbgp2",
            "snmp-server traps bulkstat collection",
            "snmp-server traps bridgemib",
            "snmp-server traps copy-complete",
            "snmp-server traps cisco-entity-ext",
            "snmp-server traps config",
            "snmp-server traps diameter peerdown",
            "snmp-server traps diameter peerup",
            "snmp-server traps diameter protocolerror",
            "snmp-server traps diameter permanentfail",
            "snmp-server traps diameter transientfail",
            "snmp-server traps entity",
            "snmp-server traps entity-redundancy all",
            "snmp-server traps entity-redundancy status",
            "snmp-server traps entity-redundancy switchover",
            "snmp-server traps entity-state operstatus",
            "snmp-server traps entity-state switchover",
            "snmp-server traps flash removal",
            "snmp-server traps flash insertion",
            "snmp-server traps hsrp",
            "snmp-server traps ipsla",
            "snmp-server traps ipsec tunnel start",
            "snmp-server traps ipsec tunnel stop",
            "snmp-server traps isis adjacency-change area-mismatch attempt-to-exceed-max-sequence "
            "authentication-failure authentication-type-failure corrupted-lsp-detected database-overload "
            "id-len-mismatch lsp-error-detected lsp-too-large-to-propagate manual-address-drops"
            " max-area-addresses-mismatch orig-lsp-buff-size-mismatch version-skew own-lsp-purge"
            " rejected-adjacency protocols-supported-mismatch sequence-number-skip",
            "snmp-server traps l2tun sessions",
            "snmp-server traps l2tun tunnel-up",
            "snmp-server traps l2tun tunnel-down",
            "snmp-server traps l2vpn all",
            "snmp-server traps l2vpn vc-up",
            "snmp-server traps l2vpn vc-down",
            "snmp-server traps msdp peer-state-change",
            "snmp-server traps ospf retransmit virt-packets",
            "snmp-server traps ospf retransmit packets",
            "snmp-server traps ospf lsa lsa-originate",
            "snmp-server traps ospf lsa lsa-maxage",
            "snmp-server traps ospf errors bad-packet",
            "snmp-server traps ospf errors authentication-failure",
            "snmp-server traps ospf errors config-error",
            "snmp-server traps ospf errors virt-bad-packet",
            "snmp-server traps ospf errors virt-authentication-failure",
            "snmp-server traps ospf errors virt-config-error",
            "snmp-server traps ospf state-change if-state-change",
            "snmp-server traps ospf state-change neighbor-state-change",
            "snmp-server traps ospf state-change virtif-state-change",
            "snmp-server traps ospf state-change virtneighbor-state-change",
            "snmp-server traps ospfv3 errors bad-packet",
            "snmp-server traps ospfv3 errors config-error",
            "snmp-server traps ospfv3 errors virt-config-error",
            "snmp-server traps ospfv3 state-change neighbor-state-change",
            "snmp-server traps ospfv3 state-change virtif-state-change",
            "snmp-server traps ospfv3 state-change virtneighbor-state-change",
            "snmp-server traps ospfv3 state-change restart-status-change",
            "snmp-server traps ospfv3 state-change restart-helper-status-change",
            "snmp-server traps ospfv3 state-change restart-virtual-helper-status-change",
            "snmp-server traps power",
            "snmp-server traps rf",
            "snmp-server traps pim neighbor-change",
            "snmp-server traps pim invalid-message-received",
            "snmp-server traps pim rp-mapping-change",
            "snmp-server traps pim interface-state-change",
            "snmp-server traps rsvp lost-flow",
            "snmp-server traps rsvp new-flow",
            "snmp-server traps rsvp all",
            "snmp-server traps selective-vrf-download role-change",
            "snmp-server traps sensor",
            "snmp-server traps vrrp events",
            "snmp-server traps syslog",
            "snmp-server traps system",
            "snmp-server traps subscriber session-agg access-interface",
            "snmp-server traps subscriber session-agg node",
            "snmp-server traps vpls all",
            "snmp-server traps vpls full-clear",
            "snmp-server traps vpls full-raise",
            "snmp-server traps vpls status",
            "snmp-server traps snmp linkup",
            "snmp-server traps snmp linkdown",
            "snmp-server traps snmp coldstart",
            "snmp-server traps snmp warmstart",
            "snmp-server traps snmp authentication",
            "snmp-server community test2 RO SDROwner IPv4 test IPv6 test1",
            "snmp-server community-map cm1 context c1 security-name s1 target-list t1",
            "snmp-server correlator ruleset rule1",
            "snmp-server correlator rule rule1 timeout 5",
            "snmp-server context c1",
            "snmp-server context c2",
            "snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1",
            "snmp-server interface  GigabitEthernet0/0/0/2",
            "snmp-server mib bulkstat object-list test1",
            "snmp-server mib bulkstat schema mib1 object-list test1",
            "snmp-server mib bulkstat schema mib1 poll-interval 1",
            "snmp-server mib bulkstat transfer-id test2 buffer-size 1024",
            "snmp-server mib bulkstat transfer-id test2 enable",
            "snmp-server mib bulkstat transfer-id test2 format schemaASCII",
            "snmp-server mib bulkstat transfer-id test2 retain 1",
            "snmp-server mib bulkstat transfer-id test2 retry 1",
            "snmp-server mib bulkstat transfer-id test2 schema test2",
            "snmp-server user u1 test2  IPv4 test1 IPv6 test2 v4acl SystemOwner",
            "snmp-server target list test2 vrf vrf2",
            "snmp-server target list test host 1.1.1.2",
            "snmp-server vrf vrf1",
            "host 1.1.1.1 traps test1",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_snmp_server_deleted(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                snmp-server vrf vrf1
                 host 1.1.1.1 traps test1
                !
                snmp-server drop report acl IPv4 test1
                snmp-server drop unknown-user
                snmp-server ipv4 dscp af11
                snmp-server ipv6 precedence routine
                snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2 v4acl
                snmp-server community test2 RW SystemOwner IPv4 test IPv6 test1
                snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1
                snmp-server queue-length 2
                snmp-server trap-timeout 3
                snmp-server trap throttle-time 12
                snmp-server traps rf
                snmp-server traps bfd
                snmp-server traps bgp cbgp2
                snmp-server traps pim neighbor-change
                snmp-server traps pim invalid-message-received
                snmp-server traps pim rp-mapping-change
                snmp-server traps pim interface-state-change
                snmp-server traps copy-complete
                snmp-server traps hsrp
                snmp-server traps ipsla
                snmp-server traps msdp peer-state-change
                snmp-server traps snmp linkup
                snmp-server traps snmp linkdown
                snmp-server traps snmp coldstart
                snmp-server traps snmp warmstart
                snmp-server traps snmp authentication
                snmp-server traps vrrp events
                snmp-server traps flash removal
                snmp-server traps flash insertion
                snmp-server traps ipsec tunnel stop
                snmp-server traps ipsec tunnel start
                snmp-server traps power
                snmp-server traps config
                snmp-server traps entity
                snmp-server traps sensor
                snmp-server traps selective-vrf-download role-change
                snmp-server traps syslog
                snmp-server traps system
                snmp-server traps ospf lsa lsa-maxage
                snmp-server traps ospf lsa lsa-originate
                snmp-server traps ospf errors bad-packet
                snmp-server traps ospf errors authentication-failure
                snmp-server traps ospf errors config-error
                snmp-server traps ospf errors virt-bad-packet
                snmp-server traps ospf errors virt-authentication-failure
                snmp-server traps ospf errors virt-config-error
                snmp-server traps ospf retransmit packets
                snmp-server traps ospf retransmit virt-packets
                snmp-server traps ospf state-change if-state-change
                snmp-server traps ospf state-change neighbor-state-change
                snmp-server traps ospf state-change virtif-state-change
                snmp-server traps ospf state-change virtneighbor-state-change
                snmp-server traps rsvp all
                snmp-server traps rsvp new-flow
                snmp-server traps rsvp lost-flow
                snmp-server traps l2tun sessions
                snmp-server traps l2tun tunnel-up
                snmp-server traps l2tun tunnel-down
                snmp-server traps vpls all
                snmp-server traps vpls status
                snmp-server traps vpls full-clear
                snmp-server traps vpls full-raise
                snmp-server traps bulkstat collection
                snmp-server traps diameter peerup
                snmp-server traps diameter peerdown
                snmp-server traps diameter protocolerror
                snmp-server traps diameter permanentfail
                snmp-server traps diameter transientfail
                snmp-server traps l2vpn all
                snmp-server traps l2vpn vc-up
                snmp-server traps l2vpn vc-down
                snmp-server traps bridgemib
                snmp-server traps ospfv3 errors bad-packet
                snmp-server traps ospfv3 errors config-error
                snmp-server traps ospfv3 errors virt-config-error
                snmp-server traps ospfv3 state-change neighbor-state-change
                snmp-server traps ospfv3 state-change virtif-state-change
                snmp-server traps ospfv3 state-change virtneighbor-state-change
                snmp-server traps ospfv3 state-change restart-status-change
                snmp-server traps ospfv3 state-change restart-helper-status-change
                snmp-server traps ospfv3 state-change restart-virtual-helper-status-change
                snmp-server traps subscriber session-agg node
                snmp-server traps subscriber session-agg access-interface
                snmp-server traps addrpool low
                snmp-server traps addrpool high
                snmp-server traps cisco-entity-ext
                snmp-server traps entity-state operstatus
                snmp-server traps entity-state switchover
                snmp-server traps entity-redundancy all
                snmp-server traps entity-redundancy status
                snmp-server traps entity-redundancy switchover
                snmp-server chassis-id test2
                snmp-server contact t1
                snmp-server location test1
                snmp-server target list test host 1.1.1.2
                snmp-server target list test2 vrf vrf2
                snmp-server context c1
                snmp-server context c2
                snmp-server logging threshold oid-processing 1
                snmp-server logging threshold pdu-processing 1
                snmp-server mib bulkstat max-procmem-size 101
                snmp-server mib bulkstat object-list test1
                !
                snmp-server timeouts duplicate 0
                snmp-server timeouts inQdrop 0
                snmp-server timeouts subagent 1
                snmp-server timeouts pdu stats 1
                snmp-server timeouts threshold 0
                snmp-server packetsize 490
                snmp-server correlator buffer-size 1024
                snmp-server trap-source GigabitEthernet0/0/0/2
                snmp-server throttle-time 60
                snmp-server community-map cm1 context c1 security-name s1 target-list t1
                snmp-server inform retries 7
                snmp-server overload-control 4 6
                snmp-server interface GigabitEthernet0/0/0/2
                !
                snmp-server ifmib internal cache max-duration 4
                snmp-server mroutemib send-all-vrf
                snmp-server notification-log-mib size 5
                snmp-server notification-log-mib GlobalSize 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="deleted"))
        commands = [
            "no snmp-server chassis-id test2",
            "no snmp-server correlator buffer-size 1024",
            "no snmp-server contact t1",
            "no snmp-server ipv4 dscp af11",
            "no snmp-server ipv6 precedence routine",
            "no snmp-server location test1",
            "no snmp-server logging threshold oid-processing 1",
            "no snmp-server logging threshold pdu-processing 1",
            "no snmp-server mib bulkstat max-procmem-size 101",
            "no snmp-server mroutemib send-all-vrf",
            "no snmp-server overload-control 4 6",
            "no snmp-server packetsize 490",
            "no snmp-server queue-length 2",
            "no snmp-server throttle-time 60",
            "no snmp-server trap-source GigabitEthernet0/0/0/2",
            "no snmp-server trap-timeout 3",
            "no snmp-server drop report acl IPv4 test1",
            "no snmp-server drop unknown-user",
            "no snmp-server ifmib internal cache max-duration 4",
            "no snmp-server inform retries 7",
            "no snmp-server notification-log-mib size 5",
            "no snmp-server notification-log-mib GlobalSize 5",
            "no snmp-server trap throttle-time 12",
            "no snmp-server timeouts threshold 0",
            "no snmp-server timeouts pdu stats 1",
            "no snmp-server timeouts subagent 1",
            "no snmp-server timeouts inQdrop 0",
            "no snmp-server timeouts duplicate 0",
            "no snmp-server traps addrpool low",
            "no snmp-server traps addrpool high",
            "no snmp-server traps bfd",
            "no snmp-server traps bgp cbgp2",
            "no snmp-server traps bulkstat collection",
            "no snmp-server traps bridgemib",
            "no snmp-server traps copy-complete",
            "no snmp-server traps cisco-entity-ext",
            "no snmp-server traps config",
            "no snmp-server traps diameter peerdown",
            "no snmp-server traps diameter peerup",
            "no snmp-server traps diameter protocolerror",
            "no snmp-server traps diameter permanentfail",
            "no snmp-server traps diameter transientfail",
            "no snmp-server traps entity",
            "no snmp-server traps entity-redundancy all",
            "no snmp-server traps entity-redundancy status",
            "no snmp-server traps entity-redundancy switchover",
            "no snmp-server traps entity-state operstatus",
            "no snmp-server traps entity-state switchover",
            "no snmp-server traps flash removal",
            "no snmp-server traps flash insertion",
            "no snmp-server traps hsrp",
            "no snmp-server traps ipsla",
            "no snmp-server traps ipsec tunnel start",
            "no snmp-server traps ipsec tunnel stop",
            "no snmp-server traps l2tun sessions",
            "no snmp-server traps l2tun tunnel-up",
            "no snmp-server traps l2tun tunnel-down",
            "no snmp-server traps l2vpn all",
            "no snmp-server traps l2vpn vc-up",
            "no snmp-server traps l2vpn vc-down",
            "no snmp-server traps msdp peer-state-change",
            "no snmp-server traps ospf retransmit virt-packets",
            "no snmp-server traps ospf retransmit packets",
            "no snmp-server traps ospf lsa lsa-originate",
            "no snmp-server traps ospf lsa lsa-maxage",
            "no snmp-server traps ospf errors bad-packet",
            "no snmp-server traps ospf errors authentication-failure",
            "no snmp-server traps ospf errors config-error",
            "no snmp-server traps ospf errors virt-bad-packet",
            "no snmp-server traps ospf errors virt-authentication-failure",
            "no snmp-server traps ospf errors virt-config-error",
            "no snmp-server traps ospf state-change if-state-change",
            "no snmp-server traps ospf state-change neighbor-state-change",
            "no snmp-server traps ospf state-change virtif-state-change",
            "no snmp-server traps ospf state-change virtneighbor-state-change",
            "no snmp-server traps ospfv3 errors bad-packet",
            "no snmp-server traps ospfv3 errors config-error",
            "no snmp-server traps ospfv3 errors virt-config-error",
            "no snmp-server traps ospfv3 state-change neighbor-state-change",
            "no snmp-server traps ospfv3 state-change virtif-state-change",
            "no snmp-server traps ospfv3 state-change virtneighbor-state-change",
            "no snmp-server traps ospfv3 state-change restart-status-change",
            "no snmp-server traps ospfv3 state-change restart-helper-status-change",
            "no snmp-server traps ospfv3 state-change restart-virtual-helper-status-change",
            "no snmp-server traps power",
            "no snmp-server traps rf",
            "no snmp-server traps pim neighbor-change",
            "no snmp-server traps pim invalid-message-received",
            "no snmp-server traps pim rp-mapping-change",
            "no snmp-server traps pim interface-state-change",
            "no snmp-server traps rsvp lost-flow",
            "no snmp-server traps rsvp new-flow",
            "no snmp-server traps rsvp all",
            "no snmp-server traps selective-vrf-download role-change",
            "no snmp-server traps sensor",
            "no snmp-server traps vrrp events",
            "no snmp-server traps syslog",
            "no snmp-server traps system",
            "no snmp-server traps subscriber session-agg access-interface",
            "no snmp-server traps subscriber session-agg node",
            "no snmp-server traps vpls all",
            "no snmp-server traps vpls full-clear",
            "no snmp-server traps vpls full-raise",
            "no snmp-server traps vpls status",
            "no snmp-server traps snmp linkup",
            "no snmp-server traps snmp linkdown",
            "no snmp-server traps snmp coldstart",
            "no snmp-server traps snmp warmstart",
            "no snmp-server traps snmp authentication",
            "no snmp-server community test2 RW SystemOwner IPv4 test IPv6 test1",
            "no snmp-server community-map cm1 context c1 security-name s1 target-list t1",
            "no snmp-server context c1",
            "no snmp-server context c2",
            "no snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1",
            "no snmp-server interface GigabitEthernet0/0/0/2",
            "no snmp-server mib bulkstat object-list test1",
            "no snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2 v4acl",
            "no snmp-server target list test host 1.1.1.2",
            "no snmp-server target list test2 vrf vrf2",
            "no snmp-server vrf vrf1",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_snmp_server_replaced(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                snmp-server vrf vrf1
                 host 1.1.1.1 traps test1
                !
                snmp-server drop report acl IPv4 test1
                snmp-server drop unknown-user
                snmp-server ipv4 dscp af11
                snmp-server ipv6 precedence routine
                snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2 v4acl
                snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
                snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1
                snmp-server queue-length 2
                snmp-server trap-timeout 3
                snmp-server trap throttle-time 12
                snmp-server traps rf
                snmp-server traps bfd
                snmp-server traps bgp cbgp2
                snmp-server traps pim neighbor-change
                snmp-server traps pim invalid-message-received
                snmp-server traps pim rp-mapping-change
                snmp-server traps pim interface-state-change
                snmp-server traps copy-complete
                snmp-server traps hsrp
                snmp-server traps ipsla
                snmp-server traps msdp peer-state-change
                snmp-server traps snmp linkup
                snmp-server traps snmp linkdown
                snmp-server traps snmp coldstart
                snmp-server traps snmp warmstart
                snmp-server traps snmp authentication
                snmp-server traps vrrp events
                snmp-server traps flash removal
                snmp-server traps flash insertion
                snmp-server traps ipsec tunnel stop
                snmp-server traps ipsec tunnel start
                snmp-server traps power
                snmp-server traps config
                snmp-server traps entity
                snmp-server traps sensor
                snmp-server traps selective-vrf-download role-change
                snmp-server traps syslog
                snmp-server traps system
                snmp-server traps ospf lsa lsa-maxage
                snmp-server traps ospf lsa lsa-originate
                snmp-server traps ospf errors bad-packet
                snmp-server traps ospf errors authentication-failure
                snmp-server traps ospf errors config-error
                snmp-server traps ospf errors virt-bad-packet
                snmp-server traps ospf errors virt-authentication-failure
                snmp-server traps ospf errors virt-config-error
                snmp-server traps ospf retransmit packets
                snmp-server traps ospf retransmit virt-packets
                snmp-server traps ospf state-change if-state-change
                snmp-server traps ospf state-change neighbor-state-change
                snmp-server traps ospf state-change virtif-state-change
                snmp-server traps ospf state-change virtneighbor-state-change
                snmp-server traps rsvp all
                snmp-server traps rsvp new-flow
                snmp-server traps rsvp lost-flow
                snmp-server traps l2tun sessions
                snmp-server traps l2tun tunnel-up
                snmp-server traps l2tun tunnel-down
                snmp-server traps vpls all
                snmp-server traps vpls status
                snmp-server traps vpls full-clear
                snmp-server traps vpls full-raise
                snmp-server traps bulkstat collection
                snmp-server traps diameter peerup
                snmp-server traps diameter peerdown
                snmp-server traps diameter protocolerror
                snmp-server traps diameter permanentfail
                snmp-server traps diameter transientfail
                snmp-server traps l2vpn all
                snmp-server traps l2vpn vc-up
                snmp-server traps l2vpn vc-down
                snmp-server traps bridgemib
                snmp-server traps ospfv3 errors bad-packet
                snmp-server traps ospfv3 errors config-error
                snmp-server traps ospfv3 errors virt-config-error
                snmp-server traps ospfv3 state-change neighbor-state-change
                snmp-server traps ospfv3 state-change virtif-state-change
                snmp-server traps ospfv3 state-change virtneighbor-state-change
                snmp-server traps ospfv3 state-change restart-status-change
                snmp-server traps ospfv3 state-change restart-helper-status-change
                snmp-server traps ospfv3 state-change restart-virtual-helper-status-change
                snmp-server traps subscriber session-agg node
                snmp-server traps subscriber session-agg access-interface
                snmp-server traps addrpool low
                snmp-server traps addrpool high
                snmp-server traps cisco-entity-ext
                snmp-server traps entity-state operstatus
                snmp-server traps entity-state switchover
                snmp-server traps entity-redundancy all
                snmp-server traps entity-redundancy status
                snmp-server traps entity-redundancy switchover
                snmp-server chassis-id test2
                snmp-server contact t1
                snmp-server location test1
                snmp-server target list test host 1.1.1.2
                snmp-server target list test2 vrf vrf2
                snmp-server context c1
                snmp-server context c2
                snmp-server logging threshold oid-processing 1
                snmp-server logging threshold pdu-processing 1
                snmp-server mib bulkstat max-procmem-size 101
                snmp-server mib bulkstat object-list test1
                !
                snmp-server mib bulkstat schema mib1
                 object-list test1
                 poll-interval 1
                !
                snmp-server mib bulkstat transfer-id test2
                 retry 1
                 buffer-size 1024
                 enable
                 format schemaASCII
                 retain 1
                 schema test2
                !
                snmp-server timeouts duplicate 0
                snmp-server timeouts inQdrop 0
                snmp-server timeouts subagent 1
                snmp-server timeouts pdu stats 1
                snmp-server timeouts threshold 0
                snmp-server packetsize 490
                snmp-server correlator rule rule1
                 timeout 5
                !
                snmp-server correlator ruleset rule1
                !
                snmp-server correlator buffer-size 1024
                snmp-server trap-source GigabitEthernet0/0/0/2
                snmp-server throttle-time 60
                snmp-server community-map cm1 context c1 security-name s1 target-list t1
                snmp-server inform retries 7
                snmp-server overload-control 4 6
                snmp-server ifmib internal cache max-duration 4
                snmp-server mroutemib send-all-vrf
                snmp-server notification-log-mib size 5
                snmp-server notification-log-mib GlobalSize 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    vrfs=[
                        dict(
                            vrf="vrf2",
                            hosts=[
                                dict(
                                    community="test1",
                                    host="1.1.1.1",
                                    traps=True,
                                ),
                            ],
                        ),
                    ],
                    users=[
                        dict(
                            Ipv4_acl="test1",
                            Ipv6_acl="test2",
                            group="test2",
                            user="u1",
                            v4_acl="v4acl",
                        ),
                    ],
                    timeouts=dict(
                        duplicate=0,
                        inQdrop=0,
                        pdu_stats=1,
                        subagent=1,
                        threshold=0,
                    ),
                    trap=dict(throttle_time=12),
                    targets=[
                        dict(name="test2", vrf="vrf2"),
                        dict(host="1.1.1.2", name="test"),
                    ],
                    ifmib=dict(internal_cache_max_duration=4),
                    inform=dict(retries=7),
                    chassis_id="test2",
                    packetsize=490,
                    queue_length=2,
                    throttle_time=60,
                    trap_source="GigabitEthernet0/0/0/2",
                    trap_timeout=3,
                    context=["c1", "c2"],
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[dict(name="rule1")],
                        rules=[dict(rule_name="rule1", timeout=5)],
                    ),
                    communities=[
                        dict(
                            name="test2",
                            ro=True,
                            sdrowner=True,
                            acl_v4="test",
                            acl_v6="test1",
                        ),
                    ],
                    community_maps=[
                        dict(
                            name="cm1",
                            context="c1",
                            target_list="t1",
                            security_name="s1",
                        ),
                    ],
                    drop=dict(report_IPv4="test1", unknown_user=True),
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    groups=[
                        dict(
                            Ipv4_acl="test",
                            Ipv6_acl="test1",
                            context="test3",
                            group="g2",
                            read="test1",
                            version="v1",
                            write="test2",
                        ),
                    ],
                    location="test",
                    logging_threshold_oid_processing=2,
                    logging_threshold_pdu_processing=1,
                    mib_bulkstat_max_procmem_size=101,
                    mroutemib_send_all_vrf=True,
                    mib_object_lists=["test1"],
                    overload_control=dict(
                        overload_drop_time=4,
                        overload_throttle_rate=6,
                    ),
                    mib_schema=[
                        dict(
                            name="mib1",
                            object_list="test1",
                            poll_interval=1,
                        ),
                    ],
                    notification_log_mib=dict(GlobalSize=5, size=5),
                    mib_bulkstat_transfer_ids=[
                        dict(
                            buffer_size=1024,
                            enable=True,
                            format_schemaASCI=True,
                            name="test2",
                            retain=1,
                            retry=1,
                            schema="test2",
                        ),
                    ],
                    traps=dict(
                        diameter=dict(
                            peerdown=True,
                            peerup=True,
                            permanentfail=True,
                            protocolerror=True,
                            transientfail=True,
                        ),
                        entity=True,
                        entity_redundancy=dict(
                            all=True,
                            status=True,
                            switchover=True,
                        ),
                        entity_state=dict(operstatus=True, switchover=True),
                        flash=dict(insertion=True, removal=True),
                        ipsec=dict(start=True, stop=True),
                        bridgemib=True,
                        bulkstat_collection=True,
                        cisco_entity_ext=True,
                        config=True,
                        copy_complete=True,
                        addrpool=dict(high=True, low=True),
                        bfd=True,
                        bgp=dict(cbgp2=True),
                        l2tun=dict(
                            sessions=True,
                            tunnel_down=True,
                            tunnel_up=True,
                        ),
                        l2vpn=dict(all=True, vc_down=True, vc_up=True),
                        msdp_peer_state_change=True,
                        ospf=dict(
                            errors=dict(
                                authentication_failure=True,
                                bad_packet=True,
                                config_error=True,
                                virt_authentication_failure=True,
                                virt_bad_packet=True,
                                virt_config_error=True,
                            ),
                            lsa=dict(lsa_maxage=True, lsa_originate=True),
                            retransmit=dict(packets=True, virt_packets=True),
                            state_change=dict(
                                if_state_change=True,
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                            ),
                        ),
                        ospfv3=dict(
                            errors=dict(
                                bad_packet=True,
                                config_error=True,
                                virt_config_error=True,
                            ),
                        ),
                        pim=dict(
                            interface_state_change=True,
                            invalid_message_received=True,
                            neighbor_change=True,
                            rp_mapping_change=True,
                        ),
                        power=True,
                        rf=True,
                        rsvp=dict(all=True, lost_flow=True, new_flow=True),
                        selective_vrf_download_role_change=True,
                        sensor=True,
                        snmp=dict(
                            authentication=True,
                            coldstart=True,
                            linkdown=True,
                            linkup=True,
                            warmstart=True,
                        ),
                        subscriber=dict(
                            session_agg_access_interface=True,
                            session_agg_node=True,
                        ),
                        syslog=True,
                        system=True,
                        vpls=dict(
                            all=True,
                            full_clear=True,
                            full_raise=True,
                            status=True,
                        ),
                        vrrp_events=True,
                    ),
                ),
                state="replaced",
            ),
        )
        commands = [
            "no snmp-server contact t1",
            "no snmp-server traps hsrp",
            "no snmp-server traps ipsla",
            "no snmp-server traps ospfv3 state-change neighbor-state-change",
            "no snmp-server traps ospfv3 state-change virtif-state-change",
            "no snmp-server traps ospfv3 state-change virtneighbor-state-change",
            "no snmp-server traps ospfv3 state-change restart-status-change",
            "no snmp-server traps ospfv3 state-change restart-helper-status-change",
            "no snmp-server traps ospfv3 state-change restart-virtual-helper-status-change",
            "no snmp-server vrf vrf1",
            "snmp-server location test",
            "snmp-server logging threshold oid-processing 2",
            "snmp-server user u1 test2  IPv4 test1 IPv6 test2 v4acl",
            "snmp-server vrf vrf2",
            "host 1.1.1.1 traps test1",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_snmp_server_replaced_idempotent(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                snmp-server vrf vrf1
                 host 1.1.1.1 traps test1
                !
                snmp-server drop report acl IPv4 test1
                snmp-server drop unknown-user
                snmp-server ipv4 dscp af11
                snmp-server ipv6 precedence routine
                snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2 v4acl
                snmp-server community test2 RW SystemOwner IPv4 test IPv6 test1
                snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1
                snmp-server queue-length 2
                snmp-server trap-timeout 3
                snmp-server trap throttle-time 12
                snmp-server traps rf
                snmp-server traps bfd
                snmp-server traps bgp cbgp2
                snmp-server traps pim neighbor-change
                snmp-server traps pim invalid-message-received
                snmp-server traps pim rp-mapping-change
                snmp-server traps pim interface-state-change
                snmp-server traps copy-complete
                snmp-server traps hsrp
                snmp-server traps ipsla
                snmp-server traps msdp peer-state-change
                snmp-server traps snmp linkup
                snmp-server traps snmp linkdown
                snmp-server traps snmp coldstart
                snmp-server traps snmp warmstart
                snmp-server traps snmp authentication
                snmp-server traps vrrp events
                snmp-server traps flash removal
                snmp-server traps flash insertion
                snmp-server traps ipsec tunnel stop
                snmp-server traps ipsec tunnel start
                snmp-server traps power
                snmp-server traps config
                snmp-server traps entity
                snmp-server traps sensor
                snmp-server traps selective-vrf-download role-change
                snmp-server traps syslog
                snmp-server traps system
                snmp-server traps ospf lsa lsa-maxage
                snmp-server traps ospf lsa lsa-originate
                snmp-server traps ospf errors bad-packet
                snmp-server traps ospf errors authentication-failure
                snmp-server traps ospf errors config-error
                snmp-server traps ospf errors virt-bad-packet
                snmp-server traps ospf errors virt-authentication-failure
                snmp-server traps ospf errors virt-config-error
                snmp-server traps ospf retransmit packets
                snmp-server traps ospf retransmit virt-packets
                snmp-server traps ospf state-change if-state-change
                snmp-server traps ospf state-change neighbor-state-change
                snmp-server traps ospf state-change virtif-state-change
                snmp-server traps ospf state-change virtneighbor-state-change
                snmp-server traps rsvp all
                snmp-server traps rsvp new-flow
                snmp-server traps rsvp lost-flow
                snmp-server traps l2tun sessions
                snmp-server traps l2tun tunnel-up
                snmp-server traps l2tun tunnel-down
                snmp-server traps vpls all
                snmp-server traps vpls status
                snmp-server traps vpls full-clear
                snmp-server traps vpls full-raise
                snmp-server traps bulkstat collection
                snmp-server traps diameter peerup
                snmp-server traps diameter peerdown
                snmp-server traps diameter protocolerror
                snmp-server traps diameter permanentfail
                snmp-server traps diameter transientfail
                snmp-server traps l2vpn all
                snmp-server traps l2vpn vc-up
                snmp-server traps l2vpn vc-down
                snmp-server traps bridgemib
                snmp-server traps ospfv3 errors bad-packet
                snmp-server traps ospfv3 errors config-error
                snmp-server traps ospfv3 errors virt-config-error
                snmp-server traps ospfv3 state-change neighbor-state-change
                snmp-server traps ospfv3 state-change virtif-state-change
                snmp-server traps ospfv3 state-change virtneighbor-state-change
                snmp-server traps ospfv3 state-change restart-status-change
                snmp-server traps ospfv3 state-change restart-helper-status-change
                snmp-server traps ospfv3 state-change restart-virtual-helper-status-change
                snmp-server traps subscriber session-agg node
                snmp-server traps subscriber session-agg access-interface
                snmp-server traps addrpool low
                snmp-server traps addrpool high
                snmp-server traps cisco-entity-ext
                snmp-server traps entity-state operstatus
                snmp-server traps entity-state switchover
                snmp-server traps entity-redundancy all
                snmp-server traps entity-redundancy status
                snmp-server traps entity-redundancy switchover
                snmp-server chassis-id test2
                snmp-server location test1
                snmp-server target list test host 1.1.1.2
                snmp-server target list test2 vrf vrf2
                snmp-server context c1
                snmp-server context c2
                snmp-server logging threshold oid-processing 1
                snmp-server logging threshold pdu-processing 1
                snmp-server mib bulkstat max-procmem-size 101
                snmp-server mib bulkstat object-list test1
                !
                snmp-server mib bulkstat schema mib1
                 object-list test1
                 poll-interval 1
                !
                snmp-server mib bulkstat transfer-id test2
                 retry 1
                 buffer-size 1024
                 enable
                 format schemaASCII
                 retain 1
                 schema test2
                !
                snmp-server timeouts duplicate 0
                snmp-server timeouts inQdrop 0
                snmp-server timeouts subagent 1
                snmp-server timeouts pdu stats 1
                snmp-server timeouts threshold 0
                snmp-server packetsize 490
                snmp-server correlator rule rule1
                 timeout 5
                !
                snmp-server correlator ruleset rule1
                !
                snmp-server correlator buffer-size 1024
                snmp-server trap-source GigabitEthernet0/0/0/2
                snmp-server throttle-time 60
                snmp-server community-map cm1 context c1 security-name s1 target-list t1
                snmp-server inform retries 7
                snmp-server overload-control 4 6
                snmp-server ifmib internal cache max-duration 4
                snmp-server mroutemib send-all-vrf
                snmp-server notification-log-mib size 5
                snmp-server notification-log-mib GlobalSize 5
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            hosts=[
                                dict(
                                    community="test1",
                                    host="1.1.1.1",
                                    traps=True,
                                ),
                            ],
                        ),
                    ],
                    users=[
                        dict(
                            Ipv4_acl="test1",
                            Ipv6_acl="test2",
                            group="test2",
                            user="u1",
                            v4_acl="v4acl",
                            version="v1",
                        ),
                    ],
                    timeouts=dict(
                        duplicate=0,
                        inQdrop=0,
                        pdu_stats=1,
                        subagent=1,
                        threshold=0,
                    ),
                    trap=dict(throttle_time=12),
                    targets=[
                        dict(name="test2", vrf="vrf2"),
                        dict(host="1.1.1.2", name="test"),
                    ],
                    ifmib=dict(internal_cache_max_duration=4),
                    inform=dict(retries=7),
                    chassis_id="test2",
                    packetsize=490,
                    queue_length=2,
                    throttle_time=60,
                    trap_source="GigabitEthernet0/0/0/2",
                    trap_timeout=3,
                    context=["c1", "c2"],
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[dict(name="rule1")],
                        rules=[dict(rule_name="rule1", timeout=5)],
                    ),
                    communities=[
                        dict(
                            name="test2",
                            rw=True,
                            systemowner=True,
                            acl_v4="test",
                            acl_v6="test1",
                        ),
                    ],
                    community_maps=[
                        dict(
                            name="cm1",
                            context="c1",
                            target_list="t1",
                            security_name="s1",
                        ),
                    ],
                    drop=dict(report_IPv4="test1", unknown_user=True),
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    groups=[
                        dict(
                            Ipv4_acl="test",
                            Ipv6_acl="test1",
                            context="test3",
                            group="g2",
                            read="test1",
                            version="v1",
                            write="test2",
                        ),
                    ],
                    location="test1",
                    logging_threshold_oid_processing=1,
                    logging_threshold_pdu_processing=1,
                    mib_bulkstat_max_procmem_size=101,
                    mroutemib_send_all_vrf=True,
                    mib_object_lists=["test1"],
                    overload_control=dict(
                        overload_drop_time=4,
                        overload_throttle_rate=6,
                    ),
                    mib_schema=[
                        dict(
                            name="mib1",
                            object_list="test1",
                            poll_interval=1,
                        ),
                    ],
                    notification_log_mib=dict(GlobalSize=5, size=5),
                    mib_bulkstat_transfer_ids=[
                        dict(
                            buffer_size=1024,
                            enable=True,
                            format_schemaASCI=True,
                            name="test2",
                            retain=1,
                            retry=1,
                            schema="test2",
                        ),
                    ],
                    traps=dict(
                        diameter=dict(
                            peerdown=True,
                            peerup=True,
                            permanentfail=True,
                            protocolerror=True,
                            transientfail=True,
                        ),
                        entity=True,
                        entity_redundancy=dict(
                            all=True,
                            status=True,
                            switchover=True,
                        ),
                        entity_state=dict(operstatus=True, switchover=True),
                        flash=dict(insertion=True, removal=True),
                        hsrp=True,
                        ipsla=True,
                        ipsec=dict(start=True, stop=True),
                        bridgemib=True,
                        bulkstat_collection=True,
                        cisco_entity_ext=True,
                        config=True,
                        copy_complete=True,
                        addrpool=dict(high=True, low=True),
                        bfd=True,
                        bgp=dict(cbgp2=True),
                        l2tun=dict(
                            sessions=True,
                            tunnel_down=True,
                            tunnel_up=True,
                        ),
                        l2vpn=dict(all=True, vc_down=True, vc_up=True),
                        msdp_peer_state_change=True,
                        ospf=dict(
                            errors=dict(
                                authentication_failure=True,
                                bad_packet=True,
                                config_error=True,
                                virt_authentication_failure=True,
                                virt_bad_packet=True,
                                virt_config_error=True,
                            ),
                            lsa=dict(lsa_maxage=True, lsa_originate=True),
                            retransmit=dict(packets=True, virt_packets=True),
                            state_change=dict(
                                if_state_change=True,
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                            ),
                        ),
                        ospfv3=dict(
                            errors=dict(
                                bad_packet=True,
                                config_error=True,
                                virt_config_error=True,
                            ),
                            state_change=dict(
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                                restart_helper_status_change=True,
                                restart_status_change=True,
                                restart_virtual_helper_status_change=True,
                            ),
                        ),
                        pim=dict(
                            interface_state_change=True,
                            invalid_message_received=True,
                            neighbor_change=True,
                            rp_mapping_change=True,
                        ),
                        power=True,
                        rf=True,
                        rsvp=dict(all=True, lost_flow=True, new_flow=True),
                        selective_vrf_download_role_change=True,
                        sensor=True,
                        snmp=dict(
                            authentication=True,
                            coldstart=True,
                            linkdown=True,
                            linkup=True,
                            warmstart=True,
                        ),
                        subscriber=dict(
                            session_agg_access_interface=True,
                            session_agg_node=True,
                        ),
                        syslog=True,
                        system=True,
                        vpls=dict(
                            all=True,
                            full_clear=True,
                            full_raise=True,
                            status=True,
                        ),
                        vrrp_events=True,
                    ),
                ),
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_snmp_server_overridden(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                snmp-server vrf vrf1
                 host 1.1.1.1 traps test1
                !
                snmp-server drop report acl IPv4 test1
                snmp-server drop unknown-user
                snmp-server ipv4 dscp af11
                snmp-server ipv6 precedence routine
                snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2 v4acl
                snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
                snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1
                snmp-server queue-length 2
                snmp-server trap-timeout 3
                snmp-server trap throttle-time 12
                snmp-server traps rf
                snmp-server traps bfd
                snmp-server traps bgp cbgp2
                snmp-server traps pim neighbor-change
                snmp-server traps pim invalid-message-received
                snmp-server traps pim rp-mapping-change
                snmp-server traps pim interface-state-change
                snmp-server traps copy-complete
                snmp-server traps hsrp
                snmp-server traps ipsla
                snmp-server traps msdp peer-state-change
                snmp-server traps snmp linkup
                snmp-server traps snmp linkdown
                snmp-server traps snmp coldstart
                snmp-server traps snmp warmstart
                snmp-server traps snmp authentication
                snmp-server traps vrrp events
                snmp-server traps flash removal
                snmp-server traps flash insertion
                snmp-server traps ipsec tunnel stop
                snmp-server traps ipsec tunnel start
                snmp-server traps power
                snmp-server traps config
                snmp-server traps entity
                snmp-server traps sensor
                snmp-server traps selective-vrf-download role-change
                snmp-server traps syslog
                snmp-server traps system
                snmp-server traps ospf lsa lsa-maxage
                snmp-server traps ospf lsa lsa-originate
                snmp-server traps ospf errors bad-packet
                snmp-server traps ospf errors authentication-failure
                snmp-server traps ospf errors config-error
                snmp-server traps ospf errors virt-bad-packet
                snmp-server traps ospf errors virt-authentication-failure
                snmp-server traps ospf errors virt-config-error
                snmp-server traps ospf retransmit packets
                snmp-server traps ospf retransmit virt-packets
                snmp-server traps ospf state-change if-state-change
                snmp-server traps ospf state-change neighbor-state-change
                snmp-server traps ospf state-change virtif-state-change
                snmp-server traps ospf state-change virtneighbor-state-change
                snmp-server traps rsvp all
                snmp-server traps rsvp new-flow
                snmp-server traps rsvp lost-flow
                snmp-server traps l2tun sessions
                snmp-server traps l2tun tunnel-up
                snmp-server traps l2tun tunnel-down
                snmp-server traps vpls all
                snmp-server traps vpls status
                snmp-server traps vpls full-clear
                snmp-server traps vpls full-raise
                snmp-server traps bulkstat collection
                snmp-server traps diameter peerup
                snmp-server traps diameter peerdown
                snmp-server traps diameter protocolerror
                snmp-server traps diameter permanentfail
                snmp-server traps diameter transientfail
                snmp-server traps l2vpn all
                snmp-server traps l2vpn vc-up
                snmp-server traps l2vpn vc-down
                snmp-server traps bridgemib
                snmp-server traps ospfv3 errors bad-packet
                snmp-server traps ospfv3 errors config-error
                snmp-server traps ospfv3 errors virt-config-error
                snmp-server traps ospfv3 state-change neighbor-state-change
                snmp-server traps ospfv3 state-change virtif-state-change
                snmp-server traps ospfv3 state-change virtneighbor-state-change
                snmp-server traps ospfv3 state-change restart-status-change
                snmp-server traps ospfv3 state-change restart-helper-status-change
                snmp-server traps ospfv3 state-change restart-virtual-helper-status-change
                snmp-server traps subscriber session-agg node
                snmp-server traps subscriber session-agg access-interface
                snmp-server traps addrpool low
                snmp-server traps addrpool high
                snmp-server traps cisco-entity-ext
                snmp-server traps entity-state operstatus
                snmp-server traps entity-state switchover
                snmp-server traps entity-redundancy all
                snmp-server traps entity-redundancy status
                snmp-server traps entity-redundancy switchover
                snmp-server chassis-id test2
                snmp-server contact t1
                snmp-server location test1
                snmp-server target list test host 1.1.1.2
                snmp-server target list test2 vrf vrf2
                snmp-server context c1
                snmp-server context c2
                snmp-server logging threshold oid-processing 1
                snmp-server logging threshold pdu-processing 1
                snmp-server mib bulkstat max-procmem-size 101
                snmp-server mib bulkstat object-list test1
                !
                snmp-server mib bulkstat schema mib1
                 object-list test1
                 poll-interval 1
                !
                snmp-server mib bulkstat transfer-id test2
                 retry 1
                 buffer-size 1024
                 enable
                 format schemaASCII
                 retain 1
                 schema test2
                !
                snmp-server timeouts duplicate 0
                snmp-server timeouts inQdrop 0
                snmp-server timeouts subagent 1
                snmp-server timeouts pdu stats 1
                snmp-server timeouts threshold 0
                snmp-server packetsize 490
                snmp-server correlator rule rule1
                 timeout 5
                !
                snmp-server correlator ruleset rule1
                !
                snmp-server correlator buffer-size 1024
                snmp-server trap-source GigabitEthernet0/0/0/2
                snmp-server throttle-time 60
                snmp-server community-map cm1 context c1 security-name s1 target-list t1
                snmp-server inform retries 7
                snmp-server overload-control 4 6
                snmp-server ifmib internal cache max-duration 4
                snmp-server mroutemib send-all-vrf
                snmp-server notification-log-mib size 5
                snmp-server notification-log-mib GlobalSize 5
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    vrfs=[
                        dict(
                            vrf="vrf2",
                            hosts=[
                                dict(
                                    community="test1",
                                    host="1.1.1.1",
                                    traps=True,
                                ),
                            ],
                        ),
                    ],
                    users=[
                        dict(
                            Ipv4_acl="test1",
                            Ipv6_acl="test2",
                            group="test2",
                            user="u1",
                            v4_acl="v4acl",
                        ),
                    ],
                    timeouts=dict(
                        duplicate=0,
                        inQdrop=0,
                        pdu_stats=1,
                        subagent=1,
                        threshold=0,
                    ),
                    trap=dict(throttle_time=12),
                    targets=[
                        dict(name="test2", vrf="vrf2"),
                        dict(host="1.1.1.2", name="test"),
                    ],
                    ifmib=dict(internal_cache_max_duration=4),
                    inform=dict(retries=7),
                    chassis_id="test2",
                    packetsize=490,
                    queue_length=2,
                    throttle_time=60,
                    trap_source="GigabitEthernet0/0/0/2",
                    trap_timeout=3,
                    context=["c1", "c2"],
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[dict(name="rule1")],
                        rules=[dict(rule_name="rule1", timeout=5)],
                    ),
                    communities=[
                        dict(
                            name="test2",
                            ro=True,
                            sdrowner=True,
                            acl_v4="test",
                            acl_v6="test1",
                        ),
                    ],
                    community_maps=[
                        dict(
                            name="cm1",
                            context="c1",
                            target_list="t1",
                            security_name="s1",
                        ),
                    ],
                    drop=dict(report_IPv4="test1", unknown_user=True),
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    groups=[
                        dict(
                            Ipv4_acl="test",
                            Ipv6_acl="test1",
                            context="test3",
                            group="g2",
                            read="test1",
                            version="v1",
                            write="test2",
                        ),
                    ],
                    location="test",
                    logging_threshold_oid_processing=2,
                    logging_threshold_pdu_processing=1,
                    mib_bulkstat_max_procmem_size=101,
                    mroutemib_send_all_vrf=True,
                    mib_object_lists=["test1"],
                    overload_control=dict(
                        overload_drop_time=4,
                        overload_throttle_rate=6,
                    ),
                    mib_schema=[
                        dict(
                            name="mib1",
                            object_list="test1",
                            poll_interval=1,
                        ),
                    ],
                    notification_log_mib=dict(GlobalSize=5, size=5),
                    mib_bulkstat_transfer_ids=[
                        dict(
                            buffer_size=1024,
                            enable=True,
                            format_schemaASCI=True,
                            name="test2",
                            retain=1,
                            retry=1,
                            schema="test2",
                        ),
                    ],
                    traps=dict(
                        diameter=dict(
                            peerdown=True,
                            peerup=True,
                            permanentfail=True,
                            protocolerror=True,
                            transientfail=True,
                        ),
                        entity=True,
                        entity_redundancy=dict(
                            all=True,
                            status=True,
                            switchover=True,
                        ),
                        entity_state=dict(operstatus=True, switchover=True),
                        flash=dict(insertion=True, removal=True),
                        ipsec=dict(start=True, stop=True),
                        bridgemib=True,
                        bulkstat_collection=True,
                        cisco_entity_ext=True,
                        config=True,
                        copy_complete=True,
                        addrpool=dict(high=True, low=True),
                        bfd=True,
                        bgp=dict(cbgp2=True),
                        l2tun=dict(
                            sessions=True,
                            tunnel_down=True,
                            tunnel_up=True,
                        ),
                        l2vpn=dict(all=True, vc_down=True, vc_up=True),
                        msdp_peer_state_change=True,
                        ospf=dict(
                            errors=dict(
                                authentication_failure=True,
                                bad_packet=True,
                                config_error=True,
                                virt_authentication_failure=True,
                                virt_bad_packet=True,
                                virt_config_error=True,
                            ),
                            lsa=dict(lsa_maxage=True, lsa_originate=True),
                            retransmit=dict(packets=True, virt_packets=True),
                            state_change=dict(
                                if_state_change=True,
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                            ),
                        ),
                        ospfv3=dict(
                            errors=dict(
                                bad_packet=True,
                                config_error=True,
                                virt_config_error=True,
                            ),
                        ),
                        pim=dict(
                            interface_state_change=True,
                            invalid_message_received=True,
                            neighbor_change=True,
                            rp_mapping_change=True,
                        ),
                        power=True,
                        rf=True,
                        rsvp=dict(all=True, lost_flow=True, new_flow=True),
                        selective_vrf_download_role_change=True,
                        sensor=True,
                        snmp=dict(
                            authentication=True,
                            coldstart=True,
                            linkdown=True,
                            linkup=True,
                            warmstart=True,
                        ),
                        subscriber=dict(
                            session_agg_access_interface=True,
                            session_agg_node=True,
                        ),
                        syslog=True,
                        system=True,
                        vpls=dict(
                            all=True,
                            full_clear=True,
                            full_raise=True,
                            status=True,
                        ),
                        vrrp_events=True,
                    ),
                ),
                state="overridden",
            ),
        )
        commands = [
            "no snmp-server contact t1",
            "no snmp-server traps hsrp",
            "no snmp-server traps ipsla",
            "no snmp-server traps ospfv3 state-change neighbor-state-change",
            "no snmp-server traps ospfv3 state-change virtif-state-change",
            "no snmp-server traps ospfv3 state-change virtneighbor-state-change",
            "no snmp-server traps ospfv3 state-change restart-status-change",
            "no snmp-server traps ospfv3 state-change restart-helper-status-change",
            "no snmp-server traps ospfv3 state-change restart-virtual-helper-status-change",
            "no snmp-server vrf vrf1",
            "snmp-server location test",
            "snmp-server logging threshold oid-processing 2",
            "snmp-server user u1 test2  IPv4 test1 IPv6 test2 v4acl",
            "snmp-server vrf vrf2",
            "host 1.1.1.1 traps test1",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_snmp_server_overridden_idempotent(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                snmp-server vrf vrf1
                 host 1.1.1.1 traps test1
                !
                snmp-server drop report acl IPv4 test1
                snmp-server drop unknown-user
                snmp-server ipv4 dscp af11
                snmp-server ipv6 precedence routine
                snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2 v4acl
                snmp-server community test2 RW SystemOwner IPv4 test IPv6 test1
                snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1
                snmp-server queue-length 2
                snmp-server trap-timeout 3
                snmp-server trap throttle-time 12
                snmp-server traps rf
                snmp-server traps bfd
                snmp-server traps bgp cbgp2
                snmp-server traps pim neighbor-change
                snmp-server traps pim invalid-message-received
                snmp-server traps pim rp-mapping-change
                snmp-server traps pim interface-state-change
                snmp-server traps copy-complete
                snmp-server traps hsrp
                snmp-server traps ipsla
                snmp-server traps msdp peer-state-change
                snmp-server traps snmp linkup
                snmp-server traps snmp linkdown
                snmp-server traps snmp coldstart
                snmp-server traps snmp warmstart
                snmp-server traps snmp authentication
                snmp-server traps vrrp events
                snmp-server traps flash removal
                snmp-server traps flash insertion
                snmp-server traps ipsec tunnel stop
                snmp-server traps ipsec tunnel start
                snmp-server traps power
                snmp-server traps config
                snmp-server traps entity
                snmp-server traps sensor
                snmp-server traps selective-vrf-download role-change
                snmp-server traps syslog
                snmp-server traps system
                snmp-server traps ospf lsa lsa-maxage
                snmp-server traps ospf lsa lsa-originate
                snmp-server traps ospf errors bad-packet
                snmp-server traps ospf errors authentication-failure
                snmp-server traps ospf errors config-error
                snmp-server traps ospf errors virt-bad-packet
                snmp-server traps ospf errors virt-authentication-failure
                snmp-server traps ospf errors virt-config-error
                snmp-server traps ospf retransmit packets
                snmp-server traps ospf retransmit virt-packets
                snmp-server traps ospf state-change if-state-change
                snmp-server traps ospf state-change neighbor-state-change
                snmp-server traps ospf state-change virtif-state-change
                snmp-server traps ospf state-change virtneighbor-state-change
                snmp-server traps rsvp all
                snmp-server traps rsvp new-flow
                snmp-server traps rsvp lost-flow
                snmp-server traps l2tun sessions
                snmp-server traps l2tun tunnel-up
                snmp-server traps l2tun tunnel-down
                snmp-server traps vpls all
                snmp-server traps vpls status
                snmp-server traps vpls full-clear
                snmp-server traps vpls full-raise
                snmp-server traps bulkstat collection
                snmp-server traps diameter peerup
                snmp-server traps diameter peerdown
                snmp-server traps diameter protocolerror
                snmp-server traps diameter permanentfail
                snmp-server traps diameter transientfail
                snmp-server traps l2vpn all
                snmp-server traps l2vpn vc-up
                snmp-server traps l2vpn vc-down
                snmp-server traps bridgemib
                snmp-server traps ospfv3 errors bad-packet
                snmp-server traps ospfv3 errors config-error
                snmp-server traps ospfv3 errors virt-config-error
                snmp-server traps ospfv3 state-change neighbor-state-change
                snmp-server traps ospfv3 state-change virtif-state-change
                snmp-server traps ospfv3 state-change virtneighbor-state-change
                snmp-server traps ospfv3 state-change restart-status-change
                snmp-server traps ospfv3 state-change restart-helper-status-change
                snmp-server traps ospfv3 state-change restart-virtual-helper-status-change
                snmp-server traps subscriber session-agg node
                snmp-server traps subscriber session-agg access-interface
                snmp-server traps addrpool low
                snmp-server traps addrpool high
                snmp-server traps cisco-entity-ext
                snmp-server traps entity-state operstatus
                snmp-server traps entity-state switchover
                snmp-server traps entity-redundancy all
                snmp-server traps entity-redundancy status
                snmp-server traps entity-redundancy switchover
                snmp-server chassis-id test2
                snmp-server location test1
                snmp-server target list test host 1.1.1.2
                snmp-server target list test2 vrf vrf2
                snmp-server context c1
                snmp-server context c2
                snmp-server logging threshold oid-processing 1
                snmp-server logging threshold pdu-processing 1
                snmp-server mib bulkstat max-procmem-size 101
                snmp-server mib bulkstat object-list test1
                !
                snmp-server mib bulkstat schema mib1
                 object-list test1
                 poll-interval 1
                !
                snmp-server mib bulkstat transfer-id test2
                 retry 1
                 buffer-size 1024
                 enable
                 format schemaASCII
                 retain 1
                 schema test2
                !
                snmp-server timeouts duplicate 0
                snmp-server timeouts inQdrop 0
                snmp-server timeouts subagent 1
                snmp-server timeouts pdu stats 1
                snmp-server timeouts threshold 0
                snmp-server packetsize 490
                snmp-server correlator rule rule1
                 timeout 5
                !
                snmp-server correlator ruleset rule1
                !
                snmp-server correlator buffer-size 1024
                snmp-server trap-source GigabitEthernet0/0/0/2
                snmp-server throttle-time 60
                snmp-server community-map cm1 context c1 security-name s1 target-list t1
                snmp-server inform retries 7
                snmp-server overload-control 4 6
                snmp-server ifmib internal cache max-duration 4
                snmp-server mroutemib send-all-vrf
                snmp-server notification-log-mib size 5
                snmp-server notification-log-mib GlobalSize 5
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            hosts=[
                                dict(
                                    community="test1",
                                    host="1.1.1.1",
                                    traps=True,
                                ),
                            ],
                        ),
                    ],
                    users=[
                        dict(
                            Ipv4_acl="test1",
                            Ipv6_acl="test2",
                            group="test2",
                            user="u1",
                            v4_acl="v4acl",
                            version="v1",
                        ),
                    ],
                    timeouts=dict(
                        duplicate=0,
                        inQdrop=0,
                        pdu_stats=1,
                        subagent=1,
                        threshold=0,
                    ),
                    trap=dict(throttle_time=12),
                    targets=[
                        dict(name="test2", vrf="vrf2"),
                        dict(host="1.1.1.2", name="test"),
                    ],
                    ifmib=dict(internal_cache_max_duration=4),
                    inform=dict(retries=7),
                    chassis_id="test2",
                    packetsize=490,
                    queue_length=2,
                    throttle_time=60,
                    trap_source="GigabitEthernet0/0/0/2",
                    trap_timeout=3,
                    context=["c1", "c2"],
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[dict(name="rule1")],
                        rules=[dict(rule_name="rule1", timeout=5)],
                    ),
                    communities=[
                        dict(
                            name="test2",
                            rw=True,
                            systemowner=True,
                            acl_v4="test",
                            acl_v6="test1",
                        ),
                    ],
                    community_maps=[
                        dict(
                            name="cm1",
                            context="c1",
                            target_list="t1",
                            security_name="s1",
                        ),
                    ],
                    drop=dict(report_IPv4="test1", unknown_user=True),
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    groups=[
                        dict(
                            Ipv4_acl="test",
                            Ipv6_acl="test1",
                            context="test3",
                            group="g2",
                            read="test1",
                            version="v1",
                            write="test2",
                        ),
                    ],
                    location="test1",
                    logging_threshold_oid_processing=1,
                    logging_threshold_pdu_processing=1,
                    mib_bulkstat_max_procmem_size=101,
                    mroutemib_send_all_vrf=True,
                    mib_object_lists=["test1"],
                    overload_control=dict(
                        overload_drop_time=4,
                        overload_throttle_rate=6,
                    ),
                    mib_schema=[
                        dict(
                            name="mib1",
                            object_list="test1",
                            poll_interval=1,
                        ),
                    ],
                    notification_log_mib=dict(GlobalSize=5, size=5),
                    mib_bulkstat_transfer_ids=[
                        dict(
                            buffer_size=1024,
                            enable=True,
                            format_schemaASCI=True,
                            name="test2",
                            retain=1,
                            retry=1,
                            schema="test2",
                        ),
                    ],
                    traps=dict(
                        diameter=dict(
                            peerdown=True,
                            peerup=True,
                            permanentfail=True,
                            protocolerror=True,
                            transientfail=True,
                        ),
                        entity=True,
                        entity_redundancy=dict(
                            all=True,
                            status=True,
                            switchover=True,
                        ),
                        entity_state=dict(operstatus=True, switchover=True),
                        flash=dict(insertion=True, removal=True),
                        hsrp=True,
                        ipsla=True,
                        ipsec=dict(start=True, stop=True),
                        bridgemib=True,
                        bulkstat_collection=True,
                        cisco_entity_ext=True,
                        config=True,
                        copy_complete=True,
                        addrpool=dict(high=True, low=True),
                        bfd=True,
                        bgp=dict(cbgp2=True),
                        l2tun=dict(
                            sessions=True,
                            tunnel_down=True,
                            tunnel_up=True,
                        ),
                        l2vpn=dict(all=True, vc_down=True, vc_up=True),
                        msdp_peer_state_change=True,
                        ospf=dict(
                            errors=dict(
                                authentication_failure=True,
                                bad_packet=True,
                                config_error=True,
                                virt_authentication_failure=True,
                                virt_bad_packet=True,
                                virt_config_error=True,
                            ),
                            lsa=dict(lsa_maxage=True, lsa_originate=True),
                            retransmit=dict(packets=True, virt_packets=True),
                            state_change=dict(
                                if_state_change=True,
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                            ),
                        ),
                        ospfv3=dict(
                            errors=dict(
                                bad_packet=True,
                                config_error=True,
                                virt_config_error=True,
                            ),
                            state_change=dict(
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                                restart_helper_status_change=True,
                                restart_status_change=True,
                                restart_virtual_helper_status_change=True,
                            ),
                        ),
                        pim=dict(
                            interface_state_change=True,
                            invalid_message_received=True,
                            neighbor_change=True,
                            rp_mapping_change=True,
                        ),
                        power=True,
                        rf=True,
                        rsvp=dict(all=True, lost_flow=True, new_flow=True),
                        selective_vrf_download_role_change=True,
                        sensor=True,
                        snmp=dict(
                            authentication=True,
                            coldstart=True,
                            linkdown=True,
                            linkup=True,
                            warmstart=True,
                        ),
                        subscriber=dict(
                            session_agg_access_interface=True,
                            session_agg_node=True,
                        ),
                        syslog=True,
                        system=True,
                        vpls=dict(
                            all=True,
                            full_clear=True,
                            full_raise=True,
                            status=True,
                        ),
                        vrrp_events=True,
                    ),
                ),
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_snmp_server_rendered(self):
        self.maxDiff = None
        set_module_args(
            dict(
                config=dict(
                    vrfs=[
                        dict(
                            vrf="vrf1",
                            hosts=[
                                dict(
                                    community="test1",
                                    host="1.1.1.1",
                                    traps=True,
                                ),
                            ],
                        ),
                    ],
                    users=[
                        dict(
                            Ipv4_acl="test1",
                            Ipv6_acl="test2",
                            group="test2",
                            user="u1",
                            v4_acl="v4acl",
                        ),
                    ],
                    timeouts=dict(
                        duplicate=0,
                        inQdrop=0,
                        pdu_stats=1,
                        subagent=1,
                        threshold=0,
                    ),
                    trap=dict(throttle_time=12),
                    targets=[
                        dict(name="test2", vrf="vrf2"),
                        dict(host="1.1.1.2", name="test"),
                    ],
                    ifmib=dict(internal_cache_max_duration=4),
                    inform=dict(retries=7),
                    chassis_id="test2",
                    packetsize=490,
                    queue_length=2,
                    throttle_time=60,
                    trap_source="GigabitEthernet0/0/0/2",
                    trap_timeout=3,
                    context=["c1", "c2"],
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[dict(name="rule1")],
                        rules=[dict(rule_name="rule1", timeout=5)],
                    ),
                    communities=[
                        dict(
                            name="test2",
                            ro=True,
                            sdrowner=True,
                            acl_v4="test",
                            acl_v6="test1",
                        ),
                    ],
                    community_maps=[
                        dict(
                            name="cm1",
                            context="c1",
                            target_list="t1",
                            security_name="s1",
                        ),
                    ],
                    drop=dict(report_IPv4="test1", unknown_user=True),
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    groups=[
                        dict(
                            Ipv4_acl="test",
                            Ipv6_acl="test1",
                            context="test3",
                            group="g2",
                            read="test1",
                            version="v1",
                            write="test2",
                        ),
                    ],
                    interfaces=[dict(name=" GigabitEthernet0/0/0/2")],
                    location="test1",
                    logging_threshold_oid_processing=1,
                    logging_threshold_pdu_processing=1,
                    mib_bulkstat_max_procmem_size=101,
                    mroutemib_send_all_vrf=True,
                    mib_object_lists=["test1"],
                    overload_control=dict(
                        overload_drop_time=4,
                        overload_throttle_rate=6,
                    ),
                    mib_schema=[
                        dict(
                            name="mib1",
                            object_list="test1",
                            poll_interval=1,
                        ),
                    ],
                    notification_log_mib=dict(GlobalSize=5, size=5),
                    mib_bulkstat_transfer_ids=[
                        dict(
                            buffer_size=1024,
                            enable=True,
                            format_schemaASCI=True,
                            name="test2",
                            retain=1,
                            retry=1,
                            schema="test2",
                        ),
                    ],
                    traps=dict(
                        diameter=dict(
                            peerdown=True,
                            peerup=True,
                            permanentfail=True,
                            protocolerror=True,
                            transientfail=True,
                        ),
                        entity=True,
                        entity_redundancy=dict(
                            all=True,
                            status=True,
                            switchover=True,
                        ),
                        entity_state=dict(operstatus=True, switchover=True),
                        flash=dict(insertion=True, removal=True),
                        hsrp=True,
                        ipsla=True,
                        ipsec=dict(start=True, stop=True),
                        bridgemib=True,
                        bulkstat_collection=True,
                        cisco_entity_ext=True,
                        config=True,
                        copy_complete=True,
                        addrpool=dict(high=True, low=True),
                        bfd=True,
                        bgp=dict(cbgp2=True),
                        l2tun=dict(
                            sessions=True,
                            tunnel_down=True,
                            tunnel_up=True,
                        ),
                        l2vpn=dict(all=True, vc_down=True, vc_up=True),
                        msdp_peer_state_change=True,
                        ospf=dict(
                            errors=dict(
                                authentication_failure=True,
                                bad_packet=True,
                                config_error=True,
                                virt_authentication_failure=True,
                                virt_bad_packet=True,
                                virt_config_error=True,
                            ),
                            lsa=dict(lsa_maxage=True, lsa_originate=True),
                            retransmit=dict(packets=True, virt_packets=True),
                            state_change=dict(
                                if_state_change=True,
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                            ),
                        ),
                        ospfv3=dict(
                            errors=dict(
                                bad_packet=True,
                                config_error=True,
                                virt_config_error=True,
                            ),
                            state_change=dict(
                                neighbor_state_change=True,
                                virtif_state_change=True,
                                virtneighbor_state_change=True,
                                restart_helper_status_change=True,
                                restart_status_change=True,
                                restart_virtual_helper_status_change=True,
                            ),
                        ),
                        pim=dict(
                            interface_state_change=True,
                            invalid_message_received=True,
                            neighbor_change=True,
                            rp_mapping_change=True,
                        ),
                        power=True,
                        rf=True,
                        rsvp=dict(all=True, lost_flow=True, new_flow=True),
                        selective_vrf_download_role_change=True,
                        sensor=True,
                        snmp=dict(
                            authentication=True,
                            coldstart=True,
                            linkdown=True,
                            linkup=True,
                            warmstart=True,
                        ),
                        subscriber=dict(
                            session_agg_access_interface=True,
                            session_agg_node=True,
                        ),
                        syslog=True,
                        system=True,
                        vpls=dict(
                            all=True,
                            full_clear=True,
                            full_raise=True,
                            status=True,
                        ),
                        vrrp_events=True,
                    ),
                ),
                state="rendered",
            ),
        )
        commands = [
            "snmp-server chassis-id test2",
            "snmp-server correlator buffer-size 1024",
            "snmp-server ipv4 dscp af11",
            "snmp-server ipv6 precedence routine",
            "snmp-server location test1",
            "snmp-server logging threshold oid-processing 1",
            "snmp-server logging threshold pdu-processing 1",
            "snmp-server mib bulkstat max-procmem-size 101",
            "snmp-server mroutemib send-all-vrf",
            "snmp-server overload-control 4 6",
            "snmp-server packetsize 490",
            "snmp-server queue-length 2",
            "snmp-server throttle-time 60",
            "snmp-server trap-source GigabitEthernet0/0/0/2",
            "snmp-server trap-timeout 3",
            "snmp-server drop report acl IPv4 test1",
            "snmp-server drop unknown-user",
            "snmp-server ifmib internal cache max-duration 4",
            "snmp-server inform retries 7",
            "snmp-server notification-log-mib size 5",
            "snmp-server notification-log-mib GlobalSize 5",
            "snmp-server trap throttle-time 12",
            "snmp-server timeouts threshold 0",
            "snmp-server timeouts pdu stats 1",
            "snmp-server timeouts subagent 1",
            "snmp-server timeouts inQdrop 0",
            "snmp-server timeouts duplicate 0",
            "snmp-server traps addrpool low",
            "snmp-server traps addrpool high",
            "snmp-server traps bfd",
            "snmp-server traps bgp cbgp2",
            "snmp-server traps bulkstat collection",
            "snmp-server traps bridgemib",
            "snmp-server traps copy-complete",
            "snmp-server traps cisco-entity-ext",
            "snmp-server traps config",
            "snmp-server traps diameter peerdown",
            "snmp-server traps diameter peerup",
            "snmp-server traps diameter protocolerror",
            "snmp-server traps diameter permanentfail",
            "snmp-server traps diameter transientfail",
            "snmp-server traps entity",
            "snmp-server traps entity-redundancy all",
            "snmp-server traps entity-redundancy status",
            "snmp-server traps entity-redundancy switchover",
            "snmp-server traps entity-state operstatus",
            "snmp-server traps entity-state switchover",
            "snmp-server traps flash removal",
            "snmp-server traps flash insertion",
            "snmp-server traps hsrp",
            "snmp-server traps ipsla",
            "snmp-server traps ipsec tunnel start",
            "snmp-server traps ipsec tunnel stop",
            "snmp-server traps l2tun sessions",
            "snmp-server traps l2tun tunnel-up",
            "snmp-server traps l2tun tunnel-down",
            "snmp-server traps l2vpn all",
            "snmp-server traps l2vpn vc-up",
            "snmp-server traps l2vpn vc-down",
            "snmp-server traps msdp peer-state-change",
            "snmp-server traps ospf retransmit virt-packets",
            "snmp-server traps ospf retransmit packets",
            "snmp-server traps ospf lsa lsa-originate",
            "snmp-server traps ospf lsa lsa-maxage",
            "snmp-server traps ospf errors bad-packet",
            "snmp-server traps ospf errors authentication-failure",
            "snmp-server traps ospf errors config-error",
            "snmp-server traps ospf errors virt-bad-packet",
            "snmp-server traps ospf errors virt-authentication-failure",
            "snmp-server traps ospf errors virt-config-error",
            "snmp-server traps ospf state-change if-state-change",
            "snmp-server traps ospf state-change neighbor-state-change",
            "snmp-server traps ospf state-change virtif-state-change",
            "snmp-server traps ospf state-change virtneighbor-state-change",
            "snmp-server traps ospfv3 errors bad-packet",
            "snmp-server traps ospfv3 errors config-error",
            "snmp-server traps ospfv3 errors virt-config-error",
            "snmp-server traps ospfv3 state-change neighbor-state-change",
            "snmp-server traps ospfv3 state-change virtif-state-change",
            "snmp-server traps ospfv3 state-change virtneighbor-state-change",
            "snmp-server traps ospfv3 state-change restart-status-change",
            "snmp-server traps ospfv3 state-change restart-helper-status-change",
            "snmp-server traps ospfv3 state-change restart-virtual-helper-status-change",
            "snmp-server traps power",
            "snmp-server traps rf",
            "snmp-server traps pim neighbor-change",
            "snmp-server traps pim invalid-message-received",
            "snmp-server traps pim rp-mapping-change",
            "snmp-server traps pim interface-state-change",
            "snmp-server traps rsvp lost-flow",
            "snmp-server traps rsvp new-flow",
            "snmp-server traps rsvp all",
            "snmp-server traps selective-vrf-download role-change",
            "snmp-server traps sensor",
            "snmp-server traps vrrp events",
            "snmp-server traps syslog",
            "snmp-server traps system",
            "snmp-server traps subscriber session-agg access-interface",
            "snmp-server traps subscriber session-agg node",
            "snmp-server traps vpls all",
            "snmp-server traps vpls full-clear",
            "snmp-server traps vpls full-raise",
            "snmp-server traps vpls status",
            "snmp-server traps snmp linkup",
            "snmp-server traps snmp linkdown",
            "snmp-server traps snmp coldstart",
            "snmp-server traps snmp warmstart",
            "snmp-server traps snmp authentication",
            "snmp-server community test2 RO SDROwner IPv4 test IPv6 test1",
            "snmp-server community-map cm1 context c1 security-name s1 target-list t1",
            "snmp-server correlator ruleset rule1",
            "snmp-server correlator rule rule1 timeout 5",
            "snmp-server context c1",
            "snmp-server context c2",
            "snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1",
            "snmp-server interface  GigabitEthernet0/0/0/2",
            "snmp-server mib bulkstat object-list test1",
            "snmp-server mib bulkstat schema mib1 object-list test1",
            "snmp-server mib bulkstat schema mib1 poll-interval 1",
            "snmp-server mib bulkstat transfer-id test2 buffer-size 1024",
            "snmp-server mib bulkstat transfer-id test2 enable",
            "snmp-server mib bulkstat transfer-id test2 format schemaASCII",
            "snmp-server mib bulkstat transfer-id test2 retain 1",
            "snmp-server mib bulkstat transfer-id test2 retry 1",
            "snmp-server mib bulkstat transfer-id test2 schema test2",
            "snmp-server user u1 test2  IPv4 test1 IPv6 test2 v4acl",
            "snmp-server target list test2 vrf vrf2",
            "snmp-server target list test host 1.1.1.2",
            "snmp-server vrf vrf1",
            "host 1.1.1.1 traps test1",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_snmp_server_gathered(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                snmp-server vrf vrf1
                 host 1.1.1.1 traps test1
                !
                snmp-server drop report acl IPv4 test1
                snmp-server drop unknown-user
                snmp-server ipv4 dscp af11
                snmp-server ipv6 precedence routine
                snmp-server user u1 test2 v1 IPv4 test1 IPv6 test2 v4acl
                snmp-server community test2 RO SDROwner IPv4 test IPv6 test1
                snmp-server group g2 v1 read test1 write test2 context test3 IPv4 test IPv6 test1
                snmp-server queue-length 2
                snmp-server trap-timeout 3
                snmp-server trap throttle-time 12
                snmp-server traps rf
                snmp-server traps bfd
                snmp-server traps bgp cbgp2
                snmp-server traps pim neighbor-change
                snmp-server traps pim invalid-message-received
                snmp-server traps pim rp-mapping-change
                snmp-server traps pim interface-state-change
                snmp-server traps copy-complete
                snmp-server traps hsrp
                snmp-server traps ipsla
                snmp-server traps msdp peer-state-change
                snmp-server traps snmp linkup
                snmp-server traps snmp linkdown
                snmp-server traps snmp coldstart
                snmp-server traps snmp warmstart
                snmp-server traps snmp authentication
                snmp-server traps vrrp events
                snmp-server traps flash removal
                snmp-server traps flash insertion
                snmp-server traps ipsec tunnel stop
                snmp-server traps ipsec tunnel start
                snmp-server traps power
                snmp-server traps config
                snmp-server traps entity
                snmp-server traps sensor
                snmp-server traps selective-vrf-download role-change
                snmp-server traps syslog
                snmp-server traps system
                snmp-server traps ospf lsa lsa-maxage
                snmp-server traps ospf lsa lsa-originate
                snmp-server traps ospf errors bad-packet
                snmp-server traps ospf errors authentication-failure
                snmp-server traps ospf errors config-error
                snmp-server traps ospf errors virt-bad-packet
                snmp-server traps ospf errors virt-authentication-failure
                snmp-server traps ospf errors virt-config-error
                snmp-server traps ospf retransmit packets
                snmp-server traps ospf retransmit virt-packets
                snmp-server traps ospf state-change if-state-change
                snmp-server traps ospf state-change neighbor-state-change
                snmp-server traps ospf state-change virtif-state-change
                snmp-server traps ospf state-change virtneighbor-state-change
                snmp-server traps rsvp all
                snmp-server traps rsvp new-flow
                snmp-server traps rsvp lost-flow
                snmp-server traps l2tun sessions
                snmp-server traps l2tun tunnel-up
                snmp-server traps l2tun tunnel-down
                snmp-server traps vpls all
                snmp-server traps vpls status
                snmp-server traps vpls full-clear
                snmp-server traps vpls full-raise
                snmp-server traps bulkstat collection
                snmp-server traps diameter peerup
                snmp-server traps diameter peerdown
                snmp-server traps diameter protocolerror
                snmp-server traps diameter permanentfail
                snmp-server traps diameter transientfail
                snmp-server traps l2vpn all
                snmp-server traps l2vpn vc-up
                snmp-server traps l2vpn vc-down
                snmp-server traps bridgemib
                snmp-server traps ospfv3 errors bad-packet
                snmp-server traps ospfv3 errors config-error
                snmp-server traps ospfv3 errors virt-config-error
                snmp-server traps ospfv3 state-change neighbor-state-change
                snmp-server traps ospfv3 state-change virtif-state-change
                snmp-server traps ospfv3 state-change virtneighbor-state-change
                snmp-server traps ospfv3 state-change restart-status-change
                snmp-server traps ospfv3 state-change restart-helper-status-change
                snmp-server traps ospfv3 state-change restart-virtual-helper-status-change
                snmp-server traps subscriber session-agg node
                snmp-server traps subscriber session-agg access-interface
                snmp-server traps addrpool low
                snmp-server traps addrpool high
                snmp-server traps cisco-entity-ext
                snmp-server traps entity-state operstatus
                snmp-server traps entity-state switchover
                snmp-server traps entity-redundancy all
                snmp-server traps entity-redundancy status
                snmp-server traps entity-redundancy switchover
                snmp-server chassis-id test2
                snmp-server contact t1
                snmp-server location test1
                snmp-server target list test host 1.1.1.2
                snmp-server target list test2 vrf vrf2
                snmp-server context c1
                snmp-server logging threshold oid-processing 1
                snmp-server logging threshold pdu-processing 1
                snmp-server mib bulkstat max-procmem-size 101
                snmp-server mib bulkstat object-list test1
                !
                snmp-server mib bulkstat schema mib1
                 object-list test1
                 poll-interval 1
                !
                snmp-server mib bulkstat transfer-id test2
                 retry 1
                 buffer-size 1024
                 enable
                 format schemaASCII
                 retain 1
                 schema test2
                !
                snmp-server timeouts duplicate 0
                snmp-server timeouts inQdrop 0
                snmp-server timeouts subagent 1
                snmp-server timeouts pdu stats 1
                snmp-server timeouts threshold 0
                snmp-server packetsize 490
                snmp-server correlator rule rule1
                 timeout 5
                !
                snmp-server correlator ruleset rule1
                !
                snmp-server correlator buffer-size 1024
                snmp-server trap-source GigabitEthernet0/0/0/2
                snmp-server throttle-time 60
                snmp-server community-map cm1 context c1 security-name s1 target-list t1
                snmp-server inform retries 7
                snmp-server overload-control 4 6
                snmp-server ifmib internal cache max-duration 4
                snmp-server mroutemib send-all-vrf
                snmp-server notification-log-mib size 5
                snmp-server notification-log-mib GlobalSize 5
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="gathered"))
        gathered = {
            "vrfs": [
                {
                    "vrf": "vrf1",
                    "hosts": [
                        {
                            "host": "1.1.1.1",
                            "traps": True,
                            "community": "test1",
                        },
                    ],
                },
            ],
            "drop": {"report_IPv4": "test1", "unknown_user": True},
            "ipv4": {"dscp": "af11"},
            "ipv6": {"precedence": "routine"},
            "users": [
                {
                    "user": "u1",
                    "group": "test2",
                    "acl_v4": "test1",
                    "acl_v6": "test2",
                    "v4_acl": "v4acl",
                    "version": "v1",
                },
            ],
            "communities": [
                {
                    "name": "test2",
                    "ro": True,
                    "acl_v4": "test",
                    "acl_v6": "test1",
                    "sdrowner": True,
                },
            ],
            "groups": [
                {
                    "group": "g2",
                    "acl_v4": "test",
                    "acl_v6": "test1",
                    "context": "test3",
                    "read": "test1",
                    "write": "test2",
                    "version": "v1",
                },
            ],
            "queue_length": 2,
            "trap_timeout": 3,
            "trap": {"throttle_time": 12},
            "traps": {
                "rf": True,
                "bfd": True,
                "bgp": {"cbgp2": True},
                "pim": {
                    "neighbor_change": True,
                    "invalid_message_received": True,
                    "rp_mapping_change": True,
                    "interface_state_change": True,
                },
                "copy_complete": True,
                "hsrp": True,
                "ipsla": True,
                "msdp_peer_state_change": True,
                "snmp": {
                    "linkup": True,
                    "linkdown": True,
                    "coldstart": True,
                    "warmstart": True,
                    "authentication": True,
                },
                "vrrp_events": True,
                "flash": {"removal": True, "insertion": True},
                "ipsec": {"stop": True, "start": True},
                "power": True,
                "config": True,
                "entity": True,
                "sensor": True,
                "selective_vrf_download_role_change": True,
                "syslog": True,
                "system": True,
                "ospf": {
                    "lsa": {"lsa_maxage": True, "lsa_originate": True},
                    "errors": {
                        "bad_packet": True,
                        "authentication_failure": True,
                        "config_error": True,
                        "virt_bad_packet": True,
                        "virt_authentication_failure": True,
                        "virt_config_error": True,
                    },
                    "retransmit": {"packets": True, "virt_packets": True},
                    "state_change": {
                        "if_state_change": True,
                        "neighbor_state_change": True,
                        "virtif_state_change": True,
                        "virtneighbor_state_change": True,
                    },
                },
                "rsvp": {"all": True, "new_flow": True, "lost_flow": True},
                "l2tun": {
                    "sessions": True,
                    "tunnel_up": True,
                    "tunnel_down": True,
                },
                "vpls": {
                    "all": True,
                    "status": True,
                    "full_clear": True,
                    "full_raise": True,
                },
                "bulkstat_collection": True,
                "diameter": {
                    "peerup": True,
                    "peerdown": True,
                    "protocolerror": True,
                    "permanentfail": True,
                    "transientfail": True,
                },
                "l2vpn": {"all": True, "vc_up": True, "vc_down": True},
                "bridgemib": True,
                "ospfv3": {
                    "errors": {
                        "bad_packet": True,
                        "config_error": True,
                        "virt_config_error": True,
                    },
                    "state_change": {
                        "neighbor_state_change": True,
                        "virtif_state_change": True,
                        "virtneighbor_state_change": True,
                        "restart_status_change": True,
                        "restart_helper_status_change": True,
                        "restart_virtual_helper_status_change": True,
                    },
                },
                "subscriber": {
                    "session_agg_node": True,
                    "session_agg_access_interface": True,
                },
                "addrpool": {"low": True, "high": True},
                "cisco_entity_ext": True,
                "entity_state": {"operstatus": True, "switchover": True},
                "entity_redundancy": {
                    "all": True,
                    "status": True,
                    "switchover": True,
                },
            },
            "chassis_id": "test2",
            "contact": "t1",
            "location": "test1",
            "targets": [
                {"name": "test", "host": "1.1.1.2"},
                {"name": "test2", "vrf": "vrf2"},
            ],
            "context": ["c1"],
            "logging_threshold_oid_processing": 1,
            "logging_threshold_pdu_processing": 1,
            "mib_bulkstat_max_procmem_size": 101,
            "mib_object_lists": ["test1"],
            "mib_schema": [
                {"name": "mib1", "object_list": "test1", "poll_interval": 1},
            ],
            "mib_bulkstat_transfer_ids": [
                {
                    "name": "test2",
                    "retry": 1,
                    "buffer_size": 1024,
                    "enable": True,
                    "format_schemaASCI": True,
                    "retain": 1,
                    "schema": "test2",
                },
            ],
            "timeouts": {
                "duplicate": 0,
                "inQdrop": 0,
                "subagent": 1,
                "pdu_stats": 1,
                "threshold": 0,
            },
            "packetsize": 490,
            "correlator": {
                "rules": [
                    {"rule_name": "rule1"},
                    {"rule_name": "rule1", "timeout": 5},
                ],
                "rule_sets": [{"name": "rule1"}],
                "buffer_size": 1024,
            },
            "trap_source": "GigabitEthernet0/0/0/2",
            "throttle_time": 60,
            "community_maps": [
                {
                    "name": "cm1",
                    "context": "c1",
                    "security_name": "s1",
                    "target_list": "t1",
                },
            ],
            "inform": {"retries": 7},
            "overload_control": {
                "overload_drop_time": 4,
                "overload_throttle_rate": 6,
            },
            "ifmib": {"internal_cache_max_duration": 4},
            "mroutemib_send_all_vrf": True,
            "notification_log_mib": {"size": 5, "GlobalSize": 5},
        }
        result = self.execute_module(changed=False)
        self.assertEqual(gathered, result["gathered"])

    def test_iosxr_snmp_server_parsed(self):
        self.maxDiff = None
        set_module_args(
            dict(
                running_config="snmp-server vrf test1\n host 1.1.1.1 traps test1\n host 1.1.1.2 traps test1\n "
                "context test2\n!\nsnmp-server drop report acl IPv6 test\nsnmp-server drop unknown-user"
                "\nsnmp-server host 1.1.1.1 traps test udp-port 1\nsnmp-server host 1.1.1.2 informs "
                "version 2c test\nsnmp-server host 1.1.1.3 traps test\nsnmp-server user test1 test2 v1 "
                "IPv4 test1 IPv6 test2 SDROwner\nsnmp-server "
                "community test RO IPv4 test IPv6 test\nsnmp-"
                "server community test1 RO\nsnmp-server group "
                "test v1 notify test1\nsnmp-server group test1 "
                "v1 read test1 write test2 context test3 IPv4 test"
                " IPv6 test1\nsnmp-server group test2 v1 "
                "notify test read test1\nsnmp-server group test4 "
                "v1 notify t1 context test\nsnmp-server queue-length "
                "1\nsnmp-server trap-timeout 1\nsnmp-server trap "
                "throttle-time 10\nsnmp-server traps rf\nsnmp-server traps "
                "bfd\nsnmp-server traps bgp cbgp2\nsnmp-server "
                "traps bgp updown\nsnmp-server traps ntp\nsnmp-server "
                "traps pim neighbor-change\nsnmp-server traps "
                "pim invalid-message-received\nsnmp-server traps pim "
                "rp-mapping-change\nsnmp-server traps pim interface-state-change"
                "\nsnmp-server traps copy-complete\nsnmp-server "
                "traps hsrp\nsnmp-server traps ipsla\nsnmp-server traps msdp "
                "peer-state-change\nsnmp-server traps vrrp events\nsnmp-server "
                "traps flash removal\nsnmp-server traps flash insertion\nsnmp-server "
                "traps ipsec tunnel stop\nsnmp-server traps ipsec tunnel start\nsnmp-server "
                "traps power\nsnmp-server traps config\nsnmp-server traps entity\nsnmp-server "
                "traps isakmp tunnel stop\nsnmp-server traps isakmp tunnel start\nsnmp-server "
                "traps isis database-overload manual-address-drops corrupted-lsp-detected "
                "attempt-to-exceed-max-sequence id-len-mismatch max-area-addresses-mismatch"
                " own-lsp-purge sequence-number-skip authentication-type-failure "
                "authentication-failure version-skew area-mismatch rejected-adjacency "
                "lsp-too-large-to-propagate orig-lsp-buff-size-mismatch protocols-supported-mismatch"
                " adjacency-change lsp-error-detected\nsnmp-server traps sensor\nsnmp-server"
                " traps selective-vrf-download role-change\nsnmp-server traps syslog"
                "\nsnmp-server traps system\nsnmp-server traps ospf lsa lsa-maxage"
                "\nsnmp-server traps ospf lsa lsa-originate\nsnmp-server traps ospf"
                " errors bad-packet\nsnmp-server traps ospf errors authentication-failure"
                "\nsnmp-server traps ospf errors config-error\nsnmp-server traps ospf"
                " errors virt-bad-packet\nsnmp-server traps ospf errors "
                "virt-authentication-failure\nsnmp-server traps ospf errors"
                " virt-config-error\nsnmp-server traps ospf retransmit"
                " packets\nsnmp-server traps ospf retransmit virt-packets"
                "\nsnmp-server traps ospf state-change if-state-change"
                "\nsnmp-server traps ospf state-change neighbor-state-change"
                "\nsnmp-server traps ospf state-change virtif-state-change\n"
                "snmp-server traps ospf state-change virtneighbor-state-change"
                "\nsnmp-server traps rsvp all\nsnmp-server traps rsvp new-flow\n"
                "snmp-server traps rsvp lost-flow\nsnmp-server traps l2tun sessions\n"
                "snmp-server traps l2tun tunnel-up\nsnmp-server traps l2tun tunnel-down"
                "\nsnmp-server traps l2tun pseudowire status\nsnmp-server traps vpls all\n"
                "snmp-server traps vpls status\nsnmp-server traps vpls full-clear\nsnmp-server "
                "traps vpls full-raise\nsnmp-server traps snmp linkup\nsnmp-server traps snmp "
                "linkdown\nsnmp-server traps snmp coldstart\nsnmp-server traps snmp warmstart"
                "\nsnmp-server traps snmp authentication\nsnmp-server traps bulkstat transfer"
                "\nsnmp-server traps bulkstat collection\nsnmp-server traps diameter peerup\
                               nsnmp-server traps diameter peerdown\nsnmp-server traps diameter protocolerror"
                "\nsnmp-server traps diameter permanentfail\nsnmp-server traps diameter transientfail"
                "\nsnmp-server traps l2vpn all\nsnmp-server traps l2vpn cisco\nsnmp-server traps "
                "l2vpn vc-up\nsnmp-server traps l2vpn vc-down\nsnmp-server traps bridgemib\nsnmp-"
                "server traps ospfv3 errors bad-packet\nsnmp-server traps ospfv3 errors config-error"
                "\nsnmp-server traps ospfv3 errors virt-bad-packet\nsnmp-server traps ospfv3 errors "
                "virt-config-error\nsnmp-server traps ospfv3 state-change if-state-change\nsnmp-"
                "server traps ospfv3 state-change neighbor-state-change\nsnmp-server traps ospfv3 "
                "state-change nssa-state-change\nsnmp-server traps ospfv3 state-change "
                "virtif-state-change\nsnmp-server traps ospfv3 state-change "
                "virtneighbor-state-change\nsnmp-server traps ospfv3 state-change "
                "restart-status-change\nsnmp-server traps ospfv3 state-change "
                "restart-helper-status-change\nsnmp-server traps ospfv3 state-change "
                "restart-virtual-helper-status-change\nsnmp-server traps fru-ctrl"
                "\nsnmp-server traps subscriber session-agg node\nsnmp-server traps "
                "subscriber session-agg access-interface\nsnmp-server traps addrpool "
                "low\nsnmp-server traps addrpool high\nsnmp-server traps cisco-entity-ext"
                "\nsnmp-server traps entity-state operstatus\nsnmp-server traps entity-state "
                "switchover\nsnmp-server traps entity-redundancy all"
                "\nsnmp-server traps entity-redundancy "
                "status\nsnmp-server traps entity-redundancy switchover\nsnmp-server chassis-id test2"
                "\nsnmp-server contact test\nsnmp-server location test\nsnmp-server target list test1 "
                "vrf vrf1\nsnmp-server target list test1 host 1.1.1.1\nsnmp-server context test\n"
                "snmp-server context test2\nsnmp-server logging threshold oid-processing 0\n"
                "snmp-server logging threshold pdu-processing 0\nsnmp-server mib bulkstat max-"
                "procmem-size 100\nsnmp-server mib bulkstat object-list test\n!\nsnmp-server mib "
                "bulkstat transfer-id test1\n retry 1\n buffer-size 1024\n enable\n format schemaASCII\n"
                " retain 1\n schema test\n!\nsnmp-server timeouts duplicate 0\nsnmp-server timeouts"
                " inQdrop 0\nsnmp-server timeouts subagent 1\nsnmp-server timeouts pdu stats"
                " 1\nsnmp-server timeouts threshold 0\nsnmp-server packetsize 485\nsnmp-server"
                " correlator buffer-size 1024\nsnmp-server trap-source GigabitEthernet0/0/0/1"
                "\nsnmp-server throttle-time 50\nsnmp-server community-map test context test "
                "security-name test2\nsnmp-server community-map test1 context test security-name "
                "test2\nsnmp-server inform pending 1\nsnmp-server inform retries 1\nsnmp-server "
                "inform timeout 1\nsnmp-server oid-poll-stats\nsnmp-server overload-control 0 0"
                "\nsnmp-server trap authentication vrf disable\nsnmp-server "
                "interface GigabitEthernet0/0/0/0\n notification linkupdown disable\n "
                "index persistence\n!\nsnmp-server ifmib ifalias long\nsnmp-server "
                "ifindex persist\nsnmp-server ifmib internal cache max-duration "
                "0\nsnmp-server ifmib ipsubscriber\nsnmp-server ifmib stats cache"
                "\nsnmp-server trap link ietf\nsnmp-server location test\nsnmp-server"
                " mroutemib send-all-vrf\nsnmp-server notification-log-mib size 1\nsnmp-server "
                "notification-log-mib default\nsnmp-server notification-log-mib disable\nsnmp-server"
                " notification-log-mib GlobalSize 1",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "vrfs": [
                {
                    "vrf": "test1",
                    "context": ["test2"],
                    "hosts": [
                        {
                            "host": "1.1.1.1",
                            "traps": True,
                            "community": "test1",
                        },
                        {
                            "host": "1.1.1.2",
                            "traps": True,
                            "community": "test1",
                        },
                    ],
                },
            ],
            "drop": {"report_IPv6": "test", "unknown_user": True},
            "hosts": [
                {
                    "host": "1.1.1.1",
                    "traps": True,
                    "community": "test",
                    "udp_port": 1,
                },
                {
                    "host": "1.1.1.2",
                    "informs": True,
                    "community": "test",
                    "version": "2c",
                },
                {"host": "1.1.1.3", "traps": True, "community": "test"},
            ],
            "users": [
                {
                    "user": "test1",
                    "group": "test2",
                    "acl_v4": "test1",
                    "acl_v6": "test2",
                    "v4_acl": "SDROwner",
                    "version": "v1",
                },
            ],
            "communities": [
                {
                    "name": "test",
                    "ro": True,
                    "acl_v4": "test",
                    "acl_v6": "test",
                },
                {"name": "test1", "ro": True},
            ],
            "groups": [
                {"group": "test", "notify": "test1", "version": "v1"},
                {
                    "group": "test1",
                    "acl_v4": "test",
                    "acl_v6": "test1",
                    "context": "test3",
                    "read": "test1",
                    "write": "test2",
                    "version": "v1",
                },
                {
                    "group": "test2",
                    "notify": "test",
                    "read": "test1",
                    "version": "v1",
                },
                {
                    "group": "test4",
                    "context": "test",
                    "notify": "t1",
                    "version": "v1",
                },
            ],
            "queue_length": 1,
            "trap_timeout": 1,
            "trap": {
                "throttle_time": 10,
                "authentication_vrf_disable": True,
                "link_ietf": True,
            },
            "traps": {
                "rf": True,
                "bfd": True,
                "bgp": {"cbgp2": True},
                "pim": {
                    "neighbor_change": True,
                    "invalid_message_received": True,
                    "rp_mapping_change": True,
                    "interface_state_change": True,
                },
                "copy_complete": True,
                "hsrp": True,
                "ipsla": True,
                "msdp_peer_state_change": True,
                "vrrp_events": True,
                "flash": {"removal": True, "insertion": True},
                "ipsec": {"stop": True, "start": True},
                "power": True,
                "config": True,
                "entity": True,
                "isakmp": {"stop": True, "start": True},
                "isis": {
                    "id_len_mismatch": True,
                    "database_overload": True,
                    "manual_address_drops": True,
                    "corrupted_lsp_detected": True,
                    "attempt_to_exceed_max_sequence": True,
                    "max_area_addresses_mismatch": True,
                    "own_lsp_purge": True,
                    "sequence_number_skip": True,
                    "authentication_type_failure": True,
                    "authentication_failure": True,
                    "version_skew": True,
                    "area_mismatch": True,
                    "rejected_adjacency": True,
                    "lsp_too_large_to_propagate": True,
                    "orig_lsp_buff_size_mismatch": True,
                    "protocols_supported_mismatch": True,
                    "adjacency_change": True,
                    "lsp_error_detected": True,
                },
                "sensor": True,
                "selective_vrf_download_role_change": True,
                "syslog": True,
                "system": True,
                "ospf": {
                    "lsa": {"lsa_maxage": True, "lsa_originate": True},
                    "errors": {
                        "bad_packet": True,
                        "authentication_failure": True,
                        "config_error": True,
                        "virt_bad_packet": True,
                        "virt_authentication_failure": True,
                        "virt_config_error": True,
                    },
                    "retransmit": {"packets": True, "virt_packets": True},
                    "state_change": {
                        "if_state_change": True,
                        "neighbor_state_change": True,
                        "virtif_state_change": True,
                        "virtneighbor_state_change": True,
                    },
                },
                "rsvp": {"all": True, "new_flow": True, "lost_flow": True},
                "l2tun": {
                    "sessions": True,
                    "tunnel_up": True,
                    "tunnel_down": True,
                },
                "vpls": {
                    "all": True,
                    "status": True,
                    "full_clear": True,
                    "full_raise": True,
                },
                "snmp": {
                    "linkup": True,
                    "linkdown": True,
                    "coldstart": True,
                    "warmstart": True,
                    "authentication": True,
                },
                "bulkstat_transfer": True,
                "bulkstat_collection": True,
                "diameter": {
                    "protocolerror": True,
                    "permanentfail": True,
                    "transientfail": True,
                },
                "l2vpn": {
                    "all": True,
                    "cisco": True,
                    "vc_up": True,
                    "vc_down": True,
                },
                "bridgemib": True,
                "ospfv3": {
                    "errors": {
                        "bad_packet": True,
                        "config_error": True,
                        "virt_bad_packet": True,
                        "virt_config_error": True,
                    },
                    "state_change": {
                        "if_state_change": True,
                        "neighbor_state_change": True,
                        "nssa_state_change": True,
                        "virtif_state_change": True,
                        "virtneighbor_state_change": True,
                        "restart_status_change": True,
                        "restart_helper_status_change": True,
                        "restart_virtual_helper_status_change": True,
                    },
                },
                "fru_ctrl": True,
                "subscriber": {
                    "session_agg_node": True,
                    "session_agg_access_interface": True,
                },
                "addrpool": {"low": True, "high": True},
                "cisco_entity_ext": True,
                "entity_state": {"operstatus": True, "switchover": True},
                "entity_redundancy": {
                    "all": True,
                    "status": True,
                    "switchover": True,
                },
            },
            "chassis_id": "test2",
            "contact": "test",
            "location": "test",
            "targets": [
                {"name": "test1", "vrf": "vrf1"},
                {"name": "test1", "host": "1.1.1.1"},
            ],
            "context": ["test", "test2"],
            "logging_threshold_oid_processing": 0,
            "logging_threshold_pdu_processing": 0,
            "mib_bulkstat_max_procmem_size": 100,
            "mib_object_lists": ["test"],
            "mib_bulkstat_transfer_ids": [
                {
                    "name": "test1",
                    "retry": 1,
                    "buffer_size": 1024,
                    "enable": True,
                    "format_schemaASCI": True,
                    "retain": 1,
                    "schema": "test",
                },
            ],
            "timeouts": {
                "duplicate": 0,
                "inQdrop": 0,
                "subagent": 1,
                "pdu_stats": 1,
                "threshold": 0,
            },
            "packetsize": 485,
            "correlator": {"buffer_size": 1024},
            "trap_source": "GigabitEthernet0/0/0/1",
            "throttle_time": 50,
            "community_maps": [
                {"name": "test", "context": "test", "security_name": "test2"},
                {"name": "test1", "context": "test", "security_name": "test2"},
            ],
            "inform": {"pending": 1, "retries": 1, "timeout": 1},
            "oid_poll_stats": True,
            "overload_control": {
                "overload_drop_time": 0,
                "overload_throttle_rate": 0,
            },
            "interfaces": [
                {
                    "name": "GigabitEthernet0/0/0/0",
                    "notification_linkupdown_disable": True,
                },
            ],
            "ifmib": {
                "ifalias_long": True,
                "internal_cache_max_duration": 0,
                "ipsubscriber": True,
                "stats": True,
            },
            "ifindex": True,
            "mroutemib_send_all_vrf": True,
            "notification_log_mib": {
                "size": 1,
                "default": True,
                "disable": True,
                "GlobalSize": 1,
            },
        }
        self.assertEqual(parsed_list, result["parsed"])
