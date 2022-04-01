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
short_description: Tests reachability using ping from Iosxr switch.
description:
- Tests reachability using ping from switch to a remote destination.
- For a general purpose network module, see the L(net_ping,https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_ping_module.html)
  module.
- For Windows targets, use the L(win_ping,https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html)
  module instead.
- For targets running Python, use the L(ping,https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html)
  module instead.
version_added: 1.0.0
notes:
- Tested against IOSXR 7.0.2.
- This module works with connection C(network_cli).
author: Ashwini Mhatre (@amhatre)
extends_documentation_fragment:
- cisco.iosxr.iosxr
options:
  count:
    description:
    - Number of packets to send.
    type: int
  dest:
    description:
    - The IP Address or hostname (resolvable by switch) of the remote node.
    required: true
    type: str
  df_bit:
    description:
    - Set the DF bit.
    default: false
    type: bool
  size:
    description:
    - Size of packets to send.
    type: int
  source:
    description:
    - The source IP Address.
    type: str
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
commands:
  description: Show the command sent.
  returned: always
  type: list
  sample: ["ping vrf prod 10.40.40.40 count 20 source loopback0"]
packet_loss:
  description: Percentage of packets lost.
  returned: always
  type: str
  sample: "0%"
packets_rx:
  description: Packets successfully received.
  returned: always
  type: int
  sample: 20
packets_tx:
  description: Packets successfully transmitted.
  returned: always
  type: int
  sample: 20
rtt:
  description: Show RTT stats.
  returned: always
  type: dict
  sample: {"avg": 2, "max": 8, "min": 1}
"""
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.iosxr import (
    run_commands,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.iosxr import (
    iosxr_argument_spec,
)
import re


def main():
    """main entry point for module execution"""
    argument_spec = dict(
        count=dict(type="int"),
        dest=dict(type="str", required=True),
        df_bit=dict(type="bool", default=False),
        size=dict(type="int"),
        source=dict(type="str"),
        state=dict(
            type="str", choices=["absent", "present"], default="present"
        ),
        vrf=dict(type="str"),
    )
    argument_spec.update(iosxr_argument_spec)
    module = AnsibleModule(argument_spec=argument_spec)
    count = module.params["count"]
    dest = module.params["dest"]
    df_bit = module.params["df_bit"]
    size = module.params["size"]
    source = module.params["source"]
    vrf = module.params["vrf"]
    warnings = list()
    results = {}
    if warnings:
        results["warnings"] = warnings
    results["commands"] = [build_ping(dest, count, source, vrf, size, df_bit)]
    ping_results = run_commands(module, commands=results["commands"])
    ping_results_list = ping_results[0].split("\n")
    stats = ""
    for line in ping_results_list:
        if line.startswith("Success"):
            stats = line
    success, rx, tx, rtt = parse_ping(stats)
    loss = abs(100 - int(success))
    results["packet_loss"] = str(loss) + "%"
    results["packets_rx"] = int(rx)
    results["packets_tx"] = int(tx)
    # Convert rtt values to int
    for k, v in rtt.items():
        if rtt[k] is not None:
            rtt[k] = int(v)
    results["rtt"] = rtt
    validate_results(module, loss, results)
    module.exit_json(**results)


def build_ping(
    dest, count=None, source=None, vrf=None, size=None, df_bit=False
):
    """
    Function to build the command to send to the terminal for the switch
    to execute. All args come from the module's unique params.
    """
    if vrf is not None:
        cmd = "ping vrf {0} {1}".format(vrf, dest)
    else:
        cmd = "ping {0}".format(dest)
    if count is not None:
        cmd += " repeat {0}".format(str(count))
    if size is not None:
        cmd += " size {0}".format(size)
    if df_bit:
        cmd += " df-bit"
    if source is not None:
        cmd += " source {0}".format(source)
    return cmd


def parse_ping(ping_stats):
    """
    Function used to parse the statistical information from the ping response.
    Example: "Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/8 ms"
    Returns the percent of packet loss, received packets, transmitted packets, and RTT dict.
    """
    rate_re = re.compile(
        "^\\w+\\s+\\w+\\s+\\w+\\s+(?P<pct>\\d+)\\s+\\w+\\s+\\((?P<rx>\\d+)/(?P<tx>\\d+)\\)"
    )
    rtt_re = re.compile(
        ".*,\\s+\\S+\\s+\\S+\\s+=\\s+(?P<min>\\d+)/(?P<avg>\\d+)/(?P<max>\\d+)\\s+\\w+\\s*$|.*\\s*$"
    )
    rate = rate_re.match(ping_stats)
    rtt = rtt_re.match(ping_stats)
    return (
        rate.group("pct"),
        rate.group("rx"),
        rate.group("tx"),
        rtt.groupdict(),
    )


def validate_results(module, loss, results):
    """
    This function is used to validate whether the ping results were unexpected per "state" param.
    """
    state = module.params["state"]
    if state == "present" and loss == 100:
        module.fail_json(msg="Ping failed unexpectedly", **results)
    elif state == "absent" and loss < 100:
        module.fail_json(msg="Ping succeeded unexpectedly", **results)


if __name__ == "__main__":
    main()
