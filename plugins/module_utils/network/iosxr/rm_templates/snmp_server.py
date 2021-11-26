# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Snmp_server parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


def community_tmplt(config_data):
    name = config_data.get("name", "")
    command = "snmp-server community {name}".format(name=name)
    if config_data.get("rw"):
        command += " RW"
    elif config_data.get("ro"):
        command += " RO"
    if config_data.get("sdrowner"):
        command += " SDROwner"
    elif config_data.get("systemowner"):
        command += " SystemOwner"
    if config_data.get("acl_v4"):
        command += " IPv4 {IPv4}".format(IPv4=config_data["acl_v4"])
    if config_data.get("acl_v6"):
        command += " IPv6 {IPv6}".format(IPv6=config_data["acl_v6"])
    if config_data.get("v4_acl"):
        command += " {v4_acl}".format(v4_acl=config_data["v4_acl"])
    return command


def community_map_tmplt(config_data):
    """

    """
    name = config_data.get("name", "")
    command = "snmp-server community-map {name}".format(name=name)
    if config_data.get("context"):
        command += " context {context}".format(context=config_data["context"])
    if config_data.get("security_name"):
        command += " security-name {security_name}".format(
            security_name=config_data["security_name"]
        )
    if config_data.get("target_list"):
        command += " target-list {target_list}".format(
            target_list=config_data["target_list"]
        )
    return command


def tmplt_correlator_rule(config_data):
    """

    """
    rule_name = config_data.get("rule_name")
    command = "snmp-server correlator rule {rule_name}".format(
        rule_name=rule_name
    )
    if config_data.get("timeout"):
        command += " timeout {timeout}".format(timeout=config_data["timeout"])
    return command


def drop_tmplt(config_data):
    """

    """
    commands = []
    command = ""
    if config_data.get("drop", {}).get("report_IPv4", ""):
        command += "snmp-server drop report acl IPv4 {report_IPv4}".format(
            report_IPv4=config_data.get("drop").get("report_IPv4")
        )
        commands.append(command)
    if config_data.get("drop", {}).get("report_IPv6", ""):
        command += "snmp-server drop report acl IPv6 {report_IPv6}".format(
            report_IPv6=config_data.get("drop").get("report_IPv6")
        )
        commands.append(command)
    if config_data.get("drop", {}).get("unknown_user", ""):
        command = "snmp-server drop unknown-user"
        commands.append(command)
    return commands


def group_tmplt(config_data):
    """

    """
    group = config_data.get("group", "")
    command = "snmp-server group {group}".format(group=group)
    if config_data.get("version"):
        command += " {version}".format(version=config_data["version"])
    if config_data.get("notify"):
        command += " notify {notify}".format(notify=config_data["notify"])
    if config_data.get("read"):
        command += " read {read}".format(read=config_data["read"])
    if config_data.get("write"):
        command += " write {write}".format(write=config_data["write"])
    if config_data.get("context"):
        command += " context {context}".format(context=config_data["context"])
    if config_data.get("Ipv4_acl"):
        command += " IPv4 {Ipv4_acl}".format(Ipv4_acl=config_data["Ipv4_acl"])
    if config_data.get("Ipv6_acl"):
        command += " IPv6 {Ipv6_acl}".format(Ipv6_acl=config_data["Ipv6_acl"])
    if config_data.get("v4_acl"):
        command += " {v4_acl}".format(v4_acl=config_data["v4_acl"])
    return command


def host_tmplt(config_data):
    """

    """
    host = config_data.get("host", "")
    command = "snmp-server host {host}".format(host=host)
    if config_data.get("informs"):
        command += " informs"
    if config_data.get("traps"):
        command += " traps"
    if config_data.get("version"):
        command += " version {version}".format(version=config_data["version"])
    if config_data.get("community"):
        command += " {community}".format(community=config_data["community"])
    if config_data.get("udp_port"):
        command += " udp-port {udp_port}".format(
            udp_port=config_data["udp_port"]
        )
    if config_data.get("write"):
        command += " write {write}".format(write=config_data["write"])
    return command


def ifmib_tmplt(config_data):
    """

    """
    config_data = config_data.get("ifmib", {})
    cmds = []
    if config_data.get("ifalias_long"):
        command = "snmp-server ifmib ifalias long"
        cmds.append(command)
    if config_data.get("ipsubscriber"):
        command = "snmp-server ifmib ipsubscriber"
        cmds.append(command)
    if config_data.get("stats"):
        command = "snmp-server ifmib stats cache"
        cmds.append(command)
    if config_data.get("internal_cache_max_duration"):
        command = (
            "snmp-server ifmib internal cache max-duration "
            "{internal_cache_max_duration}".format(
                internal_cache_max_duration=config_data[
                    "internal_cache_max_duration"
                ]
            )
        )
        cmds.append(command)
    return cmds


def interfaces_tmplt(config_data):
    """

    """
    interface = config_data.get("name", "")
    notification_linkupdown_disable = config_data.get(
        "notification_linkupdown_disable", ""
    )
    index_persistent = config_data.get("index_persistent", "")

    cmds = []
    if notification_linkupdown_disable:
        command = "snmp-server interface {interface} notification linkupdown disable".format(
            interface=interface
        )
        cmds.append(command)
    if config_data.get("index_persistent"):
        command = "snmp-server snmp-server interface {interface} index persistence".format(
            interface=interface
        )
        cmds.append(command)
    if (
        not notification_linkupdown_disable
        and not index_persistent
        and interface
    ):
        command = "snmp-server interface {interface}".format(
            interface=interface
        )
        cmds.append(command)
    return cmds


def inform_tmplt(config_data):
    """

    """
    config_data = config_data.get("inform", {})
    cmds = []

    if config_data.get("pending"):
        command = "snmp-server inform pending {pending}".format(
            pending=config_data["pending"]
        )
        cmds.append(command)
    if config_data.get("retries"):
        command = "snmp-server inform retries {retries}".format(
            retries=config_data["retries"]
        )
        cmds.append(command)
    if config_data.get("timeout"):
        command = "snmp-server inform timeout {timeout}".format(
            timeout=config_data["timeout"]
        )
        cmds.append(command)
    return cmds


def mib_schema_tmplt(config_data):
    name = config_data.get("name", "")
    object_list = config_data.get("object_list", "")
    poll_interval = config_data.get("poll_interval", "")

    cmds = []
    if object_list:
        command = "snmp-server mib bulkstat schema {name} object-list {object_list}".format(
            name=name, object_list=object_list
        )
        cmds.append(command)
    if poll_interval:
        command = "snmp-server mib bulkstat schema {name} poll-interval {poll_interval}".format(
            name=name, poll_interval=poll_interval
        )
        cmds.append(command)
    if not object_list and not poll_interval and name:
        command = "snmp-server mib bulkstat schema {name}".format(name=name)
        cmds.append(command)
    return cmds


def mib_bulkstat_transfer_ids_tmplt(config_data):
    name = config_data.get("name", "")
    buffer_size = config_data.get("buffer_size", "")
    enable = config_data.get("enable", "")
    format_schemaASCI = config_data.get("format_schemaASCI", "")
    retain = config_data.get("retain", "")
    retry = config_data.get("retry", "")
    schema = config_data.get("schema", "")
    transfer_interval = config_data.get("transfer_interval", "")

    cmds = []
    if buffer_size:
        command = "snmp-server mib bulkstat transfer-id {name} buffer-size {buffer_size}".format(
            name=name, buffer_size=buffer_size
        )
        cmds.append(command)
    if enable:
        command = "snmp-server mib bulkstat transfer-id {name} enable".format(
            name=name
        )
        cmds.append(command)
    if format_schemaASCI:
        command = "snmp-server mib bulkstat transfer-id {name} format schemaASCII".format(
            name=name
        )
        cmds.append(command)
    if retain:
        command = "snmp-server mib bulkstat transfer-id {name} retain {retain}".format(
            name=name, retain=retain
        )
        cmds.append(command)
    if retry:
        command = "snmp-server mib bulkstat transfer-id {name} retry {retry}".format(
            name=name, retry=retry
        )
        cmds.append(command)
    if schema:
        command = "snmp-server mib bulkstat transfer-id {name} schema {schema}".format(
            name=name, schema=schema
        )
        cmds.append(command)
    if transfer_interval:
        command = "snmp-server mib bulkstat transfer-id {name} transfer_interval {transfer_interval}".format(
            name=name, transfer_interval=transfer_interval
        )
        cmds.append(command)
    if (
        not any(
            [
                buffer_size,
                enable,
                format_schemaASCI,
                retry,
                retain,
                schema,
                transfer_interval,
            ]
        )
        and name
    ):
        command = "snmp-server mib bulkstat transfer-id {name}".format(
            name=name
        )
        cmds.append(command)
    return cmds


