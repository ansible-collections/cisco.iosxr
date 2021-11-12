# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Snmp_server parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


def community_tmplt():
    """

    """


class Snmp_serverTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Snmp_serverTemplate, self).__init__(
            lines=lines, tmplt=self, module=module
        )

    # fmt: off
    PARSERS = [
        {
            "name": "chassis_id",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\s+chassis-id\s(?P<chassis_id>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server chassis-id {{chassis_id}}",
            "result": {
                "chassis_id": "{{chassis_id}}"
            }
        },
        {
            "name": "community",
            "getval": re.compile(
                r"""
                ^snmp-server\scomunity
                (\s(?P<name>\S+))?
                (\svrf\s(?P<vrf>\w+))?
                (\sseverity\s(?P<severity>alerts|critical|debugging|emergencies|error|informational|notifications|warnings))?
                (\sport\s(?P<port>\S+))?
                $""", re.VERBOSE),
            "setval": community_tmplt,
            "result": {
                "community": [{
                    "name": "{{ name }}",
                    "port": "{{ port }}",
                    "vrf": "{{ vrf }}",
                    "severity": "{{severity}}"
                }]
            }

        },
        {
            "name": "ipv4.dscp",
            "getval": re.compile(
                r"""
                ^snmp-server
                \sipv4\sdscp\s(?P<dscp>\S+)
                $""", re.VERBOSE),
            "setval": "snmp-server ipv4 dscp {{ipv4.dscp}}",
            "result": {
                "ipv4": {
                    "dscp": "{{dscp}}"
                }
            },
        },
        {
            "name": "ipv6.dscp",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\sipv6\sdscp\s(?P<dscp>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server ipv6 dscp {{ipv6.dscp}}",
            "result": {
                "ipv6": {
                    "dscp": "{{dscp}}"
                }
            },
        },
        {
            "name": "ipv4.precedence",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\sipv4\sprecedence\s(?P<precedence>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server ipv4 precedence {{ipv4.precedence}}",
            "result": {
                "ipv4": {"precedence": "{{precedence}}"}
            },
        },
        {
            "name": "ipv6.precedence",
            "getval": re.compile(
                r"""
                ^snmp-server
                (\sipv6\sprecedence\s(?P<precedence>\S+))
                $""", re.VERBOSE),
            "setval": "snmp-server ipv6 precedence {{ipv6.precedence}}",
            "result": {
                "ipv6": {"precedence": "{{precedence}}"}
            },
        },
    ]
    # fmt: on
