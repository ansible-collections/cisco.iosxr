# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The iosxr_interfaces class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import Facts
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.utils.utils import (
    add_command_to_config_list,
    dict_to_set,
    filter_dict_having_none_value,
    get_interface_type,
    normalize_interface,
    remove_command_from_config_list,
    remove_duplicate_interface,
)


class Interfaces(ConfigBase):
    """
    The iosxr_interfaces class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["interfaces"]

    params = ("description", "mtu", "speed", "duplex")

    def __init__(self, module):
        super(Interfaces, self).__init__(module)

    def get_interfaces_facts(self, data=None):
        """Get the 'facts' (the current configuration)
        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        interfaces_facts = facts["ansible_network_resources"].get("interfaces")
        if not interfaces_facts:
            return []
        return interfaces_facts

    def execute_module(self):
        """Execute the module
        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        warnings = list()
        commands = list()

        if self.state in self.ACTION_STATES:
            existing_interfaces_facts = self.get_interfaces_facts()
        else:
            existing_interfaces_facts = []

        if self.state in self.ACTION_STATES or self.state == "rendered":
            commands.extend(self.set_config(existing_interfaces_facts))

        if commands and self.state in self.ACTION_STATES:
            if not self._module.check_mode:
                self._connection.edit_config(commands)
            result["changed"] = True

        if self.state in self.ACTION_STATES:
            result["commands"] = commands

        if self.state in self.ACTION_STATES or self.state == "gathered":
            changed_interfaces_facts = self.get_interfaces_facts()

        elif self.state == "rendered":
            result["rendered"] = commands

        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_interfaces_facts(data=running_config)

        if self.state in self.ACTION_STATES:
            result["before"] = existing_interfaces_facts
            if result["changed"]:
                result["after"] = changed_interfaces_facts

        elif self.state == "gathered":
            result["gathered"] = changed_interfaces_facts

        result["warnings"] = warnings
        return result

    def set_config(self, existing_interfaces_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params["config"]
        have = existing_interfaces_facts
        resp = self.set_state(want, have)

        return to_list(resp)

    def set_state(self, want, have):
        """Select the appropriate function based on the state provided
        :param want: the desired configuration as a dictionary
        :param have: the current configuration as a dictionary
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        if self.state in ("overridden", "merged", "replaced", "rendered") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    self.state,
                ),
            )

        if self.state == "overridden":
            commands = self._state_overridden(want, have)
        elif self.state == "deleted":
            commands = self._state_deleted(want, have)
        elif self.state in ("merged", "rendered"):
            commands = self._state_merged(want, have)
        elif self.state == "replaced":
            commands = self._state_replaced(want, have)

        return commands

    def _state_replaced(self, want, have):
        """The command generator when state is replaced
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []

        for interface in want:
            for each in have:
                if each["name"] == interface["name"] or interface["name"] in each["name"]:
                    break
            else:
                continue
            have_dict = filter_dict_having_none_value(interface, each)
            want = dict()
            commands.extend(self._clear_config(want, have_dict))
            commands.extend(self._set_config(interface, each))
        # Remove the duplicate interface call
        commands = remove_duplicate_interface(commands)

        return commands

    def _state_overridden(self, want, have):
        """The command generator when state is overridden
        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []
        not_in_have = set()
        in_have = set()

        for each in have:
            for interface in want:
                interface["name"] = normalize_interface(interface["name"])
                if each["name"] == interface["name"]:
                    in_have.add(interface["name"])
                    break
                if interface["name"] != each["name"]:
                    not_in_have.add(interface["name"])
            else:
                # We didn't find a matching desired state, which means we can
                # pretend we received an empty desired state.
                interface = dict(name=each["name"])
                kwargs = {"want": interface, "have": each}
                commands.extend(self._clear_config(**kwargs))
                continue
            have_dict = filter_dict_having_none_value(interface, each)
            commands.extend(self._clear_config(dict(), have_dict))
            commands.extend(self._set_config(interface, each))
        # Add the want interface that's not already configured in have interface
        for each in not_in_have - in_have:
            for every in want:
                interface = "interface {0}".format(every["name"])
                if each and interface not in commands:
                    commands.extend(self._set_config(every, {}))
        # Remove the duplicate interface call
        commands = remove_duplicate_interface(commands)

        return commands

    def _state_merged(self, want, have):
        """The command generator when state is merged
        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []
        flag = 0
        for interface in want:
            if self.state == "rendered":
                commands.extend(self._set_config(interface, dict()))
            else:
                for each in have:
                    if each["name"] == interface["name"] or interface["name"] in each["name"]:
                        flag = 1
                        break
                if flag == 1:
                    commands.extend(self._set_config(interface, each))
                else:
                    commands.extend(self._set_config(interface, dict()))

        return commands

    def _state_deleted(self, want, have):
        """The command generator when state is deleted
        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []

        if want:
            for interface in want:
                for each in have:
                    if each["name"] == interface["name"] or interface["name"] in each["name"]:
                        break
                else:
                    continue
                interface = dict(name=interface["name"])
                commands.extend(self._clear_config(interface, each))
        else:
            for each in have:
                want = dict()
                commands.extend(self._clear_config(want, each))

        return commands

    def _set_config(self, want, have):
        # Set the interface config based on the want and have config
        commands = []
        want["name"] = normalize_interface(want["name"])
        interface = "interface " + want["name"]
        # Get the diff b/w want and have
        want_dict = dict_to_set(want)
        have_dict = dict_to_set(have)
        diff = want_dict - have_dict

        if diff:
            diff = dict(diff)
            for item in self.params:
                if diff.get(item):
                    cmd = item + " " + str(want.get(item))
                    add_command_to_config_list(interface, cmd, commands)
            if diff.get("enabled"):
                add_command_to_config_list(interface, "no shutdown", commands)
            elif diff.get("enabled") is False:
                add_command_to_config_list(interface, "shutdown", commands)

        return commands

    def _clear_config(self, want, have):
        # Delete the interface config based on the want and have config
        commands = []

        if want.get("name"):
            interface_type = get_interface_type(want["name"])
            interface = "interface " + want["name"]
        else:
            interface_type = get_interface_type(have["name"])
            interface = "interface " + have["name"]

        if have.get("description") and want.get("description") != have.get(
            "description",
        ):
            remove_command_from_config_list(interface, "description", commands)

        if interface_type.lower() == "gigabitethernet":
            if (
                have.get("speed")
                and have.get("speed") != "auto"
                and want.get("speed") != have.get("speed")
            ):
                remove_command_from_config_list(interface, "speed", commands)
            if (
                have.get("duplex")
                and have.get("duplex") != "auto"
                and want.get("duplex") != have.get("duplex")
            ):
                remove_command_from_config_list(interface, "duplex", commands)

        if interface_type.lower() in [
            "gigabitethernet",
            "fourhundredgige",
            "fiftygige",
            "fortygige",
            "hundredgige",
            "twohundredgige",
            "tengige",
            "twentyfivegige",
        ]:
            if have.get("mtu") and want.get("mtu") != have.get("mtu"):
                remove_command_from_config_list(interface, "mtu", commands)

        return commands
