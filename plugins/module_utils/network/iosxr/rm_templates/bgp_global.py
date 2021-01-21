# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The Bgp_global parser templates file. This contains 
a list of parser definitions and associated functions that 
facilitates both facts gathering and native command generation for 
the given network resource.
"""

import re
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network_template import (
    NetworkTemplate,
)

def _tmplt_confederation_peers(config_data):
    cmds = []
    base_cmd = "bgp confederation peers "
    peers = config_data.get("bgp",{}).get("confederation", {}).get("peers")
    #import epdb;epdb.serve()
    if peers:
        for peer in peers:
            cmds.append(base_cmd + str(peer))
    return cmds

class Bgp_globalTemplate(NetworkTemplate):
    def __init__(self, lines=None):
        super(Bgp_globalTemplate, self).__init__(lines=lines, tmplt=self)

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
            "result": {"as_number": "{{ as_num }}"},
            "shared": True
        },
        {
            "name": "bfd_minimum_interval",
            "getval": re.compile(
                r"""
                \sbfd
                \s(?P<min_interval>minimum-interval\s\S+)
                $""", re.VERBOSE
            ),
            "compval": "bfd.minimum_interval",
            "setval": "bfd minimum-interval {{bfd.minimum_interval}}",
            "result": {
                "bfd": {
                    "minimum_interval": "{{ min_interval.split(" ")[1] }}"
                },
            }
        },
        {
            "name": "bfd_multiplier",
            "getval": re.compile(
                r"""
                \sbfd
                \s(?P<multiplier>multiplier\s\S+) 
                $""", re.VERBOSE
            ),
            "setval": "bfd multiplier {{bfd.multiplier}}",
            "compval": "bfd.multiplier",
            "result": {
                "bfd": {
                    "multiplier": "{{multiplier.split(" ")[1]}}"
                },
            }
        },
        {
            "name": "bgp_as_path_loopcheck",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<loopcheck>as-path-loopcheck)
                $""", re.VERBOSE
            ),
            "setval": "bgp as-path-loopcheck",
            "compval": "bgp.as_path_loopcheck",
            "result": {
                "bgp": {
                    "as_path_loopcheck": "{{ True if loopcheck is defined }}"
                },
            }
        },
        {
            "name": "bgp_auto_policy_soft_reset",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<auto_policy_soft_reset_disable>auto-policy-soft-reset\sdisable)
                $""", re.VERBOSE
            ),
            "setval": "bgp auto-policy-soft-reset disable",
            "compval": "bgp.auto_policy_soft_reset",
            "result": {
                "bgp": {
                    "auto_policy_soft_reset": {
                        "disable": "{{True if auto_policy_soft_reset_disable is defined}}"
                    },

                },
            }
        },
        {
            "name": "bgp_cluster_id",
            "getval": re.compile(
                r"""
                \sbgp 
                \s(?P<cluster_id>cluster-id\s\S+)
                $""", re.VERBOSE
            ),
            "setval": "bgp cluster-id {{bgp.cluster_id}}",
            "compval": "bgp.cluster_id",
            "result": {
                "bgp": {
                    "cluster_id": "{{cluster_id.split(" ")[1]}}",
                },
            }
        },
        {
            "name": "bgp_default_local_preference",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<default_local_pref>default\slocal-preference\s\S+)            
                $""", re.VERBOSE
            ),
            "setval": "bgp default local-preference {{bgp.default.local_preference}}",
            "compval": "bgp.default.local-preference",
            "result": {
                "bgp": {
                    "default":
                        {
                            "local_preference": "{{default_local_pref.split(" ")[2] }}",
                        }
                },
            }
        },
        {
            "name": "bgp_enforce_first_as_disable",
            "getval": re.compile(
                r"""
                \sbgp           
                \s(?P<enforce_first_as_disable>enforce-first-as\sdisable)
                $""", re.VERBOSE
            ),
            "setval": "bgp enforce-first-as disable",
            "compval": "bgp.enforce_first_as.disable",
            "result": {
                "bgp": {
                        "enforce_first_as": {
                            "disable": "{{ True if enforce_first_as_disable is defined }}",
                        }
                }
            }
        },
        {
            "name": "bgp_fast_external_fallover_disable",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<fast_external_fallover_disable>fast-external-fallover\sdisable)
                $""", re.VERBOSE
            ),
            "setval": "bgp fast-external-fallover disable",
            "compval": "bgp.fast_external_fallover.disable",
            "result": {
                "bgp": {
                    "fast_external_fallover": {
                        "disable": "{{True if fast_external_fallover_disable is defined}}"
                    }
                },
            }
        },
        {
            "name": "bgp_install_diversion",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<install_diversion>install\sdiversion)
                $""", re.VERBOSE
            ),
            "setval": "bgp install diversion",
            "compval": "bgp.install.diversion",
            "result": {
                "bgp": {
                    "install": {
                        "diversion": "{{True if install_diversion is defined}}",
                    }
                },
            }
        },
        {
            "name": "bgp_max_neighbors",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<max_neighbors>maximum\sneighbor\s\S+)
                $""", re.VERBOSE
            ),
            "setval": "bgp maximum neighbor {{bgp.maximum.neighbor}}",
            "compval": "bgp.maximum.neighbor",
            "result": {
                "bgp": {
                    "maximum":
                        {
                            "neighbor": "{{max_neighbors.split(" ")[2] }}",
                        },
                },
            }
        },
        {
            "name": "bgp_redistribute_internal",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<redistribute_internal>redistribute-internal)
                $""", re.VERBOSE
            ),
            "setval": "bgp redistribute-internal",
            "compval": "bgp.redistribute_internal",
            "result": {
                "bgp": {
                    "redistribute_internal": "{{ True if redistribute_internal is defined }}",
                },
            }
        },
        {
            "name": "bgp_router_id",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<router_id>router-id\s\S+)
                $""", re.VERBOSE
            ),
            "setval": "bgp router-id {{ bgp.router_id }}",
            "compval": "bgp.router_id",
            "result": {
                "bgp": {
                    "router_id": "{{router_id.split(" ")[1]}}",
                },
            }
        },
        {
            "name": "bgp_scan_time",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<scan_time>scan-time\s\S+)
                $""", re.VERBOSE
            ),
            "setval": "bgp scan-time {{ bgp.scan_time }}",
            "compval": "bgp.scan_time",
            "result": {
                "bgp": {
                    "scan_time": "{{scan_time.split(" ")[1]}}",
                },
            }
        },
        {
            "name": "bgp_unsafe_ebgp_policy",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<unsafe_ebgp_policy>unsafe-ebgp-policy)
                $""", re.VERBOSE
            ),
            "setval": "bgp unsafe-ebgp-policy",
            "compval": "bgp.unsafe_ebgp_policy",
            "result": {
                "bgp": {
                    "unsafe_ebgp_policy": "{{ True if unsafe_ebgp_policy is defined }}",
                 },
            }
        },
        {
            "name": "bgp_update_delay",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<update_delay>update-delay\s\S+)
                $""", re.VERBOSE
            ),
            "setval": "bgp update-delay {{ bgp.update_delay }}",
            "compval": "bgp.update_delay",
            "result": {
                "bgp": {
                    "update_delay": "{{update_delay.split(" ")[1]}}",

                },
            }
        },
        {
            "name": "bgp_bestpath_aigp",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<bestpath_aigp_ignore>bestpath\saigp\signore)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath aigp ignore",
            "compval": "bgp.bestpath.aigp.ignore",
            "result": {
                "bgp": {
                    "bestpath": {
                        "aigp": {
                            "ignore": "{{ True if bestpath_aigp_ignore is defined }}",
                        },
                    }
                },
            }
        },
        {
            "name": "bgp_bestpath_as_path_ignore",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<as_path_ignore>bestpath\sas-path\signore)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath as-path ignore",
            "compval": "bgp.bestpath.as_path.ignore",
            "result": {
                "bgp": {
                    "bestpath": {
                        "as_path": {
                            "ignore": "{{ True if as_path_ignore is defined }}",
                        }
                    }
                },
            }
        },
        {
            "name": "bgp_bestpath_as_path_multipath_relax",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<as_path_multipath_relax>bestpath\sas-path\smultipath-relax)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath as-path multipath-relax",
            "compval": "bgp.bestpath.as_path.multipath_relax",
            "result": {
                "bgp": {
                    "bestpath": {
                        "as_path": {
                            "multipath_relax": "{{ True if as_path_multipath_relax is defined }}",
                        }
                    }
                },
            }
        },
        {
            "name": "bgp_bestpath_med_always",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<always>bestpath\smed\salways)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath med always",
            "compval": "bgp.bestpath.med.always",
            "result": {
                "bgp": {
                    "bestpath": {
                        "med": {
                            "always": "{{ True if always is defined}}"
                        },
                    }
                },
            }
        },
        {
            "name": "bgp_bestpath_med_confed",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<confed>bestpath\smed\sconfed)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath med confed",
            "compval": "bgp.bestpath.med.confed",
            "result": {
                "bgp": {
                    "bestpath": {
                        "med":{
                            "confed": "{{ True if confed is defined}}",
                        }
                    },
                }
            }
        },
        {
            "name": "bgp_bestpath_med_missing_as_worst",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<missing_as_worst>bestpath\smed\smissing-as-worst)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath med missing-as-worst)",
            "compval": "bgp.bestpath.med.missing_as_worst",
            "result": {
                "bgp": {
                    "bestpath": {
                        "med": {
                            "missing_as_worst": "{{ True if missing_as_worst is defined}}"
                        }
                    }
                },
            }
        },
        {
            "name": "bgp_bestpath_compare_routerid",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<compare_routerid>bestpath\scompare-routerid)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath compare-routerid",
            "compval": "bgp.bestpath.compare_routerid",
            "result": {
                "bgp": {
                    "bestpath": {
                        "compare_routerid": "{{ True if compare_routerid is defined }}"
                    }
                },
            }
        },
        {
            "name": "bgp_bestpath_cost_community_ignore",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<cost_community_ignore>bestpath\scost-community\signore)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath cost-community ignore",
            "compval": "bgp.bestpath.cost_community.ignore",
            "result": {
                "bgp": {
                    "bestpath": {
                        "cost_community": {
                            "ignore": "{{ True if cost_community_ignore is defined}}"
                        }
                    }
                },
            }
        },
        {
            "name": "bgp_bestpath_origin_as_use",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<origin_as_use>bestpath\sorigin-as\suse\svalidity)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath origin-as use validity",
            "compval": "bgp.bestpath.origin_as.use.validity",
            "result": {
                "bgp": {
                    "bestpath": {
                        "origin_as":
                            {
                                "use": {"validity": "{{ True if origin_as_use is defined }}"}

                            }
                    }
                },
            }
        },
        {
            "name": "bgp_bestpath_origin_as_allow",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<origin_as_allow>bestpath\sorigin-as\sallow\sinvalid)
                $""", re.VERBOSE
            ),
            "setval": "bgp bestpath origin-as allow invalid",
            "compval": "bgp.bestpath.origin_as.allow.invalid",
            "result": {
                "bgp": {
                    "bestpath": {
                        "origin_as":
                            {
                                "allow": {"invalid": "{{ True if origin_as_allow is defined }}"}

                            }
                    }
                },
            }
        },
        {
            "name": "bgp_confederation_identifier",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<confederation_identifier>confederation\sidentifier\s\d+)
                $""", re.VERBOSE
            ),
            "setval": "bgp confederation identifier {{ bgp.confederation.identifier}}",
            "compval": "bgp.confederation.identifier",
            "result": {
                "bgp": {
                    "confederation": {
                        "identifier": "{{confederation_identifier.split(" ")[2]}}"
                    }

                },
            }
        },
        {
            "name": "bgp_graceful_restart_set",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<graceful_restart_set>graceful-restart)
                $""", re.VERBOSE
            ),
            "setval": "bgp graceful-restart",
            "compval": "bgp.graceful_restart.set",
            "result": {
                "bgp": {
                    "graceful_restart": {
                        "set": "{{ True if graceful_restart_set is defined }}"
                    }

                },
            }
        },
        {
            "name": "bgp_graceful_restart_graceful_reset",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<graceful_restart_graceful_reset>graceful-restart\sgraceful-reset)
                $""", re.VERBOSE
            ),
            "setval": "bgp graceful-restart graceful-reset",
            "compval": "bgp.graceful_restart.graceful_reset",
            "result": {
                "bgp": {
                    "graceful_restart": {
                        "graceful_reset": "{{ True if graceful_restart_graceful_reset is defined}}"
                    }

                },
            }
        },
        {
            "name": "bgp_graceful_restart_restart_time",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<graceful_restart_restart_time>graceful-restart\srestart-time\s\d+)
                $""", re.VERBOSE
            ),
            "setval": "bgp graceful-restart restart-time {{ bgp.graceful_restart.restart_time}}",
            "compval": "bgp.graceful_restart.restart_time",
            "result": {
                "bgp": {
                    "graceful_restart": {
                        "restart_time": "{{ graceful_restart_restart_time.split(" ")[2] }}"
                    }

                },
            }
        },
        {
            "name": "bgp_graceful_restart_purge_time",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<graceful_restart_purge_time>graceful-restart\spurge-time\s\d+)
                $""", re.VERBOSE
            ),
            "setval": "bgp graceful-restart purge-time {{ bgp.graceful_restart.purge_time}}",
            "compval": "bgp.graceful_restart.purge_time",
            "result": {
                "bgp": {
                    "graceful_restart": {
                        "purge_time": "{{ graceful_restart_purge_time.split(" ")[2] }}"
                    }

                },
            }
        },
        {
            "name": "bgp_graceful_restart_stalepath_time",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<graceful_restart_stalepath_time>graceful-restart\sstalepath-time\s\d+)
                $""", re.VERBOSE
            ),
            "setval": "bgp graceful-restart stalepath-time {{ bgp.graceful_restart.stalepath_time}}",
            "compval": "bgp.graceful_restart.stalepath_time",
            "result": {
                "bgp": {
                    "graceful_restart": {
                        "stalepath_time": "{{ graceful_restart_stalepath_time.split(" ")[2] }}"
                    }

                },
            }
        },
        {
            "name": "bgp_log_message",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<log_message>log\smessage\sdisable)
                $""", re.VERBOSE
            ),
            "setval": "bgp log message disable",
            "compval": "bgp.log.message.disable",
            "result": {
                "bgp": {
                    "log": {
                        "message": {"disable": "{{ True if log_message is defined }}"}
                    }

                },
            }
        },
        {
            "name": "bgp_log_neighbor_changes_detail",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<log_neighbor_changes_detail>log\sneighbor\schanges\sdetail)
                $""", re.VERBOSE
            ),
            "setval": "bgp log neighbor changes detail",
            "compval": "bgp.log.neighbor.changes.detail",
            "result": {
                "bgp": {
                    "log": {
                        "neighbor": {"changes": {"detail": "{{True if log_neighbor_changes_detail is defined }}"}}
                    }

                },
            }
        },
        {
            "name": "bgp_log_neighbor_changes_disable",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<log_neighbor_changes_disable>log\sneighbor\schanges\sdisable)
                $""", re.VERBOSE
            ),
            "setval": "bgp log neighbor changes disable",
            "compval": "bgp.log.neighbor.changes.disable",
            "result": {
                "bgp": {
                    "log": {
                        "neighbor": {"changes": {"disable": "{{ True if log_neighbor_changes_disable is defined }}"}}
                    }

                },
            }
        },
        {
            "name": "bgp_multipath_as_path_ignore_onwards",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<multipath>multipath\sas-path\signore\sonwards)
                $""", re.VERBOSE
            ),
            "setval": "bgp multipath as-path ignore onwards",
            "compval": "bgp.multipath.as_path.ignore.onwards",
            "result": {
                "bgp": {
                    "multipath": {
                        "as_path": {"ignore": {"onwards": "{{ not not multipath}}"}}
                    }

                },
            }
        },
        {
            "name": "bgp_origin_as_validation_disable",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<origin_as_validation_disable>origin-as\svalidation\sdisable)
                $""", re.VERBOSE
            ),
            "setval": "bgp origin-as validation disable",
            "compval": "bgp.origin_as.validation.disable",
            "result": {
                "bgp": {
                    "origin_as": {
                        "validation": {"disable": "{{ not not origin_as_validation_disable}}"}
                    }

                },
            }
        },
        {
            "name": "bgp_origin_as_validation_signal_ibgp",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<origin_as_validation_signal_ibgp>origin-as\svalidation\ssignal\sibgp)
                $""", re.VERBOSE
            ),
            "setval": "bgp origin-as validation signal ibgp",
            "compval": "bgp.origin_as.validation.signal.ibgp",
            "result": {
                "bgp": {
                    "origin_as": {
                        "validation": {"signal": {"ibgp": "{{ not not origin_as_validation_signal_ibgp }}"}}
                    }

                },
            }
        },
        {
            "name": "bgp_origin_as_validation_time_off",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<validation_time_off>origin-as\svalidation\stime\soff)
                $""", re.VERBOSE
            ),
            "setval": "bgp origin-as validation time off",
            "compval": "bgp.origin_as.validation.time.off",
            "result": {
                "bgp": {
                    "origin_as": {
                        "validation": {"time": {"time_off": "{{ not not validation_time_off }}"}}
                    }

                },
            }
        },
        {
            "name": "bgp_origin_as_validation_time",
            "getval": re.compile(
                r"""
                \sbgp
                \s(?P<validation_time>origin-as\svalidation\stime\s\d+)
                $""", re.VERBOSE
            ),
            "setval": "bgp origin-as validation time {{ bgp.origin_as.validation.time.time_in_second }}",
            "compval": "bgp.origin_as.validation.time.time_in_second",
            "result": {
                "bgp": {
                    "origin_as": {
                        "validation": {"time": {"time_in_second": "{{ validation_time.split(" ")[3] }}"}}
                    }

                },
            }
        },

        {
            "name": "bgp_default_information_originate",
            "getval": re.compile(
                r"""
                \sdefault-information
                \s(?P<default_information_originate>originate)
                $""", re.VERBOSE
            ),
            "setval": "default-information originate",
            "compval": "default_information.originate",
            "result": {
                "default_information": {
                    "originate": "{{ not not default_information_originate }}"
                },
            }
        },
        {
            "name": "bgp_default_metric",
            "getval": re.compile(
                r"""
                \sdefault-metric
                \s(?P<default_metric>\d+)
                $""", re.VERBOSE
            ),
            "setval": "default-metric {{config_data.default_metric}}",
            "compval": "default_metric",
            "result": {
                "default_metric": "{{ default_metric }}"
            }
        },
        {
            "name": "bgp_graceful_maintenance",
            "getval": re.compile(
                r"""
                \sgraceful-maintenance
                \sactivate
                \s(?P<graceful_maintenance>\S*)
                $""", re.VERBOSE
            ),
            "setval": "graceful_maintenance {{config_data.graceful_maintenance.activate}}",
            "compval": "graceful_maintenance",
            "result": {
                "graceful_maintenance": {"activate": "{{ graceful_maintenance }}"}
            }
        },
        {
            "name": "ibgp_policy_out_enforce_modifications",
            "getval": re.compile(
                r"""
                \sibgp
                \spolicy
                \sout
                \s(?P<ibgp_policy_out>enforce-modifications)
                $""", re.VERBOSE
            ),
            "setval": "ibgp policy out enforce-modifications",
            "compval": "graceful_maintenance",
            "result": {
                "ibgp": {"policy": {"out": "{{ not not ibgp_policy_out }}"}}
            }
        },
        {
            "name": "mpls_activate_interface",
            "getval": re.compile(
                r"""
                \smpls
                \sactivate
                \sinterface
                \s(?P<mpls_interface>\S+)
                $""", re.VERBOSE
            ),
            "setval": "mpls activate interface {{config_data.mpls.activate.interface}}",
            "compval": "mpls_activate_interface",
            "result": {
                "mpls": {"activate": {"interface": "{{ mpls_interface }}"}}
            }
        },
        {
            "name": "mvpn",
            "getval": re.compile(
                r"""
                \smvpn(?P<mvpn>)
                $""", re.VERBOSE
            ),
            "setval": "mvpn",
            "compval": "mvpn",
            "result": {
                "mvpn": "{{ not not mvpn }}"
            }
        },
        {
            "name": "nsr_set",
            "getval": re.compile(
                r"""
                \snsr(?P<nsr>)
                $""", re.VERBOSE
            ),
            "setval": "nsr",
            "compval": "nsr_set",
            "result": {
                "nsr": {"set": "{{ not not nsr }}"}
            }
        },
        {
            "name": "nsr_disable",
            "getval": re.compile(
                r"""
                \snsr
                \sdisable(?P<nsr_disable>)
                $""", re.VERBOSE
            ),
            "setval": "nsr disable",
            "compval": "nsr_disable",
            "result": {
                "nsr": {"disable": "{{ not not nsr_disable }}"}
            }
        },
        {
            "name": "socket_receive_buffer_size",
            "getval": re.compile(
                r"""
                \ssocket
                \s(?P<socket_rcv_buffer_size>receive-buffer-size\S+)
                $""", re.VERBOSE
            ),
            "setval": "socket receive-buffer-size {{ config_data.receive_buffer_size}}",
            "compval": "socket_receive_buffer_size",
            "result": {
                "socket": {"receive_buffer_size": "{{ socket_rcv_buffer_size }}"}
            }
        },
        {
            "name": "socket_send_buffer_size",
            "getval": re.compile(
                r"""
                \ssocket
                \s(?P<socket_send_buffer_size>send-buffer-size\S+)
                $""", re.VERBOSE
            ),
            "setval": "socket send-buffer-size {{ config_data.send_buffer_size}}",
            "compval": "socket_send_buffer_size",
            "result": {
                "socket": {"send_buffer_size": "{{ socket_send_buffer_size }}"}
            }
        },

    ]
    # fmt: on
