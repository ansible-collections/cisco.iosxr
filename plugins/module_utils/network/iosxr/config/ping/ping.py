#
# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr_ping config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""
# from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
#     dict_merge,
# )

# from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module import (
#     ResourceModule,
# )
# from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import (
#     Facts,
# )
# from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.ping import (
#     PingTemplate,
# )
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.iosxr import (
    run_commands,
)
import re


class Ping:  # ResourceModule
    """
    The iosxr_ping config class
    """

    def __init__(self, module):
        self.module = module
        self.result = {}
        # super(Ping, self).__init__(
        #     empty_fact_val={},
        #     facts_module=Facts(module),
        #     module=module,
        #     resource="ping",
        #     tmplt=PingTemplate(),
        # )
        # self.parsers = []

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        # if self.state not in ["parsed", "gathered"]:
        self.generate_command()
        res = self.run_command()
        return self.process_result(res)

    def build_ping(self, params):
        # ping vrf paul 10.0.2.15 count 2 df-bit sweep validate size 40 source nve 2
        # {vrf}{ping_type}{dest}{count}{df_bit}{sweep}{validate}{size}{source}

        cmd = "ping"
        if params.get("vrf"):
            cmd += " vrf " + params.get("vrf")
        if params.get("afi"):
            cmd += " " + params.get("afi")
        if params.get("dest"):
            cmd += " " + params.get("dest")
        if params.get("count"):
            cmd += " count " + str(params.get("count"))
        if params.get("df_bit"):
            cmd += " df-bit"
        if params.get("sweep"):
            cmd += " sweep"
        if params.get("validate"):
            cmd += " validate"
        if params.get("size"):
            cmd += " size " + str(params.get("size"))
        if params.get("source"):
            cmd += " source " + params.get("source")
        return cmd

    def parse_ping(self, ping_stats):
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

    def validate_results(self, module, loss, results):
        """
        This function is used to validate whether the ping results were unexpected per "state" param.
        """
        state = module.params["state"]
        if state == "present" and loss == 100:
            module.fail_json(msg="Ping failed unexpectedly", **results)
        elif state == "absent" and loss < 100:
            module.fail_json(msg="Ping succeeded unexpectedly", **results)

    def generate_command(self):
        """Generate configuration commands to send based on
        want, have and desired state.
        """
        warnings = list()  # no idea why
        if warnings:
            self.result["warnings"] = warnings
        self.result["commands"] = self.build_ping(self.module.params)

    def run_command(self):
        ping_results = run_commands(
            self.module, commands=self.result["commands"]
        )
        return ping_results

    def process_result(self, ping_results):
        ping_results_list = ping_results[0].split("\n")
        stats = ""
        for line in ping_results_list:
            if line.startswith("Success"):
                stats = line
        success, rx, tx, rtt = self.parse_ping(stats)
        loss = abs(100 - int(success))
        self.result["packet_loss"] = str(loss) + "%"
        self.result["packets_rx"] = int(rx)
        self.result["packets_tx"] = int(tx)
        # Convert rtt values to int
        for k, v in rtt.items():
            if rtt[k] is not None:
                rtt[k] = int(v)
        self.result["rtt"] = rtt
        self.validate_results(self.module, loss, self.result)
        return self.result
