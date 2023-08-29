#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The iosxr_lacp class
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to it's desired end-state is
created
"""


from __future__ import absolute_import, division, print_function


__metaclass__ = type


from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base import (
    ConfigBase,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_diff,
    remove_empties,
    to_list,
)

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import Facts
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.utils.utils import (
    flatten_dict,
)


class Lacp(ConfigBase):
    """
    The iosxr_lacp class
    """

    gather_subset = ["!all", "!min"]

    gather_network_resources = ["lacp"]

    def __init__(self, module):
        super(Lacp, self).__init__(module)

    def get_lacp_facts(self, data=None):
        """Get the 'facts' (the current configuration)

        :rtype: A dictionary
        :returns: The current configuration as a dictionary
        """
        facts, _warnings = Facts(self._module).get_facts(
            self.gather_subset,
            self.gather_network_resources,
            data=data,
        )
        lacp_facts = facts["ansible_network_resources"].get("lacp")
        if not lacp_facts:
            return {}
        return lacp_facts

    def execute_module(self):
        """Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        result = {"changed": False}
        warnings = list()
        commands = list()

        if self.state in self.ACTION_STATES:
            existing_lacp_facts = self.get_lacp_facts()
        else:
            existing_lacp_facts = {}

        if self.state in self.ACTION_STATES or self.state == "rendered":
            commands.extend(self.set_config(existing_lacp_facts))

        if commands and self.state in self.ACTION_STATES:
            if not self._module.check_mode:
                self._connection.edit_config(commands)
            result["changed"] = True

        if self.state in self.ACTION_STATES:
            result["commands"] = commands

        if self.state in self.ACTION_STATES or self.state == "gathered":
            changed_lacp_facts = self.get_lacp_facts()

        elif self.state == "rendered":
            result["rendered"] = commands

        elif self.state == "parsed":
            running_config = self._module.params["running_config"]
            if not running_config:
                self._module.fail_json(
                    msg="value of running_config parameter must not be empty for state parsed",
                )
            result["parsed"] = self.get_lacp_facts(data=running_config)

        if self.state in self.ACTION_STATES:
            result["before"] = existing_lacp_facts
            if result["changed"]:
                result["after"] = changed_lacp_facts

        elif self.state == "gathered":
            result["gathered"] = changed_lacp_facts

        result["warnings"] = warnings
        return result

    def set_config(self, existing_lacp_facts):
        """Collect the configuration from the args passed to the module,
            collect the current configuration (as a dict from facts)

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        want = self._module.params.get("config")
        if not want:
            want = {}
        have = existing_lacp_facts
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
        if self.state in ("merged", "replaced", "rendered") and not want:
            self._module.fail_json(
                msg="value of config parameter must not be empty for state {0}".format(
                    self.state,
                ),
            )

        if self.state == "deleted":
            commands = self._state_deleted(want, have)
        elif self.state in ("merged", "rendered"):
            commands = self._state_merged(want, have)
        elif self.state in ["replaced", "overridden"]:
            commands = self._state_replaced(want, have)

        return commands

    def _state_replaced(self, want, have):
        """The command generator when state is replaced

        :rtype: A list
        :returns: the commands necessary to migrate the current configuration
                  to the desired configuration
        """
        commands = []

        commands.extend(self._state_deleted(want, have))

        commands.extend(self._state_merged(want, have))

        return commands

    def _state_merged(self, want, have):
        """The command generator when state is merged

        :rtype: A list
        :returns: the commands necessary to merge the provided into
                  the current configuration
        """
        commands = []

        updates = dict_diff(have, want)
        if self.state == "rendered":
            updates = want
        if updates:
            for key, value in iteritems(
                flatten_dict(remove_empties(updates["system"])),
            ):
                commands.append(
                    "lacp system {0} {1}".format(
                        key.replace("address", "mac"),
                        value,
                    ),
                )

        return commands

    def _state_deleted(self, want, have):
        """The command generator when state is deleted

        :rtype: A list
        :returns: the commands necessary to remove the current configuration
                  of the provided objects
        """
        commands = []

        for x in [
            k for k in have.get("system", {}) if k not in remove_empties(want.get("system", {}))
        ]:
            commands.append("no lacp system {0}".format(x))

        return commands
