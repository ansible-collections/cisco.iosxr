#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_vrfs
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: iosxr_vrfs
short_description: Manages global VRF configuration.
description:
  - This module manages VRF configurations on Cisco IOS-XR devices. It enables playbooks to handle either individual VRFs or the complete VRF collection. It also permits removing non-explicitly stated VRF definitions from the setup.
version_added: 7.2.0
author: Ruchi Pakhle (@Ruchip16)
notes:
  - Tested against Cisco IOSXR Version 7.2.0
  - This module works with connection C(network_cli). See L(the IOS_XR Platform Options,../network/user_guide/platform_iosxr.html)
  - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
  - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <https://www.ansible.com/integrations/networks/cisco>`_.
options:
  config:
    description: A list of device configurations for VRF.
    type: list
    elements: dict
    suboptions:
      name:
        description: Name of the VRF.
        type: str
        required: true
      description:
        description: A description for the VRF.
        type: str
      address_families:
        description: Enable address family and enter its config mode - AFI/SAFI configuration
        type: list
        elements: dict
        suboptions:
          afi:
            description: Address Family Identifier (AFI)
            type: str
            choices: ['ipv4', 'ipv6']
          safi:
            description: Address Family modifier
            type: str
            choices: [ 'flowspec', 'multicast', 'unicast']
          export:
            description: VRF export
            type: dict
            suboptions:
              route_policy: &route_policy
                description: Use route_policy for export
                type: str
              route_target: &route_target
                description: Specify export route target extended communities.
                type: str
              to:
                description: Export routes to a VRF
                type: dict
                suboptions:
                  default_vrf: &default_vrf
                    description: Export routes to default VRF
                    type: dict
                    suboptions:
                      route_policy: *route_policy
                  vrf:
                    description: Export routes to a VRF
                    type: dict
                    suboptions:
                      allow_imported_vpn:
                        description: Allow export of imported VPN routes to non-default VRF
                        type: bool
          import_config:
            description: VRF import
            type: dict
            suboptions:
              route_policy: *route_policy
              route_target: *route_target
              from:
                description: Import routes from a VRF
                type: dict
                suboptions:
                  bridge_domain:
                    description: VRF import
                    type: dict
                    suboptions:
                      advertise_as_vpn: &advertise_as_vpn
                        description: Advertise local EVPN imported routes to PEs
                        type: bool
                  default_vrf: *default_vrf
                  vrf:
                    description: Import routes from a VRF
                    type: dict
                    suboptions:
                      advertise_as_vpn: *advertise_as_vpn
          maximum:
            description: Set maximum prefix limit
            type: dict
            suboptions:
              prefix:
                description:  Set table's maximum prefix limit.
                type: int
      evpn_route_sync:
        description: EVPN Instance VPN ID used to synchronize the VRF route(s).
        type: int
      fallback_vrf:
        description: Fallback VRF name
        type: str
      mhost:
        description: Multicast host stack options
        type: dict
        suboptions:
          afi:
            description: Address Family Identifier (AFI)
            type: str
            choices: ['ipv4', 'ipv6']
          default_interface:
            description: Default interface for multicast.
            type: str
      rd:
        description: VPN Route Distinguisher (RD).
        type: str
      remote_route_filtering:
        description: Enable/Disable remote route filtering per VRF
        type: dict
        suboptions:
          disable:
            description: Disable remote route filtering per VRF
            type: bool
      vpn:
        description: VPN ID for the VRF
        type: dict
        suboptions:
          id:
            description: VPN ID for the VRF.
            type: str
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the IOS-XR device by
        executing the command B(show running-config vrf).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    choices: [parsed, gathered, deleted, merged, replaced, rendered, overridden]
    default: merged
    description:
      - The state the configuration should be left in
      - The states I(rendered), I(gathered) and I(parsed) does not perform any change
        on the device.
      - The state I(rendered) will transform the configuration in C(config) option to
        platform specific CLI commands which will be returned in the I(rendered) key
        within the result.
      - For state I(rendered) active connection to remote host is
        not required.
      - The state I(gathered) will fetch the running configuration from device and transform
        it into structured data in the format as per the resource module argspec and
        the value is returned in the I(gathered) key within the result.
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into JSON format as per the resource module parameters and the
        value is returned in the I(parsed) key within the result. The value of C(running_config)
        option should be the same format as the output of command I(show running-config vrf).
        connection to remote host is not required.
    type: str
