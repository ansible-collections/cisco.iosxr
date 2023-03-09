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


def _tmpl_default_originate(config_data):
    conf = config_data.get("default_originate", {})
    command = ""
    if conf:
        if "set" in conf:
            command = "default-originate"
        if "inheritance_disable" in conf:
            command = "default-originate inheritance-disable"
        if "route_policy" in conf:
            command = "default-originate route_policy " + conf["route_policy"]
    return command


def _tmpl_maximum_prefix(config_data):
    conf = config_data.get("maximum_prefix", {})
    if conf:
        command = "maximum-prefix"
        if "max_limit" in conf:
            command += " " + str(conf["max_limit"])
        if "threshold_value" in conf:
            command += " " + str(conf["threshold_value"])
        if "restart" in conf:
            command += " restart " + str(conf["restart"])
        elif "warning_only" in conf:
            command += " warning-only"
        elif "discard_extra_paths" in conf:
            command += " discard-extra-paths"

    return command


def _tmpl_next_hop_unchanged(config_data):
    conf = config_data.get("next_hop_unchanged", {})
    command = ""
    if conf:
        if "set" in conf:
            command = "next-hop-unchanged"
        if "inheritance_disable" in conf:
            command += "next-hop-unchanged inheritance-disable"
        if "multipath" in conf:
            command = "next-hop-unchanged multipath"
    return command


def _tmpl_soft_reconfiguration(config_data):
    conf = config_data.get("soft_reconfiguration", {})
    if conf:
        command = "soft-reconfiguration "
        if "inbound" in conf:
            command += "inbound"
            if "set" in conf["inbound"]:
                pass
            elif "always" in conf["inbound"]:
                command += " always"
            if "inheritance_disable" in conf["inbound"]:
                command += " inheritance-disable"

    return command


def _tmpl_remove_private_AS(config_data):
    conf = config_data.get("remove_private_AS", {})
    if conf:
        command = " "
        if "set" in conf:
            command = "remove-private-AS"
        if "inbound" in conf:
            command += " inbound"
        if "entire_aspath" in conf:
            command += " entire-aspath"
        elif "inheritance_disable" in conf:
            command = "remove-private-AS inheritance-disable"
    return command


