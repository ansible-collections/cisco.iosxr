.. _cisco.iosxr.iosxr_static_routes_module:


*******************************
cisco.iosxr.iosxr_static_routes
*******************************

**Static routes resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages static routes on devices running Cisco IOS-XR.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary of static route options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address_families</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary specifying the address family to which the static route(s) belong.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the top level address family indicator.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>routes</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A dictionary that specifies the static route configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dest</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>An IPv4 or IPv6 address in CIDR notation that specifies the destination network for the static route.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>next_hops</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Next hops to the specified destination.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>admin_distance</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The administrative distance for this static route.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the description for this static route.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dest_vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The destination VRF.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>forward_router_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The IP address of the next hop that can be used to reach the destination network.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The interface to use to reach the destination.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>metric</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifes the metric for this static route.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tag</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies a numeric tag for this static route.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>track</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the object to be tracked.</div>
                        <div>This enables object tracking for static routes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tunnel_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies a tunnel id for the route.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrflabel</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the VRF label for this static route.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>safi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>unicast</li>
                                    <li>multicast</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the subsequent address family indicator.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The VRF to which the static route(s) belong.</div>
                </td>
            </tr>

            <tr>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>running_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This option is used only with state <em>parsed</em>.</div>
                        <div>The value of this option should be the output received from the IOS-XR device by executing the command <b>show running-config router static</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="5">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # Using merged

    # Before state
    # -------------
    # RP/0/RP0/CPU0:ios#show running-config router static
    # Sat Feb 22 07:46:30.089 UTC
    # % No such configuration item(s)
    #
    - name: Merge the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_static_routes:
        config:
        - address_families:
          - afi: ipv4
            safi: unicast
            routes:
            - dest: 192.0.2.16/28
              next_hops:
              - forward_router_address: 192.0.2.10
                interface: FastEthernet0/0/0/1
                description: LAB
                metric: 120
                tag: 10

              - interface: FastEthernet0/0/0/5
                track: ip_sla_1

            - dest: 192.0.2.32/28
              next_hops:
              - forward_router_address: 192.0.2.11
                admin_distance: 100

          - afi: ipv6
            safi: unicast
            routes:
            - dest: 2001:db8:1000::/36
              next_hops:
              - interface: FastEthernet0/0/0/7
                description: DC

              - interface: FastEthernet0/0/0/8
                forward_router_address: 2001:db8:2000:2::1

        - vrf: DEV_SITE
          address_families:
          - afi: ipv4
            safi: unicast
            routes:
            - dest: 192.0.2.48/28
              next_hops:
              - forward_router_address: 192.0.2.12
                description: DEV
                dest_vrf: test_1

            - dest: 192.0.2.80/28
              next_hops:
              - interface: FastEthernet0/0/0/2
                forward_router_address: 192.0.2.14
                dest_vrf: test_1
                track: ip_sla_2
                vrflabel: 124
        state: merged

    # After state
    # -------------
    # RP/0/RP0/CPU0:ios#show running-config router static
    # Sat Feb 22 07:49:11.754 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
    #    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
    #   !
    #  !
    # !

    # Using merged to update existing static routes

    # Before state
    # -------------
    # RP/0/RP0/CPU0:ios#show running-config router static
    # Sat Feb 22 07:49:11.754 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
    #    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
    #   !
    #  !
    # !

    - name: Update existing static routes configuration using merged
      cisco.iosxr.iosxr_static_routes:
        config:
        - vrf: DEV_SITE
          address_families:
          - afi: ipv4
            safi: unicast
            routes:
            - dest: 192.0.2.48/28
              next_hops:
              - forward_router_address: 192.0.2.12
                vrflabel: 2301
                dest_vrf: test_1

            - dest: 192.0.2.80/28
              next_hops:
              - interface: FastEthernet0/0/0/2
                forward_router_address: 192.0.2.14
                dest_vrf: test_1
                description: rt_test_1
        state: merged

    # After state
    # -------------
    # RP/0/RP0/CPU0:ios#show running-config router static
    # Sat Feb 22 07:49:11.754 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV vrflabel 2301
    #    192.0.2.80/28 vrf test_1 192.0.2.14 FastEthernet0/0/0/2 description rt_test_1 track ip_sla_2 vrflabel 124
    #   !
    #  !
    # !

    # Using replaced to replace all next hop entries for a single destination network

    # Before state
    # --------------

    # RP/0/RP0/CPU0:ios#sh running-config router static
    # Sat Feb 22 07:59:08.669 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
    #    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
    #    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
    #   !
    #  !
    # !

    - name: Replace device configurations of static routes with provided configurations
      cisco.iosxr.iosxr_static_routes:
        config:
        - vrf: DEV_SITE
          address_families:
          - afi: ipv4
            safi: unicast
            routes:
            - dest: 192.0.2.48/28
              next_hops:
              - forward_router_address: 192.0.2.15
                interface: FastEthernet0/0/0/3
                description: DEV_NEW
                dest_vrf: dev_test_2
        state: replaced

    # After state
    # ------------
    # RP/0/RP0/CPU0:ios#sh running-config router static
    # Sat Feb 22 08:04:07.085 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf dev_test_2 FastEthernet0/0/0/3 192.0.2.15 description DEV_NEW
    #    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
    #   !
    #  !
    # !

    # Using overridden to override all static route entries on the device

    # Before state
    # -------------
    # RP/0/RP0/CPU0:ios#sh running-config router static
    # Sat Feb 22 07:59:08.669 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
    #    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
    #    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
    #   !
    #  !
    # !

    - name: Overridde all static routes configuration with provided configuration
      cisco.iosxr.iosxr_static_routes:
        config:
        - vrf: DEV_NEW
          address_families:
          - afi: ipv4
            safi: unicast
            routes:
            - dest: 192.0.2.48/28
              next_hops:
              - forward_router_address: 192.0.2.15
                interface: FastEthernet0/0/0/3
                description: DEV1
          - afi: ipv6
            safi: unicast
            routes:
            - dest: 2001:db8:3000::/36
              next_hops:
              - interface: FastEthernet0/0/0/4
                forward_router_address: 2001:db8:2000:2::2
                description: PROD1
                track: ip_sla_1
        state: overridden

    # After state
    # -------------
    # RP/0/RP0/CPU0:ios#sh running-config router static
    # Sat Feb 22 08:07:41.516 UTC
    # router static
    #  vrf DEV_NEW
    #   address-family ipv4 unicast
    #    192.0.2.48/28 FastEthernet0/0/0/3 192.0.2.15 description DEV1
    #   !
    #   address-family ipv6 unicast
    #    2001:db8:3000::/36 FastEthernet0/0/0/4 2001:db8:2000:2::2 description PROD1 track ip_sla_1
    #   !
    #  !
    # !

    # Using deleted to delete all destination network entries under a single AFI

    # Before state
    # -------------
    # RP/0/RP0/CPU0:ios#sh running-config router static
    # Sat Feb 22 07:59:08.669 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
    #    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
    #    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
    #   !
    #  !
    # !

    - name: Delete all destination network entries under a single AFI
      cisco.iosxr.iosxr_static_routes:
        config:
        - vrf: DEV_SITE
          address_families:
          - afi: ipv4
            safi: unicast
        state: deleted

    # After state
    # ------------

    # RP/0/RP0/CPU0:ios#sh running-config router static
    # Sat Feb 22 08:16:41.464 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #  !
    # !

    # Using deleted to remove all static route entries from the device

    # Before state
    # -------------
    # RP/0/RP0/CPU0:ios#sh running-config router static
    # Sat Feb 22 07:59:08.669 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
    #    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
    #    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
    #   !
    #  !
    # !

    - name: Delete static routes configuration
      cisco.iosxr.iosxr_static_routes:
        state: deleted

    # After state
    # ------------
    # RP/0/RP0/CPU0:ios#sh running-config router static
    # Sat Feb 22 08:50:43.038 UTC
    # % No such configuration item(s)

    # Using gathered to gather static route facts from the device

    - name: Gather static routes facts from the device using iosxr_static_routes module
      cisco.iosxr.iosxr_static_routes:
        state: gathered

    # Task output (redacted)
    # -----------------------
    # "gathered": [
    #    {
    #        "address_families": [
    #            {
    #                "afi": "ipv4",
    #                "routes": [
    #                    {
    #                        "dest": "192.0.2.16/28",
    #                        "next_hops": [
    #                            {
    #                                "description": "LAB",
    #                                "forward_router_address": "192.0.2.10",
    #                                "interface": "FastEthernet0/0/0/1",
    #                                "metric": 120,
    #                                "tag": 10
    #                            },
    #                            {
    #                                "interface": "FastEthernet0/0/0/5",
    #                                "track": "ip_sla_1"
    #                            }
    #                        ]
    #                    },
    #                    {
    #                        "dest": "192.0.2.32/28",
    #                        "next_hops": [
    #                            {
    #                                "admin_distance": 100,
    #                                "forward_router_address": "192.0.2.11"
    #                            }
    #                        ]
    #                    }
    #                ],
    #                "safi": "unicast"
    #            },
    #            {
    #                "afi": "ipv6",
    #                "routes": [
    #                    {
    #                        "dest": "2001:db8:1000::/36",
    #                        "next_hops": [
    #                            {
    #                                "description": "DC",
    #                                "interface": "FastEthernet0/0/0/7"
    #                            },
    #                            {
    #                                "forward_router_address": "2001:db8:2000:2::1",
    #                                "interface": "FastEthernet0/0/0/8"
    #                            }
    #                        ]
    #                    }
    #                ],
    #                "safi": "unicast"
    #            }
    #        ]
    #    },
    #    {
    #        "address_families": [
    #            {
    #                "afi": "ipv4",
    #                "routes": [
    #                    {
    #                        "dest": "192.0.2.48/28",
    #                        "next_hops": [
    #                            {
    #                                "description": "DEV",
    #                                "dest_vrf": "test_1",
    #                                "forward_router_address": "192.0.2.12"
    #                            },
    #                            {
    #                                "forward_router_address": "192.0.3.24",
    #                                "interface": "GigabitEthernet0/0/0/1",
    #                                "vrflabel": 2302
    #                            }
    #                        ]
    #                    },
    #                    {
    #                        "dest": "192.0.2.80/28",
    #                        "next_hops": [
    #                            {
    #                                "dest_vrf": "test_1",
    #                                "forward_router_address": "192.0.2.14",
    #                                "interface": "FastEthernet0/0/0/2",
    #                                "track": "ip_sla_2",
    #                                "vrflabel": 124
    #                            }
    #                        ]
    #                    }
    #                ],
    #                "safi": "unicast"
    #            }
    #        ],
    #        "vrf": "DEV_SITE"
    #    }
    #  ]

    # Using rendered

    - name: Render platform specific commands (without connecting to the device)
      cisco.iosxr.iosxr_static_routes:
      config:
      - vrf: DEV_SITE
        address_families:
        - afi: ipv4
          safi: unicast
          routes:
          - dest: 192.0.2.48/28
            next_hops:
            - forward_router_address: 192.0.2.12
              description: DEV
              dest_vrf: test_1

          - dest: 192.0.2.80/28
            next_hops:
            - interface: FastEthernet0/0/0/2
              forward_router_address: 192.0.2.14
              dest_vrf: test_1
              track: ip_sla_2
              vrflabel: 124

    # Task Output (redacted)
    # -----------------------
    # "rendered": [
    #    "router static"s,
    #    "vrf DEV_SITE",
    #    "address-family ipv4 unicast",
    #    "192.0.2.48/28 vrf test_1 192.0.2.12 description DEV",
    #    "192.0.2.80/28 vrf test_1 192.0.2.14 FastEthernet0/0/0/2 track ip_sla_2 vrflabel 124"

    # Using parsed

    # parsed.cfg
    # ------------
    # Fri Nov 29 21:10:41.896 UTC
    # router static
    #  address-family ipv4 unicast
    #   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
    #   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
    #   192.0.2.32/28 192.0.2.11 100
    #  !
    #  address-family ipv6 unicast
    #   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
    #   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
    #  !
    #  vrf DEV_SITE
    #   address-family ipv4 unicast
    #    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
    #    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
    #   !
    #  !
    # !

    - name: Use parsed state to convert externally supplied device specific static routes
        commands to structured format
      cisco.iosxr.iosxr_static_routes:
        running_config: "{{ lookup('file', '../../fixtures/parsed.cfg') }}"
        state: parsed

    # Task output (redacted)
    # -----------------------
    # "parsed": [
    #        {
    #            "address_families": [
    #                {
    #                    "afi": "ipv4",
    #                    "routes": [
    #                        {
    #                            "dest": "192.0.2.16/28",
    #                            "next_hops": [
    #                                {
    #                                    "description": "LAB",
    #                                    "forward_router_address": "192.0.2.10",
    #                                    "interface": "FastEthernet0/0/0/1",
    #                                    "metric": 120,
    #                                    "tag": 10
    #                                },
    #                                {
    #                                    "interface": "FastEthernet0/0/0/5",
    #                                    "track": "ip_sla_1"
    #                                }
    #                            ]
    #                        },
    #                        {
    #                            "dest": "192.0.2.32/28",
    #                            "next_hops": [
    #                                {
    #                                    "admin_distance": 100,
    #                                    "forward_router_address": "192.0.2.11"
    #                                }
    #                            ]
    #                        }
    #                    ],
    #                    "safi": "unicast"
    #                },
    #                {
    #                    "afi": "ipv6",
    #                    "routes": [
    #                        {
    #                            "dest": "2001:db8:1000::/36",
    #                            "next_hops": [
    #                                {
    #                                    "description": "DC",
    #                                    "interface": "FastEthernet0/0/0/7"
    #                                },
    #                                {
    #                                    "forward_router_address": "2001:db8:2000:2::1",
    #                                    "interface": "FastEthernet0/0/0/8"
    #                                }
    #                            ]
    #                        }
    #                    ],
    #                    "safi": "unicast"
    #                }
    #            ]
    #        },
    #        {
    #            "address_families": [
    #                {
    #                    "afi": "ipv4",
    #                    "routes": [
    #                        {
    #                            "dest": "192.0.2.48/28",
    #                            "next_hops": [
    #                                {
    #                                    "description": "DEV",
    #                                    "dest_vrf": "test_1",
    #                                    "forward_router_address": "192.0.2.12"
    #                                }
    #                            ]
    #                        },
    #                        {
    #                            "dest": "192.0.2.80/28",
    #                            "next_hops": [
    #                                {
    #                                    "dest_vrf": "test_1",
    #                                    "forward_router_address": "192.0.2.14",
    #                                    "interface": "FastEthernet0/0/0/2",
    #                                    "track": "ip_sla_2",
    #                                    "vrflabel": 124
    #                                }
    #                            ]
    #                        }
    #                    ],
    #                    "safi": "unicast"
    #                }
    #            ],
    #            "vrf": "DEV_SITE"
    #        }
    #    ]
    # }



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>after</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when changed</td>
                <td>
                            <div>The resulting configuration model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>before</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The configuration prior to the model invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format
     of the parameters above.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;router static&#x27;, &#x27;vrf dev_site&#x27;, &#x27;address-family ipv4 unicast&#x27;, &#x27;192.0.2.48/28 192.0.2.12 FastEthernet0/0/0/1 track ip_sla_10 description dev1&#x27;, &#x27;address-family ipv6 unicast&#x27;, &#x27;no 2001:db8:1000::/36&#x27;, &#x27;2001:db8:3000::/36 2001:db8:2000:2::2 FastEthernet0/0/0/4 track ip_sla_11 description prod1&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nilashish Chakraborty (@NilashishC)