"""

EXAMPLES = """
# Using merged
# Before state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config vrf
# Fri Feb  9 07:02:35.789 UTC
# !
# cdp
# cdp holdtime 30
# cdp advertise v1
# vrf tet
#
- name: Merge provided configuration with device configuration
  hosts: iosxr
  gather_facts: false
  tasks:
    - name: Merge provided configuration with device configuration
      cisco.iosxr.iosxr_vrfs:
        config:
          - name: VRF4
            description: VRF4 Description
            evpn_route_sync: 793
            fallback_vrf: "test-vrf"
            address_families:
              - afi: "ipv4"
                safi: "unicast"
                export:
                  route_target: "10.0.0.1:300"
                  route_policy: "rm-policy"
                  to:
                    default_vrf:
                      route_policy: "rm-policy"
                    vrf:
                      allow_imported_vpn: "true"
                import_config:
                  route_target: "10.1.3.4:400"
                  route_policy: "test-policy"
                  from:
                    bridge_domain:
                      advertise_as_vpn: "true"
                    default_vrf:
                      route_policy: "test-policy"
                    vrf:
                      advertise_as_vpn: "true"
                maximum:
                  prefix: 100
            remote_route_filtering:
              disable: "true"
            rd: "3:4"
            mhost:
              afi: "ipv4"
              default_interface: "Loopback0"
            vpn:
              id: "2:3"
        state: merged
# Task output
# -------------
# commands:
# - vrf VRF4
# - description VRF4 Description
# - evpn-route-sync 793
# - fallback-vrf test-vrf
# - mhost ipv4 default-interface Loopback0
# - rd 3:4
# - remote-route-filtering disable
# - vpn id 2:3
# - address-family ipv4 unicast
# - export route-policy rm-policy
# - export route-target 10.0.0.1:300
# - export to default-vrf route-policy rm-policy
# - export to vrf allow-imported-vpn
# - import route-target 10.1.3.4:400
# - import route-policy test-policy
# - import from bridge-domain advertise-as-vpn
# - import from default-vrf route-policy test-policy
# - import from vrf advertise-as-vpn
# - maximum prefix 100
#
#
# after:
#   name: VRF4
#   description: VRF4 Description
#   evpn_route_sync: 793
#   fallback_vrf: "test-vrf"
#   mhost:
#     afi: "ipv4"
#     default_interface: "Loopback0"
#   rd: "3:4"
#   remote_route_filtering:
#     disable: "true"
#   vpn:
#     id: "2:3"
#   address_families:
#     - afi: "ipv4"
#       safi: "unicast"
#       export:
#         route_target: "10.0.0.1:300"
#         route_policy: "rm-policy"
#         to:
#           default_vrf:
#             route_policy: "rm-policy"
#           vrf:
#             allow_imported_vpn: "true"
#       import_config:
#         route_target: "10.1.3.4:400"
#         route_policy: "test-policy"
#         from:
#           bridge_domain:
#             advertise_as_vpn: "true"
#           default_vrf:
#             route_policy: "test-policy"
#           vrf:
#             advertise_as_vpn: "true"
#       maximum:
#         prefix: 10
#
# After state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config vrf
# Sat Feb 20 03:49:43.618 UTC
#  vrf VRF4
#  description "This is test VRF"
#  address-family ipv4 unicast
#   export to default-vrf route-policy "rm-policy"
#   export to vrf allow-imported-vpn
#   export route-policy "export-policy"
#   export route-target
#    10.1.2.3:200
#   import route-target
#    10.0.0.1:300
#   import route-policy "test-policy"
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy "new-policy"
#   import from vrf advertise-as-vpn
#   maximum prefix 23
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 456
#  vpn 56
#  fallback-vrf "test-vrf"
#  remote-route-filtering disable
#  address-family ipv4 flowspec
#  rd "testing"
#
# Using replaced
# Before state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config vrf
# Sat Feb 20 03:49:43.618 UTC
#  vrf VRF4
#  description "This is test VRF"
#  address-family ipv4 unicast
#   export to default-vrf route-policy "rm-policy"
#   export to vrf allow-imported-vpn
#   export route-policy "export-policy"
#   export route-target
#    10.1.2.3:200
#   import route-target
#    10.0.0.1:300
#   import route-policy "test-policy"
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy "new-policy"
#   import from vrf advertise-as-vpn
#   maximum prefix 23
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 456
#  vpn 56
#  fallback-vrf "test-vrf"
#  remote-route-filtering disable
#  address-family ipv4 flowspec
#  rd "testing"
#
#
- name: Replace the provided configuration with the existing running configuration
  hosts: iosxr
  gather_facts: false
  tasks:
    - name: Replace the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_vrfs:
        config:
          - name: VRF7
            description: VRF7 description
            evpn_route_sync: 398
            fallback_vrf: "replaced-vrf"
            address_families:
              - afi: "ipv4"
                safi: "unicast"
                export:
                  route_target: "192.12.3.2:300"
                  route_policy: "rm-policy"
                  to:
                    default_vrf:
                      route_policy: "rm-policy"
                    vrf:
                      allow_imported_vpn: "true"
                import_config:
                  route_target: "12.2.3.4:900"
                  route_policy: "test-policy"
                  from:
                    bridge_domain:
                      advertise_as_vpn: "true"
                    default_vrf:
                      route_policy: "test-policy"
                    vrf:
                      advertise_as_vpn: "true"
                maximum:
                  prefix: 200
            remote_route_filtering:
              disable: "true"
            rd: "67:9"
            mhost:
              afi: "ipv4"
              default_interface: "Loopback0"
            vpn:
              id: "4:5"
        state: replaced

