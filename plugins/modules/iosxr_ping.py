#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_ping
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: iosxr_ping
short_description: Tests reachability using ping from IOSXR switch.
description:
- Tests reachability using ping from switch to a remote destination.
- For a general purpose network module, see the L(net_ping,https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_ping_module.html)
  module.
- For Windows targets, use the L(win_ping,https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html)
  module instead.
- For targets running Python, use the L(ping,https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html)
  module instead.
notes:
- Tested against IOSXR 7.2.2.
- This module works with connection C(network_cli).
author: Sagar Paul (@KB-perByte)
options:
  count:
    description:
    - Repeat count the number of packets to send.
    type: int
  afi:
    description:
    - Define echo type ipv4 or ipv6.
    choices:
    - ipv4
    - ipv6
    default: ipv4
    type: str
  dest:
    description:
    - The IP Address or hostname (resolvable by switch) of the remote node.
    required: true
    type: str
  df_bit:
    description:
    - Set the DF bit in IP-header.
    default: false
    type: bool
  sweep:
    description:
    - Sweep ping.
    default: false
    type: bool
  validate:
    description:
    - Validate return packet.
    default: false
    type: bool
  source:
    description:
    - Source address or source interface.
    type: str
  size:
    description:
    - Datagram size the size of packets to send.
    type: int
  state:
    description:
    - Determines if the expected result is success or fail.
    choices:
    - absent
    - present
    default: present
    type: str
  vrf:
    description:
    - The VRF to use for forwarding.
    type: str
notes:
- For a general purpose network module, see the L(net_ping,https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_ping_module.html)
  module.
- For Windows targets, use the L(win_ping,https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html)
  module instead.
- For targets running Python, use the L(ping,https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html) module instead.
"""

EXAMPLES = """
- name: Test reachability to 10.10.10.10 using default vrf
  cisco.iosxr.iosxr_ping:
    dest: 10.10.10.10
- name: Test reachability to 10.20.20.20 using prod vrf
  cisco.iosxr.iosxr_ping:
    dest: 10.20.20.20
    vrf: prod
- name: Test unreachability to 10.30.30.30 using default vrf
  cisco.iosxr.iosxr_ping:
    dest: 10.30.30.30
    state: absent
- name: Test reachability to 10.40.40.40 using prod vrf and setting count and source
  cisco.iosxr.iosxr_ping:
    dest: 10.40.40.40
    source: loopback0
    vrf: prod
    count: 20
- name: Test reachability to 10.50.50.50 using df-bit and size
  cisco.iosxr.iosxr_ping:
    dest: 10.50.50.50
    df_bit: true
    size: 1400
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
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.ping.ping import (
    PingArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.ping.ping import (
    Ping,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=PingArgs.argument_spec)

    result = Ping(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