def notification_log_mib_tmplt(config_data):
    """

    """
    config_data = config_data.get("notification_log_mib", {})
    cmds = []
    if config_data.get("size"):
        command = "snmp-server notification-log-mib size {size}".format(
            size=config_data["size"]
        )
        cmds.append(command)
    if config_data.get("default"):
        command = "snmp-server notification-log-mib default"
        cmds.append(command)
    if config_data.get("disable"):
        command = "snmp-server notification-log-mib disable"
        cmds.append(command)
    if config_data.get("GlobalSize"):
        command = "snmp-server notification-log-mib GlobalSize {GlobalSize}".format(
            GlobalSize=config_data["GlobalSize"]
        )
        cmds.append(command)
    return cmds


def overload_control_tmplt(config_data):
    """

    """
    config_data = config_data.get("overload_control", {})
    command = "snmp-server overload-control"
    if config_data.get("overload_drop_time"):
        command += " {overload_drop_time}".format(
            overload_drop_time=config_data["overload_drop_time"]
        )
    if config_data.get("overload_throttle_rate"):
        command += " {overload_throttle_rate}".format(
            overload_throttle_rate=config_data["overload_throttle_rate"]
        )
    return command


def targets_tmplt(config_data):
    name = config_data.get("name", "")
    command = ""
    if name:
        command = "snmp-server target list {name}".format(name=name)
    if config_data.get("host"):
        command += " host {host}".format(host=config_data["host"])
    if config_data.get("vrf"):
        command += " vrf {vrf}".format(vrf=config_data["vrf"])
    return command


def timeouts_tmplt(config_data):
    """

    """
    config_data = config_data.get("timeouts", {})
    cmds = []
    if config_data.get("duplicate"):
        command = "snmp-server timeouts duplicate {duplicate}".format(
            duplicate=config_data["duplicate"]
        )
        cmds.append(command)
    if config_data.get("inQdrop"):
        command = "snmp-server timeouts inQdrop {inQdrop}".format(
            inQdrop=config_data["inQdrop"]
        )
        cmds.append(command)
    if config_data.get("pdu_stats"):
        command = "snmp-server timeouts pdu stats {pdu_stats}".format(
            pdu_stats=config_data["pdu_stats"]
        )
        cmds.append(command)
    if config_data.get("subagent"):
        command = "snmp-server timeouts subagent {subagent}".format(
            subagent=config_data["subagent"]
        )
        cmds.append(command)
    if config_data.get("threshold"):
        command = "snmp-server timeouts threshold {threshold}".format(
            threshold=config_data["threshold"]
        )
        cmds.append(command)
    return cmds


def trap_tmplt(config_data):
    """

    """
    config_data = config_data.get("trap", {})
    cmds = []
    if config_data.get("authentication_vrf_disable"):
        command = "snmp-server trap authentication vrf disable"
        cmds.append(command)
    if config_data.get("link_ietf"):
        command = "snmp-server trap link ietf"
        cmds.append(command)
    if config_data.get("throttle_time"):
        command = "snmp-server trap throttle-time {throttle_time}".format(
            throttle_time=config_data["throttle_time"]
        )
        cmds.append(command)
    return cmds


def tmplt_traps_diameter(cmds, diameter):
    """

    """
    if diameter:
        if diameter.get("peerdown"):
            command = "snmp-server traps diameter peerdown"
            cmds.append(command)
        if diameter.get("peerup"):
            command = "snmp-server traps diameter peerup"
            cmds.append(command)
        if diameter.get("permanentfail"):
            command = "snmp-server traps diameter permanentfail"
            cmds.append(command)
        if diameter.get("protocolerror"):
            command = "snmp-server traps diameter protocolerror"
            cmds.append(command)
        if diameter.get("transientfail"):
            command = "snmp-server traps diameter transientfail"
            cmds.append(command)
    return cmds


def tmplt_traps_entity_redundancy(cmds, entity_redundancy):
    """

    """
    if entity_redundancy:
        if entity_redundancy.get("all"):
            command = "snmp-server traps entity-redundancy all"
            cmds.append(command)
        if entity_redundancy.get("status"):
            command = "snmp-server traps entity-redundancy status"
            cmds.append(command)
        if entity_redundancy.get("switchover"):
            command = "snmp-server traps entity-redundancy switchover"
            cmds.append(command)
    return cmds


def tmplt_traps_entity_state(cmds, entity_state):
    """

    """
    if entity_state:
        if entity_state.get("operstatus"):
            command = "snmp-server traps entity-state operstatus"
            cmds.append(command)
        if entity_state.get("switchover"):
            command = "snmp-server traps entity-state switchover"
            cmds.append(command)
    return cmds


def tmplt_traps_flash(cmds, flash):
    """

    """
    if flash:
        if flash.get("insertion"):
            command = "snmp-server traps flash insertion"
            cmds.append(command)
        if flash.get("removal"):
            command = "snmp-server traps flash removal"
            cmds.append(command)
    return cmds


def tmplt_traps_ipsec(cmds, ipsec):
    """

    """
    if ipsec:
        if ipsec.get("start"):
            command = "snmp-server traps ipsec tunnel start"
            cmds.append(command)
        if ipsec.get("stop"):
            command = "snmp-server traps ipsec tunnel stop"
            cmds.append(command)
    return cmds


def tmplt_traps_isakmp(cmds, ipsec):
    """

    """
    if ipsec:
        if ipsec.get("start"):
            command = "snmp-server traps isakmp tunnel start"
            cmds.append(command)
        if ipsec.get("stop"):
            command = "snmp-server traps isakmp tunnel stop"
            cmds.append(command)
    return cmds


def tmplt_traps_isis(cmds, isis):
    """

    """
    command = "snmp-server traps isis"
    if isis.get("all"):
        command += " all"
    else:
        if isis.get("adjacency_change"):
            command += " adjacency-change"
        if isis.get("area_mismatch"):
            command += " area-mismatch"
        if isis.get("attempt_to_exceed_max_sequence"):
            command += " attempt-to-exceed-max-sequence"
        if isis.get("authentication_failure"):
            command += " authentication-failure"
        if isis.get("authentication_type_failure"):
            command += " authentication-type-failure"
        if isis.get("corrupted_lsp_detected"):
            command += " corrupted-lsp-detected"
        if isis.get("database_overload"):
            command += " database-overload"
        if isis.get("id_len_mismatch"):
            command += " id-len-mismatch"
        if isis.get("lsp_error_detected"):
            command += " lsp-error-detected"
        if isis.get("lsp_too_large_to_propagate"):
            command += " lsp-too-large-to-propagate"
        if isis.get("manual_address_drops"):
            command += " manual-address-drops"
        if isis.get("max_area_addresses_mismatch"):
            command += " max-area-addresses-mismatch"
        if isis.get("orig_lsp_buff_size_mismatch"):
            command += " orig-lsp-buff-size-mismatch"
        if isis.get("version_skew"):
            command += " version-skew"
        if isis.get("own_lsp_purge"):
            command += " own-lsp-purge"
        if isis.get("rejected_adjacency"):
            command += " rejected-adjacency"
        if isis.get("protocols_supported_mismatch"):
            command += " protocols-supported-mismatch"
        if isis.get("sequence_number_skip"):
            command += " sequence-number-skip"
    cmds.append(command)

    return cmds


def tmplt_traps_l2tun(cmds, l2tun):
    """

    """
    if l2tun:
        if l2tun.get("pseudowire_status"):
            command = "snmp-server traps l2tun pseudowire-status"
            cmds.append(command)
        if l2tun.get("sessions"):
            command = "snmp-server traps l2tun sessions"
            cmds.append(command)
        if l2tun.get("tunnel_down"):
            command = "snmp-server traps l2tun tunnel-down"
            cmds.append(command)
        if l2tun.get("tunnel_up"):
            command = "snmp-server traps l2tun tunnel-up"
            cmds.append(command)
    return cmds


