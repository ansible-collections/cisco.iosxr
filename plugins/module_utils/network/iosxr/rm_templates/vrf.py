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
        super(VrfTemplate, self).__init__(
            lines=lines,
            tmplt=self,
            module=module,
        )

    # fmt: off
    PARSERS = [
        {
            "name": "description",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+description\s(?P<description>.+$)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} description {{ description }}",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    'description': '{{ description }}',
                },
            },
        },
        {
            "name": "address_family",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} address-families {{ afi}} {{safi}}",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                        },
                    },
                },
            },
            # "shared": True,
        },
        {
            "name": "export_route_policy",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+export\sroute-policy\s(?P<export_route_policy>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} export {{ export_route_policy }}",
            "compval": "export",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "export": {
                                "route_policy": "{{ export_route_policy }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "export_route_target",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+export\sroute-target\s(?P<export_route_target>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} export {{ export_route_target }}",
            "compval": "export",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "export": {
                                "route_target": "{{ export_route_target }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "export_to_default_vrf_route_policy",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+export\sto\sdefault-vrf\sroute-policy\s(?P<export_to_default_vrf_route_policy>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} export to default-vrf route-policy {{ export to default-vrf route_policy }}",
            "compval": "default_vrf",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "export": {
                                "to": {
                                    "default_vrf": {
                                        "route_policy": "{{ export_to_default_vrf_route_policy }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "export_to_vrf_allow_imported_vpn",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+export\sto\svrf\s(?P<allow_imported_vpn>allow-imported-vpn)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} export to vrf allow-imported-vpn",
            "compval": "import",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "export": {
                                "to": {
                                    "vrf": {
                                        "allow_imported_vpn": "{{ true if allow_imported_vpn is defined }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "import_route_target",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sroute-target\s(?P<import_route_target>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} import {{ import_route_target }}",
            "compval": "import",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import": {
                                "route_target": "{{import_route_target}}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "import_route_policy",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sroute-policy\s(?P<import_route_policy>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} import {{ import_route_policy }}",
            "compval": "import",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import": {
                                "route_policy": "{{import_route_policy}}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "import_from_bridge_domain_advertise_as_vpn",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sfrom\sbridge-domain\s(?P<advertise_as_vpn>advertise-as-vpn)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} import from bridge-domain advertise-as-vpn",
            "compval": "import",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import": {
                                "from": {
                                    "bridge_domain": {
                                        "advertise_as_vpn": "{{ true if advertise_as_vpn is defined }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "import_from_default_vrf_route_policy",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sfrom\sdefault-vrf\sroute-policy\s(?P<import_from_default_vrf_route_policy>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} import from default-vrf route-policy {{ import from default-vrf route_policy }}",
            "compval": "default_vrf",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import": {
                                "from": {
                                    "default_vrf": {
                                        "route_policy": "{{ import_from_default_vrf_route_policy }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "import_from_vrf_advertise_as_vpn",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sfrom\svrf\s(?P<advertise_as_vpn>advertise-as-vpn)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} import from vrf advertise-as-vpn",
            "compval": "vrf_advertise_as_vpn",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import": {
                                "from": {
                                    "vrf": {
                                        "advertise_as_vpn": "{{ true if advertise_as_vpn is defined }}",
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
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+maximum\sprefix\s(?P<maximum_prefix>\d+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} maximum-prefix {{ maximum_prefix }}",
            "compval": "maximum_prefix",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "maximum": {
                                "prefix": "{{ maximum_prefix }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "maximum_threshold",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+maximum\sthreshold\s(?P<maximum_threshold>\d+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} maximum-threshold {{ maximum_threshold }}",
            "compval": "maximum_threshold",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "maximum": {
                                "threshold": "{{ maximum_threshold }}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "evpn_route_sync",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+evpn-route-sync\s(?P<evpn_route_sync>\d+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} evpn-route-sync {{ evpn_route_sync }}",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "evpn_route_sync": "{{ evpn_route_sync }}",
                },
            },
        },
        {
            "name": "fallback_vrf",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+fallback-vrf\s\"(?P<fallback_vrf>\S+)\"
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} fallback-vrf {{ fallback_vrf }}",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "fallback_vrf": "{{ fallback_vrf }}",
                },
            },
        },
        {
            "name": "mhost_ipv4_default_interface",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+mhost
                (\s(?P<afi>ipv4|ipv6))?
                \s+default-interface\s(?P<ipv4_default_interface>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} mhost ipv4 default-interface {{ mhost ipv4 default_interface }}",
            "compval": "mhost.ipv4.default.interface",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "mhost": {
                        "afi": "{{ afi }}",
                        "default_interface": "{{ ipv4_default_interface }}",
                    },
                },
            },
        },
        {
            "name": "rd",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+rd\s(?P<rd>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} rd {{ rd }}",
            "compval": "rd",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "rd": "{{ rd }}",
                },
            },
        },
        {
            "name": "remote_route_filtering_disable",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+remote-route-filtering\s(?P<disable>disable)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} remote-route-filtering disable",
            "compval": "remote_route_filtering.disable",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "remote_route_filtering": "{{ True if disable is defined }}",
                },
            },
        },
        {
            "name": "vpn_id",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+vpn\s(?P<id>\d+)
                $""", re.VERBOSE,
            ),
            "setval": "vrf {{ name }} vpn {{ id }}",
            "compval": "vpn_id",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "vpn": {
                        "id": "{{ id }}",
                    },
                },
            },
        },
    ]
    # fmt: on
