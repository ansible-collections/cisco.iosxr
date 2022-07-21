#!/usr/bin/python
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
#

"""
The module file for iosxr_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type
DOCUMENTATION = """
module: iosxr_interfaces
short_description: Resource module to configure interfaces.
description: This module manages the interface attributes on Cisco IOS-XR network
  devices.
version_added: 1.0.0
author:
- Sumit Jaiswal (@justjais)
- Rohit Thakur (@rohitthakur2590)
notes:
- This module works with connection C(network_cli). See L(the IOS-XR Platform Options,../network/user_guide/platform_iosxr.html).
options:
  config:
    description: A dictionary of interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of the interface to configure in C(type + path) format. e.g. C(GigabitEthernet0/0/0/0)
        type: str
        required: true
      description:
        description:
        - Interface description.
        type: str
      enabled:
        default: true
        description:
        - Administrative state of the interface.
        - Set the value to C(True) to administratively enable the interface or C(False)
          to disable it.
        type: bool
      speed:
        description:
        - Configure the speed for an interface. Default is auto-negotiation when not
          configured.
        type: int
      mtu:
        description:
        - Sets the MTU value for the interface. Applicable for Ethernet interfaces
          only.
        - Refer to vendor documentation for valid values.
        type: int
      duplex:
        description:
        - Configures the interface duplex mode. Default is auto-negotiation when not
          configured.
        type: str
        choices:
        - full
        - half
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the IOS-XR device
      by executing the command B(show running-config interface).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    choices:
    - merged
    - parsed
    - deleted
    - replaced
    - rendered
    - gathered
    - overridden
    default: merged
    description:
    - The state of the configuration after module completion
    type: str
"""

EXAMPLES = """
# Using merged
# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Replaced by Ansible Team
#  mtu 2000
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  dot1q native vlan 1021
# !
- name: Configure Ethernet interfaces
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
      description: Configured by Ansible
      enabled: true
    - name: GigabitEthernet0/0/0/3
      description: Configured by Ansible Network
      enabled: false
      duplex: full
    state: merged
# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured and Merged by Ansible Network
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured and Merged by Ansible Network
#  mtu 2600
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex full
#  shutdown
#  dot1q native vlan 1021
# !
# Using replaced
# Before state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  description Configured by Ansible
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Test
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  dot1q native vlan 1021
# !
- name: Configure following interfaces and replace their existing config
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
      description: Configured by Ansible
      enabled: true
      mtu: 2000
    - name: GigabitEthernet0/0/0/3
      description: Configured by Ansible Network
      enabled: false
      duplex: auto
    state: replaced
# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  description Configured by Ansible
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured and Replaced by Ansible
#  mtu 2000
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured and Replaced by Ansible Network
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex half
#  shutdown
#  dot1q native vlan 1021
# !
# Using overridden
# Before state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured by Ansible
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured by Ansible
#  mtu 2600
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex full
#  shutdown
#  dot1q native vlan 1021
# !
- name: Override interfaces
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
      description: Configured by Ansible
      enabled: true
      duplex: auto
    - name: GigabitEthernet0/0/0/3
      description: Configured by Ansible Network
      enabled: false
      speed: 1000
    state: overridden
# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured and Overridden by Ansible Network
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  speed 1000
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured and Overridden by Ansible Network
#  mtu 2000
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex full
#  shutdown
#  dot1q native vlan 1021
# !
# Using deleted
# Before state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  description Configured and Overridden by Ansible Network
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  speed 1000
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  description Configured and Overridden by Ansible Network
#  mtu 2000
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  duplex full
#  shutdown
#  dot1q native vlan 1021
# !
- name: Delete IOSXR interfaces as in given arguments
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/2
    - name: GigabitEthernet0/0/0/3
    state: deleted
# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  vrf custB
#  ipv4 address 178.18.169.23 255.255.255.0
#  dot1q native vlan 30
# !
# interface GigabitEthernet0/0/0/3
#  vrf custB
#  ipv4 address 10.10.0.2 255.255.255.0
#  dot1q native vlan 1021
# !
# Using parsed
# parsed.cfg
# ------------
#
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
#  description Configured and Merged by Ansible-Network
#  mtu 110
#  ipv4 address 172.31.1.1 255.255.255.0
#  duplex half
# !
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !
# - name: Convert ACL interfaces config to argspec without connecting to the appliance
#   cisco.iosxr.iosxr_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": [
#        {
#            "name": "MgmtEth0/RP0/CPU0/0"
#        },
#        {
#            "access_groups": [
#                {
#                    "acls": [
#                        {
#                            "direction": "in",
#                            "name": "acl_1"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "acl_2"
#                        }
#                    ],
#                    "afi": "ipv4"
#                },
#                {
#                    "acls": [
#                        {
#                            "direction": "in",
#                            "name": "acl6_1"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "acl6_2"
#                        }
#                    ],
#                    "afi": "ipv6"
#                }
#            ],
#            "name": "GigabitEthernet0/0/0/0"
#        },
#        {
#            "access_groups": [
#                {
#                    "acls": [
#                        {
#                            "direction": "out",
#                            "name": "acl_1"
#                        }
#                    ],
#                    "afi": "ipv4"
#                }
#            ],
#            "name": "GigabitEthernet0/0/0/1"
#        }
#    ]
# }
# Using rendered
- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_interfaces:
    config:
    - name: GigabitEthernet0/0/0/0
      description: Configured and Merged by Ansible-Network
      mtu: 110
      enabled: true
      duplex: half
    - name: GigabitEthernet0/0/0/1
      description: Configured and Merged by Ansible-Network
      mtu: 2800
      enabled: false
      speed: 100
      duplex: full
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": [
#         "interface GigabitEthernet0/0/0/0",
#         "description Configured and Merged by Ansible-Network",
#         "mtu 110",
#         "duplex half",
#         "no shutdown",
#         "interface GigabitEthernet0/0/0/1",
#         "description Configured and Merged by Ansible-Network",
#         "mtu 2800",
#         "speed 100",
#         "duplex full",
#         "shutdown"
#     ]
# Using gathered
# Before state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config  interface
# interface Loopback888
# description test for ansible
# shutdown
# !
# interface MgmtEth0/0/CPU0/0
# ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
# description Configured and Merged by Ansible-Network
# mtu 110
# ipv4 address 172.31.1.1 255.255.255.0
# duplex half
# !
# interface GigabitEthernet0/0/0/3
# shutdown
# !
# interface GigabitEthernet0/0/0/4
# shutdown
# !
- name: Gather IOSXR interfaces as in given arguments
  cisco.iosxr.iosxr_interfaces:
    config:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": [
#         {
#             "description": "test for ansible",
#             "enabled": false,
#             "name": "Loopback888"
#         },
#         {
#             "description": "Configured and Merged by Ansible-Network",
#             "duplex": "half",
#             "enabled": true,
#             "mtu": 110,
#             "name": "GigabitEthernet0/0/0/0"
#         },
#         {
#             "enabled": false,
#             "name": "GigabitEthernet0/0/0/3"
#         },
#         {
#             "enabled": false,
#             "name": "GigabitEthernet0/0/0/4"
#         }
#     ]
# After state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config  interface
# interface Loopback888
# description test for ansible
# shutdown
# !
# interface MgmtEth0/0/CPU0/0
# ipv4 address 10.8.38.70 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
# description Configured and Merged by Ansible-Network
# mtu 110
# ipv4 address 172.31.1.1 255.255.255.0
# duplex half
# !
# interface GigabitEthernet0/0/0/3
# shutdown
# !
# interface GigabitEthernet0/0/0/4
# shutdown
# !
"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
commands:
  description: The set of commands pushed to the remote device
  returned: always
  type: list
  sample: ['interface GigabitEthernet0/0/0/2', 'description: Configured by Ansible', 'shutdown']
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.interfaces.interfaces import (
    InterfacesArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.interfaces.interfaces import (
    Interfaces,
)


def main():
    """
    Main entry point for module execution
    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]
    module = AnsibleModule(
        argument_spec=InterfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
