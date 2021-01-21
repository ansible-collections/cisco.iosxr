#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The iosxr_bgp_global config file.
It is in this file where the current configuration (as dict)
is compared to the provided configuration (as dict) and the command set
necessary to bring the current configuration to its desired end-state is
created.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_merge,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.resource_module import (
    ResourceModule,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.facts import (
    Facts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.rm_templates.bgp_global import (
    Bgp_globalTemplate,
)


class Bgp_global(ResourceModule):
    """
    The iosxr_bgp_global config class
    """

    def __init__(self, module):
        super(Bgp_global, self).__init__(
            empty_fact_val={},
            facts_module=Facts(module),
            module=module,
            resource="bgp_global",
            tmplt=Bgp_globalTemplate(),
        )
        self.parsers = [
            'router',
            'bfd_multiplier',
            'bfd_minimum_interval',
            'bgp_auto_policy_soft_reset',
            'bgp_as_path_loopcheck',
            'bgp_cluster_id',
            'bgp_default_local_preference',
            'bgp_enforce_first_as_disable',
            'bgp_fast_external_fallover_disable',
            'bgp_install_diversion',
            'bgp_max_neighbors',
            'bgp_redistribute_internal',
            'bgp_router_id',
            'bgp_scan_time',
            'bgp_unsafe_ebgp_policy',
            'bgp_update_delay',
            'bgp_bestpath_aigp',
            'bgp_bestpath_as_path_ignore',
            'bgp_bestpath_as_path_multipath_relax',
            'bgp_bestpath_med_always',
            'bgp_bestpath_med_confed',
            'bgp_bestpath_med_missing_as_worst',
            'bgp_bestpath_compare_routerid',
            'bgp_bestpath_cost_community_ignore',
            'bgp_bestpath_origin_as_use',
            'bgp_bestpath_origin_as_allow',
            'bgp_confederation_identifier',
            'bgp_graceful_restart_set',
            'bgp_graceful_restart_graceful_reset',
            'bgp_graceful_restart_restart_time',
            'bgp_graceful_restart_purge_time',
            'bgp_graceful_restart_stalepath_time',
            'bgp_log_message',
            'bgp_log_neighbor_changes_detail',
            'bgp_log_neighbor_changes_disable',
            'bgp_multipath_as_path_ignore_onwards',
            'bgp_origin_as_validation_disable',
            'bgp_origin_as_validation_signal_ibgp',
            'bgp_origin_as_validation_time_off',
            'bgp_origin_as_validation_time',
            'bgp_default_information_originate',
            'bgp_default_metric',
            'bgp_graceful_maintenance',
            'ibgp_policy_out_enforce_modifications',
            'mpls_activate_interface',
            'mvpn',
            'nsr_set',
            'nsr_disable',
            'socket_receive_buffer_size',
            'socket_send_buffer_size',

        ]

    def execute_module(self):
        """ Execute the module

        :rtype: A dictionary
        :returns: The result from module execution
        """
        if self.state not in ["parsed", "gathered"]:
            self.generate_commands()
            self.run_commands()
        return self.result

    def generate_commands(self):
        """ Generate configuration commands to send based on
            want, have and desired state.
        """
        #import epdb;epdb.serve()
        """ Generate configuration commands to send based on
                    want, have and desired state.
                """
        #for entry in self.want, self.have:
        #    self._bgp_list_to_dict(entry)

        # if state is deleted, clean up global params
        if self.state == "deleted":
            if not self.want or (self.have.get("as_number") == self.want.get("as_number")):
                self._compare(want={}, have=self.have)

        elif self.state == "purged":
            self.addcmd(self.have or {}, "asn", True)

        else:
            wantd = self.want
            # if state is merged, merge want onto have and then compare
            if self.state == "merged":
                wantd = dict_merge(self.have, self.want)

            self._compare(want=wantd, have=self.have)

    def _compare(self, want, have):
        """Leverages the base class `compare()` method and
           populates the list of commands to be run by comparing
           the `want` and `have` data with the `parsers` defined
           for the Bgp_global network resource.
        """
        self.compare(parsers=self.parsers, want=want, have=have)
        #import epdb;epdb.serve()
        if self.commands and "router bgp" not in self.commands[0]:
            self.commands.insert(
                0, self._tmplt.render({"as_number": want['as_number']}, "router", False)
            )