def _templ_local_as(config_data):
    conf = config_data.get("local_as", {})
    if conf.get("value"):
        command = "local-as " + str(conf.get("value", {}))
    if "no_prepend" in conf:
        if "replace_as" in conf.get("no_prepend", {}):
            if "dual_as" in conf.get("no_prepend", {}).get("replace_as", {}):
                command += " no-prepend replace-as dual-as"
            elif "set" in conf.get("no_prepend", {}).get("replace_as", {}):
                command += " no-prepend replace-as"
        elif "set" in conf.get("no_prepend", {}):
            command += " no-prepend"
    return command


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
                (?P<nbr_address>neighbor-group\s\S+)
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
                (?P<nbr_address>neighbor-group\s\S+)
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
            "name": "advertise",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \sadvertise
                (\slocal-labeled-route(?P<set>))?
                (\sdisable(?P<l_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "'advertise local-labeled-route disable' if {{advertise.local_labeled_route.disable}} else 'advertise local-labeled-route' ",
            "result": {
                "neighbor": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "address_family": {
                            '{{"address_family_" + afi + "_" + safi }}': {
                                "advertise": {
                                    "local_labeled_route": {
                                        "set": "{{ True if disable not defined and set is defined}}",
                                        "disable": "{{ True if disable is defined}}",
                                    },
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
                (?P<nbr_address>neighbor-group\s\S+)
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
        {
            "name": "allowas_in",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \sallowas-in(?P<allowas_in>)(\s(?P<value>\S+))?
                $""", re.VERBOSE,
            ),
            "setval": "allowas-in {{allowas_in.value if allowas_in.value is defined }}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "allowas_in": {
                                            "set": "{{True if allowas_in is defined and value is not defined}}",
                                            "value": "{{value }}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "as_override",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sas-override(?P<as_override>)
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "as-override{{' inheritance-disable' if as_override.inheritance_disable is defined else ''}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "as_override": {
                                            "set": "{{True if as_override is defined "
                                                   "and inheritance_disable is not defined}}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "bestpath_origin_as_allow_invalid",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sbestpath\sorigin-as\sallow\sinvalid(?P<invalid>)
                $""", re.VERBOSE,
            ),
            "setval": "bestpath origin-as allow invalid",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "bestpath_origin_as_allow_invalid": "{{ True if invalid is defined}}",
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "capability_orf_prefix",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \scapability\sorf\sprefix\s(?P<capability_orf_prefix>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "capability orf prefix {{capability_orf_prefix }}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "capability_orf_prefix": "{{capability_orf_prefix}}",
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "default_originate",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \sdefault-originate(?P<default_originate>)
                (\sroute-policy\s(?P<route_policy>\S+))?
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": _tmpl_default_originate,
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi}}': {
                                        "default_originate": {
                                            "set": "{{True if default_originate is defined}}",
                                            "route_policy": "{{route_policy}}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "encapsulation_type_srv6",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \sencapsulation\stype\ssrv6(?P<encapsulation_type_srv6>)
                $""", re.VERBOSE,
            ),
            "setval": "capability orf prefix {{capability_orf_prefix }}",
            "result": {
                "neighbor": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "address_family": {
                            '{{"address_family_" + afi + "_" + safi }}': {
                                "encapsulation_type_srv6": "{{true if encapsulation_type_srv6 is defined}}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "long_lived_graceful_restart_capable",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \s+long-lived-graceful-restart
                \s(?P<capable>capable)
                $""", re.VERBOSE,
            ),
            "setval": "long-lived-graceful-restart capable",
            "compval": "long_lived_graceful_restart.capable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "long_lived_graceful_restart": {
                                            "capable": "{{True if capable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "long_lived_graceful_restart_stale_time",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \s+long-lived-graceful-restart
                \s+stale-time\ssend\s(?P<stale_time_send>\d+)\saccept\s(?P<accept>\d+)
                $""", re.VERBOSE,
            ),
            "setval": "long-lived-graceful-restart stale-time send "
                      "{{stale_time.send}} accept {{stale_time.accept}}",
            "compval": "long_lived_graceful_restart.stale_time",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "long_lived_graceful_restart": {
                                            "stale_time": {
                                                "send": "{{stale_time_send}}",
                                                "accept": "{{accept}}",
                                            },
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "maximum_prefix",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \s+maximum-prefix
                (\s(?P<maximum_prefix>\d+))?
                (\s(?P<threshold_value>\d+))?
                (\srestart\s(?P<restart>\d+))?
                (\swarning-only\s(?P<warning_only>))?
                (\sdiscard-extra-paths\s(?P<discard_extra_paths>))?
                $""", re.VERBOSE,
            ),
            "setval": _tmpl_maximum_prefix,
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "maximum_prefix": {
                                            "max_limit": "{{maximum_prefix}}",
                                            "threshold_value": "{{threshold_value}}",
                                            "restart": "{{restart}}",
                                            "warning_only": "{{ True if warning_only is defined}}",
                                            "discard_extra_paths": "{{ True if discard_extra_paths is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "multipath",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \smultipath(?P<multipath>)
                $""", re.VERBOSE,
            ),
            "setval": "multipath",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "multipath": "{{True if multipath is defined}}",
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "next_hop_self",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \snext-hop-self(?P<next_hop_self>)
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "next-hop-self{{' inheritance-disable' if next_hop_self.inheritance_disable is defined else ''}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "next_hop_self": {
                                            "set": "{{True if next_hop_self is defined and"
                                                   " inheritance_disable is not defined}}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "next_hop_unchanged",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \snext-hop-unchanged(?P<next_hop_unchanged>)
                (\sinheritance-disable(?P<inheritance_disable>))?
                (\smultipath(?P<multipath>))?
                $""", re.VERBOSE,
            ),
            "setval": _tmpl_next_hop_unchanged,
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi}}': {
                                        "next_hop_unchanged": {
                                            "set": "{{True if next_hop_self is defined }}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                            "multipath": "{{True if multipath is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "optimal_route_reflection_group_name",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \soptimal-route-reflection\s(?P<group_name>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "optimal-route-reflection {{optimal_route_reflection_group_name}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "optimal_route_reflection_group_name": "{{ group_name}}",
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "orf_route_policy",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor\s\S+)
                \sorf\sroute-policy\s(?P<orf_rr>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "orf route-policy {{orf_route_policy}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "orf_route_policy": "{{orf_rr}}",
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "origin_as",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sorigin-as\svalidation\sdisable(?P<origin_as>)
                $""", re.VERBOSE,
            ),
            "setval": "origin-as validation disable",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "origin_as": {
                                            "validation": {
                                                "disable": "{{True if origin_as is defined }}",
                                            },
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "remove_private_AS",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \sremove-private-AS(?P<remove_private_AS>)
                (\sinbound(?P<inbound>))?
                (\sentire-aspath(?P<entire_aspath>))?
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": _tmpl_remove_private_AS,
            "result": {
                        "neighbors": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "remove_private_AS": {
                                            "set": "{{True if remove_private_AS is defined}}",
                                            "inbound": "{{True if inbound is defined}}",
                                            "entire_aspath": "{{True if entire_aspath is defined}}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "route_policy.inbound",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \sroute-policy\s(?P<route_policy>\S+)
                \sin
                $""", re.VERBOSE,
            ),
            "setval": "route-policy {{route_policy.inbound}} in",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "route_policy": {
                                            "inbound": "{{route_policy}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "route_policy.outbound",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \sroute-policy\s(?P<route_policy>\S+)
                \sout
                $""", re.VERBOSE,
            ),
            "setval": "route-policy {{route_policy.outbound}} out",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "route_policy": {
                                            "outbound": "{{route_policy}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "route_reflector_client",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sroute-reflector-client(?P<route_reflector_client>)
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "route-reflector-client{{' inheritance-disable' "
                      "if route_reflector_client.inheritance_disable is defined }}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "route_reflector_client": {
                                            "set": "{{True if route_reflector_client is defined and "
                                                   "inheritance_disable is not defined }}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "send_community_ebgp",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \ssend-community-ebgp(?P<send_community_ebgp>)
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "send-community-ebgp{{' inheritance-disable' "
                      "if send_community_ebgp.inheritance_disable is defined else ''}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "send_community_ebgp": {
                                            "set": "{{True if send_community_ebgp is defined and "
                                                   "inheritance_disable is not defined}}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "send_community_gshut_ebgp",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \ssend-community-gshut-ebgp(?P<send_community_gshut_ebg>)
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "send-community-gshut-ebgp{{' inheritance-disable' "
                      "if send_community_gshut_ebgp.inheritance_disable is defined else ''}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "send_community_gshut_ebgp": {
                                            "set": "{{True if send_community_gshut_ebg is defined and "
                                                   "inheritance_disable is not defined}}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "send_extended_community_ebgp",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \ssend-extended-community-ebgp(?P<send_extended_community_ebgp>)
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "send-extended-community-ebgp{{' inheritance-disable' "
                      "if send_extended_community_ebgp.inheritance_disable is defined else ''}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "send_extended_community_ebgp": {
                                            "set": "{{True if send_extended_community_ebgp is defined and "
                                                   "inheritance_disable is not defined}}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "send_multicast_attributes",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \s+(?P<send_multicast_attributes>send-multicast-attributes)
                (\sdisable(?P<disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "send-multicast-attributes{{' disable' "
                      "if send_multicast_attributes.disable is defined else ''}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "send_multicast_attributes": {
                                            "set": "{{True if send_multicast_attributes is "
                                                   "defined and disable is not defined}}",
                                            "disable": "{{True if disable is defined}}",
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "soft_reconfiguration",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \ssoft-reconfiguration
                \sinbound(?P<inbound>)
                (\salways(?P<always>))?
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE,
            ),
            "setval": _tmpl_soft_reconfiguration,
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "soft_reconfiguration": {
                                            "inbound": {
                                                "set": "{{True if inbound is defined and "
                                                       "inheritance_disable is not defined and "
                                                       "always is not defined}}",
                                                "always": "{{True if always is defined }}",
                                                "inheritance_disable": "{{True if inheritance_disable is defined}}",
                                            },
                                        },
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "weight",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \sweight\s(?P<weight>\d+)
                $""", re.VERBOSE,
            ),
            "setval": "weight {{weight}}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + safi }}': {
                                        "weight": "{{weight}}",
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "use",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \suse\s(?P<af_use>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "weight {{weight}}",
            "result": {
                "neighbor": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "address_family": {
                            '{{"address_family_" + afi + "_" + safi }}': {
                                "use": "{{af_use}}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "update",
            "getval": re.compile(
                r"""
                (?P<nbr_address>neighbor-group\s\S+)
                \supdate\sout\soriginator-loopcheck(?P<set>)
                (\sdisable(?P<disable>))?
                $""", re.VERBOSE,
            ),
            "setval": "weight {{weight}}",
            "result": {
                "neighbor": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "address_family": {
                            '{{"address_family_" + afi + "_" + safi }}': {
                                "update":
                                    {
                                        "out_originator_loopcheck_disable": "{{True if disable is defined}}",
                                        "out_originator_loopcheck_set": "{{True if set is defined and disable is not defined}}",
                                    },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "advertisement_interval",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<advertise_in>advertisement-interval\s\d+)
                $""", re.VERBOSE,
            ),
            "setval": "advertisement-interval {{ advertisement_interval }}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "advertisement_interval": "{{ advertise_in.split(" ")[1] }}",
                            },
                        },
            },
        },
        {
            "name": "bfd_fast_detect_disable",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sbfd
                \sfast-detect
                \s(?P<disable>disable)
                $""", re.VERBOSE,
            ),
            "setval": "bfd fast-detect disable",
            "compval": "bfd.fast_detect.disable",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "bfd": {
                                    "fast_detect": {"disable": "{{ True if disable is defined }}"},
                                },
                            },
                        },
            },
        },
        {
            "name": "bfd_fast_detect_set",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sbfd
                \s(?P<fast_detect>fast-detect)
                $""", re.VERBOSE,
            ),
            "setval": "bfd fast-detect",
            "compval": "bfd.fast_detect.set",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "bfd": {
                                    "fast_detect": {"set": "{{ True if fast_detect is defined }}"},
                                },
                            },
                        },

            },
        },
        {
            "name": "bfd_fast_detect_strict_mode",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sbfd
                \sfast-detect
                \s(?P<strict_mode>strict-mode)
                $""", re.VERBOSE,
            ),
            "setval": "bfd fast-detect strict-mode",
            "compval": "bfd.fast_detect.strict_mode",
            "result": {
                "neighbor": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "bfd": {
                            "fast_detect": {"strict_mode": "{{ True if strict_mode is defined }}"},
                        },
                    },
                },
            },
        },
        {
            "name": "bfd_nbr_multiplier",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \sbfd
                \s(?P<multiplier>multiplier\s\S+)
                $""", re.VERBOSE,
            ),
            "setval": "bfd multiplier {{ bfd.multiplier}}",
            "compval": "bfd.multiplier",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}":
                                {
                                    "bfd":
                                        {
                                            "multiplier": "{{multiplier.split(" ")[1]}}",
                                        },
                                },
                        },
            },
        },
        {
            "name": "bfd_nbr_minimum_interval",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \sbfd
                \s(?P<min_interval>minimum-interval\s\S+)
                $""", re.VERBOSE,
            ),
            "setval": "bfd minimum-interval {{ bfd.minimum_interval}}",
            "compval": "bfd.minimum_interval",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}":
                                {
                                    "bfd":
                                        {
                                            "minimum_interval": "{{min_interval.split(" ")[1]}}",
                                        },
                                },
                        },
            },
        },
        {
            "name": "bmp_activate",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sbmp-activate
                \s(?P<bmp_activate>server\s\d+)
                $""", re.VERBOSE,
            ),
            "setval": "bmp-activate server {{bmp_activate.server}}",
            "compval": "bmp_activate.serevr",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "bmp_activate": {"server": "{{ bmp_activate.split(" ")[1] }}"},
                            },
                        },
            },
        },
        {
            "name": "neighbor_cluster_id",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<cluster_id>cluster-id\s\d+)
                $""", re.VERBOSE,
            ),
            "setval": "cluster-id {{ cluster_id }}",
            "compval": "cluster_id",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {"cluster_id": "{{ cluster_id.split(" ")[1] }}"},
                        },
            },
        },
        {
            "name": "neighbor_description",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sdescription\s(?P<description>.+)
                $""", re.VERBOSE,
            ),
            "setval": "description {{ description }}",
            "compval": "description",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {"description": "{{ description }}"},
                        },
            },
        },
        {
            "name": "dmz_link_bandwidth",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<dmz_link_bandwidth>dmz-link-bandwidth)
                $""", re.VERBOSE,
            ),
            "setval": "dmz-link-bandwidth",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}":
                                {
                                    "dmz_link_bandwidth":
                                        {
                                            "set": "{{ True if dmz_link_bandwidth is defined }}",
                                        },
                                },
                        },
            },
        },
        {
            "name": "dmz_link_bandwidth_inheritance_disable",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \sdmz-link-bandwidth
                \s(?P<dmz_link_bandwidth>inheritance_disable)
                $""", re.VERBOSE,
            ),
            "setval": "dmz-link-bandwidth inheritance-disable",
            "compval": "dmz_link_bandwidth.inheritance_disable",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "dmz_link_bandwidth":
                                    {
                                        "inheritance_disable": "{{ True if dmz_link_bandwidth is defined }}",
                                    },
                            },
                        },
            },
        },
        {
            "name": "dscp",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<dscp>dscp\s\S+)
                $""", re.VERBOSE,
            ),
            "setval": "dscp {{ dscp }}",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "dscp": "{{ dscp.split(" ")[1] }}",
                            },
                        },
            },
        },
        {
            "name": "ebgp_multihop_value",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<ebgp_multihop>ebgp-multihop\s\S+)
                $""", re.VERBOSE,
            ),
            "setval": "ebgp-multihop {{ ebgp_multihop.value}}",
            "compval": "ebgp_multihop.value",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "ebgp_multihop": {
                                    "value": "{{ ebgp_multihop.split(" ")[1] }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "ebgp_multihop_mpls",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<ebgp_multihop>ebgp-multihop\s\S*\smpls)
                $""", re.VERBOSE,
            ),
            "setval": "ebgp-multihop mpls",
            "compval": "ebgp_multihop.mpls",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "ebgp_multihop": {"mpls": "{{ True if ebgp_multihop is defined }}"},
                            },
                        },
            },

        },
        {
            "name": "ebgp_recv_extcommunity_dmz",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<ebgp_recv_extcommunity_dmz>ebgp-recv-extcommunity-dmz\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "ebgp-recv-extcommunity-dmz inheritance-disable ",
            "compval": "ebgp_recv_extcommunity_dmz.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "ebgp_recv_extcommunity_dmz": {
                                    "inheritance_disable": "{{ True if ebgp_recv_extcommunity_dmz is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "ebgp_send_extcommunity_dmz",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<ebgp_send_extcommunity_dmz>ebgp-send-extcommunity-dmz\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "ebgp-send-extcommunity-dmz inheritance-disable ",
            "compval": "ebgp_send_extcommunity_dmz.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "ebgp_send_extcommunity_dmz": {
                                    "inheritance_disable": "{{ True if ebgp_send_extcommunity_dmz is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "ebgp_send_extcommunity_dmz_set",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<ebgp_send_extcommunity_dmz>ebgp-send-extcommunity-dmz)
                $""", re.VERBOSE,
            ),
            "setval": "ebgp-send-extcommunity-dmz",
            "compval": "ebgp_send_extcommunity_dmz.set",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "ebgp_send_extcommunity_dmz": {
                                    "set": "{{ True if ebgp_send_extcommunity_dmz is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "ebgp_send_extcommunity_dmz_cumulatie",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<ebgp_send_extcommunity_dmz>ebgp-send-extcommunity-dmz\scumulatie)
                $""", re.VERBOSE,
            ),
            "setval": "ebgp-send-extcommunity-dmz cumulatie ",
            "compval": "ebgp_send_extcommunity_dmz.cumulatie",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "ebgp_send_extcommunity_dmz": {
                                    "cumulatie": "{{ True if ebgp_send_extcommunity_dmz is defined }}",
                                },
                            },
                        },

            },
        },
        {
            "name": "egress_engineering",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<egress_engineering>egress-engineering\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "egress-engineering inheritance-disable ",
            "compval": "egress_engineering.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "egress_engineering": {
                                    "inheritance_disable": "{{ True if egress_engineering is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "egress_engineering_set",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<egress_engineering>egress-engineering)
                $""", re.VERBOSE,
            ),
            "setval": "egress-engineering",
            "compval": "egress_engineering.set",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "egress_engineering": {
                                    "set": "{{ True if egress_engineering is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "neighbor_enforce_first_as_disable",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<enforce_first_as_disable>enforce-first-as\sdisable)
                $""", re.VERBOSE,
            ),
            "setval": "enforce-first-as disable",
            "compval": "enforce_first_as.disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "enforce_first_as": {
                                    "disable": "{{ True if enforce_first_as_disable is defined }}",
                                },
                            },
                        },
            },
        },
        {
            "name": "neighbor_graceful_restart_restart_time",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<graceful_restart_restart_time>graceful-restart\srestart-time\s\d+)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-restart restart-time {{ graceful_restart.restart_time}}",
            "compval": "graceful_restart.restart_time",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_restart": {
                                    "restart_time": "{{ graceful_restart_restart_time.split(" ")[2] }}",
                                },
                            },

                        },
            },
        },
        {
            "name": "neighbor_graceful_restart_stalepath_time",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<graceful_restart_stalepath_time>graceful-restart\sstalepath-time\s\d+)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-restart stalepath-time {{ graceful_restart.stalepath_time}}",
            "compval": "graceful_restart.stalepath_time",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_restart": {
                                    "stalepath_time": "{{ graceful_restart_stalepath_time.split(" ")[2] }}",
                                },
                            },
                        },
            },


        },
        {
            "name": "neighbor_graceful_maintenance_set",
            "getval": re.compile(
                r"""
               \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<graceful_maintenance>graceful-maintenance)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-maintenance",
            "compval": "graceful_maintenance.set",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_maintenance": {
                                    "set": "{{ True if graceful_maintenance is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "neighbor_graceful_maintenance_activate",
            "getval": re.compile(
                r"""
               \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<graceful_maintenance>graceful-maintenance\sactivate)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-maintenance activate",
            "compval": "graceful_maintenance.activate.set",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_maintenance": {
                                    "activate": {"set": "{{ True if graceful_maintenance is defined }}"},
                                },
                            },
                        },
            },

        },
        {
            "name": "neighbor_graceful_maintenance_activate_inheritance_disable",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<graceful_maintenance>activate\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-maintenance activate inheritance-disable",
            "compval": "graceful_maintenance.activate.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_maintenance": {
                                    "activate": {
                                        "inheritance_disable": "{{ True if graceful_maintenance is defined }}",
                                    },
                                },
                            },
                        },
            },

        },
        {
            "name": "neighbor_graceful_maintenance_as_prepends",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<as_prepends>as-prepends\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-maintenance as-prepends inheritance-disable",
            "compval": "graceful_maintenance.as_prepends.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_maintenance": {
                                    "as_prepends": {
                                        "inheritance_disable": "{{ True if as_prepends is defined }}",
                                    },
                                },
                            },
                        },

            },
        },
        {
            "name": "neighbor_graceful_maintenance_local_preference_disable",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<local_preference>local-preference\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-maintenance local-preference inheritance-disable",
            "compval": "graceful_maintenance.local_preference.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_maintenance": {
                                    "local_preference": {
                                        "inheritance_disable": "{{ True if local_preference is defined }}",
                                    },
                                },
                            },
                        },

            },
        },
        {
            "name": "neighbor_graceful_maintenance_local_preference",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<local_preference>local-preference\s\d+)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-maintenance local-preference {{ graceful_maintenance.local_preference.value}}",
            "compval": "graceful_maintenance.local_preference.value",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_maintenance": {
                                    "local_preference": {
                                        "value": "{{ local_preference.split(" ")[1]}}",
                                    },
                                },
                            },
                        },
            },

        },
        {
            "name": "neighbor_graceful_maintenance_as_prepends_value",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<as_prepends>as-prepends\s\d+)
                $""", re.VERBOSE,
            ),
            "setval": "graceful-maintenance as-prepends {{ graceful_maintenance.as_prepends.value }}",
            "compval": "graceful_maintenance.as_prepends.value",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "graceful_maintenance": {
                                    "as_prepends": {
                                        "value": "{{ as_prepends.split(" ")[1]}}",
                                    },
                                },
                            },
                        },
            },

        },
        {
            "name": "ignore_connected_check_set",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<ignore_connected_check>ignore-connected-check)
                $""", re.VERBOSE,
            ),
            "setval": "ignore-connected-check",
            "compval": "ignore_connected_check.set",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "ignore_connected_check": {
                                    "set": "{{ True if ignore_connected_check is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "ignore_connected_check",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<ignore_connected_check>ignore-connected-check\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "ignore-connected-check inheritance-disable ",
            "compval": "ignore_connected_check.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "ignore_connected_check": {
                                    "inheritance_disable": "{{ True if ignore_connected_check is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "idle_watch_time",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \sidle-watch-time(?P<idle_watch_time>\s\S+)
                $""", re.VERBOSE,
            ),
            "setval": "idle_watch_time {{idle_watch_time}} ",
            "result": {

                "neighbor": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "idle_watch_time": "{{idle_watch_time}}",
                    },
                },
            },

        },
        {
            "name": "internal_vpn_client",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                (?P<idle_watch_time>\sinternal-vpn-client)
                $""", re.VERBOSE,
            ),
            "setval": "internal-vpn-client ",
            "result": {

                "neighbor": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "internal_vpn_client": "{{true if internal_vpn_client is defined}}",
                    },
                },
            },

        },
        {
            "name": "keychain",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<keychain>keychain\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "keychain inheritance-disable ",
            "compval": "keychain.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "keychain": {
                                    "inheritance_disable": "{{ True if keychain is defined }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "keychain_name",
            "getval": re.compile(
                r"""
                 \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<keychain>keychain\s\S+)
                $""", re.VERBOSE,
            ),
            "setval": "keychain {{ name }}",
            "compval": "keychain.name",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "keychain": {
                                    "name": "{{ keychain.split(" ")[1] }}",
                                },
                            },
                        },
            },

        },
        {
            "name": "local_address",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \slocal
                \s(?P<local>address\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "local address inheritance-disable",
            "compval": "local.address.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "local": {
                                    "address": {
                                        "inheritance_disable": "{{ True if local is defined }}",
                                    },
                                },
                            },
                        },
            },

        },
        {
            "name": "local",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \slocal
                \s(?P<local>address\s\S+)
                $""", re.VERBOSE,
            ),
            "setval": "local address {{ local.address.ipv4_address }}",
            "compval": "local.address.ipv4_address",
            "result": {
                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "local": {
                                    "address": {
                                        "ipv4_address": "{{ local.split(" ")[1] }}",
                                    },
                                },
                            },
                        },
            },
        },
        {
            "name": "local_as",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \s(?P<local_as>local-as\s\S+)
                (\s(?P<no_prepend>no-prepend))?
                (\s(?P<replace_as>replace-as))?
                (\s(?P<dual_as>dual-as))?
                $""", re.VERBOSE,
            ),
            "setval": _templ_local_as,
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "local_as": {
                                    "value": "{{ local_as.split(" ")[1] }}",
                                    "no_prepend":
                                        {
                                            "set": "{{ True if no_prepend is defined and replace_as is undefined and dual_as is undefined else None}}",
                                            "replace_as": {
                                                "set": "{{ True if replace_as is defined and dual_as is undefined}}",
                                                "dual_as": "{{ not not dual_as}}",
                                            },
                                        },
                                },
                            },
                        },
            },

        },
        {
            "name": "local_address",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor-group\s\S+)
                \slocal
                \s(?P<local>address\sinheritance-disable)
                $""", re.VERBOSE,
            ),
            "setval": "local address inheritance-disable",
            "compval": "local.address.inheritance_disable",
            "result": {

                        "neighbor": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "local": {
                                    "address": {
                                        "inheritance_disable": "{{ True if local is defined }}",
                                    },
                                },
                            },
                        },
            },

        },

    ]
    # fmt: on
