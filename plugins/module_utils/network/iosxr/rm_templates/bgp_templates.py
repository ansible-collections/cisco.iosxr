# -*- coding: utf-8 -*-
# Copyright 2023 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Bgp_templates parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


def _tmpl_aigp(config_data):
    conf = config_data.get("aigp", {})
    commands = []
    if conf:
        if "set" in conf:
            commands.append("aigp")
        if "disable" in conf:
            commands.append("aigp disable")
        if "send_cost_community_disable" in conf:
            commands.append("aigp send cost-community disable")
        if "send_med" in conf and "set" in conf.get("send_med", {}):
            commands.append("aigp send med")
        if "send_med" in conf and "disable" in conf.get("send_med", {}):
            commands.append("aigp send med disable")
    return commands


class Bgp_templatesTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Bgp_templatesTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "router",
            "getval": re.compile(
                r"""
                ^router\s
                bgp
                \s(?P<as_num>\S+)
                $""",
                re.VERBOSE,
            ),
            "setval": "router bgp {{ as_number }}",
            "compval": "as_number",
            "result": {"as_number": "{{ as_num }}"},
            "shared": True,
        },
        {
            "name": "address_family",
            "getval": re.compile(
                r"""
                (\s+(?P<nbr_address>neighbor-group\s\S+))
                (?P<address_family>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                $""", re.VERBOSE,
            ),
            "setval": "address-family {{ afi}} {{safi}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "name": "{{nbr_address.split(" ")[1]}}",
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "afi": "{{ afi}}",
                                        "safi": "{{safi}}",
                                    },
                                },
                            },
                        },
            },
            "shared": True,
        },
        {
            "name": "signalling",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sSignalling(?P<signalling>)
                (\sbgp\sdisable(?P<b_disable>))?
                (\sldp\sdisable(?P<l_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "'signalling bgp disable' if {{signalling.bgp_disable}} else 'signalling ldp disable' ",
            "result": {
                "neighbor": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "address_family": {
                            '{{"address_family_" + afi + "_" + safi }}': {
                                "signalling": {
                                    "bgp_disable": "{{ True if b_disable is defined }}",
                                    "ldp_disable": "{{ True if l_disable is defined}}",
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "aigp",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \saigp(?P<aigp>)
                (\sdisable(?P<disable>))?
                (\ssend\smed(?P<send_med>))?
                (\ssend\smed\sdisable(?P<send_disable>))?
                (\ssend\scost-community\sdisable(?P<cc_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": _tmpl_aigp,
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "aigp": {
                                            "set": "{{ True if aigp is defined }}",
                                            "disable": "{{ True if disable is defined}}",
                                            "send_med": {
                                                "set": "{{ True if send_med is defined }}",
                                                "disable": "{{ True if send_disable is defined}}",
                                            },
                                            "send_cost_community_disable": "{{True if cc_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
    ]
    # fmt: on
