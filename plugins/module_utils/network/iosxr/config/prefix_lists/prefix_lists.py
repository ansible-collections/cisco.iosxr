#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr_prefix_lists config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module import (
    ResourceModule,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import (
    Facts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.prefix_lists import (
    Prefix_listsTemplate,
)


class Prefix_lists(ResourceModule):
    """
    The iosxr_prefix_lists config class
    """

    def __init__(self, module):
        super(Prefix_lists, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="prefix_lists",
            tmplt=Prefix_listsTemplate(),
        )
        self.parsers = [
            "prefix",
            "description",
            "prefix_list"
        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """

        wantd = self._list_to_dict(self.want)
        haved = self._list_to_dict(self.have)


        # if state is merged, merge want onto have and then compare
        if self.state == "merged":
            wantd = dict_merge(haved, wantd)

        # if state is deleted, empty out wantd and set haved to wantd
        if self.state == "deleted":
            haved = {
                k: v for k, v in iteritems(haved) if k in wantd or not wantd
            }
            wantd = {}

        # remove superfluous config for overridden and deleted
        if self.state in ["deleted", "overridden"]:
            for k, have in iteritems(haved):
                if k not in wantd:
                    cmd = self._tmplt.render(have, "prefix_list", True)
                    if cmd not in self.commands:
                        self.commands.append(cmd)
            # for overridden
            haved = {}


        for k, want in iteritems(wantd):
            self._compare(want=want, have=haved.pop(k, {}))

        if self.state in ["replaced", "overridden"]:
            self.commands = [
                                each for each in self.commands if "no" in each
                            ] + [each for each in self.commands if "no" not in each]

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Prefix_lists network resource.
        """

        self.compare(parsers=self.parsers, want=want, have=have)


    def _list_to_dict(self, entry):
         new_entry = {}
         if len(entry) != 0:
             for x in entry:
                 for prefix_list in x.get("prefix_lists", []):
                     if prefix_list.get("entries"):
                         for seq in prefix_list.get("entries", []):
                             seq.update(afi=x.get("afi"))
                             seq.update(name=prefix_list.get("name"))
                             new_entry[x.get("afi") + "_" + prefix_list.get("name") + str(seq.get("sequence"))] = seq

         return new_entry
