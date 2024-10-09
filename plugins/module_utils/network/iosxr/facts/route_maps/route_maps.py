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


from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.route_maps.route_maps import (
    Route_mapsArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.route_maps import (
    Route_mapsTemplate,
)


class Route_mapsFacts(object):
    """The iosxr route_maps facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Route_mapsArgs.argument_spec

    def get_policynames(self, connection):
        return connection.get("show running-config | include route-policyx")

    def get_policydata(self, connection, name):
        return connection.get(f"show running-config route-policy {name}")

    def parse_condition(self, condition):
        if condition.startswith("if "):
            condition_type, cond = "if", (condition.lstrip("if ")).rstrip(" then")
        elif condition.startswith("elseif "):
            condition_type, cond = "elseif", (condition.lstrip("elseif ")).rstrip(" then")
        elif condition.startswith("else"):
            condition_type, cond = "else", ""
        elif condition.startswith("global"):
            condition_type, cond = "global", ""
        return condition_type, cond

    def parse_route_policy(self, route_policy):
        result = {}
        lines = route_policy.splitlines()
        current_key = None
        current_value = []
        store_global = True
        global_value = []
        else_data = {}

        def process_else(else_line):
            else_result = {}
            else_current_key = None
            else_current_value = []
            else_store_global = True
            else_global_value = []

            for line in else_line:
                line = line.strip()
                if line.startswith("if ") or line.startswith("elseif ") or line.startswith("else"):
                    else_store_global = False
                    if else_current_key:
                        else_result[else_current_key] = else_current_value
                    else_current_key = line
                    else_current_value = []
                else:
                    else_current_value.append(line)

                if else_store_global:
                    else_global_value.append(line)

                if else_global_value:
                    else_result["global"] = else_global_value

            if else_current_key:
                else_result[else_current_key] = else_current_value

            return else_result

        for idx, line in enumerate(lines):
            line = line.strip()

            if line.startswith("if ") or line.startswith("elseif "):
                store_global = False
                if current_key:
                    result[current_key] = current_value
                current_key = line
                current_value = []
            else:
                current_value.append(line)

            if not (line.startswith("if ") or line.startswith("elseif ")) and line.startswith(
                "else",
            ):
                else_data = process_else(lines[idx + 1 : :])  # noqa: E203
                break

            if store_global:
                global_value.append(line)

        # Add the last block
        if current_key:
            result[current_key] = current_value

        if else_data:
            result["else"] = else_data

        if global_value:
            result["global"] = global_value

        return result

    def get_policy_config(self, policy_data, name):
        policy_map_structured = self.parse_route_policy(policy_data)

        def else_resolve_policy_data(else_policy_map):
            else_policy_route = {}
            if_elif = []

            for condition, policy in else_policy_map.items():
                if_elif_data = {}
                cond_type, actual_cond = self.parse_condition(condition)

                route_maps_parser = Route_mapsTemplate(lines=policy, module=self._module)
                objs = list(route_maps_parser.parse().values())
                if cond_type in ["if", "global"]:
                    if objs:
                        else_policy_route[cond_type] = objs[0]
                        if cond_type != "global":
                            else_policy_route[cond_type]["condition"] = actual_cond
                elif cond_type == "elseif":
                    if_elif_data.update(objs[0])
                    if_elif_data["condition"] = actual_cond
                    if_elif.append(if_elif_data)
                elif cond_type == "else":
                    if objs:
                        else_policy_route[cond_type] = objs[0]

            if if_elif:
                else_policy_route["elseif"] = if_elif

            return else_policy_route

        def rec_resolve_policy_data(policy_map):
            policy_route = {
                "name": name,
            }
            if_elif = []
            else_data = {}

            for condition, policy in policy_map.items():
                if_elif_data = {}
                cond_type, actual_cond = self.parse_condition(condition)

                route_maps_parser = Route_mapsTemplate(lines=policy, module=self._module)
                objs = list(route_maps_parser.parse().values())
                if cond_type in ["if", "global"]:
                    if objs:
                        policy_route[cond_type] = objs[0]
                        if cond_type != "global":
                            policy_route[cond_type]["condition"] = actual_cond
                elif cond_type == "elseif":
                    if_elif_data.update(objs[0])
                    if_elif_data["condition"] = actual_cond
                    if_elif.append(if_elif_data)
                elif cond_type == "else":
                    else_data = else_resolve_policy_data(policy)

            if if_elif:
                policy_route["elseif"] = if_elif
            if else_data:
                policy_route["else"] = else_data

            return policy_route

        rec_policy_route = rec_resolve_policy_data(policy_map_structured)

        return rec_policy_route

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
        policy_names = []
        mock_data = False

        if not data:
            data = self.get_policynames(connection=connection)
        else:
            mock_data = True  # for states like parsed to work

        # parse native config using the Route_maps template
        route_maps_parser = Route_mapsTemplate(lines=[], module=self._module)

        for name in data.splitlines():
            if name.startswith("route-policy "):
                policy_names.append(name.split()[1])

        if mock_data:
            data_for_parsed = data.split("end-policy\n!")

        for idx, policy in enumerate(policy_names):
            if mock_data:
                policy_data = data_for_parsed[idx]
            else:
                policy_data = self.get_policydata(connection=connection, name=policy)
            objs.append(self.get_policy_config(policy_data=policy_data, name=policy))

        ansible_facts["ansible_network_resources"].pop("route_maps", None)

        params = utils.remove_empties(
            route_maps_parser.validate_config(self.argument_spec, {"config": objs}, redact=True),
        )

        facts["route_maps"] = params["config"]
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts
