# -*- coding: utf-8 -*-
# Copyright 2024 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Vrf parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class VrfTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(VrfTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "vrf",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<vrf>\S+)
                $""", re.VERBOSE),
            "setval": "",
            "result": {
                "vrf": "{{ vrf }}",
            },
            "shared": True
        },
        {
            "name": "address_family",
            "getval": re.compile(
                r"""
                \saddress-family
                (\s(?P<afi>ipv4|ipv6))?
                (\s(?P<safi>flowspec|multicast|unicast))?
                $""", re.VERBOSE,
            ),
            "setval": "address-family {{ afi}} {{safi}}",
            "result": {
                "address_family": {
                    '{{"address_family_" + afi + "_" + safi }}': {
                        "afi": "{{ afi}}",
                        "safi": "{{safi}}",
                    },
                },
            },
            "shared": True,
        },
        {
            "name": "export",
            "getval": re.compile(
                r"""
                \s+export\s(?P<value>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "export {{ export }}",
            "compval": "export",
            "result": {
                "address_family": {
                    '{{"address_family_" + afi + "_" + safi }}': {
                        "export": "{{value}}",
                    },
                },
            },
        },
        {
            "name": "import",
            "getval": re.compile(
                r"""
                \s+import\s(?P<value>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "import {{ import }}",
            "compval": "import",
            "result": {
                "address_family": {
                    '{{"address_family_" + afi + "_" + safi }}': {
                        "import": "{{value}}",
                    },
                },
            },
        },
        {
            "name": "route_target",
            "getval": re.compile(
                r"""
                \s+route-target\s(?P<route_target>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "route-target {{ route_target }}",
            "compval": "route_target",
            "result": {
                "address_family": {
                    '{{"address_family_" + afi + "_" + safi }}': {
                        "route_target": "{{route_target}}",
                    },
                },
            },
        },
        {
            "name": "route_policy",
            "getval": re.compile(
                r"""
                \s+route-policy\s(?P<route_policy>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "route-policy {{ route_policy }}",
            "compval": "route_policy",
            "result": {
                "address_family": {
                    '{{"address_family_" + afi + "_" + safi }}': {
                        "route_policy": "{{route_policy}}",
                    },
                },
            },
        },
        {
            "name": "bridge_domain_advertise_as_vpn",
            "getval": re.compile(
                r"""
                \s+bridge-domain\s(?P<bridge_domain_advertise_as_vpn>advertise-as-vpn\S+)
                $""", re.VERBOSE,
            ),
            "setval": "bridge-domain {{ bridge_domain_advertise_as_vpn }}",
            "compval": "bridge_domain_advertise_as_vpn",
            "result": {
                "address_family": {
                    '{{"address_family_" + afi + "_" + safi }}': {
                        "bridge_domain_advertise_as_vpn": "{{True is bridge_domain_advertise_as_vpn is defined}}",
                    },
                },
            },
        },
        {
            "name": "default_vrf",
            "getval": re.compile(
                r"""
                ^default-vrf\s(?P<default_vrf>\S+)
                $""", re.VERBOSE),
            "setval": "default-vrf {{ default_vrf }}",
            "compval": "default_vrf",
            "result": {
                "address_family": {
                    '{{"address_family_" + afi + "_" + safi }}': {
                        "default_vrf": "{{ True if vrf is defined}}",
                    },
                },
            },
        },
        {
            "name": "vrf_advertise_as_vpn",
            "getval": re.compile(
                r"""
                \s+vrf\s(?P<vrf_advertise_as_vpn>advertise-as-vpn\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ vrf_advertise_as_vpn }}",
            "compval": "vrf_advertise_as_vpn",
            "result": {
                "address_family": {
                    '{{"address_family_" + afi + "_" + safi }}': {
                        "vrf_advertise_as_vpn": "{{True is advertise_as_vpn is defined}}",
                    },
                },
            },
        },
        {
            "name": "evpn_route_sync",
            "getval": re.compile(
                r"""
                ^evpn-route-sync\s(?P<evpn_route_sync>\d+)
                $""", re.VERBOSE),
            "setval": "",
            "result": {
                "evpn_route_sync": "{{ evpn_route_sync }}",
            },
        },
        {
            "name": "fallback_vrf",
            "getval": re.compile(
                r"""
                ^fallback_vrf:\s+(?P<fallback_vrf>\S+)
                \s+description:\s+(?P<description>.*)
                \s+type:\s+(?P<type>\S+)
                $""", re.VERBOSE),
            "setval": "",
            "result": {
                "fallback_vrf": "{{ fallback_vrf }}",
                "description": "{{ description }}",
                "type": "{{ type }}",
            },
        },
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^description\s(?P<description>.+)
                $""", re.VERBOSE),
            "setval": "",
            "result": {
                "description": "{{ description }}",
            },
        },
        {
            "name": "mhost_ipv4_default_interface",
            "getval": re.compile(
                r"""
                \s+mhost\s(?P<ipv4_default_interface>ipv4\sdefault\sinterface\s\S+)
                $""", re.VERBOSE,
            ),
            "setval": "mhost ipv4 default interface {{ mhost.ipv4.default.interface }}",
            "compval": "mhost.ipv4.default.interface",
            "result": {
                "mhost": {
                    "ipv4": {
                        "default_interface": "{{ ipv4_default_interface.split(" ")[3] }}",
                    },
                },
            },
        },
        {
            "name": "rd",
            "getval": re.compile(
                r"""
                \s+rd\s(?P<rd>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "rd {{ rd }}",
            "compval": "rd",
            "result": {
                "rd": "{{ rd }}",
            },
        },
        {
            "name": "remote_route_filtering_disable",
            "getval": re.compile(
                r"""
                \s+remote-route-filtering\s(?P<disable>disable)
                $""", re.VERBOSE,
            ),
            "setval": "remote-route-filtering disable",
            "compval": "remote_route_filtering.disable",
            "result": {
                "remote_route_filtering": {
                    "disable": "{{ True if disable is defined }}",
                },
            },
        },
        {
            "name": "vpn_id",
            "getval": re.compile(
                r"""
                \s+vpn\s(?P<vpn_id>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vpn {{ vpn_id }}",
            "compval": "vpn_id",
            "result": {
                "vpn_id": "{{ vpn_id }}",
            },
        }

    ]
    # fmt: on