def tmplt_traps_l2vpn(cmds, l2vpn):
    """

    """
    if l2vpn:
        if l2vpn.get("all"):
            command = "snmp-server traps l2vpn all"
            cmds.append(command)
        if l2vpn.get("cisco"):
            command = "snmp-server traps l2vpn cisco"
            cmds.append(command)
        if l2vpn.get("vc_down"):
            command = "snmp-server traps l2vpn vc-down"
            cmds.append(command)
        if l2vpn.get("vc_up"):
            command = "snmp-server traps l2vpn vc-up"
            cmds.append(command)
    return cmds


def tmplt_traps_ospf(cmds, ospf):
    """

    """
    errors = ospf.get("errors")
    lsa = ospf.get("lsa")
    retransmit = ospf.get("retransmit")
    state_change = ospf.get("state_change")
    if errors:
        if errors.get("bad_packet"):
            command = "snmp-server traps ospf errors bad-packet"
            cmds.append(command)
        if errors.get("authentication_failure"):
            command = "snmp-server traps ospf errors authentication-failure"
            cmds.append(command)
        if errors.get("config_error"):
            command = "snmp-server traps ospf errors config-error"
            cmds.append(command)
        if errors.get("virt_bad_packet"):
            command = "snmp-server traps ospf errors virt-bad-packet"
            cmds.append(command)
        if errors.get("virt_authentication_failure"):
            command = (
                "snmp-server traps ospf errors virt-authentication-failure"
            )
            cmds.append(command)
        if errors.get("virt_config_error"):
            command = "snmp-server traps ospf errors virt-config-error"
            cmds.append(command)
    if lsa:
        if lsa.get("lsa_maxage"):
            command = "snmp-server traps ospf lsa lsa-maxage"
            cmds.append(command)
        if lsa.get("lsa_originate"):
            command = "snmp-server traps ospf lsa lsa-originate"
            cmds.append(command)
    if retransmit:
        if retransmit.get("packets"):
            command = "snmp-server traps ospf retransmit packets"
            cmds.append(command)
        if retransmit.get("virt_packets"):
            command = "snmp-server traps ospf retransmit virt-packets"
            cmds.append(command)
    if state_change:
        if state_change.get("if_state_change"):
            command = "snmp-server traps ospf state-change if-state-change"
            cmds.append(command)
        if state_change.get("neighbor_state_change"):
            command = (
                "snmp-server traps ospf state-change neighbor-state-change"
            )
            cmds.append(command)
        if state_change.get("virtif_state_change"):
            command = "snmp-server traps ospf state-change virtif-state-change"
            cmds.append(command)
        if state_change.get("virtneighbor_state_change"):
            command = (
                "snmp-server traps ospf state-change virtneighbor-state-change"
            )
            cmds.append(command)
    return cmds


def tmplt_traps_ospfv3(cmds, ospfv3):
    """

    """
    errors = ospfv3.get("errors")
    state_change = ospfv3.get("state_change")
    if errors:
        if errors.get("bad_packet"):
            command = "snmp-server traps ospfv3 errors bad-packet"
            cmds.append(command)
        if errors.get("config_error"):
            command = "snmp-server traps ospfv3 errors config-error"
            cmds.append(command)
        if errors.get("virt_bad_packet"):
            command = "snmp-server traps ospfv3 errors virt-bad-packet"
            cmds.append(command)
        if errors.get("virt_config_error"):
            command = "snmp-server traps ospfv3 errors virt-config-error"
            cmds.append(command)
    if state_change:
        if state_change.get("if_state_change"):
            command = "snmp-server traps ospfv3 state-change if-state-change"
            cmds.append(command)
        if state_change.get("neighbor_state_change"):
            command = (
                "snmp-server traps ospfv3 state-change neighbor-state-change"
            )
            cmds.append(command)
        if state_change.get("virtif_state_change"):
            command = (
                "snmp-server traps ospfv3 state-change virtif-state-change"
            )
            cmds.append(command)
        if state_change.get("virtneighbor_state_change"):
            command = "snmp-server traps ospfv3 state-change virtneighbor-state-change"
            cmds.append(command)
        if state_change.get("nssa_state_change"):
            command = "snmp-server traps ospfv3 state-change nssa-state-change"
            cmds.append(command)
        if state_change.get("restart_status_change"):
            command = (
                "snmp-server traps ospfv3 state-change restart-status-change"
            )
            cmds.append(command)
        if state_change.get("restart_helper_status_change"):
            command = "snmp-server traps ospfv3 state-change restart-helper-status-change"
            cmds.append(command)
        if state_change.get("restart_virtual_helper_status_change"):
            command = "snmp-server traps ospfv3 state-change restart-virtual-helper-status-change"
            cmds.append(command)
    return cmds


def tmplt_traps_rsvp(cmds, rsvp):
    """

    """
    if rsvp:
        if rsvp.get("all"):
            command = "snmp-server traps rsvp all"
            cmds.append(command)
        if rsvp.get("lost_flow"):
            command = "snmp-server traps rsvp lost-flow"
            cmds.append(command)
        if rsvp.get("new_flow"):
            command = "snmp-server traps rsvp new-flow"
            cmds.append(command)
    return cmds


def tmplt_traps_pim(cmds, pim):
    """

    """
    if pim:
        if pim.get("interface_state_change"):
            command = "snmp-server traps pim interface-state-change"
            cmds.append(command)
        if pim.get("invalid_message_received"):
            command = "snmp-server traps pim invalid-message-received"
            cmds.append(command)
        if pim.get("neighbor_change"):
            command = "snmp-server traps pim neighbor-change"
            cmds.append(command)
        if pim.get("neighbor_change"):
            command = "snmp-server traps pim neighbor-change"
            cmds.append(command)
        if pim.get("rp_mapping_change"):
            command = "snmp-server traps pim rp-mapping-change"
            cmds.append(command)
    return cmds


def tmplt_traps_snmp(cmds, snmp):
    """

    """
    if snmp:
        if snmp.get("authentication"):
            command = "snmp-server traps snmp authentication"
            cmds.append(command)
        if snmp.get("linkdown"):
            command = "snmp-server traps snmp linkdown"
            cmds.append(command)
        if snmp.get("linkup"):
            command = "snmp-server traps snmp linkup"
            cmds.append(command)
        if snmp.get("coldstart"):
            command = "snmp-server traps snmp coldstart"
            cmds.append(command)
        if snmp.get("warmstart"):
            command = "snmp-server traps snmp warmstart"
            cmds.append(command)
    return cmds


def tmplt_traps_subscriber(cmds, subscriber):
    """

    """
    if subscriber:
        if subscriber.get("session_agg_access_interface"):
            command = (
                "snmp-server traps subscriber session-agg access-interface"
            )
            cmds.append(command)
        if subscriber.get("session_agg_node"):
            command = "snmp-server traps subscriber session-agg node"
            cmds.append(command)

    return cmds


def tmplt_traps_vpls(cmds, vpls):
    """

    """
    if vpls:
        if vpls.get("all"):
            command = "snmp-server traps vpls all"
            cmds.append(command)
        if vpls.get("full_raise"):
            command = "snmp-server traps vpls full-raise"
            cmds.append(command)
        if vpls.get("full_clear"):
            command = "snmp-server traps vpls full-clear"
            cmds.append(command)
        if vpls.get("status"):
            command = "snmp-server traps vpls status"
            cmds.append(command)
    return cmds


