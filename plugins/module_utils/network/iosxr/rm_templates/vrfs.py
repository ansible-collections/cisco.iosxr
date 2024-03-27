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
            "setval": "description {{ description }}",
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
            "setval": "address-family {{ afi}} {{safi}}",
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
            "setval": "export route-policy {{ export.route_policy }}",
            "compval": "export.route_policy",
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
            "setval": "export route-target {{ export.route_target }}",
            "compval": "export.route_target",
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
            "setval": "export to default-vrf route-policy {{ export.to.default_vrf.route_policy }}",
            "compval": "export.to.default_vrf.route_policy",
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
            "setval": "export to vrf allow-imported-vpn",
            "compval": "export.to.vrf.allow_imported_vpn",
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
            "name": "import_config_route_target",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sroute-target\s(?P<import_config_route_target>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "import route-target {{ import_config.route_target }}",
            "compval": "import_config.route_target",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import_config": {
                                "route_target": "{{import_config_route_target}}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "import_config_route_policy",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sroute-policy\s(?P<import_config_route_policy>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "import route-policy {{ import_config.route_policy }}",
            "compval": "import_config.route_policy",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import_config": {
                                "route_policy": "{{import_config_route_policy}}",
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "import_config_from_bridge_domain_advertise_as_vpn",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sfrom\sbridge-domain\s(?P<advertise_as_vpn>advertise-as-vpn)
                $""", re.VERBOSE,
            ),
            "setval": "import from bridge-domain advertise-as-vpn",
            "compval": "import_config.from.bridge_domain.advertise_as_vpn",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import_config": {
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
            "name": "import_config_from_default_vrf_route_policy",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sfrom\sdefault-vrf\sroute-policy\s(?P<import_config_from_default_vrf_route_policy>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "import from default-vrf route-policy {{ import_config.from.default_vrf.route_policy }}",
            "compval": "import_config.from.default_vrf.route_policy",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import_config": {
                                "from": {
                                    "default_vrf": {
                                        "route_policy": "{{ import_config_from_default_vrf_route_policy }}",
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        {
            "name": "import_config_from_vrf_advertise_as_vpn",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<address_families>\s+address-family\s(?P<afi>\S+)\s(?P<safi>\S+))
                \s+import\sfrom\svrf\s(?P<advertise_as_vpn>advertise-as-vpn)
                $""", re.VERBOSE,
            ),
            "setval": "import from vrf advertise-as-vpn",
            "compval": "import_config.from.vrf.advertise_as_vpn",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "address_families": {
                        '{{"address_families_" + afi + "_" + safi }}': {
                            "afi": "{{ afi}}",
                            "safi": "{{safi}}",
                            "import_config": {
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
            "setval": "maximum prefix {{ maximum.prefix }}",
            "compval": "maximum.prefix",
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
            "name": "evpn_route_sync",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+evpn-route-sync\s(?P<evpn_route_sync>\d+)
                $""", re.VERBOSE,
            ),
            "setval": "evpn-route-sync {{ evpn_route_sync }}",
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
                \s+fallback-vrf\s(?P<fallback_vrf>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "fallback-vrf {{ fallback_vrf }}",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "fallback_vrf": "{{ fallback_vrf }}",
                },
            },
        },
        {
            "name": "mhost_default_interface",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                (?P<mhost>\s+mhost\s(?P<afi>\S+))
                \s+default-interface\s(?P<default_interface>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "mhost {{ mhost.afi }} default-interface {{ mhost.default_interface }}",
            "compval": "mhost.default_interface",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "mhost": {
                        "afi": "{{ afi }}",
                        "default_interface": "{{ default_interface }}",
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
            "setval": "rd {{ rd }}",
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
            "setval": "remote-route-filtering disable",
            "compval": "remote_route_filtering.disable",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "remote_route_filtering": {
                        "disable": "{{ true if disable is defined }}",
                    },
                },
            },
        },
        {
            "name": "vpn_id",
            "getval": re.compile(
                r"""
                ^vrf\s(?P<name>\S+)
                \s+vpn\sid\s(?P<vpn_id>\S+)
                $""", re.VERBOSE,
            ),
            "setval": "vpn id {{ vpn.id }}",
            "compval": "vpn.id",
            "result": {
                '{{ name }}': {
                    'name': '{{ name }}',
                    "vpn": {
                        "id": "{{ vpn_id }}",
                    },
                },
            },
        },
    ]
    # fmt: on
