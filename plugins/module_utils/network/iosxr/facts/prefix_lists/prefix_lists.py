# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr prefix_lists fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy


from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.prefix_lists import (
    Prefix_listsTemplate,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.prefix_lists.prefix_lists import (
    Prefix_listsArgs,
)

class Prefix_listsFacts(object):
    """ The iosxr prefix_lists facts class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = Prefix_listsArgs.argument_spec

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Prefix_lists network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        afi_list = []
        obj = []
        if not data:
            data = connection.get("show running-config")

        # parse native config using the Prefix_lists template
        prefix_lists_parser = Prefix_listsTemplate(lines=data.splitlines(), module=self._module)
        objs = prefix_lists_parser.parse()
        for ob in objs.values():
            if ob.get("afi") not in afi_list:
                afi_list.append(ob.get("afi"))

        for afi in afi_list:
            entry = {"afi": afi, "prefix_lists": []}
            obj.append(entry)

        for item in objs:
            if "ipv4" in item:
                for entry in obj:
                    if entry.get("afi") == "ipv4":
                        del objs[item]["afi"]
                        if len(objs[item]) != 0:
                            entry.get("prefix_lists").append(objs[item])
            else:
                for entry in obj:
                    if entry.get("afi") == "ipv6":
                        del objs[item]["afi"]
                        if len(objs[item]) != 0:
                            entry.get("prefix_lists").append(objs[item])
        ansible_facts['ansible_network_resources'].pop('prefix_lists', None)
        #import epdb;epdb.serve()
        params = utils.remove_empties(
            prefix_lists_parser.validate_config(
                self.argument_spec, {"config": obj}, redact=True
            )
        )

        facts['prefix_lists'] = params.get('config')
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts
