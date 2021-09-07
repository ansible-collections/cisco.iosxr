#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_ntp_global
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: iosxr_ntp_global
short_description: Manages ntp resource module
description: This module configures and manages the attributes of  ntp on Cisco
  IOSXR platforms.
version_added: 2.5.0
author: Ashwini Mhatre (@amhatre)
notes:
  - Tested against IOSXR 7.0.2.
  - This module works with connection C(network_cli).
options:
  config:
    description: A dictionary of ntp options
    type: dict
    suboptions:
        access_group:
          description: Control NTP access
          type: list
          elements: dict
          suboptions:
            ipv4: &ipv4
              type: dict
              description: Configure IPv4 access
              suboptions:
                peer: &peer
                  type: str
                  description: Provide full access
                query_only: &query_only
                  type: str
                  description: Allow only control queries.
                serve: &serve
                  type: str
                  description: Provide server and query access.
                serve_only: &serve_only
                  type: str
                  description: Provide only server access.
            ipv6: &ipv6
              type: dict
              description: Configure IPv6 access
              suboptions:
                peer: *peer
                query_only: *query_only
                serve: *serve
                serve_only: *serve_only
            vrf:
              type: dict
              description: Specify non-default VRF.
              suboptions:
                name:
                  type: str
                  description: Specify non-default VRF.
                ipv4: *ipv4
                ipv6: *ipv6
        authenticate:
          description: Authenticate time sources
          type: bool
        authentication_keys:
          description: Authentication key for trusted time sources
          type: list
          elemnets: dict
          suboptions:
            id:
              description: <1-65535>  Key number
              type: int
            key:
              description: Authentication key.
              type: str
              no_log: True
            encrypted:
              description: Type of key encrypted or clear-text.
              type: bool
        broadcastdelay:
          type: int
          description: Estimated round-trip delay in microseconds.
        drift:
          type: dict
          description: Drift(cisco-support)
          suboptions:
            aging_time:
              type: int
              description: Aging time in hours.
            file:
              description: File for drift values.
              type: str
        interfaces:
          type: list
          elements: dict
          description: Configure NTP on an interface.
          suboptions:
            broadcast_client:
              type: bool
              description: Listen to NTP broadcasts
            broadcast:
              type: dict
              description: Configure NTP broadcast service.
              suboptions:
                destination:
                  type: str
                  description: Configure broadcast destination address.
                key:
                  type: int
                  description: Broadcast key number.
                version:
                  type: int
                  description: <2-4>  NTP version number.
            multicast:
              type: dict
              description: Configure NTP multicast service.
              suboptions:
                key:
                  type: int
                  description: Configure multicast authentication key.
                ttl:
                  type: int
                  description: Configure TTL to use.
                client:
                  type: str
                  description:
                destination:
                  type: str
                  description:
                version:
                  type: int
                  description: <2-4>  NTP version number.
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
              choices: [ "critical", "flash", "flash-override", "immediate", "internet", "network", "priority", "routine" ]
        ipv6: *ip
        log_internal_sync:
          type: bool
          description: Logs internal synchronization changes.
        master:
          type: int
          description: Use NTP as clock source with stratum number <1-15>
        max_associations:
          type: int
          description: <0-4294967295>  Number of associations.
        passive:
          type: bool
          description: Enable the passive associations.
        trusted_keys:
          type: list
          elements: int
          description: Key numbers for trusted time sources.
        update_calendar:
          type: bool
          description: Periodically update calendar with NTP time.
        source:
          type: str
          description: Configure default interface.
        servers:
          description: Configure NTP server.
          type: list
          elements: dict
          suboptions:
            vrf: &vrf
              description: vrf name.
              type: str
            server: &host
              description: Hostname or A.B.C.D or A:B:C:D:E:F:G:H.
              type: str
              required: True
            burst: &burst
              description: Use burst mode.
              type: bool
            iburst: &iburst
              description: Use initial burst mode.
              type: bool
            key: &key
              description: SConfigure peer authentication key
              type: int
            source: &source
              description: Interface for source address.
              type: str
            maxpoll: &maxpoll
              description: configure Maximum poll interval.
              type: int
            minpoll: &minpoll
              description: configure Minimum poll interval.
              type: int
            prefer: &prefer
              description: Prefer this peer when possible
              type: bool
            version: &version
              description: NTP version.
              type: int
        peers:
          description: Configure NTP peer.
          type: list
          elements: dict
          suboptions:
            vrf: *vrf
            peer: *host
            burst: *burst
            iburst: *iburst
            key: *key
            source: *source
            maxpoll: *maxpoll
            minpoll: *minpoll
            prefer: *prefer
            version: *version
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the IOSXR device by
        executing the command B(show running-config ntp).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
      - deleted
      - merged
      - overridden
      - replaced
      - gathered
      - rendered
      - parsed
    default: merged
"""
EXAMPLES = """

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.ntp_global.ntp_global import (
    Ntp_globalArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.ntp_global.ntp_global import (
    Ntp_global,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Ntp_globalArgs.argument_spec,
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

    result = Ntp_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
