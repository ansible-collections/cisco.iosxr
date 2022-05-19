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

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.iosxr import (
    run_commands,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.ping import (
    PingTemplate,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)


class Ping:
    """
    The iosxr_ping config class
    """

    def __init__(self, module):
        self.module = module
        self.result = {}

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        self.generate_command()
        res = self.run_command()
        return self.process_result(res)

    def build_ping(self, params):
        tmplt = PingTemplate()
        params = utils.remove_empties(params)
        cmd = tmplt.render(params, "rate", False)
        return cmd

    def parse_ping(self, ping_stats):
        """
        Function used to parse the statistical information from the ping response.
        Example: "Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/8 ms"
        Returns the percent of packet loss, received packets, transmitted packets, and RTT data.
        """
        ping_data = PingTemplate(lines=ping_stats.splitlines())
        obj = list(ping_data.parse().values())
        return (
            obj[0].get("loss_percentage"),
            obj[0].get("rx"),
            obj[0].get("tx"),
            obj[0].get("rtt"),
            obj[0].get("loss"),
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
        warnings = list()
        if warnings:
            self.result["warnings"] = warnings
        self.result["commands"] = self.build_ping(self.module.params)

    def run_command(self):
        ping_results = run_commands(
            self.module, commands=self.result["commands"]
        )
        return ping_results

    def process_result(self, ping_results):
        (
            self.result["packet_loss"],
            self.result["packets_rx"],
            self.result["packets_tx"],
            self.result["rtt"],
            loss,
        ) = self.parse_ping(ping_results[0])
        self.validate_results(self.module, loss, self.result)
        return self.result
