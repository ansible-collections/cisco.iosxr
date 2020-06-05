import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)
from ansible.module_utils.six import iteritems


def _tmplt_ospf_default_information(config_data):
    if "default_information_originate" in config_data:
        command = "default-information originate"
        if "always" in config_data["default_information_originate"]:
            command += " always"
        if "metric" in config_data["default_information_originate"]:
            command += " metric {metric}".format(
                **config_data["default_information_originate"]
            )
        if "metric_type" in config_data["default_information_originate"]:
            command += " metric-type {metric_type}".format(
                **config_data["default_information_originate"]
            )
        if "route_policy" in config_data["default_information_originate"]:
            command += " route-policy {route_policy}".format(
                **config_data["default_information_originate"]
            )
        return command


def _tmplt_ospf_auto_cost(config_data):
    if "auto_cost" in config_data:
        command = "auto-cost"
        if "disable" in config_data["auto_cost"]:
            command += " disable"
        if "reference_bandwidth" in config_data["auto_cost"]:
            command += " reference-bandwidth {reference_bandwidth}".format(
                **config_data["auto_cost"]
            )
        return command


def _tmplt_ospf_bfd(config_data):
    if "bfd" in config_data:
        command = "bfd"
        if "minimum_interval" in config_data["bfd"]:
            command += " minimum-interval {minimum_interval}".format(
                **config_data["bfd"]
            )

        if "multiplier" in config_data["bfd"]:
            command += " multiplier {multiplier}".format(**config_data["bfd"])

        return command


def _tmplt_ospf_security(config_data):
    if "security_ttl" in config_data:
        command = "security_ttl"
        if "set" in config_data["security_ttl"]:
            command += " ttl"
        elif config_data["security_ttl"].get("hops"):
            command += " ttl hops {hops}".format(
                config_data["security_ttl"].get("hops")
            )
        return command


def _tmplt_ospf_distance_admin(config_data):
    if "admin_distance" in config_data:
        command = "distance"
        if config_data["admin_distance"].get("value"):
            command += " {value}".format(
                config_data["admin_distance"].get("value")
            )
        if config_data["admin_distance"].get("source"):
            command += " {source}".format(
                config_data["admin_distance"].get("source")
            )
        if config_data["admin_distance"].get("wildcard"):
            command += " {wildcard}".format(
                config_data["admin_distance"].get("wildcard")
            )
        if config_data["admin_distance"].get("access_list"):
            command += " {access_list}".format(
                config_data["admin_distance"].get("access_list")
            )
        return command


def _tmplt_ospf_distance_ospf(config_data):
    if "ospf_distance" in config_data:
        command = "distance ospf"
        if config_data["ospf_distance"].get("external"):
            command += " external {external}".format(
                config_data["ospf_distance"].get("external")
            )
        if config_data["ospf_distance"].get("inter_area"):
            command += " inter-area {inter_area}".format(
                config_data["ospf_distance"].get("inter_area")
            )
        if config_data["ospf_distance"].get("intra_area"):
            command += " intra-area {intra_area}".format(
                config_data["ospf_distance"].get("intra_area")
            )
        return command


def _tmplt_ospf_nsr(config_data):
    if "nsr" in config_data:
        command = "nsr"
        if "set" in config_data["nsr"]:
            command += " nsr"
        elif config_data["nsr"].get("disable"):
            command += " nsr {disable}".format("disable")
        return command


def _tmplt_ospf_protocol(config_data):
    if "protocol_shutdown" in config_data:
        command = "protocol"
        if "set" in config_data["protocol_shutdown"]:
            command += " shutdown"
        elif config_data["shutdown"].get("host_mode"):
            command += " shutdown host-mode"
        elif config_data["shutdown"].get("on_reload"):
            command += " shutdown on-reload"
        return command


def _tmplt_ospf_bfd_fast_detect(config_data):
    if "bfd" in config_data:
        command = "bfd"
        if "fast_detect" in config_data["bfd"]:
            fast_detect = config_data["bfd"].get("fast_detect")
            command += " fast-detect"
            if "strict_mode" in fast_detect:
                command += " strict-mode"
        return command


def _tmplt_ospf_authentication_md(config_data):
    command = []
    if "authentication" in config_data:
        if config_data["authentication"].get("message_digest"):
            command = "authentication message-digest"
            md = config_data["authentication"].get("message_digest")
            if md.get("keychain"):
                command += " keychain " + md.get("keychain")
        return command


