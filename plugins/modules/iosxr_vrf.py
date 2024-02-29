#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_vrf
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
          import:
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
    description: The state the configuration should be left in.
      - State I(deleted) only removes VRF attributes that this modules
      manages and does not negate the VRF process completely. Thereby, preserving
      address_family related configurations under VRF context.
      - Refer to examples for more details.https://github.com/ansible-network/resource_module_models/pull/243/commits/4c40fc3daa8e484051aac3eddf7c4b420b06dbdb
    type: str
  state:
    description: The state the configuration should be left in.
    type: str
    choices: [parsed, gathered, deleted, merged, replaced, rendered, overridden]
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
from ansible_collections.cisco.iosxr.iosxr.plugins.module_utils.network.iosxr.argspec.vrf.vrf import (
    VrfArgs,
)
from ansible_collections.cisco.iosxr.iosxr.plugins.module_utils.network.iosxr.config.vrf.vrf import (
    Vrf,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=VrfArgs.argument_spec,
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
