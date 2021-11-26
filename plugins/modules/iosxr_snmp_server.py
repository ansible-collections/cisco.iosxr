#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_snmp_server
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: iosxr_snmp_server
short_description: Manages snmp-server resource module
description: This module configures and manages the attributes of snmp-server on Cisco
  IOSXR platforms.
version_added: 2.6.0
author: Ashwini Mhatre (@amhatre)
notes:
- Tested against Cisco Iosxr 7.0.2
- This module works with connection C(network_cli).
options:
  config:
    description: SNMP server configuration.
    type: dict
    suboptions:
      chassis_id:
        description: SNMP chassis identifier.
        type: str
      community:
        description: Enable SNMP;  set community string and access privileges.
        type: list
        elements: dict
        suboptions:
          name:
            description: Community name.
            type: str
          acl_v4:
            description: standard access-list name.
            type: str
          acl_v6:
            description: IPv6 access list name.
            type: str
          ro:
            description: Only reads are permitted.
            type: bool
          rw:
            description: Read-write access.
            type: bool
          sdrowner:
            type: bool
            description: SDR Owner permissions for MIB Objects.
          systemowner:
            type: bool
            description: System Owner permissions for MIB objects.
          v4_acl:
            description: V4 Access-list name.
            type: str
      community_map:
        description: Community Mapping as per RFC-2576.
        type: list
        elements: dict
        suboptions:
          name:
            description: Community name
            type: str
          context:
            description: Context Name for the community mapping.
            type: str
          security_name:
            description: Security Name for the community mapping.
            type: str
          target_list:
            description: list of targets valid with this community.
            type: str
      correlator:
        description: Configure properties of the event correlator
        type: dict
        suboptions:
          buffer_size:
            type: int
            description: Configure size of the correlator buffer.
          rules:
            type: list
            elements: dict
            description: Configure a specified correlation rule.
            suboptions:
              rule_name:
                type: str
                description: name of rule.
              timeout:
                type: int
                description: Specify timeout.
          rule_sets:
            type: list
            elements: dict
            description: Configure a specified correlation ruleset.
            suboptions:
              name:
                type: str
                description: Name of the ruleset
      contact:
        description: Person to contact about the syste,.
        type: str
      context:
        description: Create/Delete a context apart from default
        type: list
        elements: str
      drop:
        type: dict
        description: Silently drop SNMP packets
        suboptions:
          unknown_user:
            description: Silently drop unknown v3 user packets
            type: bool
          report_IPv4:
            description: Config to drop snmpv3 error reports matching Ipv4 ACL.
            type: str
          report_IPv6:
            description: Config to drop snmpv3 error reports matching Ipv4 ACL.
            type: str
      engineid:
        description: SNMPv3 engine ID configuration.
        type: dict
        suboptions:
          local:
            description:  Local SNMP agent
            type: str
      groups:
        description: SNMP USM group
        type: list
        elements: dict
        suboptions:
          group:
            description: SNMP group for the user
            type: str
          version:
            description: snmp security group version
            type: str
            choices: ['v1', 'v3', 'v2c']
          context:
            description: Specify a context to associate with the group
            type: str
          notify:
            description: View to restrict notifications
            type: str
          read:
            description: View to restrict read access
            type: str
          write:
            description: View to restrict write access
            type: str
          Ipv4_acl:
            description: Ipv4 Type of Access-list
            type: str
          Ipv6_acl:
            description: Ipv6 Type of Access-list
            type: str
          v4_acl:
            description: V4 Access-list name
            type: str
      hosts: &hosts
        description: Notification destinations
        type: list
        elements: dict
        suboptions:
          host:
            description: Hostname or IP address of SNMP notification host.
            type: str
          community:
            description: community string.
            type: str
          udp_port:
            description: UDP destination port for notification messages.
            type: int
          informs:
            description: Use SNMP inform messages.
            type: bool
          traps:
            description: Use SNMP trap messages
            type: bool
          version:
            description: Notification message SNMP version.
            type: str
            choices: ['1', '2c', '3']
      ifindex:
        description: Enable ifindex persistence
        type: bool
      ifmib:
        type: dict
        description: IF-MIB configuration commands.
        suboptions:
          ifalias_long:
            type: bool
            description: Modify parameters for ifAlias object.
          internal_cache_max_duration:
            type: int
            description: IFMIB internal lookahead cache.
          ipsubscriber:
            type: bool
            description: Enable ipsubscriber interfaces in IFMIB.
          stats:
            type: bool
            description: Modify IF-MIB statistics parameters.
      inform:
        description: Configure SNMP Informs options
        suboptions:
          pending:
            description: Set number of unacked informs to hold
            type: int
          retries:
            description: Set retry count for informs
            type: int
          timeout:
            description: Set timeout for informs
            type: int
        type: dict
      interfaces:
        type: list
        elements: dict
        description: Enter the SNMP interface configuration commands.
        suboptions:
          name:
            type: str
            description: Name of interface.
          notification_linkupdown_disable:
            type: bool
            description: Disable linkUp and linkDown notification.
          index_persistent:
            type: bool
            description: Configure ifIndex attributes Persistency across system reloads.
      ipv4: &ip
        description: Mark the dscp/precedence bit for ipv4 packets.
        type: dict
        suboptions:
          dscp:
            description: Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries.
            type: str
          precedence:
            description: Set precedence Please refer vendor document for valid entries.
            type: str
      ipv6: *ip
      location:
        description: The sysLocation string.
        type: str
      logging_threshold_oid_processing:
        type: int
        description: Configure threshold to start logging slow OID requests processing.
      logging_threshold_pdu_processing:
        type: int
        description: Configure threshold to start logging slow PDU requests processing.
      mib_bulkstat_max_procmem_size:
        type: int
        description: per process memory limit in kilo bytes
      mib_object_lists:
        type: list
        elements: str
      mib_schema:
        type: list
        elements: dict
        suboptions:
          name:
            type: str
            description: mib schema name.
          object_list:
            type: str
            description: Name of an object List.
          poll_interval:
            type: int
            description: Periodicity for polling of objects in this schema in Min.
      mib_bulkstat_transfer_ids:
        type: list
        elements: dict
        suboptions:
          name:
            type: str
            description: mib transfer-id name.
          buffer_size:
            type: int
            description: Bulkstat data file maximum size.
          enable:
            type: bool
            description: Start Data Collection for this Configuration
          format_schemaASCI:
            type: bool
            description: format
          retain:
            type: int
            description: Retention period in Min.
          retry:
            type: int
            description: Number of Retries.
          schema:
            type: str
            description: Schema that contains objects to be collected.
          transfer_interval:
            type: int
            description: transfer-interval
      mroutemib_send_all_vrf:
        type: bool
        description: Configurations related to IPMROUTE-MIB(cisco-support).
      notification_log_mib:
        type: dict
        suboptions:
          GlobalSize:
            type: int
            description: GlobalSize, max number of notifications that can be logged in all logs.
          default:
            type: bool
            description: To create a default log
          disable:
            type: bool
            description: disable, to disable the logging in default log.
          size:
            description: size, The max number of notifications that this log (default) can hold.
            type: int
      oid_poll_stats:
        type: bool
        description: Enable OID poll stats oper CLI
      overload_control:
        type: dict
        description: Set overload-control params for handling incoming messages in critical processing mode.
        suboptions:
          overload_drop_time:
            type: int
            description: Overload drop time (in seconds) for incoming queue (default 1 sec).
          overload_throttle_rate:
            type: int
            description: Overload throttle rate for incoming queue (default 500 msec)
      packetsize:
        type: int
        description: Largest SNMP packet size.
      queue_length:
        type: int
        description: Queue length (default 100).
      targets:
        type: list
        elements: dict
        suboptions:
          name:
            type: str
            description: Name of the target list.
          host:
            type: str
            description: Specify host name.
          vrf:
            type: str
            description: Specify VRF name.
      throttle_time:
        type: int
        description: Set throttle time for handling incoming messages.
      timeouts:
        type: dict
        description: SNMP timeouts
        suboptions:
          duplicate:
            decsription: Duplicate request feature timeout
            type: int
          inQdrop:
            type: int
            description: incoming queue drop feature.
          pdu_stats:
            type: int
            description: SNMP pdu statistics end to end.
          subagent:
            type: int
            description: Sub-Agent Request timeout.
          threshold:
            type: int
            description: threshold incoming queue drop feature.
      trap:
        type: dict
        description: MIB trap configurations.
        suboptions:
          authentication_vrf_disable:
            type: bool
            description: Disable authentication traps for packets on a vrf.
          link_ietf:
            type: bool
            description: Link up/down trap configuratio.
          throttle_time:
            type: int
            description: Set throttle time for handling more traps.
      trap_source:
        description: Assign an interface for the source address of all traps
        type: str
      trap_timeout:
        description: Set timeout for TRAP message retransmissions
        type: int
      traps:
        description: Enable traps to all configured recipients.
        type: dict
        suboptions:
          addrpool:
            type: dict
            description: Enable SNMP Address Pool traps.
            suboptions:
              low:
                type: bool
                description: Enable SNMP Address Pool Low Threshold trap.
              high:
                type: bool
                description: Enable SNMP Address Pool High Threshold trap.
          bfd:
            type: bool
            description: Enable BFD traps.
          bgp:
            description: Enable Bgp traps.
            type: dict
            suboptions:
              cbgp2:
                type: bool
                description: Enable CISCO-BGP4-MIB v2 traps.
              updown:
                type: bool
                description: Enable CISCO-BGP4-MIB v2 up/down traps.
          bulkstat_collection:
            type: bool
            description: Enable Data-Collection-MIB Collection notifications.
          bulkstat_transfer:
            type: bool
            description: Enable Data-Collection-MIB Trnasfer notifications.
          bridgemib:
            type: bool
            description: Enable SNMP Trap for Bridge MIB.
          copy_complete:
            type: bool
            description: Enable CISCO-CONFIG-COPY-MIB ccCopyCompletion traps.
          cisco_entity_ext:
            type: bool
            description: Enable SNMP entity traps
          config:
            type: bool
            description: Enable SNMP config traps.
          diameter:
            type: dict
            description: Enable SNMP diameter traps.
            suboptions:
              peerdown:
                type: bool
                description: Enable peer connection down notification.
              peerup:
                type: bool
                description: Enable peer connection up notification.
              permanentfail:
                type: bool
                description: Enable permanent failure notification.
              protocolerror:
                type: bool
                description: Enable protocol error notifications
              transientfail:
                type: bool
                description: Enable transient failure notification.
          entity:
            type: bool
            description: Enable SNMP entity traps.
          entity_redundancy:
            type: dict
            description: Enable SNMP CISCO-ENTITY-REDUNDANCY-MIB traps.
            suboptions:
              all:
                type: bool
                description: Enable all CISCO-ENTITY-REDUNDANCY-MIB traps
              status:
                type: bool
                description: Enable status change traps
              switchover:
                type: bool
                description: Enable switchover traps.
          entity_state:
            type: dict
            description: Enable SNMP entity-state traps.
            suboptions:
              operstatus:
                type: bool
                description: Enable entity oper status enable notification.
              switchover:
                description: Enable entity state switchover notifications
                type: bool
          flash:
            type: dict
            description: Enable  flash-mib traps.
            suboptions:
              insertion:
                type: bool
                descriptioon: Enable ciscoFlashDeviceInsertedNotif.
              removal:
                type: bool
                description: Enable ciscoFlashDeviceRemovedNotif.
          fru_ctrl:
            type: bool
            description: Enable SNMP entity FRU control traps.
          hsrp:
            type: bool
            description: Enable SNMP hsrp traps.
          ipsla:
            type: bool
            description: Enable SNMP hipsla traps.
          ipsec:
            type: dict
            description: Enable SNMP IPSec traps.
            suboptions:
              start:
                type: bool
                description: Enable SNMP IPsec Tunnel Start trap.
              stop:
                type: bool
                description: Enable SNMP IPsec Tunnel Stop trap.
          isakmp:
            type: dict
            description: Enable SNMP isakmp traps.
            suboptions:
              start:
                type: bool
                description: Enable SNMP isakmp Tunnel Start trap.
              stop:
                type: bool
                description: Enable SNMP isakmp Tunnel Stop trap.

          isis:
            description: Enable isis traps. If set to enabled , all the traps are set.
            type: dict
            suboptions:
              adjacency_change:
                description: adjacency-change
                type: bool
              all:
                type: bool
                description: anable all is-is traps.
              area_mismatch:
                description: area-mismatch
                type: bool
              attempt_to_exceed_max_sequence:
                description: attempt-to-exceed-max-sequence
                type: bool
              authentication_failure:
                description: authentication-failure.
                type: bool
              authentication_type_failure:
                description: authentication-type-failure.
                type: bool
              corrupted_lsp_detected:
                description: isisCorruptedLSPDetected
                type: bool
              database_overload:
                description: database-overload
                type: bool
              id_len_mismatch:
                type: bool
                description: isisIDLenMismatch
              lsp_error_detected:
                type: bool
                description: lsp-error-detected.
              lsp_too_large_to_propagate:
                type: bool
                description: lsp-too-large-to-propagate
              manual_address_drops:
                type: bool
                description: manual_address_drops
              max_area_addresses_mismatch:
                type: bool
                description: max_area_addresses_mismatch
              orig_lsp_buff_size_mismatch:
                type: bool
                description: orig-lsp-buff-size-mismatch
              version_skew:
                type: bool
                description: version-skew
              own_lsp_purge:
                description: own-lsp-purge
                type: bool
              rejected_adjacency:
                description: rejected-adjacency
                type: bool
              protocols_supported_mismatch:
                description: protocols-supported-mismatch
                type: bool
              sequence_number_skip:
                description: sequence-number-skip.
                type: bool
          l2tun:
            type: dict
            description: Enable L2TUN traps.
            suboptions:
              pseudowire_status:
                type: bool
                description: Enable L2TUN pseudowire status traps.
              sessions:
                type: bool
                description: Enable L2TUN sessions traps.
              tunnel_down:
                type: bool
                description: Enable L2TUN tunnel DOWN traps.
              tunnel_up:
                type: bool
                description: Enable L2TUN tunnel UP traps.
          l2vpn:
            type: dict
            description: Enable L2VPN traps.
            suboptions:
              all:
                type: bool
                description: Enable L2VPN ALL traps.
              cisco:
                type: bool
                description: Enable L2VPN CISCO  traps.
              vc_down:
                type: bool
                description: Enable L2VPN VC DOWN traps.
              vc_up:
                type: bool
                description: Enable L2VPN VC UP traps.
          msdp_peer_state_change:
            type: bool
            decsription: Enable SNMP MSDP traps
          ntp:
            type: bool
            description: Enable SNMP Cisco Ntp traps.
          ospf:
            description: Enable Ospf traps. If set to enabled , all the traps are set.
            type: dict
            suboptions:
              errors:
                description: error
                type: dict
                suboptions:
                  bad_packet:
                    type: bool
                    description: bad-packet
                  authentication_failure:
                    type: bool
                    description: authentication-failure.
                  config_error:
                    type: bool
                    description: config-error
                  virt_bad_packet:
                    type: bool
                    description: virt-bad-packet
                  virt_authentication_failure:
                    type: bool
                    description: virt-authentication-failure
                  virt_config_error:
                    type: bool
                    description: virt_config_error
              lsa:
                description: lsa
                type: dict
                suboptions:
                  lsa_maxage:
                    type: bool
                    description: lsa-maxage
                  lsa_originate:
                    type: bool
                    description: lsa-originate
              retransmit:
                description: retransmit
                type: dict
                suboptions:
                  packets:
                    type: bool
                    description: packets
                  virt_packets:
                    type: bool
                    description: virt-packets
              state_change:
                description: state-change.
                type: dict
                suboptions:
                  if_state_change:
                    type: bool
                    description: if-state-change
                  neighbor_state_change:
                    type: bool
                    description: neighbor-state-change
                  virtif_state_change:
                    type: bool
                    description: virtif-state-change
                  virtneighbor_state_change:
                    type: bool
                    description: virtneighbor-state-change
          ospfv3:
            description: Enable Ospfv3 traps. If set to enabled , all the traps are set.
            type: dict
            suboptions:
              errors:
                description: error
                type: dict
                suboptions:
                  bad_packet:
                    type: bool
                    description: bad-packet
                  config_error:
                    type: bool
                    description: config-error
                  virt_bad_packet:
                    type: bool
                    description: virt-bad-packet
                  virt_config_error:
                    type: bool
                    description: virt_config_error
              state_change:
                description: state-change.
                type: dict
                suboptions:
                  if_state_change:
                    type: bool
                    description: if-state-change
                  neighbor_state_change:
                    type: bool
                    description: neighbor-state-change
                  virtif_state_change:
                    type: bool
                    description: virtif-state-change
                  virtneighbor_state_change:
                    type: bool
                    description: virtneighbor-state-change
                  nssa_state_change:
                    type: bool
                    description: nssa-state-change
                  restart_status_change:
                    type: bool
                    description: restart-status-change
                  restart_helper_status_change:
                    type: bool
                    description: restart-helper-status-change
                  restart_virtual_helper_status_change:
                    type: bool
                    description: restart-virtual-helper-status-change
          power:
            type: bool
            description: Enable SNMP entity power traps.
          rf:
            type: bool
            description: Enable SNMP RF-MIB traps.
          pim:
            description: Enable Pim traps. If set to enabled , all the traps are set.
            type: dict
            suboptions:
              interface_state_change :
                description: interface-state-change .
                type: bool
              invalid_message_received :
                description: invalid-message-received
                type: bool
              neighbor_change:
                description: neighbor-change.
                type: bool
              rp_mapping_change:
                description: rp-mapping-change.
                type: bool
          rsvp:
            description: Enable rsvp traps. If set to enabled , all the traps are set.
            type: dict
            suboptions:
              all:
                description: enable all traps.
                type: bool
              lost_flow:
                description: lost-flow
                type: bool
              new_flow:
                description: new-flow
                type: bool
          selective_vrf_download_role_change:
            type: bool
            description: Enable selective VRF download traps.
          sensor:
            type: bool
            description: Enable SNMP entity sensor traps
          snmp:
            description: Enable snmp traps. If set to enabled , all the traps are set.
            type: dict
            suboptions:
              authentication:
                description: authentication
                type: bool
              linkdown:
                description: link-down
                type: bool
              linkup:
                description: link-up
                type: bool
              warmstart:
                description: warmstart.
                type: bool
              coldstart:
                description: coldstart.
                type: bool
          vrrp_events:
            description: vrrp
            type: bool
          syslog:
            type: bool
            description: syslog
          subscriber:
            type: dict
            description: Subscriber notification commands.
            suboptions:
              session_agg_access_interface:
                type: bool
                description: Subscriber notification at access interface level
              session_agg_node:
                type: bool
                description: Subscriber notification at node level
          system:
            type: bool
            description: Enable SNMP SYSTEMMIB-MIB traps.
          vpls:
            type: dict
            description: Enable VPLS traps
            suboptions:
              all:
                type: bool
                description: Enable all VPLS traps.
              full_clear:
                type: bool
                description: Enable VPLS Full Clear traps.
              full_raise:
                type: bool
                description: Enable VPLS Full Raise traps.
              status:
                type: bool
                description: Enable VPLS Status traps
      users:
        description: SNMP user configuration.
        type: list
        elements: dict
        suboptions:
          user:
            description: SNMP user name
            type: str
          group:
            description: SNMP group for the user.
            type: str
          Ipv4_acl:
            description: Type of Access-list
            type: str
          Ipv6_acl:
            description: Type of Access-list
            type: str
          SDROwner:
            description:  SDR Owner permissions for MIB Objects.
            type: bool
          SystemOwner:
            description: System Owner permissions for MIB objects.
            type: bool
          v4_acl:
            type: str
            description: V4 Access-list name
          version:
            description: snmp security version
            type: str
            choices: ['v1', 'v2c', 'v3']
      vrfs:
        description: Specify the VRF in which the source address is used
        type: list
        elements: dict
        suboptions:
          vrf:
            description: vrf name.
            type: str
          context:
            description: Configure the source interface for SNMP notifications
            type: list
            elements: str
          hosts: *hosts
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the IOSXR device by
      executing the command B(show running-config snmp-server).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state the configuration should be left in.
    - The states I(replaced) and I(overridden) have identical
       behaviour for this module.
    - Please refer to examples for more details.
    type: str
    choices: [deleted, merged, overridden, replaced, gathered, rendered, parsed]
    default: merged
"""

EXAMPLES = """

"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.snmp_server.snmp_server import (
    Snmp_serverArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.snmp_server.snmp_server import (
    Snmp_server,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Snmp_serverArgs.argument_spec,
        mutually_exclusive=[["config", "running_config"]],
        required_if=[
            ["state", "merged", ["config"]],
            ["state", "replaced", ["config"]],
            ["state", "overridden", ["config"]],
            ["state", "rendered", ["config"]],
            ["state", "parsed", ["running_config"]],
        ],
        supports_check_mode=True,
    )

    result = Snmp_server(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