# -------------
# commands:
# - vrf VRF7
# - description VRF7 description
# - evpn-route-sync 398
# - fallback-vrf replaced-vrf
# - mhost ipv4 default-interface Loopback0
# - rd 67:9
# - remote-route-filtering disable
# - vpn id 4:5
# - address-family ipv4 unicast
# - export route-policy rm-policy
# - export route-target 192.12.3.2:300
# - export to default-vrf route-policy rm-policy
# - export to vrf allow-imported-vpn
# - import route-target 12.2.3.4:900
# - import route-policy test-policy
# - import from bridge-domain advertise-as-vpn
# - import from default-vrf route-policy test-policy
# - import from vrf advertise-as-vpn
# - maximum prefix 200
#
# after:
#   name: VRF7
#   description: VRF7 description
#   evpn_route_sync: 398
#   fallback_vrf: "replaced-vrf"
#   address_families:
#     - afi: "ipv4"
#       safi: "unicast"
#       export:
#         route_target: "192.12.3.2:300"
#         route_policy: "rm-policy"
#         to:
#           default_vrf:
#             route_policy: "rm-policy"
#           vrf:
#             allow_imported_vpn: "true"
#       import_config:
#         route_target: "12.2.3.4:900"
#         route_policy: "test-policy"
#         from:
#           bridge_domain:
#             advertise_as_vpn: "true"
#           default_vrf:
#             route_policy: "test-policy"
#           vrf:
#             advertise_as_vpn: "true"
#       maximum:
#         prefix: 200
#   remote_route_filtering:
#     disable: "true"
#   rd: "67:9"
#   mhost:
#     afi: "ipv4"
#     default_interface: "Loopback0"
#   vpn:
#     id: "4:5"
#
# After state:
# -------------
# RP/0/RP0/CPU0:ios(config)#show running-config vrf
# Sun Mar 10 16:48:53.204 UTC
# vrf VRF4
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 793
#  description VRF4 Description
#  vpn id 2:3
#  fallback-vrf parsed-vrf
#  remote-route-filtering disable
#  rd 3:4
#  address-family ipv4 unicast
#  --More-- vrf VRF4
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 793
#  description VRF4 Description
#  vpn id 2:3
#  fallback-vrf parsed-vrf
#  remote-route-filtering disable
#  rd 3:4
#  address-family ipv4 unicast
#   import route-policy test-policy
#   import from vrf advertise-as-vpn
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy test-policy
#   import route-target
#    10.1.3.4:400
#   !
#   export route-policy rm-policy
#   export to vrf allow-imported-vpn
#   export to default-vrf route-policy rm-policy
#   export route-target
#    10.0.0.1:300
#   !
#   maximum prefix 100
#  !
# !
# vrf VRF7
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 398
#  description VRF7 description
#  vpn id 4:5
#  fallback-vrf replaced-vrf
#  remote-route-filtering disable
#  rd 67:9
#  address-family ipv4 unicast
#   import route-policy test-policy
#   import from vrf advertise-as-vpn
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy test-policy
#   import route-target
#    12.2.3.4:900
#   !
#   export route-policy rm-policy
#   export to vrf allow-imported-vpn
#   export to default-vrf route-policy rm-policy
#   export route-target
#    192.12.3.2:300
#   !
#   maximum prefix 200
#  !
# !
#
# Using overridden
# Before state:
# -------------
# RP/0/RP0/CPU0:ios(config)#show running-config vrf
# Sun Mar 10 16:48:53.204 UTC
# vrf VRF4
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 793
#  description VRF4 Description
#  vpn id 2:3
#  fallback-vrf parsed-vrf
#  remote-route-filtering disable
#  rd 3:4
#  address-family ipv4 unicast
#  --More-- vrf VRF4
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 793
#  description VRF4 Description
#  vpn id 2:3
#  fallback-vrf parsed-vrf
#  remote-route-filtering disable
#  rd 3:4
#  address-family ipv4 unicast
#   import route-policy test-policy
#   import from vrf advertise-as-vpn
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy test-policy
#   import route-target
#    10.1.3.4:400
#   !
#   export route-policy rm-policy
#   export to vrf allow-imported-vpn
#   export to default-vrf route-policy rm-policy
#   export route-target
#    10.0.0.1:300
#   !
#   maximum prefix 100
#  !
# !
# vrf VRF7
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 398
#  description VRF7 description
#  vpn id 4:5
#  fallback-vrf replaced-vrf
#  remote-route-filtering disable
#  rd 67:9
#  address-family ipv4 unicast
#   import route-policy test-policy
#   import from vrf advertise-as-vpn
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy test-policy
#   import route-target
#    12.2.3.4:900
#   !
#   export route-policy rm-policy
#   export to vrf allow-imported-vpn
#   export to default-vrf route-policy rm-policy
#   export route-target
#    192.12.3.2:300
#   !
#   maximum prefix 200
#  !
# !
- name: Override the provided configuration with the existing running configuration
  hosts: iosxr
  gather_facts: false
  tasks:
    - name: Override the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_vrfs:
        state: overridden
        config:
          - name: VRF6
            description: VRF6 Description
            evpn_route_sync: 101
            fallback_vrf: "overridden-vrf"
            address_families:
              - afi: "ipv4"
                safi: "unicast"
                export:
                  route_target: "10.0.0.1:300"
                  route_policy: "rm-policy1"
                  to:
                    default_vrf:
                      route_policy: "rm-policy"
                    vrf:
                      allow_imported_vpn: "true"
                import_config:
                  route_target: "10.1.3.4:900"
                  route_policy: "test-policy"
                  from:
                    bridge_domain:
                      advertise_as_vpn: "true"
                    default_vrf:
                      route_policy: "test-policy"
                    vrf:
                      advertise_as_vpn: "true"
                maximum:
                  prefix: 500
            remote_route_filtering:
              disable: "true"
            rd: "67:9"
            mhost:
              afi: "ipv4"
              default_interface: "Loopback0"
            vpn:
              id: "4:5"

