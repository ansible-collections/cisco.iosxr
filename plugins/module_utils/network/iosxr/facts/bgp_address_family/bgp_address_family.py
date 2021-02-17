# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr bgp_address_family fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.bgp_address_family import (
    Bgp_address_familyTemplate,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.bgp_address_family.bgp_address_family import (
    Bgp_address_familyArgs,
)


class Bgp_address_familyFacts(object):
    """ The iosxr bgp_address_family facts class
    """

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = Bgp_address_familyArgs.argument_spec
        spec = deepcopy(self.argument_spec)
        if subspec:
            if options:
                facts_argument_spec = spec[subspec][options]
            else:
                facts_argument_spec = spec[subspec]
        else:
            facts_argument_spec = spec

        self.generated_spec = utils.generate_dict(facts_argument_spec)

    def get_config(self, connection):
        return connection.get("show running-config router bgp")

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Bgp_address_family network resource
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []
        if not data:
            data = self.get_config(connection)

        nb_data = self._flatten_config(data, "neighbor")
        data = self._flatten_config(nb_data, "vrf")
        # parse native config using the Bgp_global template
        bgp_global_parser = Bgp_address_familyTemplate(lines=data.splitlines())
        objs = bgp_global_parser.parse()

        af = objs.get("address_family")
        if af:
            self._post_parse(objs)
        else:
            objs["address_family"] = []

        ansible_facts["ansible_network_resources"].pop(
            "bgp_address_family", None
        )

        params = utils.remove_empties(
            utils.validate_config(self.argument_spec, {"config": objs})
        )

        facts["bgp_address_family"] = params.get("config", {})
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts

    def _post_parse(self, obj):
        """ Converts the intermediate data structure
            to valid format as per argspec.
        :param obj: dict
        """
        af = obj.get("address_family", {})
        if af:
            obj["address_family"] = list(af.values())

    def _flatten_config(self, data, context):
        """ Flatten different contexts in
            the running-config for easier parsing.
        :param obj: dict
        :returns: flattened running config
        """
        data = data.split("\n")
        in_nbr_cxt = False
        cur_nbr = {}

        for x in data:
            cur_indent = len(x) - len(x.lstrip())
            if x.strip().startswith(context):
                in_nbr_cxt = True
                cur_nbr["nbr"] = x
                cur_nbr["indent"] = cur_indent
            elif cur_nbr and (cur_indent <= cur_nbr["indent"]):
                in_nbr_cxt = False
            elif in_nbr_cxt:
                data[data.index(x)] = cur_nbr["nbr"] + " " + x.strip()
        return "\n".join(data)