def _tmplt_ospf_authentication(config_data):
    command = []
    if "authentication" in config_data:
        if config_data["authentication"].get("keychain"):
            command = "authentication keychain " + config_data[
                "authentication"
            ].get("keychain")
        elif config_data["authentication"].get("no_auth"):
            command = "authentication null"
        return command


def _tmplt_ospf_authentication(config_data):
    command = []
    if "authentication" in config_data:
        if config_data["authentication"].get("keychain"):
            command = "authentication keychain " + config_data[
                "authentication"
            ].get("keychain")
        elif config_data["authentication"].get("no_auth"):
            command = "authentication null"
        return command


def _tmplt_ospf_adjacency_stagger(config_data):
    if "adjacency_stagger" in config_data:
        command = "adjacency stagger".format(**config_data)
        if config_data["adjacency_stagger"].get(
            "min_adjacency"
        ) and config_data["adjacency_stagger"].get("min_adjacency"):
            command += " {} {}".format(
                config_data["adjacency_stagger"].get("min_adjacency"),
                config_data["adjacency_stagger"].get("max_adjacency"),
            )
        elif config_data["adjacency_stagger"].get("disable"):
            command += " disable"
        return command


def _tmplt_ospf_capability_opaque(config_data):
    if "capability" in config_data:
        if "opaque" in config_data["capability"]:
            command = "capability opaque"
            opaque = config_data["capability"].get("opaque")
            if "disable" in opaque:
                command += "capability opaque disable"
        return command


def _tmplt_ospf_authentication_key(config_data):
    if "authentication_key" in config_data:
        command = "authentication-key".format(**config_data)
        if config_data["authentication_key"].get("password"):
            command += " {password}".format(
                config_data["authentication_key"].get("password")
            )
        return command


def _tmplt_ospf_area_authentication(config_data):
    if "authentication" in config_data:
        command = "area {area_id} authentication".format(**config_data)
        if config_data["authentication"].get("keychain"):
            command += " keychain " + config_data["authentication"].get(
                "keychain"
            )
        elif config_data["authentication"].get("no_auth"):
            command += " null"
        return command


def _tmplt_ospf_area_authentication_md(config_data):
    if "authentication" in config_data:
        command = "area {area_id} authentication".format(**config_data)
        if config_data["authentication"].get("message_digest"):
            command = "authentication message-digest"
            md = config_data["authentication"].get("message_digest")
            if md.get("keychain"):
                command += " keychain " + md.get("keychain")
        return command


def _tmplt_ospf_area_authentication_key(config_data):
    if "authentication_key" in config_data:
        command = "area {area_id} authentication-key".format(**config_data)
        if config_data["authentication_key"].get("password"):
            command += " {password}".format(
                config_data["authentication_key"].get("password")
            )
        return command


def _tmplt_ospf_area_mpls_ldp(config_data):
    commands = []
    if "mpls" in config_data:
        command = "area {area_id} mpls".format(**config_data)
        if config_data["mpls"].get("ldp"):
            ldp = config_data["mpls"].get("ldp")
            if "auto_config" in ldp:
                command += " auto-config"
                commands.append(command)
            if "sync" in ldp:
                command += " sync"
                commands.append(command)
            if "sync_igp_shortcuts" in ldp:
                command += " sync-igp-shortcuts"
                commands.append(command)
        return commands


def _tmplt_ospf_area_bfd(config_data):
    if "bfd" in config_data:
        command = "area {area_id} bfd".format(**config_data)
        if "minimum_interval" in config_data["bfd"]:
            command += " minimum-interval {minimum_interval}".format(
                **config_data["bfd"]
            )

        if "multiplier" in config_data["bfd"]:
            command += " multiplier {multiplier}".format(**config_data["bfd"])

        return command


def _tmplt_ospf_area_bfd_fast_detect(config_data):
    if "bfd" in config_data:
        command = "area {area_id} bfd".format(**config_data)
        if "fast_detect" in config_data["bfd"]:
            fast_detect = config_data["bfd"].get("fast_detect")
            command += " fast-detect"
            if "strict_mode" in fast_detect:
                command += " strict-mode"
        return command


def _tmplt_ospf_area_nssa(config_data):
    if "nssa" in config_data:
        command = "area {area_id} nssa".format(**config_data)
        if config_data["nssa"].get("no_redistribution"):
            command += " no-redistribution"
        if config_data["nssa"].get("no_summary"):
            command += " no-summary"
        return command


