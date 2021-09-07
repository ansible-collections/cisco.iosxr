# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Ntp_global parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)

class Ntp_globalTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(Ntp_globalTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            "name": "log_internal_sync",
            "getval": re.compile(
                r"""
                ^ntp\s(?P<log_internal_sync>log-internal-sync)
                $""", re.VERBOSE),
            "setval": "ntp log-internal-sync",
            "result": {
                "log_internal_sync": "{{ not not log_internal_sync }}",
            },
        },
        {
            "name": "max_associations",
            "getval": re.compile(
                r"""
                ^ntp\smax-associations\s(?P<max_associations>\d+)
                $""", re.VERBOSE),
            "setval": "ntp max-associations {{ max_associations }}",
            "result": {
                "max_associations": "{{ max-associations }}",
            },
        },
        {
            "name": "master",
            "getval": re.compile(
                r"""
                ^ntp\smaster\s(?P<master>\d+)
                $""", re.VERBOSE),
            "setval": "ntp master {{ master }}",
            "result": {
                "master": "{{ master }}",
            },
        },
        {
            "name": "passive",
            "getval": re.compile(
                r"""
                ^ntp\s(?P<passive>passive)
                $""", re.VERBOSE),
            "setval": "ntp passive",
            "result": {
                "passive": "{{ not not passive }}",
            },
        },
        {
            "name": "update_calendar",
            "getval": re.compile(
                r"""
                ^ntp\s(?P<update_calendar>update-calendar)
                $""", re.VERBOSE),
            "setval": "ntp update-calendar",
            "result": {
                "update_calendar": "{{ not not update_calendar }}",
            },
        },
        {
            "name": "source",
            "getval": re.compile(
                r"""
                ^ntp\ssource\s(?P<source>\S+)
                $""", re.VERBOSE),
            "setval": "ntp source {{ source }}",
            "result": {
                "source": "{{ source }}",
            },
        },
        {
            "name": "trusted_keys",
            "getval": re.compile(
                r"""
                ^ntp\strusted-key\s(?P<key>\d+)
                $""", re.VERBOSE),
            "setval": "ntp trusted-key {{ key }}",
            "result": {
                "trusted_keys": [
                    "{{ key }}",
                ]
            },
        },

    ]
    # fmt: on
