# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The iosxr route_maps fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

import re

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.route_maps.route_maps import (
    Route_mapsArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.route_maps import (
    Route_mapsName,
    Route_mapsTemplate,
)


class Route_mapsFacts(object):
    """The iosxr route_maps facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Route_mapsArgs.argument_spec

    def get_policynames(self, connection):
        return connection.get("show running-config | include route-policy")

    def process_conditions(self, line):
        """
        Checks if a line starts with 'if', then splits it based on 'and', 'or', 'then' delimiters.

        Args:
            line: The line to process.

        Returns:
            A list of conditions and the 'then' part if the line starts with 'if', otherwise an empty list.
        """
        line = line.strip()
        if line.startswith("if "):
            line = line[3:]  # Remove the leading "if "
            conditions = re.split(r"\s+(and|or|then)\s+", line)
            # Recombine the split parts, adding back the delimiters
            result = []
            for i in range(0, len(conditions), 2):
                condition = conditions[i]
                if i + 1 < len(conditions):
                    condition += " " + conditions[i + 1] + " "
                result.append(condition)
            return result
        else:
            return []

    def parse_route_policy(policy_text):
        """Parses route policy text and stores lines under if/else/elif statements in a dictionary.

        Args:
            policy_text (str): The route policy text.

        Returns:
            dict: A dictionary where keys are 'if', 'elif', or 'else' and values are lists of lines.
        """

        result = {}
        current_block = None
        indent_level = 0

        for line in policy_text.splitlines():
            line = line.strip()
            if not line:
                continue

            # Check for if/elif/else blocks
            match = re.match(r"(if|elif|else)(.*)", line)
            if match:
                current_block = match.group(1)
                result[current_block] = []
                indent_level = line.index(current_block)  # Get indentation level
            elif current_block:
                # Check if line is indented under the current block
                if line.startswith(" " * indent_level):
                    result[current_block].append(line.strip())
                else:
                    current_block = None  # Reset block if indentation doesn't match

        return result

    def get_policy_config(self, connection, name):
        policy_data = connection.get(f"show running-config route-policy {name}")
        route_maps_parser = Route_mapsTemplate(lines=policy_data.splitlines(), module=self._module)
        objs = list(route_maps_parser.parse().values())
        return objs

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Route_maps network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []
        policy_list = []

        if not data:
            data = self.get_policynames(connection=connection)

        # parse native config using the Route_maps template
        route_maps_parser = Route_mapsName(lines=data.splitlines(), module=self._module)
        objs = list(route_maps_parser.parse().values())

        for policies in objs:
            policy_list.append(self.get_policy_config(connection=connection, name=policies))

        ansible_facts["ansible_network_resources"].pop("route_maps", None)

        params = utils.remove_empties(
            route_maps_parser.validate_config(self.argument_spec, {"config": objs}, redact=True),
        )

        facts["route_maps"] = params["config"]
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts
