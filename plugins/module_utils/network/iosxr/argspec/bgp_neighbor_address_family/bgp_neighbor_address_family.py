# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the iosxr_bgp_neighbor_address_family module
"""


class Bgp_neighbor_address_familyArgs(object):  # pylint: disable=R0903
    """The arg spec for the iosxr_bgp_neighbor_address_family module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "type": "dict",
            "options": {
                "as_number": {"type": "str"},
                "neighbors": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "neighbor_address": {"type": "str", "required": True},
                        "address_family": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "afi": {
                                    "type": "str",
                                    "choices": ["ipv4", "ipv6"],
                                },
                                "safi": {
                                    "type": "str",
                                    "choices": [
                                        "flowspec",
                                        "mdt",
                                        "multicast",
                                        "mvpn",
                                        "rt-filter",
                                        "tunnel",
                                        "unicast",
                                        "labeled-unicast",
                                    ],
                                },
                                "aigp": {
                                    "type": "dict",
                                    "options": {
                                        "disable": {"type": "bool"},
                                        "set": {"type": "bool"},
                                        "send_cost_community_disable": {
                                            "type": "bool"
                                        },
                                        "send_med": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "disable": {"type": "bool"},
                                            },
                                        },
                                    },
                                },
                                "allowas_in": {
                                    "type": "dict",
                                    "options": {
                                        "value": {"type": "int"},
                                        "set": {"type": "bool"},
                                    },
                                },
                                "as_override": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "bestpath_origin_as_allow_invalid": {
                                    "type": "bool"
                                },
                                "capability_orf_prefix": {
                                    "type": "str",
                                    "choices": [
                                        "both",
                                        "send",
                                        "none",
                                        "receive",
                                    ],
                                },
                                "default_originate": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "route_policy": {"type": "str"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "long_lived_graceful_restart": {
                                    "type": "dict",
                                    "options": {
                                        "capable": {"type": "bool"},
                                        "stale_time": {
                                            "type": "dict",
                                            "options": {
                                                "send": {"type": "int"},
                                                "accept": {"type": "int"},
                                            },
                                        },
                                    },
                                },
                                "maximum_prefix": {
                                    "type": "dict",
                                    "options": {
                                        "max_limit": {"type": "int"},
                                        "threshold_value": {"type": "int"},
                                        "restart": {"type": "int"},
                                        "warning_only": {"type": "bool"},
                                        "discard_extra_paths": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "multipath": {"type": "bool"},
                                "next_hop_self": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "next_hop_unchanged": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                        "multipath": {"type": "bool"},
                                    },
                                },
                                "optimal_route_reflection_group_name": {
                                    "type": "str"
                                },
                                "orf_route_policy": {"type": "str"},
                                "origin_as": {
                                    "type": "dict",
                                    "options": {
                                        "validation": {
                                            "type": "dict",
                                            "options": {
                                                "disable": {"type": "bool"}
                                            },
                                        }
                                    },
                                },
                                "remove_private_AS": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "inbound": {"type": "bool"},
                                        "entire_aspath": {"type": "bool"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "route_policy": {
                                    "type": "dict",
                                    "options": {
                                        "inbound": {"type": "str"},
                                        "outbound": {"type": "str"},
                                    },
                                },
                                "route_reflector_client": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "send_community_ebgp": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "send_community_gshut_ebgp": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "send_extended_community_ebgp": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "inheritance_disable": {
                                            "type": "bool"
                                        },
                                    },
                                },
                                "send_multicast_attributes": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "disable": {"type": "bool"},
                                    },
                                },
                                "soft_reconfiguration": {
                                    "type": "dict",
                                    "options": {
                                        "inbound": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "always": {"type": "bool"},
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        }
                                    },
                                },
                                "weight": {"type": "int"},
                                "validation": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "redirect": {"type": "bool"},
                                        "disable": {"type": "bool"},
                                    },
                                },
                            },
                        },
                    },
                },
                "vrfs": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "vrf": {"type": "str"},
                        "neighbors": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "neighbor_address": {
                                    "type": "str",
                                    "required": True,
                                },
                                "address_family": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "afi": {
                                            "type": "str",
                                            "choices": ["ipv4", "ipv6"],
                                        },
                                        "safi": {
                                            "type": "str",
                                            "choices": [
                                                "flowspec",
                                                "multicast",
                                                "mvpn",
                                                "unicast",
                                                "labeled-unicast",
                                            ],
                                        },
                                        "aigp": {
                                            "type": "dict",
                                            "options": {
                                                "disable": {"type": "bool"},
                                                "set": {"type": "bool"},
                                                "send_cost_community_disable": {
                                                    "type": "bool"
                                                },
                                                "send_med": {
                                                    "type": "dict",
                                                    "options": {
                                                        "set": {
                                                            "type": "bool"
                                                        },
                                                        "disable": {
                                                            "type": "bool"
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        "allowas_in": {
                                            "type": "dict",
                                            "options": {
                                                "value": {"type": "int"},
                                                "set": {"type": "bool"},
                                            },
                                        },
                                        "as_overrride": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "capability_orf_prefix": {
                                            "type": "str",
                                            "choices": [
                                                "both",
                                                "send",
                                                "none",
                                                "receive",
                                            ],
                                        },
                                        "default_originate": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "route_policy": {
                                                    "type": "str"
                                                },
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "long_lived_graceful_restart": {
                                            "type": "dict",
                                            "options": {
                                                "capable": {"type": "bool"},
                                                "stale_time": {
                                                    "type": "dict",
                                                    "options": {
                                                        "send": {
                                                            "type": "int"
                                                        },
                                                        "accept": {
                                                            "type": "int"
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                        "maximum_prefix": {
                                            "type": "dict",
                                            "options": {
                                                "max_limit": {"type": "int"},
                                                "threshold_value": {
                                                    "type": "int"
                                                },
                                                "restart": {"type": "int"},
                                                "warning_only": {
                                                    "type": "bool"
                                                },
                                                "discard_extra_paths": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "multipath": {"type": "bool"},
                                        "next_hop_self": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "next_hop_unchanged": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                                "multipath": {"type": "bool"},
                                            },
                                        },
                                        "optimal_route_reflection_group_name": {
                                            "type": "str"
                                        },
                                        "orf_route_policy": {"type": "str"},
                                        "remove_private_AS": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "inbound": {"type": "bool"},
                                                "entire_aspath": {
                                                    "type": "bool"
                                                },
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "route_policy": {
                                            "type": "dict",
                                            "options": {
                                                "inbound": {"type": "str"},
                                                "outbound": {"type": "str"},
                                            },
                                        },
                                        "route_reflector_client": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "send_community_ebgp": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "send_community_gshut_ebgp": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "send_extended_community_ebgp": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "inheritance_disable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "soft_reconfiguration": {
                                            "type": "dict",
                                            "options": {
                                                "inbound": {
                                                    "type": "dict",
                                                    "options": {
                                                        "set": {
                                                            "type": "bool"
                                                        },
                                                        "always": {
                                                            "type": "bool"
                                                        },
                                                        "inheritance_disable": {
                                                            "type": "bool"
                                                        },
                                                    },
                                                }
                                            },
                                        },
                                        "site_of_origin": {"type": "str"},
                                        "weight": {"type": "int"},
                                        "validation": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "redirect": {"type": "bool"},
                                                "disable": {"type": "bool"},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
        "running_config": {"type": "str"},
        "state": {
            "type": "str",
            "choices": [
                "deleted",
                "merged",
                "overridden",
                "replaced",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