# Task output
# -------------
# commands:
# - vrf VRF6
# - description VRF6 Description
# - evpn-route-sync 101
# - fallback-vrf overridden-vrf
# - mhost ipv4 default-interface Loopback0
# - rd 67:9
# - remote-route-filtering disable
# - vpn id 4:5
# - address-family ipv4 unicast
# - export route-policy rm-policy1
# - export route-target 10.0.0.1:300
# - export to default-vrf route-policy rm-policy
# - export to vrf allow-imported-vpn
# - import route-target 10.1.3.4:900
# - import route-policy test-policy
# - import from bridge-domain advertise-as-vpn
# - import from default-vrf route-policy test-policy
# - import from vrf advertise-as-vpn
# - maximum prefix 500
# - no vrf VRF7
# - no vrf VRF4
#
#
# after:
# name: VRF6
# description: VRF6 Description
# evpn_route_sync: 101
# fallback_vrf: "overridden-vrf"
# address_families:
#   - afi: "ipv4"
#     safi: "unicast"
#     export:
#       route_target: "10.0.0.1:300"
#       route_policy: "rm-policy1"
#       to:
#         default_vrf:
#           route_policy: "rm-policy"
#         vrf:
#           allow_imported_vpn: "true"
#     import_config:
#       route_target: "10.1.3.4:900"
#       route_policy: "test-policy"
#       from:
#         bridge_domain:
#           advertise_as_vpn: "true"
#         default_vrf:
#           route_policy: "test-policy"
#         vrf:
#           advertise_as_vpn: "true"
#     maximum:
#       prefix: 500
# remote_route_filtering:
#   disable: "true"
# rd: "67:9"
# mhost:
#   afi: "ipv4"
#   default_interface: "Loopback0"
# vpn:
#   id: "4:5"
#
# After state:
# -------------
# RP/0/RP0/CPU0:ios(config)#show running-config vrf
# Sun Mar 10 16:54:53.007 UTC
# vrf VRF6
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 101
#  description VRF6 Description
#  vpn id 4:5
#  fallback-vrf overridden-vrf
#  remote-route-filtering disable
#  rd 67:9
#  address-family ipv4 unicast
#   import route-policy test-policy
#   import from vrf advertise-as-vpn
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy test-policy
#   import route-target
#    10.1.3.4:900
#   !
#   export route-policy rm-policy1
#   export to vrf allow-imported-vpn
#   export to default-vrf route-policy rm-policy
#   export route-target
#    10.0.0.1:300
#   !
#   maximum prefix 500
#
#
# Using deleted
# Before state:
# -------------
# RP/0/RP0/CPU0:ios(config)#show running-config vrf
# Sun Mar 10 16:54:53.007 UTC
# vrf VRF6
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 101
#  description VRF6 Description
#  vpn id 4:5
#  fallback-vrf overridden-vrf
#  remote-route-filtering disable
#  rd 67:9
#  address-family ipv4 unicast
#   import route-policy test-policy
#   import from vrf advertise-as-vpn
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy test-policy
#   import route-target
#    10.1.3.4:900
#   !
#   export route-policy rm-policy1
#   export to vrf allow-imported-vpn
#   export to default-vrf route-policy rm-policy
#   export route-target
#    10.0.0.1:300
#   !
#   maximum prefix 500
#
- name: Delete the provided configuration
  hosts: iosxr
  gather_facts: false
  tasks:
    - name: Delete the provided configuration
      cisco.iosxr.iosxr_vrfs:
        state: deleted