def _tmplt_ospf_area_nssa_def_info_origin(config_data):
    if "nssa" in config_data:
        command = "area {area_id} nssa".format(**config_data)
        if config_data["nssa"].get("default_information_originate"):
            command += " default-information-originate"
            def_info_origin = config_data["nssa"].get(
                "default_information_originate"
            )
            if "metric" in def_info_origin:
                command += " metric {metric}".format(def_info_origin["metric"])
            if "metric_type" in def_info_origin:
                command += " metric-type {metric_type}".format(
                    def_info_origin["metric_type"]
                )
        return command


def _tmplt_ospf_area_nssa_translate(config_data):
    if "nssa" in config_data:
        command = "area {area_id} nssa".format(**config_data)
        if config_data["nssa"].get("translate"):
            command += " translate"
            translate = config_data["nssa"].get("translate")
            if "type7" in translate:
                command += " type7"
            if translate["type7"].get("always"):
                command += " always"
        return command


def _tmplt_ospf_vrf_cmd(process):
    command = "router ospf {process_id}".format(**process)
    if "vrf" in process:
        command += " vrf {vrf}".format(**process)
    return command


def _tmplt_ospf_area_stub(config_data):
    if "stub" in config_data:
        command = "area {area_id} stub".format(**config_data)
        if config_data["stub"].get("no_summary"):
            command += " no-summary"
        return command


def _tmplt_ospf_area_ranges(config_data):
    if "ranges" in config_data:
        commands = []
        for k, v in iteritems(config_data["ranges"]):
            cmd = "area {area_id} range".format(**config_data)
            temp_cmd = " {address}".format(**v)
            if "advertise" in v:
                temp_cmd += " advertise"
            elif "not_advertise" in v:
                temp_cmd += " not-advertise"
            cmd += temp_cmd
            commands.append(cmd)
        return commands


