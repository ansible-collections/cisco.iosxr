# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The iosxr vrf fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.vrfs.vrfs import (
    VrfsArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.vrfs import (
    VrfTemplate,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.utils.utils import (
    flatten_config,
)


class VrfFacts(object):
    """The iosxr vrf facts class"""

    def __init__(self, module, subspec="config", options="options"):
        self._module = module
        self.argument_spec = VrfsArgs.argument_spec

    def get_config(self, connection):
        """Get the configuration from the device"""

        return connection.get("show running-config vrf")

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for Vrf network resource
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """

        facts = {}
        objs = []
        obj = {}

        if not data:
            data = self.get_config(connection)

        export_data = flatten_config(data, "export")
        import_data = flatten_config(export_data, "import")
        address_data = flatten_config(import_data, "address-family")
        data = flatten_config(address_data, "vrf")

        # parse native config using the Vrf template
        vrf_parser = VrfTemplate(lines=data.splitlines(), module=self._module)
        obj = vrf_parser.parse()
        objs = list(obj.values())

        for vrf in objs:
            af = vrf.get("address_families", {})
            if af:
                self._post_parse(vrf)
            else:
                vrf["address_families"] = []

        ansible_facts["ansible_network_resources"].pop("vrf", None)
        params = utils.remove_empties(
            vrf_parser.validate_config(
                self.argument_spec,
                {"config": objs},
                redact=True,
            ),
        )

        facts["vrf"] = params.get("config", {})
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts

    def _post_parse(self, af_data):
        """Converts the intermediate data structure
            to valid format as per argspec.
        :param obj: dict
        """
        af = af_data.get("address_families", {})
        if af:
            af_data["address_families"] = list(af.values())
