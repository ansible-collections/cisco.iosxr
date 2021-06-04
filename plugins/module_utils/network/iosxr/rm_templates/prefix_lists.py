# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Prefix_lists parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)
def _tmpl_description(config):
    """

    """
    import epdb;epdb.serve()
class Prefix_listsTemplate(NetworkTemplate):
    def __init__(self, lines=None):
        super(Prefix_listsTemplate, self).__init__(lines=lines, tmplt=self)

    # fmt: off
    PARSERS = [
        {
            "name": "prefix_list",
            "getval": re.compile(
                r"""
                        (?P<afi>^(ipv4|ipv6))
                        \sprefix-list\s(?P<pl>\S+)
                        $""",
                re.VERBOSE,
            ),
            "setval": "{{afi}} prefix-list {{name}}",
            "result": {
                "{{afi}}" + "_" + "{{pl}}":  {
                        "afi": "{{afi}}",
                        "name": "{{pl}}",
                }

            },
            "shared": True,
        },
        {
            "name": "prefix",
            "getval": re.compile(
                r"""
                        \s(?P<sequence>\d+)
                        \s(?P<action>deny|permit)
                        \s(?P<prefix>\S+)
                        $""",
                re.VERBOSE,
            ),
            "setval": "{{afi}} prefix-list {{name}} {{sequence}} {{action}} {{prefix}}",
            "result": {
                    "{{afi}}" + "_" + "{{pl}}": {
                            "afi": "{{afi}}",
                            "name": "{{pl}}",
                            "entries": [
                                {
                                    "sequence": "{{sequence}}",
                                    "action": "{{action}}",
                                    "prefix": "{{prefix}}"
                                }

                            ]
                    }
                }
        },
        {
            "name": "description",
            "getval": re.compile(
                r"""
                        \s(?P<sequence>\d+)
                        \s(?P<action>remark)
                        \s(?P<desc>\S+)
                        $""",
                re.VERBOSE,
            ),
            "setval": "{{afi}} prefix-list {{name}} {{sequence}} {{action}} {{description}}",
            "result": {
                "{{afi}}" + "_" + "{{pl}}": {
                    "afi": "{{afi}}",
                    "name": "{{pl}}",
                    "entries": [
                        {
                            "sequence": "{{sequence}}",
                            "action": "{{action}}",
                            "description": "{{desc}}"
                        }

                    ]
                }
            }
        },

    ]
    # fmt: on
