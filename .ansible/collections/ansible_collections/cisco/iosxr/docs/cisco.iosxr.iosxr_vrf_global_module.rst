.. _cisco.iosxr.iosxr_vrf_global_module:


****************************
cisco.iosxr.iosxr_vrf_global
****************************

**Manages global VRF configuration.**


Version added: 9.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages VRF configurations on Cisco IOS-XR devices.
- It enables playbooks to handle either individual VRFs or the complete VRF collection.
- It also permits removing non-explicitly stated VRF definitions from the setup.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="3">
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
                        <div>A dictionary of options for VRF configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>A description for the VRF.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>evpn_route_sync</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>EVPN Instance VPN ID used to synchronize the VRF route(s).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fallback_vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Fallback VRF name</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mhost</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Multicast host stack options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>Address Family Identifier (AFI)</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Default interface for multicast.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the VRF.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rd</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VPN Route Distinguisher (RD).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>remote_route_filtering</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Enable/Disable remote route filtering per VRF</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disable</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Disable remote route filtering per VRF</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vpn</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VPN ID for the VRF</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VPN ID for the VRF.</div>
                </td>
            </tr>


            <tr>
                <td colspan="3">
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
                        <div>The value of this option should be the output received from the IOS-XR device by executing the command <b>show running-config vrf</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>parsed</li>
                                    <li>gathered</li>
                                    <li>deleted</li>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>rendered</li>
                                    <li>overridden</li>
                                    <li>purged</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The states <em>rendered</em>, <em>gathered</em> and <em>parsed</em> does not perform any change on the device.</div>
                        <div>The state <em>rendered</em> will transform the configuration in <code>config</code> option to platform specific CLI commands which will be returned in the <em>rendered</em> key within the result. For state <em>rendered</em> active connection to remote host is not required.</div>
                        <div>The state <em>gathered</em> will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into JSON format as per the resource module parameters and the value is returned in the <em>parsed</em> key within the result. The value of <code>running_config</code> option should be the same format as the output of command <em>show running-config vrf</em>. connection to remote host is not required.</div>
                        <div>The state <em>purged</em> removes all the VRF configurations from the target device. Use caution with this state.</div>
                        <div>The state <em>deleted</em> only removes the VRF attributes that this module manages and does not negate the VRF completely. Thereby, preserving address-family related configurations under VRF context.</div>
                        <div>Refer to examples for more details.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Cisco IOS-XR Version 9.0.0
   - This module works with connection ``network_cli``.
   - See `the IOS_XR Platform Options <https://github.com/ansible-collections/cisco.iosxr/blob/main/platform_guide.rst>`_.
   - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state:
    # -------------
    #
    # RP/0/0/CPU0:iosxr-02#show running-config vrf
    # Fri Feb  9 07:02:35.789 UTC
    # !
    # vrf test
    #

    - name: Merge provided configuration with device configuration
      cisco.iosxr.iosxr_vrf_global:
        config:
          - name: VRF4
            description: VRF4 Description
            evpn_route_sync: 793
            fallback_vrf: "test-vrf"
            remote_route_filtering:
              disable: "true"
            rd: "3:4"
            mhost:
              afi: "ipv4"
              default_interface: "Loopback0"
            vpn:
              id: "2:3"
        state: merged

    # Task Output:
    # ------------
    #
    # before: []
    #
    # commands:
    # - vrf VRF4
    # - description VRF4 Description
    # - evpn-route-sync 793
    # - fallback-vrf test-vrf
    # - mhost ipv4 default-interface Loopback0
    # - rd 3:4
    # - remote-route-filtering disable
    # - vpn id 2:3
    #
    # after:
    # - name: VRF4
    #   description: VRF4 Description
    #   evpn_route_sync: 793
    #   fallback_vrf: "test-vrf"
    #   mhost:
    #     afi: "ipv4"
    #     default_interface: "Loopback0"
    #   rd: "3:4"
    #   remote_route_filtering:
    #     disable: "true"
    #   vpn:
    #     id: "2:3"
    #
    # After state:
    # ------------
    #
    # RP/0/0/CPU0:iosxr-02#show running-config vrf
    # Sat Feb 20 03:49:43.618 UTC
    # vrf VRF4
    #  description "VRF4 Description"
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 793
    #  vpn id 2:3
    #  fallback-vrf "test-vrf"
    #  remote-route-filtering disable
    #  rd "3:4"

    # Using replaced
    #
    # Before state:
    # -------------
    #
    # RP/0/0/CPU0:iosxr-02#show running-config vrf
    # Sat Feb 20 03:49:43.618 UTC
    # vrf VRF4
    #  description "VRF4 Description"
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 793
    #  vpn id 2:3
    #  fallback-vrf "test-vrf"
    #  remote-route-filtering disable
    #  rd "3:4"

    - name: Replace the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_vrf_global:
        config:
          - name: VRF7
            description: VRF7 description
            evpn_route_sync: 398
            fallback_vrf: "replaced-vrf"
            remote_route_filtering:
              disable: "true"
            rd: "67:9"
            mhost:
              afi: "ipv4"
              default_interface: "Loopback0"
            vpn:
              id: "4:5"
        state: replaced

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    #   description: VRF4 Description
    #   evpn_route_sync: 793
    #   fallback_vrf: "test-vrf"
    #   mhost:
    #     afi: "ipv4"
    #     default_interface: "Loopback0"
    #   rd: "3:4"
    #   remote_route_filtering:
    #     disable: "true"
    #   vpn:
    #     id: "2:3"
    #
    # commands:
    # - vrf VRF4
    # - no vpn id 2:3
    # - vrf VRF7
    # - description VRF7 description
    # - evpn-route-sync 398
    # - fallback-vrf replaced-vrf
    # - mhost ipv4 default-interface Loopback0
    # - rd 6:9
    # - remote-route-filtering disable
    # - vpn id 4:5
    #
    # after:
    #   - name: VRF4
    #     description: VRF4 Description
    #     evpn_route_sync: 793
    #     fallback_vrf: "test-vrf"
    #     mhost:
    #       afi: "ipv4"
    #       default_interface: "Loopback0"
    #     rd: "3:4"
    #     remote_route_filtering:
    #       disable: "true"
    #   - name: VRF7
    #     description: VRF7 description
    #     evpn_route_sync: 398
    #     fallback_vrf: "replaced-vrf"
    #     remote_route_filtering:
    #       disable: true
    #     rd: "67:9"
    #     mhost:
    #       afi: "ipv4"
    #       default_interface: "Loopback0"
    #     vpn:
    #       id: "4:5"
    #
    # After state:
    # ------------
    #
    # RP/0/RP0/CPU0:ios(config)#show running-config vrf
    # Sun Mar 10 16:48:53.204 UTC
    # vrf VRF4
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 793
    #  description VRF4 Description
    #  fallback-vrf test-vrf
    #  remote-route-filtering disable
    #  rd 3:4
    # !
    # vrf VRF7
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 398
    #  description VRF7 description
    #  vpn id 4:5
    #  fallback-vrf replaced-vrf
    #  remote-route-filtering disable
    #  rd 67:9
    #  !
    # !

    # Using overridden
    #
    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios(config)#show running-config vrf
    # Sun Mar 10 16:48:53.204 UTC
    # vrf VRF4
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 793
    #  description VRF4 Description
    #  fallback-vrf test-vrf
    #  remote-route-filtering disable
    #  rd 3:4
    #  !
    # !
    # vrf VRF7
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 398
    #  description VRF7 description
    #  vpn id 4:5
    #  fallback-vrf replaced-vrf
    #  remote-route-filtering disable
    #  rd 67:9
    #  !
    # !

    - name: Override the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_vrf_global:
        state: overridden
        config:
          - name: VRF6
            description: VRF6 Description
            evpn_route_sync: 101
            fallback_vrf: "overridden-vrf"
            remote_route_filtering:
              disable: "true"
            rd: "9:8"
            mhost:
              afi: "ipv4"
              default_interface: "Loopback0"
            vpn:
              id: "23:3"

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    #   description: VRF4 Description
    #   evpn_route_sync: 793
    #   fallback_vrf: "test-vrf"
    #   mhost:
    #     afi: "ipv4"
    #     default_interface: "Loopback0"
    #   rd: "3:4"
    #   remote_route_filtering:
    #     disable: "true"
    # - name: VRF7
    #   description: VRF7 description
    #   evpn_route_sync: 398
    #   fallback_vrf: "replaced-vrf"
    #   remote_route_filtering:
    #     disable: true
    #   rd: "67:9"
    #   mhost:
    #     afi: "ipv4"
    #     default_interface: "Loopback0"
    #   vpn:
    #     id: "4:5"
    #
    # commands:
    # - vrf VRF4
    # - no description VRF4 Description
    # - no evpn-route-sync 793
    # - no fallback-vrf test-vrf
    # - no mhost ipv4 default-interface Loopback0
    # - no rd 3:4
    # - no remote-route-filtering disable
    # - vrf VRF7
    # - no description VRF7 description
    # - no evpn-route-sync 398
    # - no fallback-vrf replaced-vrf
    # - no mhost ipv4 default-interface Loopback0
    # - no rd 67:9
    # - no remote-route-filtering disable
    # - no vpn id 4:5
    # - vrf VRF6
    # - description VRF6 Description
    # - evpn-route-sync 101
    # - fallback-vrf overridden-vrf
    # - mhost ipv4 default-interface Loopback0
    # - rd 9:8
    # - remote-route-filtering disable
    # - vpn id 23:3
    #
    # after:
    # - name: VRF4
    # - name: VRF6
    #   description: VRF6 Description
    #   evpn_route_sync: 101
    #   fallback_vrf: "overridden-vrf"
    #   remote_route_filtering:
    #     disable: "true"
    #   rd: "9:8"
    #   mhost:
    #     afi: "ipv4"
    #     default_interface: "Loopback0"
    #   vpn:
    #     id: "23:3"
    # - name: VRF7
    #
    # After state:
    # -------------
    # RP/0/RP0/CPU0:ios(config)#show running-config vrf
    # Sun Mar 10 16:54:53.007 UTC
    # vrf VRF4
    # vrf VRF6
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 101
    #  description VRF6 Description
    #  vpn id 23:3
    #  fallback-vrf overridden-vrf
    #  remote-route-filtering disable
    #  rd 9:8
    # vrf VRF7

    # Using deleted
    #
    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios(config)#show running-config vrf
    # Sun Mar 10 16:54:53.007 UTC
    # vrf VRF4
    # vrf VRF6
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 101
    #  description VRF6 Description
    #  vpn id 23:3
    #  fallback-vrf overridden-vrf
    #  remote-route-filtering disable
    #  rd 9:8
    # vrf VRF7

    - name: Delete the provided configuration
      cisco.iosxr.iosxr_vrf_global:
        config:
        state: deleted

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    # - name: VRF6
    #   description: VRF6 Description
    #   evpn_route_sync: 101
    #   fallback_vrf: "overridden-vrf"
    #   remote_route_filtering:
    #     disable: "true"
    #   rd: "9:8"
    #   mhost:
    #     afi: "ipv4"
    #     default_interface: "Loopback0"
    #   vpn:
    #     id: "23:3"
    # - name: VRF7

    # commands:
    # - vrf VRF4
    # - vrf VRF6
    # - no description VRF6 Description
    # - no evpn-route-sync 101
    # - no fallback-vrf overridden-vrf
    # - no mhost ipv4 default-interface Loopback0
    # - no rd 9:8
    # - no remote-route-filtering disable
    # - no vpn id 23:3
    # - vrf VRF7
    #
    # after:
    # - name: VRF4
    # - name: VRF6
    # - name: VRF7
    #
    # After state:
    # ------------
    #
    # RP/0/RP0/CPU0:ios(config)#show running-config vrf
    # Sun Mar 10 17:02:38.981 UTC
    # vrf VRF4
    # vrf VRF6
    # vrf VRF7

    # Using purged
    #
    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios(config)#show running-config vrf
    # vrf VRF4
    # vrf VRF6
    # vrf VRF7

    - name: Purge all the configuration from the device
      cisco.iosxr.iosxr_vrf_global:
        state: purged

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    # - name: VRF6
    # - name: VRF7
    #
    # commands:
    # - no vrf VRF4
    # - no vrf VRF6
    # - no vrf VRF7
    #
    # after: []
    #
    # After state:
    # -------------
    # RP/0/RP0/CPU0:ios(config)#show running-config vrf
    # Sun Mar 10 17:02:38.981 UTC
    # -

    # Using rendered
    #
    - name: Render provided configuration with device configuration
      cisco.iosxr.iosxr_vrf_global:
        config:
          - name: VRF4
            description: VRF4 Description
            evpn_route_sync: 793
            fallback_vrf: "test-vrf"
            remote_route_filtering:
              disable: "true"
            rd: "3:4"
            mhost:
              afi: "ipv4"
              default_interface: "Loopback0"
            vpn:
              id: "2:3"
        state: rendered

    # Task Output:
    # ------------
    #
    # rendered:
    # - vrf VRF4
    # - description VRF4 Description
    # - evpn-route-sync 793
    # - fallback-vrf test-vrf
    # - mhost ipv4 default-interface Loopback0
    # - rd 3:4
    # - remote-route-filtering disable
    # - vpn id 2:3

    # Using gathered
    #
    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios(config)#show running-config vrf
    # Sun Mar 10 17:02:38.981 UTC
    # vrf VRF4
    #  description "VRF4 Description"
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 793
    #  vpn id 2:3
    #  fallback-vrf "test-vrf"
    #  remote-route-filtering disable
    #  rd "3:4"

    - name: Gather existing running configuration
      cisco.iosxr.iosxr_vrf_global:
        state: gathered

    # Task Output:
    # ------------
    #
    # gathered:
    # - name: VRF4
    #   description: VRF4 Description
    #   evpn_route_sync: 793
    #   fallback_vrf: "test-vrf"
    #   mhost:
    #     afi: "ipv4"
    #     default_interface: "Loopback0"
    #   rd: "3:4"
    #   remote_route_filtering:
    #     disable: "true"
    #   vpn:
    #     id: "2:3"

    # Using parsed
    #
    # File: parsed.cfg
    # ----------------
    #
    # vrf test
    #  description "This is test VRF"
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 456
    #  vpn id 56
    #  fallback-vrf "test-vrf"
    #  remote-route-filtering disable
    #  rd "testing"
    #  !
    # !
    # vrf my_vrf
    #  mhost ipv4 default-interface Loopback0
    #  evpn-route-sync 235
    #  description "this is sample vrf for feature testing"
    #  fallback-vrf "parsed-vrf"
    #  rd "2:3"
    #  remote-route-filtering disable
    #  vpn id 23
    #  !
    # !

    - name: Parse the provided configuration
      cisco.iosxr.iosxr_vrf_global:
        running_config: "{{ lookup('file', 'parsed.cfg') }}"
        state: parsed

    # Task Output:
    # ------------
    #
    # parsed:
    # - description: This is test VRF
    #   evpn_route_sync: 456
    #   fallback_vrf: test-vrf
    #   mhost:
    #     afi: ipv4
    #     default_interface: Loopback0
    #   name: test
    #   rd: testing
    #   remote_route_filtering:
    #     disable: true
    #   vpn:
    #     id: '56'
    # - description: this is sample vrf for feature testing
    #   evpn_route_sync: 235
    #   fallback_vrf: parsed-vrf
    #   mhost:
    #     afi: ipv4
    #     default_interface: Loopback0
    #   name: my_vrf
    #   rd: '2:3'
    #   remote_route_filtering:
    #     disable: true
    #   vpn:
    #     id: '23'



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
                      <span style="color: purple">dictionary</span>
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
                      <span style="color: purple">dictionary</span>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;vrf VRF7&#x27;, &#x27;description VRF7 description&#x27;, {&#x27;rd&#x27;: 4029}, &#x27;fallback-vrf replaced-vrf&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>gathered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>gathered</code></td>
                <td>
                            <div>Facts about the network resource gathered from the remote device as structured data.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>parsed</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>parsed</code></td>
                <td>
                            <div>The device native config provided in <em>running_config</em> option parsed into structured data as per module argspec.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>rendered</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>when <em>state</em> is <code>rendered</code></td>
                <td>
                            <div>The provided configuration in the task rendered in device-native format (offline).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;vrf VRF4&#x27;, &#x27;description VRF4 Description&#x27;, &#x27;evpn-route-sync 793&#x27;, &#x27;fallback-vrf parsed-vrf&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ruchi Pakhle (@Ruchip16)