def traps_tmplt(config_data):
    """

    """
    config_data = config_data.get("traps", {})
    cmds = []
    addrpool = config_data.get("addrpool", {})
    bgp = config_data.get("bgp", {})

    if addrpool:
        if addrpool.get("low"):
            command = "snmp-server traps addrpool low"
            cmds.append(command)
        if addrpool.get("high"):
            command = "snmp-server traps addrpool high"
            cmds.append(command)
    if config_data.get("bfd"):
        command = "snmp-server traps bfd"
        cmds.append(command)
    if bgp:
        if bgp.get("cbgp2"):
            command = "snmp-server traps bgp cbgp2"
            cmds.append(command)
        if bgp.get("updown"):
            command = "snmp-server traps bgp updown"
            cmds.append(command)
    if config_data.get("bulkstat_collection"):
        command = "snmp-server traps bulkstat collection"
        cmds.append(command)
    if config_data.get("bulkstat_transfer"):
        command = "snmp-server traps bulkstat transfer"
        cmds.append(command)
    if config_data.get("bridgemib"):
        command = "snmp-server traps bridgemib"
        cmds.append(command)
    if config_data.get("copy_complete"):
        command = "snmp-server traps copy-complete"
        cmds.append(command)
    if config_data.get("cisco_entity_ext"):
        command = "snmp-server traps cisco-entity-ext"
        cmds.append(command)
    if config_data.get("config"):
        command = "snmp-server traps config"
        cmds.append(command)
    if config_data.get("diameter"):
        cmds = tmplt_traps_diameter(cmds, config_data.get("diameter"))
    if config_data.get("entity"):
        command = "snmp-server traps entity"
        cmds.append(command)
    if config_data.get("entity_redundancy"):
        cmds = tmplt_traps_entity_redundancy(
            cmds, config_data.get("entity_redundancy")
        )
    if config_data.get("entity_state"):
        cmds = tmplt_traps_entity_state(cmds, config_data.get("entity_state"))
    if config_data.get("flash"):
        cmds = tmplt_traps_flash(cmds, config_data.get("flash"))
    if config_data.get("fru_ctrl"):
        command = "snmp-server traps fru-ctrl"
        cmds.append(command)
    if config_data.get("hsrp"):
        command = "snmp-server traps hsrp"
        cmds.append(command)
    if config_data.get("ipsla"):
        command = "snmp-server traps ipsla"
        cmds.append(command)
    if config_data.get("ipsec"):
        cmds = tmplt_traps_ipsec(cmds, config_data.get("ipsec"))
    if config_data.get("isakmp"):
        cmds = tmplt_traps_isakmp(cmds, config_data.get("isakmp"))
    if config_data.get("isis"):
        cmds = tmplt_traps_isis(cmds, config_data.get("isis"))
    if config_data.get("l2tun"):
        cmds = tmplt_traps_l2tun(cmds, config_data.get("l2tun"))
    if config_data.get("l2vpn"):
        cmds = tmplt_traps_l2vpn(cmds, config_data.get("l2vpn"))
    if config_data.get("msdp_peer_state_change"):
        command = "snmp-server traps msdp peer-state-change"
        cmds.append(command)
    if config_data.get("ntp"):
        command = "snmp-server traps ntp"
        cmds.append(command)
    if config_data.get("ospf"):
        cmds = tmplt_traps_ospf(cmds, config_data.get("ospf"))
    if config_data.get("ospfv3"):
        cmds = tmplt_traps_ospfv3(cmds, config_data.get("ospfv3"))
    if config_data.get("power"):
        command = "snmp-server traps power"
        cmds.append(command)
    if config_data.get("rf"):
        command = "snmp-server traps rf"
        cmds.append(command)
    if config_data.get("pim"):
        cmds = tmplt_traps_pim(cmds, config_data.get("pim"))
    if config_data.get("rsvp"):
        cmds = tmplt_traps_rsvp(cmds, config_data.get("rsvp"))
    if config_data.get("snmp"):
        cmds = tmplt_traps_snmp(cmds, config_data.get("snmp"))
    if config_data.get("selective_vrf_download_role_change"):
        command = "snmp-server traps selective-vrf-download role-change"
        cmds.append(command)
    if config_data.get("sensor"):
        command = "snmp-server traps sensor"
        cmds.append(command)
    if config_data.get("vrrp_events"):
        command = "snmp-server traps vrrp events"
        cmds.append(command)
    if config_data.get("syslog"):
        command = "snmp-server traps syslog"
        cmds.append(command)
    if config_data.get("system"):
        command = "snmp-server traps system"
        cmds.append(command)
    if config_data.get("subscriber"):
        cmds = tmplt_traps_subscriber(cmds, config_data.get("subscriber"))
    if config_data.get("vpls"):
        cmds = tmplt_traps_vpls(cmds, config_data.get("vpls"))
    return cmds


def user_tmplt(config_data):
    user = config_data.get("user", "")
    group = config_data.get("group", "")
    version = config_data.get("version", "")
    command = "snmp-server user {user} {group} {version}".format(
        user=user, group=group, version=version
    )
    if config_data.get("Ipv4_acl"):
        command += " IPv4 {IPv4}".format(IPv4=config_data["Ipv4_acl"])
    if config_data.get("Ipv4_acl"):
        command += " IPv6 {IPv6}".format(IPv6=config_data["Ipv6_acl"])
    if config_data.get("v4_acl"):
        command += " {v4_acl}".format(v4_acl=config_data["v4_acl"])
    if config_data.get("sdrowner"):
        command += " SDROwner"
    elif config_data.get("systemowner"):
        command += " SystemOwner"
    return command