class Ospfv2Template(NetworkTemplate):
    def __init__(self, lines=[]):
        super(Ospfv2Template, self).__init__(lines=lines, tmplt=self)

    # fmt: off
    PARSERS = [
        {
            "name": "pid",
            "getval": re.compile(
                r"""
                        ^router
                        \sospf\s(?P<pid>\S+)
                        $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_vrf_cmd,
            "result": {
                "processes": {"{{ pid }}": {"process_id": "{{ pid }}"}}
            },
            "shared": True,
        },
        {
            "name": "cost",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \scost(?P<cost>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "cost {{ cost }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                     "cost": "{{ cost|int }}",
                    }
                }
            },
        },
        {
            "name": "default_metric",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sdefault-metric(?P<default_metric>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "default-metric {{ default_metric }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "default_metric": "{{ default_metric|int }}",
                    }
                }
            },
        },
        {
            "name": "packet_size",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \spacket-size(?P<packet_size>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "packet-size {{ packet_size }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "packet_size": "{{ packet_size|int }}",
                    }
                }
            },
        },
        {
            "name": "dead_interval",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sdead-interval(?P<dead_interval>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "dead-interval {{ dead_interval }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "dead_interval": "{{ dead_interval|int }}",
                    }
                }
            },
        },
        {
            "name": "hello_interval",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \shello-interval(?P<hello_interval>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "hello-interval {{ hello_interval }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "hello_interval": "{{ hello_interval|int }}",
                    }
                }
            },
        },
        {
            "name": "priority",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \spriority(?P<priority>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "priority {{ priority }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "priority": "{{ priority|int }}",
                    }
                }
            },
        },
        {
            "name": "weight",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sweight(?P<weight>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "weight {{ weight }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "weight": "{{ weight|int }}",
                    }
                }
            },
        },
        {
            "name": "retransmit_interval",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sretransmit-interval(?P<retransmit_interval>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "retransmit-interval {{ retransmit_interval }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "retransmit_interval": "{{ retransmit_interval|int }}",
                    }
                }
            },
        },
        {
            "name": "transmit_delay",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \stransmit-delay(?P<transmit_delay>\s\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "transmit-delay {{ transmit_delay }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "transmit_delay": "{{ transmit_delay|int }}",
                    }
                }
            },
        },
        {
            "name": "passive",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \spassive\s(?P<passive>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "passive {{ passive }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "passive": "{{ passive }}",
                    }
                }
            },
        },
        {
            "name": "process.database_filter",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sdatabase-filter
                \sall
                \sout\s(?P<database_filter>\s\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "process.database_filter",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "database_filter": "{{ database_filter }}",
                    }
                }
            },
        },
        {
            "name": "demand_circuit",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sdemand-circuit\s(?P<demand_circuit>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "demand-circuit {{ demand_circuit }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "demand_circuit": "{{ demand_circuit }}",
                    }
                }
            },
        },
        {
            "name": "external_out",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sexternal-out\s(?P<external_out>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "external-out {{ external_out }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "external_out": "{{ external_out }}",
                    }
                }
            },
        },
        {
            "name": "router_id",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \srouter-id\s(?P<router_id>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "router-id {{ router_id }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "router_id": "{{ router_id }}",
                    }
                }
            },
        },
        {
            "name": "summary_in",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \ssummary-in\s(?P<summary_in>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "summary-in {{ summary_in }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "summary_in": "{{ summary_in }}",
                    }
                }
            },
        },

        {
            "name": "mtu_ignore",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \smtu-ignore\s(?P<mtu_ignore>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "mtu-ignore {{ mtu_ignore }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "mtu_ignore": "{{ mtu_ignore }}",
                    }
                }
            },
        },
        {
            "name": "flood_reduction",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sflood-reduction\s(?P<flood_reduction>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "flood-reduction {{ flood_reduction }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "flood_reduction": "{{ flood_reduction }}",
                    }
                }
            },
        },
        {
            "name": "loopback_stub_network",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sloopback(?P<loopback>)
                \sstub-network\s(?P<stub_network>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "loopback stub-network {{ stub_network }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "loopback_stub_network": "{{ loopback_stub_network }}",
                    }
                }
            },
        },
        {
            "name": "address_family_unicast",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \saddress-family(?P<address_family>)
                \sipv4(?P<ipv4>)
                \sunicast(?P<unicast>)
                $""",
                re.VERBOSE,
            ),

            "setval": "address_family_unicast",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "address_family_unicast": "{{ True if unicast is defined }}",
                    }
                }
            },
        },
        {
            "name": "process.apply_weight",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sapply-weight(?P<apply_weight>)
                    (\sbandwidth(?P<bandwidth>\s\d+))?
                    (\sdefault-weight(?P<default_weight>\s\d+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_nssa_translate,
            "compval": "process.apply_weight",
            "result": {
                "processes": {
                    "{{ pid }}": {
                            "apply_weight": {
                                "bandwidth": "{{ bandwidth|int }}",
                                "default_weight": "{{ default_weight|int }}",
                            }
                    }
                }
            },
        },
        {
            "name": "adjacency_stagger",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sadjacency(?P<adjacency>)
                    \sstagger(?P<stagger>)
                    (\s(?P<min_adjacency>\d+))?
                    (\s(?P<max_adjacency>\d+))?
                    (\sdisable(?P<disable>\S+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_adjacency_stagger,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "adjacency_stagger": {
                            "min_adjacency": "{{ min_adjacency|int }}",
                            "max_adjacency": "{{ max_adjacency }}",
                            "disable": "{{ True if disable is defined }}",
                        },
                    }
                }
            },
        },
        {
            "name": "authentication",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sauthentication(?P<auth>)
                    (\skeychain\s(?P<keychain>\S+)*)?
                    (\snull(?P<no_auth>))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_authentication,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "authentication": {
                            "no_auth": "{{ True if no_auth is defined }}",
                            "keychain": "{{ keychain }}",
                        },
                    }
                }
            },
        },
        {
            "name": "authentication.message_digest",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sauthentication(?P<auth>)
                    \smessage-digest(?P<md>)
                    \skeychain\s(?P<md_key>\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_authentication_md,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "authentication": {
                            "message_digest": {
                                "keychain": "{{ md_key }}",
                                "set": "{{ True if md is defined and md_key is undefined }}",
                            }
                        },
                    }
                }
            },
        },
        {
            "name": "default_information_originate",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sdefault-information(?P<default_information>)
                    (\soriginate(?P<originate>))?
                    (\salways(?P<always>))?
                    (\smetric\s(?P<metric>\d+))?
                    (\smetric-type\s(?P<metric_type>\d+))?
                    (\sroute_policy\s(?P<route_policy>)\S+)?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_default_information,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "default_information_originate": {
                            "always": "{{ True if always is defined }}",
                            "metric": "{{ metric|int }}",
                            "metric_type": "{{ metric_type|int }}",
                            "route_policy": "{{ route_policy }}",
                            "set": "{{ True if default_information is defined and always is undefined and metric is undefined and metric_type is undefined and route_policy is undefined }}"
                        },
                    }
                }
            },
        },
        {
            "name": "auto_cost",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sauto-cost(?P<auto_cost>)
                    (\sreference-bandwidth\s(?P<reference_bandwidth>\d+))?
                    (\sdisable(?P<disable>))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_auto_cost,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "auto_cost": {
                            "disable": "{{ True if disable is defined }}",
                            "reference_bandwidth": "{{ reference_bandwidth|int }}",
                        },
                    }
                }
            },
        },
        {
            "name": "bfd",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sbfd(?P<bfd>)
                    (\sminimum-interval\s(?P<minimum_interval>\d+))?
                    (\smultiplier\s(?P<multiplier>\d+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_bfd,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "bfd": {
                            "minimum_interval": "{{ minimum_interval|int }}",
                            "multiplier": "{{ multiplier|int }}",
                        },
                    }
                }
            },
        },
        {
            "name": "bfd.fast_detect",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sbfd(?P<bfd>)
                    \sfast-detect(?P<fast_detect>)
                    (\s(?P<disable>disable))?
                    (\s(?P<strict_mode>strict-mode))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_bfd_fast_detect,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "bfd": {
                            "fast_detect": {
                                "set": "{{ True if disable is undefined and strict_mode is undefined }}",
                                "strict_mode": "{{ True if strict_mode is defined }}",
                            },
                        },
                    }
                },
            },
        },
        {
            "name": "security",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \ssecurity(?P<security>)
                    \sttl(?P<ttl>)?
                    (\shops\s(?P<hops>\d+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_security,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "security_ttl": {
                            "set": "{{ True if ttl is defined and hops is undefined }}",
                            "hops": "{{ hops }}",
                        },
                    }
                }
            },
        },
        {
            "name": "nsr",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \snsr(?P<nsr>)
                    \sdisable(?P<disable>)?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_nsr,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "nsr": {
                            "set": "{{ True if nsr is defined and disable is undefined }}",
                            "disable": "{{ True if disable is defined }}",
                        },
                    }
                }
            },
        },
        {
            "name": "protocol",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sprotocol(?P<protocol>)
                    \s(shutdown(?P<shutdown>))
                    (\shost-mode(?P<host_mode>))?
                    (\son-reload\s(?P<on_reload>\d+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_protocol,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "protocol_shutdown": {
                            "set": "{{ True if shutdown is defined and host-mode is undefined and on_reload is undefined  }}",
                            "host_mode": "{{ True if host_mode is defined }}",
                            "on_reload": "{{ True if on_reload is defined }}",
                        },
                    }
                }
            },
        },
        {
            "name": "capability",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \scapability(?P<capability>)
                    (\stype7\s(?P<type7>\S+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": "capability type7 {{ type7 }}",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "capability": {
                            "type7": "{{ type7 }}"
                        },
                    }
                }
            },
        },
        {
            "name": "capability.opaque",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \scapability(?P<capability>)?
                    \sopaque(?P<opaque>)
                    (\sdisable(?P<disable>))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_capability_opaque,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "capability": {
                            "opaque": {
                                "disable": "{{ True if disable is defined }}",
                                "set": "{{ True if opaque is defined and disable is undefined }}",
                            },
                        },
                    }
                }
            },
        },
        {
            "name": "admin_distance",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sdistance\s(?P<value>d+)
                    \s(?P<source>\S+)
                    \s(?P<wildcard>\S+)
                    (\s(?P<access_list>\S+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_distance_admin,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "distance": {
                            "admin_distance": {
                                "value": "{{ value|int }}",
                                "source": "{{ source }}",
                                "wildcard": "{{ wildcard }}",
                                "access_list": "{{ access_list }}",
                            }
                        },
                    }
                }
            },
        },

        {
            "name": "ospf_distance",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sdistance(?P<value>)
                    \sospf(?P<ospf>)
                    (\sexternal\s(?P<external>\d+))?
                    (\sinter-area\s(?P<inter_area>\d+))?
                    (\sintra-area\s(?P<intra_area>\d+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_distance_ospf,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "distance": {
                            "ospf_distance": {
                                "external": "{{ external|int }}",
                                "inter_area": "{{ inter_area|int }}",
                                "intra_area": "{{ intra_area|int }}",
                            }
                        },
                    }
                }
            },
        },
        {
            "name": "authentication_key",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sauthentication-key(?P<auth_key>)
                    (\s(?P<password>\S+))?
                    (\sclear\s(?P<clear>)\S+)?
                    (\sencrypted(?P<encrypted>\S+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_authentication_key,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "authentication_key": {
                            "clear": "{{ clear }}",
                            "encrypted": "{{ encrypted}}",
                            "password": "{{ password if clear is undefined and encrypted is undefined }}",
                        },
                    }
                }
            },
        },
        {
            "name": "area.default_cost",
            "getval": re.compile(
                r"""
                   ^router
                   \sospf\s(?P<pid>\S+)
                   \sarea\s(?P<area_id>\S+)
                   \sdefault-cost\s(?P<default_cost>\d+)
                   $""",
                   re.VERBOSE,
            ),

            "setval": "area {{ area_id }} default-cost {{ default_cost }}",
            "compval": "default_cost",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "default_cost": "{{ default_cost|int }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.dead_interval",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \sdead-interval\s(?P<dead_interval>\d+)
                $""",
                re.VERBOSE,
            ),

            "setval": "area {{ area_id }} dead-interval {{ dead_interval }}",
            "compval": "dead_interval",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "dead_interval": "{{ dead_interval|int }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.hello_interval",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \shello-interval\s(?P<hello_interval>\d+)
                $""",
                re.VERBOSE,
            ),
            "setval": "area {{ area_id }} hello-interval {{ hello_interval }}",
            "compval": "hello_interval",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "hello_interval": "{{ hello_interval|int }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.transmit_delay",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \stransmit-delay\s(?P<transmit_delay>\d+)
                $""",
                re.VERBOSE,
            ),
            "setval": "area {{ area_id }} transmit-delay {{ transmit_delay }}",
            "compval": "transmit_delay",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "transmit_delay": "{{ transmit_delay|int }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.cost",
            "getval": re.compile(
                r"""
                   ^router
                   \sospf\s(?P<pid>\S+)
                   \sarea\s(?P<area_id>\S+)
                   \scost\s(?P<cost>\d+)
                   $""",
                   re.VERBOSE,
            ),
            "setval": "area {{ area_id }} cost {{ cost }}",
            "compval": "cost",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "cost": "{{ cost|int }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.priority",
            "getval": re.compile(
                r"""
                   ^router
                   \sospf\s(?P<pid>\S+)
                   \sarea\s(?P<area_id>\S+)
                   \spriority\s(?P<priority>\d+)
                   $""",
                re.VERBOSE,
            ),
            "setval": "area {{ area_id }} priority {{ priority }}",
            "compval": "priority",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "priority": "{{ priority|int }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.weight",
            "getval": re.compile(
                r"""
                   ^router
                   \sospf\s(?P<pid>\S+)
                   \sarea\s(?P<area_id>\S+)
                   \sweight\s(?P<weight>\d+)
                   $""",
                re.VERBOSE,
            ),
            "setval": "area {{ area_id }} weight {{ weight }}",
            "compval": "weight",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "weight": "{{ weight|int }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.packet_size",
            "getval": re.compile(
                r"""
                   ^router
                   \sospf\s(?P<pid>\S+)
                   \sarea\s(?P<area_id>\S+)
                   \spacket-size\s(?P<packet_size>\d+)
                   $""",
                re.VERBOSE,
            ),
            "setval": "area {{ area_id }} packet-size {{ packet_size }}",
            "compval": "packet_size",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "packet_size": "{{ packet_size|int }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.summary_in",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \ssummary-in\s(?P<summary_in>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "area {{ area_id }} summary-in {{ summary_in }}",
            "compval": "summary_in",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "summary_in": "{{ summary_in }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.demand_circuit",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \sdemand-circuit\s(?P<demand_circuit>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "area {{ area_id }} demand-circuit {{ demand_circuit }}",
            "compval": "demand_circuit",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "demand_circuit": "{{ demand_circuit }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.passive",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \spassive\s(?P<passive>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "area {{ area_id }} passive {{ passive }}",
            "compval": "passive",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "passive": "{{ passive }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.external_out",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \sexternal-out\s(?P<external_out>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "area {{ area_id }} external-out {{ external_out }}",
            "compval": "passive",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "external_out": "{{ external_out }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.mtu_ignore",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \smtu-ignore\s(?P<mtu_ignore>\S+)
                $""",
                re.VERBOSE,
            ),

            "setval": "area {{ area_id }} mtu-ignore {{ mtu_ignore }}",
            "compval": "mtu_ignore",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "mtu_ignore": "{{ mtu_ignore }}",
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.authentication",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \sauthentication(?P<auth>)
                    (\skeychain\s(?P<keychain>\S+))?
                    (\snull(?P<no_auth>))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_authentication,
            "compval": "authentication",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "authentication": {
                                    "no_auth": "{{ True if no_auth is defined }}",
                                    "keychain": "{{ keychain }}",
                                },
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.authentication_key",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \sauthentication-key(?P<auth_key>)
                    (\s(?P<password>\S+))?
                    (\sclear\s(?P<clear>)\S+)?
                    (\sencrypted(?P<encrypted>\S+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_authentication_key,
            "compval": "authentication_key",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "authentication_key": {
                                    "clear": "{{ clear }}",
                                    "encrypted": "{{ encrypted}}",
                                    "password": "{{ password if clear is undefined and encrypted is undefined }}",
                                },
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.authentication.message_digest",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \sauthentication(?P<auth>)
                    \smessage-digest(?P<md>)
                    \skeychain(?P<md_key>\s\S+)
                    *$""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_authentication_md,
            "compval": "authentication.message_digest",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "authentication": {
                                    "message_digest": {
                                        "keychain": "{{ md_key }}",
                                    }
                                },
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.mpls_traffic_eng",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \smpls(?P<mpls>)
                    \straffic-end(?P<traffic_eng>)
                    $""",
                re.VERBOSE,
            ),
            "setval": "area {{ area_id }} mpls traffic-eng",
            "compval": "mpls_traffic_eng",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "mpls": {
                                    "traffic_eng": "{{ True if traffic_eng is defined }}",
                                },
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.mpls_ldp",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \smpls(?P<mpls>)
                    (\sauto-config(?P<auto_config>))?
                    (\ssync(?P<sync>))?
                    (\ssync-igp-shortcuts(?P<syn_igp_shortcuts>))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_mpls_ldp,
            "compval": "mpls_ldp",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "mpls": {
                                    "ldp": {
                                        "auto_config": "{{ True if auto_config is defined }}",
                                        "sync": "{{ True if sync is defined }}",
                                        "sync_igp_shortcuts": "{{ True if sync_igp_shortcuts is defined }}",

                                    }
                                },
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.bfd",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \sbfd(?P<bfd>)
                    (\sminimum-interval\s(?P<minimum_interval>\d+))?
                    (\smultiplier\s(?P<multiplier>\d+))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_bfd,
            "compval": "bfd",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "bfd": {
                                    "minimum_interval": "{{ minimum_interval|int }}",
                                    "multiplier": "{{ multiplier|int }}",
                                },
                            }
                        }
                    }
                }
            },
        },
        {
            "name": "area.bfd.fast_detect",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sbfd(?P<bfd>)
                    \sarea(?P<area_id>)
                    \sfast-detect(?P<fast_detect>)
                    (\s(?P<disable>disable))?
                    (\s(?P<strict_mode>strict-mode))?
                    $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_bfd_fast_detect,
            "compval": "bfd.fast_detect",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "area_id": "{{ area_id }}",
                                "bfd": {
                                    "fast_detect": {
                                        "set": "{{ True if disable is undefined and strict_mode is undefined }}",
                                        "strict_mode": "{{ True if strict_mode is defined }}",
                                    },
                                },
                            }
                        }
                    }
                },
            },
        },
        {
            "name": "area.stub",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \sstub(?P<nssa>)
                (\sno-summary(?P<no_sum>))?
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_stub,
            "compval": "stub",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "area_id": "{{ area_id }}",
                            "stub": {
                                "set": "{{ True if stub is defined and no_summary is undefined }}",
                                "no_summary": "{{ True if no_summary is defined }}",
                            }
                        }
                    }
                }
            },
        },
            {
            "name": "area.nssa",
            "getval": re.compile(
                r"""
                ^router
                \sospf\s(?P<pid>\S+)
                \sarea\s(?P<area_id>\S+)
                \snssa(?P<nssa>)
                (\sno-redistribution(?P<no_redis>))?
                (\sno-summary(?P<no_sum>))?
                $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_area_nssa,
            "compval": "nssa",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "area_id": "{{ area_id }}",
                            "nssa": {
                                "set": "{{ True if nssa is defined and no_summary is undefined and no_redis is undefined }}",
                                "no_summary": "{{ True if no_summary is defined }}",
                                "no_redistribution": "{{ True if no_redis is defined }}"
                            }
                        }
                    }
                }
            },
        },
            {
                "name": "area.nssa.default_information_originate",
                "getval": re.compile(
                    r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \snssa(?P<nssa>)
                    (\sno-redistribution(?P<no_redis>))?
                    (\sdefault-information-originate(?P<def_info_origin>))?
                    (\smetric\s(?P<metric>\d+))?
                    (\smetric-type\s(?P<metric_type>\d+))?
                    $""",
                    re.VERBOSE,
                ),
                "setval": _tmplt_ospf_area_nssa_def_info_origin,
                "compval": "nssa.default_information_originate",
                "result": {
                    "processes": {
                        "{{ pid }}": {
                            "areas": {
                                "area_id": "{{ area_id }}",
                                "nssa": {
                                    "default_information_originate": {
                                        "metric": "{{ metric|int }}",
                                        "metric_type": "{{ metric_type|int }}",
                                    },
                                }
                            }
                        }
                    }
                },
            },
            {
                "name": "area.ranges",
                "getval": re.compile(
                    r"""
                        ^router
                        \sospf\s(?P<pid>\S+)
                        \sarea\s(?P<area_id>\S+)
                        \srange(?P<range>)
                        \s(?P<address>\S+)
                        (\sadvertise(?P<advertise>))
                        (\snot-advertise(?P<not_advertise>))?
                        $""",
                    re.VERBOSE,
                ),
                "setval": _tmplt_ospf_area_ranges,
                "compval": "ranges",
                "result": {
                    "processes": {
                        "{{ pid }}": {
                            "areas": {
                                "{{ area_id }}": {
                                    "area_id": "{{ area_id }}",
                                    "ranges": [
                                        {
                                            "address": "{{ address }}",
                                            "advertise": "{{ True if advertise is defined }}",
                                            "not_advertise": "{{ True if not_advertise is defined }}",
                                        }
                                    ],
                                }
                            }
                        }
                    }
                },
            },

            {
                "name": "area.nssa.translate",
                "getval": re.compile(
                    r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \snssa(?P<nssa>)
                    \stranslate(?P<translate>)
                    \stype7(?P<type7>)
                    \salways\s(?P<always>)
                    $""",
                    re.VERBOSE,
                ),
                "setval": _tmplt_ospf_area_nssa_translate,
                "compval": "nssa.translate",
                "result": {
                    "processes": {
                        "{{ pid }}": {
                            "areas": {
                                "area_id": "{{ area_id }}",
                                "nssa": {
                                    "translate": {
                                        "type7": {
                                            "always": "{{ True if always is defined }}"
                                      }
                                    },
                                }
                            }
                        }
                    }
                },
            },
    ]
    '''
        {
            "name": "virtual_link.hello_interval",
            "getval": re.compile(
                r"""
                    ^router
                    \sospf\s(?P<pid>\S+)
                    \sarea\s(?P<area_id>\S+)
                    \svirtual-link\s(?P<id>\S+)
                    \shello-interval\s(?P<hello_interval>\d+)
                    $""",
                re.VERBOSE,
            ),
            "setval": "area {{ area_id }} virtual-link {{ id }} hello-interval {{ hello_interval }}",
            "compval": "hello_interval",
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "areas": {
                            "{{ area_id }}": {
                                "virtual_link": {
                                    "id":   "{{ id }}",
                                    "hello_interval": "{{ hello_interval|int }}"
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            "name": "pid",
            "getval": re.compile(
                r"""
                        ^router
                        \sospf\s(?P<pid>\S+)
                        $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_vrf_cmd,
            "result": {
                "processes": {"{{ pid }}": {"process_id": "{{ pid }}"}}
            },
            "shared": True,
        },
        {
            "name": "pid",
            "getval": re.compile(
                r"""
                        ^router\s
                        ospf*
                        \s(?P<pid>\S+)
                        \svrf
                        \s(?P<vrf>\S+)
                        $""",
                re.VERBOSE,
            ),
            "setval": _tmplt_ospf_vrf_cmd,
            "result": {
                "processes": {
                    "{{ pid }}": {
                        "process_id": "{{ pid|int }}",
                        "vrf": "{{ vrf }}",
                    }
                }
            },
            "shared": True,
        },
    '''
