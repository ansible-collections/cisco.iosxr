#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_bgp_address_family
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: iosxr_bgp_global
short_description: Manages BGP global resource module.
description:
- This module configures and manages the attributes of BGP global on Cisco IOS-XR platforms.
version_added: 1.3.0
author: Ashwini Mhatre (amhatre)
notes:
- Tested against Cisco IOS-XR 6.1.3.
- This module works with connection C(network_cli).
options:
    config:
      description: A list of configurations for BGP address family.
      type: dict
      suboptions:
        as_number:
          description: Autonomous system number.
          type: str
        address_family:
          description: Enable address family and enter its config mode
          type: list
          elements: dict
          suboptions:
            afi:
              description: address family.
              type: str
              choices: ['ipv4', 'ipv6', 'l2vpn', 'link-state', 'vpnv4', 'vpnv6']
            af_modifier:
              description: Address Family modifier
              type: str
              choices: [ 'flowspec', 'mdt', 'multicast', 'mvpn', 'rt-filter', 'tunnel', 'unicast', 'evpn', 'mspw', 'vpls-vpws', 'link-state' ]
            additional_paths: &additional_paths
              description: BGP additional-paths commands
              type: str
              choices: [ 'send', 'receive' ]
            advertise_best_external: &advertise
              description: Advertise best-external path.
              type: bool
            aggregate_address: &aggrigate_address
              description: Configure BGP aggregate entries.
              type: dict
              suboptions:
                value:
                  type: str
                  description: IPv4 Aggregate address and mask or masklength.
                as_set:
                  type: bool
                  description: Generate AS set path information.
                as_confed_set:
                  type: bool
                  description: Generate AS confed set path information.
                summary_only:
                  type: bool
                  description: Filter more specific routes from updates.
                route_policy:
                  description: Policy to condition advertisement, suppression, and attributes.
                  type: str
            allocate_label: &allocate_label
              type: dict
              description: Allocate labels.
              suboptions:
                all:
                  type: bool
                  description:  Allocate labels for all prefixes.
                route_policy:
                  description: Use a route policy to select prefixes for label allocation.
                  type: str
            as_path_loopcheck_out_disable: &as_path_loopcheck
              type: bool
              description: Configure AS Path loop checking for outbound updates.
            bgp:
              type: dict
              description: BGP Commands.
              suboptions:
                attribute_download: &attribute_download
                  type: bool
                  description: Configure attribute download for this address-family.
                bestpath:
                  type: dict
                  description: Change default route selection criteria.
                  suboptions:
                    origin_as:
                      description: BGP origin-AS knobs.
                      type: dict
                      suboptions:
                        use:
                          description: BGP origin-AS knobs.
                          type: dict
                          suboptions:
                            validity:
                              description: BGP bestpath selection will use origin-AS validity
                              type: bool
                        allow:
                          description: BGP origin-AS knobs.
                          type: dict
                          suboptions:
                            invalid:
                              description: BGP bestpath selection will allow 'invalid' origin-AS
                              type: bool
                client_to_client:
                  type: dict
                  description: Configure client to client route reflection.
                  suboptions:
                    reflection:
                      type: dict
                      description: disable client to client reflection of cluster id.
                      suboptions:
                        cluster_id_disable:
                          type: dict
                          description: ID of Cluster for which reflection is to be disabled.
                          suboptions:
                            cluster_id:
                              type: str
                              description: ID of Cluster for which reflection is to be disabled.
                            disable:
                              type: bool
                              description: disable cluster id.
                        disable:
                          type: bool
                          disable: disable reflection.
                dampening: &dampening
                  type: dict
                  description: Enable route-flap dampening
                  suboptions:
                    set:
                      type: bool
                      description: Enable dampening.
                    value:
                      type: int
                      description: Half-life time for the penalty
                    route_policy:
                      description: Route policy to specify criteria for dampening.
                      type: str
                label_delay:
                  type: dict
                  description: Specify delay for batching label processing
                  suboptions:
                    delay_second_parts:
                      type: int
                      description: Delay, seconds part <0-10>.
                    delay_ms_parts:
                      type: int
                      description: milliseconds part <0-999>.
                import_delay:
                  type: dict
                  description: Specify delay for batching import processing.
                  suboptions:
                    delay_second_parts:
                      type: int
                      description: Delay, seconds part <0-10>.
                    delay_ms_parts:
                      type: int
                      description: milliseconds part <0-999>.
                origin_as:
                  description: BGP origin-AS knobs.
                  type: dict
                  suboptions:
                    validation:
                      description: BGP origin-AS validation knobs.
                      type: dict
                      suboptions:
                        disable:
                          description: Disable RPKI origin-AS validation.
                          type: bool
                        signal:
                          description: Signal origin-AS validity towards peers.
                          type: dict
                          suboptions:
                            ibgp:
                              description: Signal origin-AS validity towards iBGP peers
                              type: bool
                scan_time:
                  description: Configure background scanner interval for this address-family Example- <5-3600>.
                  type: int
            default_martian_check_disable:
              type: bool
              description: Martian check default
            distance: &distance
              type: dict
              description: Define an administrative distance.
              suboptions:
                routes_external_to_as:
                  type: int
                  description: Distance for routes external to the AS <1-255>.
                routes_internal_to_as:
                  type: int
                  description: Distance for routes internal to the AS <1-255>.
                local_routes:
                  type: int
                  description: Distance for local routes <1-255>.
            dynamic_med: &dynamic_med
              type: int
              description: Dynamic MED Interval.
            maximum_paths: &maximum_paths
              type: dict
              description: Forward packets over multiple paths.
              suboptions:
                ibgp:
                  type: dict
                  description: iBGP-multipath.
                  suboptions:
                    max_path_value:
                      type: int
                      description: <2-64>  Number of paths (limit includes backup path).
                    order_igp_metric:
                      description: Order candidate multipaths for selection as per configured number(cisco-support).
                      type: bool
                    selective_order_igp_metric:
                      description: Allow multipaths only from marked neighbors
                      type: bool
                    unequal_cost:
                      type: dict
                      description: Allow multipaths to have different BGP nexthop IGP metrics.
                      suboptions:
                        set:
                          type: bool
                          description: set unequal_cost.
                        order_igp_metric:
                          description: Order candidate multipaths for selection as per configured number(cisco-support).
                          type: bool
                        selective_order_igp_metric:
                          description: Allow multipaths only from marked neighbors
                          type: bool
                ebgp:
                  type: dict
                  description: ebgp-multipath.
                  suboptions:
                    max_path_value:
                      type: int
                      description: <2-64>  Number of paths (limit includes backup path).
                    order_igp_metric:
                      description: Order candidate multipaths for selection as per configured number(cisco-support).
                      type: bool
                    selective_order_igp_metric:
                      description: Allow multipaths only from marked neighbors
                      type: bool
                eibgp:
                  type: dict
                  description: eiBGP-multipath.
                  suboptions:
                    max_path_value:
                      type: int
                      description: <2-64>  Number of paths (limit includes backup path).
                    order_igp_metric:
                      description: Order candidate multipaths for selection as per configured number(cisco-support).
                      type: bool
                    selective_order_igp_metric:
                      description: Allow multipaths only from marked neighbors
                      type: bool
            network: &network
              type: dict
              description:
              suboptions:
                value:
                  type: str
                  description: Specify a network to announce via BGP.
                backdoor_route_policy:
                  type: str
                  description: Specify a BGP backdoor route.
                route_policy:
                  type: str
                  description: Route-policy to modify the attributes.
            nexthop: &nexthop
              type: dict
              description: Nexthop
              suboptions:
                resolution_prefix_length_minimum:
                  type: int
                  description: Set minimum prefix-length for nexthop resolution.
                  choices: [0,32]
                route_policy:
                  type: str
                  description: Policy to filter out nexthop notification.
                trigger_delay_critical:
                  description: For critical notification
                  type: int
                trigger_delay_non_critical:
                  type: int
                  description: For non critical notification.
            optimal_route_reflection: &optimal_rr
              type: dict
              description: Configure optimal-route-reflection group.
              suboptions:
                group_name:
                  type: str
                  description: ORR group name - maximum 32 characters.
                primary_address:
                  type: str
                  description: IPv4 primary address.
                secondary_address:
                  type: str
                  description: IPv4 secondary address
            permanent_network_route_policy:
              type: str
              description: Name of the policy.
            retain_local_label:
              type: int
              description: Label retention time in minutes <3-60>.
            table_policy: &table_policy
              type: str
              description: Configure policy for installation of routes to RIB.
            update:
              type: dict
              descriptions: BGP Update generation configuration.
              suboptions:
                limit:
                  type: dict
                  descriptions: Update limit
                  suboptions:
                    sub_group:
                      type: dict
                      description: Update limit for address-family.
                      suboptions:
                        ibgp:
                          type: int
                          descriptions: Update limit for iBGP sub-groups<1-512.
                        ebgp:
                          type: int
                          descriptions: Update limit for eBGP sub-groups<1-512.
                    address_family:
                      type: int
                      descriptions: Update limit for sub-groups.
                wait_install:
                  type: bool
                  description: Wait for route install.
            redistribute: &redistribute
              type: dict
              description: Redistribute information from another routing protocol.
              suboptions:
                application:
                  type: dict
                  description: OnePK application routes.
                  suboptions:
                    name:
                      type: str
                      description: name of application
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                connected:
                  type: dict
                  description: Connected routes.
                  suboptions:
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                eigrp:
                  type: dict
                  description: Enhanced Interior Gateway Routing Protocol (EIGRP).
                  suboptions:
                    name:
                      type: str
                      description: EIGRP instance name.
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                    internal:
                      type: bool
                      description: Redistribute EIGRP internal routes.
                    external:
                      type: bool
                      description: Redistribute EIGRP external routes.
                isis:
                  type: dict
                  description: ISO IS-IS.
                  suboptions:
                    name:
                      type: str
                      description: IS-IS instance name.
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                    level:
                      type: str
                      description:
                      - Redistribute routes from the specified ISIS levels.
                      - Redistribute ISIS level 1 routes
                      - Redistribute ISIS level 1 inter-area routes
                      - Redistribute ISIS level 2 ISIS routes
                      choices: ['1', '2', '1-inter-area']
                lisp:
                  type: dict
                  description: Locator/ID Separation Protocol (LISP).
                  suboptions:
                    set:
                      type: bool
                      description: set lisp.
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                mobile:
                  type: dict
                  description: Mobile routes.
                  suboptions:
                    set:
                      type: bool
                      description: set Mobile routes.
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                ospf:
                  type: dict
                  description:  Open Shortest Path First (OSPF).
                  suboptions:
                    name:
                      type: str
                      description: OSPF router tag
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                    internal:
                      type: bool
                      description: Redistribute OSPF internal routes.
                    nssa_external:
                      type: bool
                      description: Redistribute OSPF NSSA external routes
                    external:
                      type: int
                      description: Redistribute OSPF external routes.
                      choices: [1, 2]
                rip:
                  type: dict
                  description: Routing Information Protocol (RIP).
                  suboptions:
                    set:
                      type: bool
                      description: set RIP.
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                static:
                  type: dict
                  description: Static routes.
                  suboptions:
                    set:
                      type: bool
                      description: set Static routes.
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
                subscriber:
                  type: dict
                  description: subscriber routes.
                  suboptions:
                    set:
                      type: bool
                      description: set subscriber routes.
                    metric:
                      type: int
                      description: Metric for redistributed routes.
                    route_policy:
                      type: str
                      description: Route-policy for reference.
            inter_as_install:
              type: bool
              description: Install remote mvpn routes in default vrf.This is applicable for mvpn afi.
            segmented_multicast:
              type: bool
              description:  Enable segmented multicast.This is applicable for mvpn afi.
            global_table_multicast:
              type: bool
              description: Enable global table multicast.
            vrf_all_conf:
              type: dict
              description: configuration is for all vrfs and its applicable for afi vpn6 and modifier unicast.
              suboptions:
                source_rt_import_policy:
                  type: bool
                  description: Source import route-targets from import-policy.
                table_policy:
                  type: str
                  description: Configure policy for installation of routes to RIB.
                label_mode:
                  type: dict
                  description: Label-related configuration.
                  suboptions:
                    per_ce: &per_ce
                      type: bool
                      description: Set per CE label mode
                    per_vrf: &per_vrf
                      type: bool
                      description: Set per VRF label mode.
                    route_policy: &route_policy
                      type: str
                      description: Use a route policy to select prefixes for label allocation mode.
            weight: &wt
              type: dict
              description: Define or modify weight.
              suboptions:
                reset_on_import_disable:
                  type: bool
                  description: disable reset_on_import.
                reset_on_import:
                  type: bool
                  description: set reset_on_import.
        vrfs:
          description: Configure BGP in a VRF.
          type: list
          elements: dict
          suboptions:
            vrf:
             description: VRF name.
             type: str
            address_family:
              description: Enable address family and enter its config mode
              type: list
              elements: dict
              suboptions:
                afi:
                  description: address family.
                  type: str
                  choices: ['ipv4', 'ipv6']
                af_modifier:
                  description: Address family type for ipv4.
                  type: str
                  choices: ['unicast', 'multicast', 'flowspec', 'mvpn']
                additional_paths: *additional_paths
                advertise_best_external: *advertise
                as_path_loopcheck_out_disable: *as_path_loopcheck
                aggrigate_address: *aggrigate_address
                allocate_label: *allocate_label
                allow_vpn_default_originate:
                  type: bool
                  description: Allow sending default originate route to VPN neighbor.
                bgp:
                  description: BGP parameters.
                  type: dict
                  suboptions:
                    dampening: *dampening
                    attribute_download: *attribute_download
                nexthop: *nexthop
                distance: *distance
                dynamic_med: *dynamic_med
                label_mode:
                  type: dict
                  description: label configuration.
                  suboptions:
                    per_ce: *per_ce
                    per_vrf: *per_vrf
                    route_policy: *route_policy
                    per_prefix:
                      type: bool
                      description: Set per perfix label mode.
                maximum_paths: *maximum_paths
                mvpn_single_forwarder_selection_all:
                  type: bool
                  description: Enable single forwarder selection  for all
                mvpn_single_forwarder_selection_highest_ip_address:
                  type: bool
                  description: Enable single forwarder selection  for PE with highest ip address.
                network: *network
                optimal_route_reflection: *optimal_rr
                redistribute: *redistribute
                table_policy: *table_policy
                route_target_download:
                  description: Route target RIB installation.
                  type: bool
                weight: *wt
    running_config:
      description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the EOS device by
        executing the command B(show running-config | section bgp).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
      type: str
    state:
      description:
      - The state the configuration should be left in.
      type: str
      choices: [deleted, merged, overridden, replaced, gathered, rendered, parsed]
      default: merged
"""
EXAMPLES = """
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.bgp_address_family.bgp_address_family import (
    Bgp_address_familyArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.bgp_address_family.bgp_address_family import (
    Bgp_address_family,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Bgp_address_familyArgs.argument_spec,
        mutually_exclusive=[["config", "running_config"]],
        required_if=[
            ["state", "merged", ["config"]],
            ["state", "replaced", ["config"]],
            ["state", "overridden", ["config"]],
            ["state", "rendered", ["config"]],
            ["state", "parsed", ["running_config"]],
        ],
        supports_check_mode=True,
    )

    result = Bgp_address_family(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