# Task output
# -------------
# commands:
# - no vrf VRF6
#
# After state:
# -------------
# RP/0/RP0/CPU0:ios(config)#show running-config vrf
# Sun Mar 10 17:02:38.981 UTC
# % No such configuration item(s)
#
# Using rendered
# -------------
#
- name: Render provided configuration with device configuration
      cisco.iosxr.iosxr_vrfs:
        config:
          - name: VRF4
            description: VRF4 Description
            evpn_route_sync: 793
            fallback_vrf: "parsed-vrf"
            address_families:
              - afi: "ipv4"
                safi: "unicast"
                export:
                  route_target: "10.0.0.1:300"
                  route_policy: "rm-policy"
                  to:
                    default_vrf:
                      route_policy: "rm-policy"
                    vrf:
                      allow_imported_vpn: "true"
                import_config:
                  route_target: "10.1.3.4:400"
                  route_policy: "test-policy"
                  from:
                    bridge_domain:
                      advertise_as_vpn: "true"
                    default_vrf:
                      route_policy: "test-policy"
                    vrf:
                      advertise_as_vpn: "true"
                maximum:
                  prefix: 100
            remote_route_filtering:
              disable: "true"
            rd: "3:4"
            mhost:
              afi: "ipv4"
              default_interface: "Loopback0"
            vpn:
              id: "2:3"
        state: rendered