class Snmp_serverTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Snmp_serverTemplate, self).__init__(
            lines=lines, tmplt=self, module=module
        )

    # fmt: off
    PARSERS = [
        {
            "name": "chassis_id",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\s+chassis-id\s(?P<chassis_id>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server chassis-id {{chassis_id}}",
            "result": {
                "chassis_id": "{{chassis_id}}"
            }
        },
        {
            "name": "community",
            "getval": re.compile(
                r"""
                ^snmp-server\scommunity
                (\s(?P<name>\S+))?
                (\sRW(?P<rw>))?
                (\sRO(?P<ro>))?
                (\sSDROwner(?P<sdrowner>))?
                (\sSystemOwner(?P<systemowner>))?
                (\sIPv4\s(?P<ipv4>\S+))?
                (\sIPv6\s(?P<ipv6>\S+))?
                (\s(?P<v4acl>\S+))?
                $""", re.VERBOSE),
            "setval": community_tmplt,
            "result": {
                "community": [
                    {
                        "name": "{{ name }}",
                        "rw": "{{ True if rw is defined }}",
                        "ro": "{{ True if ro is defined }}",
                        "acl_v4": "{{ipv4}}",
                        "acl_v6": "{{ipv6}}",
                        "sdrowner": "{{True if sdrowner is defined}}",
                        "systemowner": "{{True if systemowner is defined }}",
                        "v4_acl": "{{v4acl}}"
                    }
                ]
            }
        },
        {
            "name": "community_map",
            "getval": re.compile(
                r"""
                ^snmp-server\scommunity-map
                (\s(?P<name>\S+))?
                (\scontext\s(?P<context>\S+))?
                (\ssecurity-name\s(?P<security_name>\S+))?
                (\starget-list\s(?P<target_list>\S+))?
                $""", re.VERBOSE),
            "setval": community_map_tmplt,
            "result": {
                "community_map": [
                    {
                        "name": "{{ name }}",
                        "context": "{{context}}",
                        "security_name": "{{security_name}}",
                        "target_list": "{{target_list}}",
                    }
                ]
            }
        },
        {
            "name": "correlator.buffer_size",
            "getval": re.compile(
                r"""
                ^snmp-server\scorrelator
                (\sbuffer-size\s(?P<buffer_size>\S+))?
                $""", re.VERBOSE),
            "setval": "snmp-server correlator buffer-size {{correlator.buffer_size }}",
            "result": {
                "correlator": {
                    "buffer_size": "{{ buffer_size }}"
                }
            }
        },
        {
            "name": "correlator.rules",
            "getval": re.compile(
                r"""
                ^snmp-server\scorrelator
                (\srule\s(?P<name>\S+))?
                (\s+timeout\s(?P<timeout>\S+))?
                $""", re.VERBOSE),
            "setval": tmplt_correlator_rule,
            "result": {
                "correlator": {
                    "rules": [{
                            "rule_name": "{{ name }}",
                            "timeout": "{{ timeout }}",

                    }
                ]
                }
            }
        },
        {
            "name": "correlator.rule_sets",
            "getval": re.compile(
                r"""
                ^snmp-server\scorrelator\sruleset\s(?P<name>\S+)
                $""", re.VERBOSE),
            "setval": "snmp-server correlator ruleset {{name}}",
            "result": {
                "correlator": {
                    "rule_sets":
                        [
                            {"name": "{{ name }}"}
                        ]
                }
            }
        },
        {
            "name": "contact",
            "getval": re.compile(
                r"""
                ^snmp-server\scontact\s(?P<name>\S+)
                $""", re.VERBOSE),
            "setval": "snmp-server contact {{contact}}",
            "result": {
                "contact": "{{name}}"
            }
        },
        {
            "name": "context",
            "getval": re.compile(
                r"""
                ^snmp-server\scontext\s(?P<name>\S+)
                $""", re.VERBOSE),
            "setval": "snmp-server context {{name}}",
            "result": {
                "context": {
                    "{{name}}": "{{name}}"
                }
            }
        },
        {
            "name": "drop",
            "getval": re.compile(
                r"""
                ^snmp-server\sdrop
                (\sreport\sacl\sIPv6\s(?P<report_IPv6>\S+))?
                (\sreport\sacl\sIPv4\s(?P<report_IPv4>\S+))?
                (\sunknown-user(?P<unknown_user>))?

                $""", re.VERBOSE),
            "setval": drop_tmplt,
            "result": {
                "drop": {
                    "report_IPv6": "{{report_IPv6}}",
                    "report_IPv4": "{{report_IPv4}}",
                    "unknown_user": "{{True if unknown_user is defined}}",
                }
            }
        },
        {
            "name": "groups",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\sgroup\s(?P<group>\S+))
                (\s(?P<version>v1|v2c|v3))
                (\snotify\s(?P<notify>\S+))?
                (\sread\s(?P<read>\S+))?
                (\swrite\s(?P<write>\S+))?
                (\scontext\s(?P<context>\S+))?
                (\sIPv4\s(?P<IPv4>\S+))?
                (\sIPv6\s(?P<IPv6>\S+))?
                (\s(?P<v4acl>\S+))?
                $""", re.VERBOSE),
            "setval": group_tmplt,
            "result": {
                "groups": [
                    {
                        "group": "{{ group }}",
                        "Ipv4_acl": "{{IPv4}}",
                        "Ipv6_acl": "{{IPv6}}",
                        "context": "{{context}}",
                        "notify": "{{notify}}",
                        "read": "{{read}}",
                        "write": "{{write}}",
                        "v4acl": "{{v4acl}}",
                        "version": "{{version}}"
                    }
                ]
            }
        },
        {
            "name": "hosts",
            "getval": re.compile(
                r"""
                ^snmp-server(\shost\s(?P<host>\S+))
                (\s(?P<traps>traps))?
                (\s(?P<informs>informs))?
                (\sversion\s(?P<version>1|2c|3))?
                (\s(?P<community>\S+))?
                (\sudp-port\s(?P<port>\d+))?
                $""", re.VERBOSE),
            "setval": host_tmplt,
            "result": {
                "hosts": [
                    {
                        "host": "{{ host }}",
                        "traps": "{{True if traps is defined}}",
                        "informs": "{{True if informs is defined}}",
                        "community": "{{community}}",
                        "udp_port": "{{port}}",
                        "version": "{{version}}"
                    }
                ]
            }
        },
        {
            "name": "ifindex",
            "getval": re.compile(
                r"""
                ^snmp-server(\sifindex\spersist(?P<ifindex>))
                $""", re.VERBOSE),
            "setval": "snmp-server ifindex persist",
            "result": {
                "ifindex": "{{True if ifindex is defined}}"
            }
        },
        {
            "name": "ifmib",
            "getval": re.compile(
                r"""
                ^snmp-server\sifmib
                (\sinternal\scache\smax-duration\s(?P<cache>\S+))?
                (\sipsubscriber(?P<ipsub>))?
                (\sstats\scache(?P<s_cache>))?
                (\sifalias\slong(?P<long>))?
                $""", re.VERBOSE),
            "setval": ifmib_tmplt,
            "result": {
                "ifmib": {
                    "internal_cache_max_duration": "{{cache}}",
                    "ipsubscriber": "{{True if ipsub is defined}}",
                    "stats": "{{True if s_cache is defined}}",
                    "ifalias_long":  "{{True if long is defined}}"
                }
            }
        },
        {
            "name": "inform",
            "getval": re.compile(
                r"""
                ^snmp-server\sinform
                (\spending\s(?P<pending>\d+))?
                (\sretries\s(?P<retries>\d+))?
                (\stimeout\s(?P<timeout>\d+))?
                $""", re.VERBOSE),
            "setval": inform_tmplt,
            "result": {
                "inform": {
                    "pending": "{{pending}}",
                    "retries": "{{retries}}",
                    "timeout": "{{timeout}}"

                }
            }
        },
        {
            "name": "interfaces",
            "getval": re.compile(
                r"""
                ^snmp-server(\sinterface\s(?P<interface>\S+))
                (\snotification\slinkupdown\sdisable(?P<notification_linkupdown_disable>))?
                (\sndex\spersistence(?P<index_persistent>))?
                $""", re.VERBOSE),
            "setval": interfaces_tmplt,
            "result": {
                "interfaces": {
                    "{{interface}}": {
                        "name": "{{ interface }}",
                        "notification_linkupdown_disable": "{{True if notification_linkupdown_disable is defined}}",
                        "index_persistent": "{{True if index_persistent is defined}}",
                    }
                }
            }
        },
        {
            "name": "ipv4.dscp",
            "getval": re.compile(
                r"""
                ^snmp-server
                \sipv4\sdscp\s(?P<dscp>\S+)
                $""", re.VERBOSE),
            "setval": "snmp-server ipv4 dscp {{ipv4.dscp}}",
            "result": {
                "ipv4": {
                    "dscp": "{{dscp}}"
                }
            },
        },
        {
            "name": "ipv6.dscp",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\sipv6\sdscp\s(?P<dscp>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server ipv6 dscp {{ipv6.dscp}}",
            "result": {
                "ipv6": {
                    "dscp": "{{dscp}}"
                }
            },
        },
        {
            "name": "ipv4.precedence",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\sipv4\sprecedence\s(?P<precedence>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server ipv4 precedence {{ipv4.precedence}}",
            "result": {
                "ipv4": {"precedence": "{{precedence}}"}
            },
        },
        {
            "name": "ipv6.precedence",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\sipv6\sprecedence\s(?P<precedence>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server ipv6 precedence {{ipv6.precedence}}",
            "result": {
                "ipv6": {"precedence": "{{precedence}}"}
            },
        },
        {
            "name": "location",
            "getval": re.compile(
                r"""
                ^snmp-server(\slocation\s(?P<loc>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server location {{location}}",
            "result": {
                "location": "{{ loc }}"
            }
        },
        {
            "name": "logging_threshold_oid_processing",
            "getval": re.compile(
                r"""
                ^snmp-server(\slogging\sthreshold\soid-processing\s(?P<loc>\d+))
                $""", re.VERBOSE),
            "setval": "snmp-server logging threshold oid-processing {{logging_threshold_oid_processing}}",
            "result": {
                "logging_threshold_oid_processing": "{{ loc }}"
            }
        },
        {
            "name": "logging_threshold_pdu_processing",
            "getval": re.compile(
                r"""
                ^snmp-server(\slogging\sthreshold\spdu-processing\s(?P<loc>\d+))
                $""", re.VERBOSE),
            "setval": "snmp-server logging threshold pdu-processing {{logging_threshold_pdu_processing}}",
            "result": {
                "logging_threshold_pdu_processing": "{{ loc }}"
            }
        },
        {
            "name": "mib_bulkstat_max_procmem_size",
            "getval": re.compile(
                r"""
                ^snmp-server(\smib\sbulkstat\smax-procmem-size\s(?P<loc>\d+))
                $""", re.VERBOSE),
            "setval": "snmp-server mib bulkstat max-procmem-size {{mib_bulkstat_max_procmem_size}}",
            "result": {
                "mib_bulkstat_max_procmem_size": "{{ loc }}"
            }
        },
        {
            "name": "mib_object_lists",
            "getval": re.compile(
                r"""
                ^snmp-server(\smib\sbulkstat\sobject-list\s(?P<o_list>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server mib bulkstat object-list {{mib_object}}",
            "result": {
                "mib_object_lists": {
                    "{{o_list}}": "{{o_list}}"
                }
            }
        },
        {
            "name": "mib_schema",
            "getval": re.compile(
                r"""
                ^snmp-server(\smib\sbulkstat\sschema\s(?P<mib>\S+))
                (\sobject-list\s(?P<o_list>\S+))?
                (\spoll-interval\s(?P<p_interval>\S+))?
                $""", re.VERBOSE),
            "setval": mib_schema_tmplt,
            "result": {
                "mib_schema": {
                    "{{mib}}": {
                        "name": "{{ mib }}",
                        "poll_interval": "{{p_interval}}",
                        "object_list": "{{o_list}}"
                    }
                }
            }
        },
        {
            "name": "mib_bulkstat_transfer_ids",
            "getval": re.compile(
                r"""
                ^snmp-server(\smib\sbulkstat\stransfer-id\s(?P<mib1>\S+))
                (\sretry\s(?P<retry>\S+))?
                (\sbuffer-size\s(?P<buffer_size>\S+))?
                (\senable(?P<enable>))?
                (\sformat\sschemaASCII(?P<format>))?
                (\sretain\s(?P<retain>\S+))?
                (\sschema\s(?P<schema>\S+))?
                (\stransfer-interval\s(?P<ti>\S+))?

                $""", re.VERBOSE),
            "setval": mib_bulkstat_transfer_ids_tmplt,
            "result": {
                "mib_bulkstat_transfer_ids": {
                    "{{mib1}}": {
                        "name": "{{ mib1 }}",
                        "buffer_size": "{{buffer_size}}",
                        "enable": "{{True if enable is defined}}",
                        "format_schemaASCI": "{{True if format is defined}}",
                        "retain": "{{retain}}",
                        "schema": "{{schema}}",
                        "retry": "{{retry}}",
                        "transfer_interval": "{{ti}}"
                    }
                }
            }
        },
        {
            "name": "mroutemib_send_all_vrf",
            "getval": re.compile(
                r"""
                ^snmp-server(\smroutemib\ssend-all-vrf(?P<send>))
                $""", re.VERBOSE),
            "setval": "snmp-server mroutemib send-all-vrf",
            "result": {
                "mroutemib_send_all_vrf": "{{ True if send is defined }}"
            }
        },
        {
            "name": "notification_log_mib",
            "getval": re.compile(
                r"""
                ^snmp-server\snotification-log-mib
                (\ssize\s(?P<size>\d+))?
                (\sdefault(?P<default>))?
                (\sdisable(?P<disable>))?
                (\sGlobalSize\s(?P<gsize>\d+))?
                $""", re.VERBOSE),
            "setval": notification_log_mib_tmplt,
            "result": {
                "notification_log_mib": {
                    "size": "{{size}}",
                    "default": "{{True if default is defined}}",
                    "disable": "{{True if disable is defined}}",
                    "GlobalSize": "{{gsize}}"

                }
            }
        },
        {
            "name": "oid_poll_stats",
            "getval": re.compile(
                r"""
                ^snmp-server(\soid-poll-stats(?P<oid_stats>))
                $""", re.VERBOSE),
            "setval": "snmp-server oid-poll-stats",
            "result": {
                "oid_poll_stats": "{{ True if oid_stats is defined }}"
            }
        },
        {
            "name": "overload_control",
            "getval": re.compile(
                r"""
                ^snmp-server\soverload-control
                (\s(?P<overload_drop_time>\d+))?
                (\s(?P<overload_throttle_rate>\d+))?
                $""", re.VERBOSE),
            "setval": overload_control_tmplt,
            "result": {
                "overload_control": {
                    "overload_drop_time": "{{overload_drop_time}}",
                    "overload_throttle_rate": "{{overload_throttle_rate}}",
                }
            }
        },
        {
            "name": "packetsize",
            "getval": re.compile(
                r"""
                ^snmp-server(\spacketsize\s(?P<packetsize>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server packetsize {{packetsize}}",
            "result": {
                "packetsize": "{{ packetsize }}"
            }
        },
        {
            "name": "queue_length",
            "getval": re.compile(
                r"""
                ^snmp-server(\squeue-length\s(?P<queue_length>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server queue-length {{queue_length}}",
            "result": {
                "queue_length": "{{ queue_length }}"
            }
        },
        {
            "name": "targets",
            "getval": re.compile(
                r"""
                ^snmp-server(\starget\slist\s(?P<targets>\S+))
                (\shost\s(?P<host>\S+))?
                (\svrf\s(?P<vrf>\S+))?
                $""", re.VERBOSE),
            "setval": targets_tmplt,
            "result": {
                "targets": [
                    {
                        "name": "{{ targets }}",
                        "host": "{{host}}",
                        "vrf": "{{vrf}}",
                    }
                ]
            }
        },
        {
            "name": "throttle_time",
            "getval": re.compile(
                r"""
                ^snmp-server(\sthrottle-time\s(?P<throttle_time>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server throttle-time {{throttle_time}}",
            "result": {
                "throttle_time": "{{ throttle_time }}"
            }
        },
        {
            "name": "timeouts",
            "getval": re.compile(
                r"""
                ^snmp-server\stimeouts
                (\sduplicate\s(?P<duplicate>\d+))?
                (\sinQdrop\s(?P<inQdrop>\d+))?
                (\ssubagent\s(?P<subagent>\d+))?
                (\spdu\sstats\s(?P<pdu>\d+))?
                (\sthreshold\s(?P<threshold>\d+))?
                $""", re.VERBOSE),
            "setval": timeouts_tmplt,
            "result": {
                "timeouts": {
                    "subagent": "{{subagent}}",
                    "inQdrop": "{{inQdrop}}",
                    "duplicate": "{{duplicate}}",
                    "threshold": "{{threshold}}",
                    "pdu_stats": "{{pdu}}"

                }
            }
        },
        {
            "name": "trap",
            "getval": re.compile(
                r"""
                ^snmp-server\strap
                (\sauthentication\svrf\sdisable(?P<authentication_vrf_disable>))?
                (\slink\sietf(?P<link_ietf>))?
                (\sthrottle-time\s(?P<throttle_time>\d+))?
                $""", re.VERBOSE),
            "setval": trap_tmplt,
            "result": {
                "trap": {
                    "authentication_vrf_disable": "{{True if authentication_vrf_disable is defined}}",
                    "link_ietf": "{{True if link_ietf is defined}}",
                    "throttle_time": "{{throttle_time}}",

                }
            }
        },
        {
            "name": "trap_source",
            "getval": re.compile(
                r"""
                ^snmp-server(\strap-source\s(?P<trap_source>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server trap-source {{trap_source}}",
            "result": {
                "trap_source": "{{ trap_source }}"
            }
        },
        {
            "name": "trap_timeout",
            "getval": re.compile(
                r"""
                ^snmp-server(\strap-timeout\s(?P<trap_timeout>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server trap-timeout {{trap_timeout}}",
            "result": {
                "trap_timeout": "{{ trap_timeout }}"
            }
        },
        {
            "name": "traps",
            "getval": re.compile(
                r"""
                ^snmp-server\straps
                (\saddrpool\slow(?P<addrpool_low>))?
                (\saddrpool\shigh(?P<addrpool_high>))?
                (\sbfd(?P<bfd>))?
                (\sbgp\scbgp2(?P<bgp_cgp2>))?
                (\sbgp\supdown(?P<updown>))?
                (\sbulkstat\scollection(?P<bulkstat_collection>))?
                (\sbulkstat\stransfer(?P<bulkstat_transfer>))?
                (\sbridgemib(?P<bridgemib>))?
                (\scopy-complete(?P<copy_complete>))?
                (\scisco-entity-ext(?P<cisco_entity_ext>))?
                (\sconfig(?P<config>))?
                (\sdiameter\speerdown(?P<peerdown>))?
                (\sdiameter\speerup(?P<peerup>))?
                (\sdiameter\sprotocolerror(?P<protocolerror>))?
                (\sdiameter\spermanentfail(?P<permanentfail>))?
                (\sdiameter\stransientfail(?P<transientfail>))?
                (\sentity(?P<entity>))?
                (\sentity-redundancy\sall(?P<all>))?
                (\sentity-redundancy\sstatus(?P<status>))?
                (\sentity-redundancy\sswitchover(?P<switchover>))?
                (\sentity-state\soperstatus(?P<e_s_status>))?
                (\sentity-state\sswitchover(?P<e_s_switchover>))?
                (\sflash\sinsertion(?P<f_insertion>))?
                (\sflash\sremoval(?P<f_removal>))?
                (\sfru_ctrl(?P<fru_ctrl>))?
                (\shsrp(?P<hsrp>))?
                (\sipsla(?P<ipsla>))?
                (\sipsec\stunnel\sstart(?P<ipsec_start>))?
                (\sipsec\stunnel\sstop(?P<ipsec_stop>))?
                (\sisakmp\stunnel\sstart(?P<isakmp_start>))?
                (\sisakmp\stunnel\sstart(?P<isakmp_stop>))?
                (\sisis\sall(?P<isis_all>))?
                (\sisis(\sdatabase-overload(?P<database_overload>))?(\smanual-address-drops(?P<manual_address_drops>))?
                (\scorrupted-lsp-detected(?P<corrupted_lsp_detected>))?
                (\sattempt-to-exceed-max-sequence(?P<attempt_to_exceed_max_sequence>))?
                (\sid-len-mismatch(?P<id_len_mismatch>))?
                (\smax-area-addresses-mismatch(?P<max_area_addresses_mismatch>))?
                (\sown-lsp-purge(?P<own_lsp_purge>))?
                (\ssequence-number-skip(?P<sequence_number_skip>))?
                (\sauthentication-type-failure(?P<authentication_type_failure>))?
                (\sauthentication-failure(?P<authentication_failure>))?
                (\sversion-skew(?P<version_skew>))?
                (\sarea-mismatch(?P<area_mismatch>))?
                (\srejected-adjacency(?P<rejected_adjacency>))?
                (\slsp-too-large-to-propagate(?P<lsp_too_large_to_propagate>))?
                (\sorig-lsp-buff-size-mismatch(?P<orig_lsp_buff_size_mismatch>))?
                (\sprotocols-supported-mismatch(?P<protocols_supported_mismatch>))?
                (\sadjacency-change(?P<adjacency_change>))?
                (\slsp-error-detected(?P<lsp_error_detected>))?)?
                (\sl2tun\spseudowire-status(?P<pseudowire_status>))?
                (\sl2tun\ssessions(?P<sessions>))?
                (\sl2tun\stunnel-down(?P<tunnel_down>))?
                (\sl2tun\stunnel-up(?P<tunnel_up>))?
                (\sl2vpn\sall(?P<l2vpn_all>))?
                (\sl2vpn\scisco(?P<l2vpn_cisco>))?
                (\sl2vpn\svc-up(?P<vc_up>))?
                (\sl2vpn\svc-down(?P<vc_down>))?
                (\smsdp\speer-state-change(?P<msdp>))?
                (\sospf\slsa\slsa-maxage(?P<lsa_maxage>))?
                (\sospf\slsa\slsa-originate(?P<lsa_originate>))?
                (\sospf\serrors\sbad-packet(?P<bad_packet>))?
                (\sospf\serrors\sauthentication-failure(?P<authentication_failure_ospf>))?
                (\sospf\serrors\sconfig-error(?P<config_error>))?
                (\sospf\serrors\svirt-bad-packet(?P<virt_bad_packet>))?
                (\sospf\serrors\svirt-authentication-failure(?P<virt_authentication_failure>))?
                (\sospf\serrors\svirt-config-error(?P<virt_config_error>))?
                (\sospf\sretransmit\spackets(?P<packets>))?
                (\sospf\sretransmit\svirt-packets(?P<virt_packets>))?
                (\sospf\sstate-change\sif-state-change(?P<if_state_change>))?
                (\sospf\sstate-change\sneighbor-state-change(?P<neighbor_state_change>))?
                (\sospf\sstate-change\svirtif-state-change(?P<virtif_state_change>))?
                (\sospf\sstate-change\svirtneighbor-state-change(?P<virtneighbor_state_change>))?
                (\sospfv3\serrors\sbad-packet(?P<bad_packet_v3>))?
                (\sospfv3\serrors\svirt-config-error(?P<virt_config_error_v3>))?
                (\sospfv3\serrors\sconfig-error(?P<config_error_v3>))?
                (\sospf3\serrors\svirt-bad-packet(?P<virt_bad_packet_v3>))?
                (\sospfv3\sstate-change\sif-state-change(?P<if_state_change_3>))?
                (\sospfv3\sstate-change\sneighbor-state-change(?P<neighbor_state_change_v3>))?
                (\sospfv3\sstate-change\svirtif-state-change(?P<virtif_state_change_v3>))?
                (\sospfv3\sstate-change\svirtneighbor-state-change(?P<virtneighbor_state_change_v3>))?
                (\sospfv3\sstate-change\srestart-status-change(?P<restart_status_change>))?
                (\sospfv3\sstate-change\srestart-helper-status-change(?P<restart_helper_status_change>))?
                (\sospfv3\sstate-change\srestart-virtual-helper-status-change(?P<restart_virtual_helper_status_change>))?
                (\sospfv3\sstate-change\snssa_state_change(?P<nssa_state_change>))?
                (\spower(?P<power>))?
                (\srf(?P<rf>))?
                (\spim\sneighbor-change(?P<neighbor_change>))?
                (\spim\sinvalid-message-received(?P<invalid_message_received>))?
                (\spim\srp-mapping-change(?P<rp_mapping_change>))?
                (\spim\sinterface-state-change(?P<interface_state_change>))?
                (\srsvp\slost-flow(?P<lost_flow>))?
                (\srsvp\snew-flow(?P<new_flow>))?
                (\srsvp\sall(?P<rsvpall>))?
                (\sselective-vrf-download\srole-change(?P<selective_vrf_download_role_change>))?
                (\ssensor(?P<sensor>))?
                (\svrrp\sevents(?P<vrrp_events>))?
                (\ssyslog(?P<syslog>))?
                (\ssystem(?P<system>))?
                (\ssubscriber\ssession-agg\saccess-interface(?P<session_agg_access_interface>))?
                (\ssubscriber\ssession-agg\snode(?P<session_agg_node>))?
                (\svpls\sall(?P<vpls_all>))?
                (\svpls\sfull-clear(?P<full_clear>))?
                (\svpls\sfull-raise(?P<full_raise>))?
                (\svpls\sstatus(?P<vpls_status>))?
                (\ssnmp\slinkup(?P<linkup>))?
                (\ssnmp\slinkdown(?P<linkdown>))?
                (\ssnmp\scoldstart(?P<coldstart>))?
                (\ssnmp\swarmstart(?P<warmstart>))?
                (\ssnmp\sauthentication(?P<authentication>))?
                $""", re.VERBOSE),
            "setval": traps_tmplt,
            "result": {
                "traps": {
                    "addrpool": {
                        "low": "{{True if addrpool_low is defined}}",
                        "high": "{{True if addrpool_high is defined}}",
                    },
                    "bfd": "{{True if bfd is defined}}",
                    "bgp": {
                        "cbgp2": "{{True if bgp_cgp2 is defined}}",
                        "updown": "{{True if updown is defined}}"
                    },
                    "bulkstat_collection": "{{True if bulkstat_collection is defined}}",
                    "bulkstat_transfer": "{{True if bulkstat_tranfer is defined}}",
                    "bridgemib": "{{True if bridgemib is defined}}",
                    "copy_complete": "{{True if copy_complete is defined}}",
                    "cisco_entity_ext": "{{True if cisco_entity_ext is defined}}",
                    "config": "{{True if config is defined}}",
                    "diameter": {
                        "peerdown": "{{True if peerdown is defined}}",
                        "peerup": "{{True if peerup is defined}}",
                        "protocolerror": "{{True if protocolerror is defined }}",
                        "permanentfail": "{{True if permanentfail is defined}}",
                        "transientfail": "{{True if transientfail is defined}}"
                    },
                    "entity": "{{True if entity is defined}}",
                    "entity_redundancy": {
                        "all": "{{True if all is defined }}",
                        "status": "{{True if status is defined}}",
                        "switchover": "{{True if switchover is defined}}"
                    },
                    "entity_state": {
                        "operstatus": "{{True if e_s_status is defined }}",
                        "switchover": "{{True if e_s_switchover is defined }}"
                    },
                    "flash": {
                        "insertion": "{{True if f_insertion is defined }}",
                        "removal": "{{True if f_removal is defined }}"
                    },
                    "fru_ctrl": "{{True if fru_ctrl is defined}}",
                    "hsrp": "{{True if hsrp is defined}}",
                    "ipsla": "{{True if ipsla is defined}}",
                    "ipsec": {
                        "start": "{{True if ipsec_start is defined}}",
                        "stop": "{{True if ipsec_stop is defined}}",
                    },
                    "isakmp": {
                        "start":"{{True if isakmp_start is defined}}",
                        "stop": "{{True if isakmp_stop is defined}}",
                    },
                    "isis": {
                        "all": "{{True if isis_all is defined}}",
                        "id_len_mismatch": "{{True if id_len_mismatch is defined}}",
                        "database_overload": "{{True if database_overload is defined}}",
                        "manual_address_drops": "{{True if manual_address_drops is defined}}",
                        "corrupted_lsp_detected": "{{True if corrupted_lsp_detected is defined}}",
                        "attempt_to_exceed_max_sequence": "{{True if attempt_to_exceed_max_sequence is defined}}",
                        "max_area_addresses_mismatch": "{{True if max_area_addresses_mismatch is defined}}",
                        "own_lsp_purge": "{{True if own_lsp_purge is defined}}",
                        "sequence_number_skip":"{{True if sequence_number_skip is defined}}",
                        "authentication_type_failure": "{{True if authentication_type_failure is defined}}",
                        "authentication_failure": "{{True if authentication_failure is defined}}",
                        "version_skew": "{{True if version_skew is defined}}",
                        "area_mismatch": "{{True if area_mismatch is defined}}",
                        "rejected_adjacency": "{{True if rejected_adjacency is defined}}",
                        "lsp_too_large_to_propagate": "{{True if lsp_too_large_to_propagate is defined}}",
                        "orig_lsp_buff_size_mismatch": "{{True if orig_lsp_buff_size_mismatch is defined}}",
                        "protocols_supported_mismatch": "{{True if protocols_supported_mismatch is defined}}",
                        "adjacency_change": "{{True if adjacency_change is defined}}",
                        "lsp_error_detected": "{{True if lsp_error_detected is defined}}"

                    },
                    "l2tun": {
                        "pseudowire_status": "{{True if pseudowire_status is defined}}",
                        "sessions": "{{True if sessions is defined}}",
                        "tunnel_down": "{{True if tunnel_down is defined}}",
                        "tunnel_up": "{{True if tunnel_up is defined }}"
                    },
                    "l2vpn": {
                        "all": "{{True if l2vpn_all is defined}}",
                        "cisco": "{{True if cisco is defined}}",
                        "vc_up": "{{True if vc_up is defined}}",
                        "vc_down": "{{True if vc_down is defined}}",
                    },
                    "msdp_peer_state_change": "{{True if msdp is defined}}",
                    "ntp": "{{True if ntp is defined}}",
                    "ospf": {
                        "errors": {
                            "bad_packet": "{{True if bad_packet is defined}}",
                            "authentication_failure": "{{True if authentication_failure_ospf is defined}}",
                            "config_error": "{{True if config_error is defined}}",
                            "virt_bad_packet": "{{True if virt_bad_packet is defined}}",
                            "virt_authentication_failure": "{{True if virt_authentication_failure is defined}}",
                            "virt_config_error": "{{True if virt_config_error is defined}}"
                        },
                        "lsa": {
                            "lsa_maxage": "{{True if lsa_maxage is defined}}",
                            "lsa_originate": "{{True if lsa_originate is defined}}"
                        },
                        "retransmit": {
                            "packets": "{{True if packets is defined}}",
                            "virt_packets": "{{True if virt_packets is defined}}"
                        },
                        "state_change": {
                            "if_state_change": "{{True if if_state_change is defined}}",
                            "neighbor_state_change": "{{True if neighbor_state_change is defined}}",
                            "virtif_state_change": "{{True if virtif_state_change is defined}}",
                            "virtneighbor_state_change": "{{True if virtneighbor_state_change is defined}}"
                        }

                    },
                    "ospfv3": {
                        "errors": {
                            "bad_packet": "{{True if bad_packet_v3 is defined}}",
                            "config_error": "{{True if config_error_v3 is defined}}",
                            "virt_bad_packet": "{{True if virt_bad_packet_v3 is defined}}",
                            "virt_config_error": "{{True if virt_config_error_v3 is defined}}"
                        },
                        "state_change": {
                            "if_state_change": "{{True if if_state_change_v3 is defined}}",
                            "neighbor_state_change": "{{True if neighbor_state_change_v3 is defined}}",
                            "virtif_state_change": "{{True if virtif_state_change_v3 is defined}}",
                            "virtneighbor_state_change": "{{True if virtneighbor_state_change_v3 is defined}}",
                            "nssa_state_change": "{{True if nssa_state_change is defined}}",
                            "restart_status_change": "{{True if restart_status_change is defined}}",
                            "restart_helper_status_change": "{{True if restart_helper_status_change is defined}}",
                            "restart_virtual_helper_status_change": "{{True if restart_virtual_helper_status_change is defined}}"
                        }

                    },
                    "power": "{{True if power is defined }}",
                    "rf": "{{True if rf is defined}}",
                    "pim": {
                        "interface_state_change": "{{True if interface_state_change is defined}}",
                        "invalid_message_received": "{{True if invalid_message_received is defined}}",
                        "neighbor_change": "{{True if neighbor_change is defined}}",
                        "rp_mapping_change": "{{True if rp_mapping_change is defined}}"
                     },
                    "rsvp": {
                        "all": "{{True if rsvpall is defined}}",
                        "lost_flow": "{{True if lost_flow is defined}}",
                        "new_flow": "{{True if new_flow is defined}}"
                    },
                    "selective_vrf_download_role_change": "{{True if selective_vrf_download_role_change is defined}}",
                    "sensor": "{{True if sensor is defined}}",
                    "vrrp_events": "{{True if vrrp_events is defined}}",
                    "syslog": "{{True if syslog is defined}}",
                    "system": "{{True if system is defined}}",
                    "subscriber": {
                        "session_agg_access_interface": "{{True if session_agg_access_interface is defined}}",
                        "session_agg_node": "{{True if session_agg_node is defined}}"
                    },
                    "vpls": {
                        "all": "{{True if vpls_all is defined}}",
                        "status": "{{True if vpls_status is defined}}",
                        "full_clear": "{{True if full_clear is defined}}",
                        "full_raise": "{{True if full_raise is defined}}"
                    },
                    "snmp": {
                        "authentication": "{{True if authentication is defined}}",
                        "coldstart": "{{True if coldstart is defined}}",
                        "warmstart": "{{True if warmstart is defined}}",
                        "linkdown": "{{True if linkdown is defined}}",
                        "linkup": "{{True if linkup is defined}}"
                    }
                }
            }
        },
        {
            "name": "users",
            "getval": re.compile(
                r"""
                ^snmp-server\suser
                (\s(?P<name>\S+))
                (\s(?P<group>\S+))
                (\s(?P<version>v1|v2c|v3))
                (\sIPv4\s(?P<ipv4>\S+))?
                (\sIPv6\s(?P<ipv6>\S+))?
                (\s(?P<v4acl>\S+))?
                (\sSDROwner\s(?P<sdrowner>))?
                (\sSystemOwner\s(?P<systemowner>))?
                $""", re.VERBOSE),
            "setval": user_tmplt,
            "result": {
                "users": [
                    {
                        "user": "{{ name }}",
                        "group": "{{ group }}",
                        "Ipv4_acl": "{{ipv4}}",
                        "Ipv6_acl": "{{ipv6}}",
                        "SDROwner": "{{True if sdowner is defined}}",
                        "SystemOwner": "{{True if systemowner is defined }}",
                        "v4_acl": "{{v4acl}}",
                        "version": "{{version}}"
                    }
                ]
            }
        },
        {
            "name": "vrfs",
            "getval": re.compile(
                r"""
                ^snmp-server\svrf
                (\s(?P<vrf>\S+))
                (\scontext\s(?P<context>\S+))?
                ((\shost\s(?P<host>\S+))?
                (\s(?P<traps>traps))?
                (\s(?P<informs>informs))?
                (\sversion\s(?P<version>1|2c|3))?
                (\s(?P<community>\S+))?
                (\sudp-port\s(?P<port>\d+))?)?

                $""", re.VERBOSE),
            "setval": "snmp-server vrf {{vrf}}",
            "result": {
                "vrfs": {
                    "{{vrf}}": {
                        "vrf": "{{vrf}}",
                        "context": {
                            "{{context if context is defined}}": "{{context if context is defined}}"
                        },
                        "hosts": [
                                    {
                                        "host": "{{ host }}",
                                        "traps": "{{True if traps is defined}}",
                                        "informs": "{{True if informs is defined}}",
                                        "community": "{{community}}",
                                        "udp_port": "{{port}}",
                                        "version": "{{version}}"
                                    }
                        ]
                    }
                }
            }
        },





    ]
    # fmt: on
