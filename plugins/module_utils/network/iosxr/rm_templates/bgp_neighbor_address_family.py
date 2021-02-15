# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Bgp_neighbor_address_family parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)

def _tmpl_long_lived_graceful_restart(config_data):
    """
    
    """


def _tmpl_aigp(config_data):
    conf = config_data.get("aigp", {})
    commands = []
    #import epdb; epdb.serve()
    if conf:
        base_command = "aigp"
        if "set" in conf:
            commands.append("aigp")
        if "disable" in conf:
           commands.append("aigp disable")
        if "send_cost_community_disable" in conf:
            commands.append("aigp send cost-community disable")
        if "send_med" in conf and "set" in conf.get("send_med", {}):
            commands.append("aigp send med")
        if "send_med" in conf and "set" in conf.get("send_med", {}):
            commands.append("aigp send med")
    return commands
class Bgp_neighbor_address_familyTemplate(NetworkTemplate):
    def __init__(self, lines=None):
        super(Bgp_neighbor_address_familyTemplate, self).__init__(lines=lines, tmplt=self)

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
            "shared": True
        },
        {
            "name": "vrf",
            "getval": re.compile(
                r"""
                \s+vrf
                \s(?P<vrf>\S+)$""",
                re.VERBOSE,
            ),
            "setval": "vrf {{ vrf }}",
            "result": {
                "vrfs": {
                    '{{ "vrf_" + vrf|d() }}': {
                        "vrf": "{{ vrf }}"
                    }
                }
            },
            "shared": True,
        },
        {
            "name": "address_family",
            "getval": re.compile(
                r"""
                (\s+vrf\s(?P<vrf>\b(?!all\b)\S+))?    
                (?P<address_family>\s+address-family\s(?P<afi>\S+)\s(?P<af_modifier>\S+))
                $""", re.VERBOSE
            ),
            "setval": "address-family {{ afi}} {{af_modifier}}",
            "result": {
                "vrfs": {
                    '{{ "vrf_" + vrf|d() }}': {
                        "address_family": {
                            '{{"address_family_" + afi + "_" + af_modifier}}':
                                {
                                    "afi": "{{ afi}}",
                                    "af_modifier": "{{af_modifier}}",
                                }
                        }
                    }
                }
            },
            "shared": True,
        },
        {
            "name": "advertise_permanent_network",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor\s\S+)
                \sadvertise\s(?P<permanent_network>permanent-network)
                $""", re.VERBOSE
            ),
            "setval": "advertise permanent-network",
            "result": {
                "neighbors": {
                    "{{nbr_address.split(" ")[1]}}": {
                        "address_family": {
                            '{{"address_family_" + afi + "_" + af_modifier}}': {
                                "advertise_permanent_network": "{{True if permanent_network is defined }}"
                            }
                        }
                    }
                }
            }
        },
        {
            "name": "aigp",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor\s\S+)
                \saigp(?P<aigp>)
                (\sdisable(?P<disable>))?
                (\ssend\s(?P<send_med>med))?
                (\ssend\smed(?P<send_disable>disable))?
                (\ssend\scost-community\s(?P<cc_disable>disable))?
                $""", re.VERBOSE
            ),
            "setval": _tmpl_aigp,
            "result": {
                "vrfs": {
                    '{{ "vrf_" + vrf|d() }}': {
                        "neighbors": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + af_modifier}}': {
                                        "aigp": {
                                            "set": "{{ True if aigp is difined }}",
                                            "disable": "{{ True if disable is defined}}",
                                            "send_med": {
                                                "set": "{{ True if send_med is defined }}",
                                                "disable": "{{ True if send_disable is defined}}",
                                            },
                                            "send_cost_community_disable": "{{True if cc_disable is defined}}"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            "name": "allowas_in",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor\s\S+)
                \sallowas-in(?P<allowas_in>)(\s(?P<value>\S+))?
                $""", re.VERBOSE
            ),
            "setval": "allowas-in {{allowas_in.value if allowas_in.value is defined }}",
            "result": {
                "vrfs": {
                    '{{ "vrf_" + vrf|d() }}': {
                        "neighbors": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + af_modifier}}': {
                                        "allowas_in": {
                                            "set": "{{True if allowas_in is defined }}",
                                            "value": "{{value}}"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            "name": "as_overrride",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor\s\S+)
                \sas-override(?P<as_override>)
                (\sinheritance-disable(?P<inheritance_disable>))?
                $""", re.VERBOSE
            ),
            "setval": "as-override {{inheritance-disable if as_override.inheritance_disable is defined }}",
            "result": {
                "vrfs": {
                    '{{ "vrf_" + vrf|d() }}': {
                        "neighbors": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + af_modifier}}': {
                                        "as-override": {
                                            "set": "{{True if as_override is defined }}",
                                            "inheritance_disable": "{{True if inheritance_disable is defined}}"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            "name": "bestpath_origin_as_allow_invalid",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor\s\S+)
                \sbestpath\sorigin-as\sallow\s(?P<invalid>invalid)
                $""", re.VERBOSE
            ),
            "setval": "as-override {{inheritance-disable if as_override.inheritance_disable is defined }}",
            "result": {
                "vrfs": {
                    '{{ "vrf_" + vrf|d() }}': {
                        "neighbors": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + af_modifier}}': {
                                        "bestpath_origin_as_allow_invalid": "{{ True if invalid is defined}}"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            "name": "capability_orf_prefix",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor\s\S+)
                \scapability\sorf\sprefix\s(?P<capability_orf_prefix>\S+)
                $""", re.VERBOSE
            ),
            "setval": "capability orf prefix {{capability_orf_prefix }}",
            "result": {
                "vrfs": {
                    '{{ "vrf_" + vrf|d() }}': {
                        "neighbors": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + af_modifier}}': {
                                        "capability_orf_prefix": "{{capability_orf_prefix}}"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            "name": "long_lived_graceful_restart",
            "getval": re.compile(
                r"""
                \s+(?P<nbr_address>neighbor\s\S+)
                (\slong-lived-graceful-restart\s(?P<capable>capable))?
                (\slong-lived-graceful-restart\sstale-time-send\s(?P<stale_time_send>\S+))?
                $""", re.VERBOSE
            ),
            "setval": _tmpl_long_lived_graceful_restart,
            "result": {
                "vrfs": {
                    '{{ "vrf_" + vrf|d() }}': {
                        "neighbors": {
                            "{{nbr_address.split(" ")[1]}}": {
                                "address_family": {
                                    '{{"address_family_" + afi + "_" + af_modifier}}': {
                                        "long_lived_graceful_restart": {
                                            "capable": "{{True if capable is defined}}",
                                            "stale_time_send": "{{stale_time_send}}"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },


    ]
    # fmt: on