# Task output
# -------------
# commands:
# - vrf VRF4
# - description VRF4 Description
# - evpn-route-sync 793
# - fallback-vrf parsed-vrf
# - mhost ipv4 default-interface Loopback0
# - rd 3:4
# - remote-route-filtering disable
# - vpn id 2:3
# - address-family ipv4 unicast
# - export route-policy rm-policy
# - export route-target 10.0.0.1:300
# - export to default-vrf route-policy rm-policy
# - export to vrf allow-imported-vpn
# - import route-target 10.1.3.4:400
# - import route-policy test-policy
# - import from bridge-domain advertise-as-vpn
# - import from default-vrf route-policy test-policy
# - import from vrf advertise-as-vpn
# - maximum prefix 100
#
# Using gathered
# -------------
- name: Display existing running configuration
  hosts: iosxr
  gather_facts: false
  tasks:
    - name: Gather existing running configuration
      cisco.iosxr.iosxr_vrfs:
        state: gathered

# gathered:
#
# name: VRF7
# description: VRF7 description
# evpn_route_sync: 398
# fallback_vrf: "replaced-vrf"
# address_families:
#   - afi: "ipv4"
#     safi: "unicast"
#     export:
#       route_target: "192.12.3.2:300"
#       route_policy: "rm-policy"
#       to:
#         default_vrf:
#           route_policy: "rm-policy"
#         vrf:
#           allow_imported_vpn: "true"
#     import_config:
#       route_target: "12.2.3.4:900"
#       route_policy: "test-policy"
#       from:
#         bridge_domain:
#           advertise_as_vpn: "true"
#         default_vrf:
#           route_policy: "test-policy"
#         vrf:
#           advertise_as_vpn: "true"
#     maximum:
#       prefix: 200
# remote_route_filtering:
#   disable: "true"
# rd: "67:9"
# mhost:
#   afi: "ipv4"
#   default_interface: "Loopback0"
# vpn:
#   id: "4:5"
#
# Using parsed
#
# parsed.cfg
# ------------
# vrf test
#  description "This is test VRF"
#  address-family ipv4 unicast
#   export to default-vrf route-policy "rm-policy"
#   export to vrf allow-imported-vpn
#   export route-policy "export-policy"
#   export route-target
#    10.1.2.3:200
#   import route-target
#    10.0.0.1:300
#   import route-policy "test-policy"
#   import from bridge-domain advertise-as-vpn
#   import from default-vrf route-policy "new-policy"
#   import from vrf advertise-as-vpn
#   maximum prefix 23
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 456
#  vpn 56
#  fallback-vrf "test-vrf"
#  remote-route-filtering disable
#  address-family ipv4 flowspec
#  rd "testing"
#  !
# !
# vrf my_vrf
#  mhost ipv4 default-interface Loopback0
#  evpn-route-sync 235
#  description "this is sample vrf for feature testing"
#  fallback-vrf "parsed-vrf"
#  rd "2:3"
#  remote-route-filtering disable
#  vpn 23
#  address-family ipv4 flowspec
#   import route-policy rm-policy
#   import from bridge-domain advertise-as-vpn
#   import route-target
#    10.1.2.3:300
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.vrfs.vrfs import (
    VrfsArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.vrfs.vrfs import (
    Vrf,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=VrfsArgs.argument_spec,
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

    result = Vrf(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
