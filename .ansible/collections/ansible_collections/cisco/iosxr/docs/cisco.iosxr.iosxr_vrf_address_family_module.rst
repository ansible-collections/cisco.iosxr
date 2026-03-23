.. _cisco.iosxr.iosxr_vrf_address_family_module:


************************************
cisco.iosxr.iosxr_vrf_address_family
************************************

**Resource module to configure VRF Address family.**


Version added: 10.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages the attributes of VRF address family on Cisco IOS-XR devices.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="6">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="6">
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
                        <div>VRF address family configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
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
                        <div>Enable address family and enter its config mode - AFI/SAFI configuration</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>export</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRF export</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use route_policy for export</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_target</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify export route target extended communities.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>to</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Export routes to a VRF</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Export routes to default VRF</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use route_policy for export</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Export routes to a VRF</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>allow_imported_vpn</b>
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
                        <div>Allow export of imported VPN routes to non-default VRF</div>
                </td>
            </tr>



            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>import_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRF import</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>from_config</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Import routes from a VRF</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bridge_domain</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VRF import</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_as_vpn</b>
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
                        <div>Advertise local EVPN imported routes to PEs</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>default_vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Export routes to default VRF</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use route_policy for export</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Import routes from a VRF</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advertise_as_vpn</b>
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
                        <div>Advertise local EVPN imported routes to PEs</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use route_policy for export</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>route_target</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify export route target extended communities.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maximum</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set maximum prefix limit</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set table&#x27;s maximum prefix limit.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>safi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>flowspec</li>
                                    <li>multicast</li>
                                    <li>unicast</li>
                        </ul>
                </td>
                <td>
                        <div>Address Family modifier</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="5">
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
                <td colspan="6">
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
                <td colspan="6">
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
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The states <em>rendered</em>, <em>gathered</em> and <em>parsed</em> does not perform any change on the device.</div>
                        <div>The state <em>rendered</em> will transform the configuration in <code>config</code> option to platform specific CLI commands which will be returned in the <em>rendered</em> key within the result. For state <em>rendered</em> active connection to remote host is not required.</div>
                        <div>The state <em>gathered</em> will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into JSON format as per the resource module parameters and the value is returned in the <em>parsed</em> key within the result. The value of <code>running_config</code> option should be the same format as the output of command <em>show running-config vrf</em>. connection to remote host is not required.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Cisco IOSXR Version 10.0.0
   - This module works with connection ``network_cli``. See `the IOS_XR Platform Options <../network/user_guide/platform_iosxr.html>`_
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
   - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <https://www.ansible.com/integrations/networks/cisco>`.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state:
    # -------------
    #
    # RP/0/0/CPU0:iosxr#show running-config vrf
    # vrf test
    #

    - name: Merge provided configuration with device configuration
      cisco.iosxr.iosxr_vrf_address_family:
        config:
          - name: VRF4
            address_families:
              - afi: "ipv4"
                safi: "unicast"
                export:
                  route_target: "192.0.2.1:400"
                  route_policy: "rm-policy"
                  to:
                    default_vrf:
                      route_policy: "rm-policy"
                    vrf:
                      allow_imported_vpn: true
                import_config:
                  route_target: "192.0.2.6:200"
                  route_policy: "test-policy"
                  from_config:
                    bridge_domain:
                      advertise_as_vpn: true
                    default_vrf:
                      route_policy: "test-policy"
                    vrf:
                      advertise_as_vpn: true
                maximum:
                  prefix: 100
        state: merged

    # Task Output:
    # ------------
    #
    # before: []
    #
    # commands:
    # - vrf VRF4
    # - address-family ipv4 unicast
    # - export route-policy rm-policy
    # - export route-target 192.0.2.1:400
    # - export to default-vrf route-policy rm-policy
    # - export to vrf allow-imported-vpn
    # - import route-target 192.0.2.6:200
    # - import route-policy test-policy
    # - import from bridge-domain advertise-as-vpn
    # - import from default-vrf route-policy test-policy
    # - import from vrf advertise-as-vpn
    # - maximum prefix 100
    #
    # after:
    # - name: VRF4
    #   address_families:
    #     - afi: "ipv4"
    #       safi: "unicast"
    #       export:
    #         route_target: "192.0.2.1:400"
    #         route_policy: "rm-policy"
    #         to:
    #           default_vrf:
    #             route_policy: "rm-policy"
    #           vrf:
    #             allow_imported_vpn: true
    #       import_config:
    #         route_target: "192.0.2.6:200"
    #         route_policy: "test-policy"
    #         from_config:
    #           bridge_domain:
    #             advertise_as_vpn: true
    #           default_vrf:
    #             route_policy: "test-policy"
    #           vrf:
    #             advertise_as_vpn: true
    #       maximum:
    #         prefix: 100
    #
    # After state:
    # ------------
    #
    # RP/0/0/CPU0:iosxr#show running-config vrf
    # vrf VRF4
    #  address-family ipv4 unicast
    #   export route-policy rm-policy
    #   export route-target 192.0.2.1:400
    #   export to default-vrf route-policy rm-policy
    #   export to vrf allow-imported-vpn
    #   import route-target 192.0.2.6:200
    #   import route-policy test-policy
    #   import from bridge-domain advertise-as-vpn
    #   import from default-vrf route-policy test-policy
    #   import from vrf advertise-as-vpn
    #   maximum prefix 100

    # Using replaced
    #
    # Before state:
    # -------------
    #
    # RP/0/0/CPU0:iosxr#show running-config vrf
    # vrf VRF4
    #  address-family ipv4 unicast
    #   export route-policy rm-policy
    #   export route-target 192.0.2.1:400
    #   export to default-vrf route-policy rm-policy
    #   export to vrf allow-imported-vpn
    #   import route-target 192.0.2.6:200
    #   import route-policy test-policy
    #   import from bridge-domain advertise-as-vpn
    #   import from default-vrf route-policy test-policy
    #   import from vrf advertise-as-vpn
    #   maximum prefix 100

    - name: Replace the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_vrf_address_family:
        config:
          - name: VRF7
            address_families:
              - afi: "ipv4"
                safi: "unicast"
                export:
                  route_target: "192.0.2.2:400"
                  route_policy: "rm-policy"
                  to:
                    default_vrf:
                      route_policy: "rm-policy"
                    vrf:
                      allow_imported_vpn: true
                import_config:
                  route_target: "192.0.2.4:400"
                  route_policy: "test-policy"
                  from_config:
                    bridge_domain:
                      advertise_as_vpn: true
                    default_vrf:
                      route_policy: "test-policy"
                    vrf:
                      advertise_as_vpn: true
                maximum:
                  prefix: 200
        state: replaced

    # Task Output:
    # ------------
    #
    # - name: VRF4
    #   address_families:
    #     - afi: "ipv4"
    #       safi: "unicast"
    #       export:
    #         route_target: "192.0.2.1:400"
    #         route_policy: "rm-policy"
    #         to:
    #           default_vrf:
    #             route_policy: "rm-policy"
    #           vrf:
    #             allow_imported_vpn: true
    #       import_config:
    #         route_target: "192.0.2.6:200"
    #         route_policy: "test-policy"
    #         from_config:
    #           bridge_domain:
    #             advertise_as_vpn: true
    #           default_vrf:
    #             route_policy: "test-policy"
    #           vrf:
    #             advertise_as_vpn: true
    #       maximum:
    #         prefix: 100
    #
    # commands:
    # - vrf VRF7
    # - address-family ipv4 unicast
    # - export route-policy rm-policy
    # - export route-target 192.0.2.2:400
    # - export to default-vrf route-policy rm-policy
    # - export to vrf allow-imported-vpn
    # - import route-target 192.0.2.4:400
    # - import route-policy test-policy
    # - import from bridge-domain advertise-as-vpn
    # - import from default-vrf route-policy test-policy
    # - import from vrf advertise-as-vpn
    # - maximum prefix 200
    #
    # after:
    # - name: VRF7
    #   address_families:
    #     - afi: "ipv4"
    #       safi: "unicast"
    #       export:
    #         route_target: "192.0.2.2:400"
    #         route_policy: "rm-policy"
    #         to:
    #           default_vrf:
    #             route_policy: "rm-policy"
    #           vrf:
    #             allow_imported_vpn: true
    #       import_config:
    #         route_target: "192.0.2.4:400"
    #         route_policy: "test-policy"
    #         from_config:
    #           bridge_domain:
    #             advertise_as_vpn: true
    #           default_vrf:
    #             route_policy: "test-policy"
    #           vrf:
    #             advertise_as_vpn: true
    #       maximum:
    #         prefix: 200
    #
    # After state:
    # ------------
    #
    # RP/0/RP0/CPU0:iosxr(config)#show running-config vrf
    # vrf VRF7
    #  address-family ipv4 unicast
    #   import route-policy test-policy
    #   import from bridge-domain advertise-as-vpn
    #   import from default-vrf route-policy test-policy
    #   import from vrf advertise-as-vpn
    #   import route-target
    #    192.0.2.4:400
    #   !
    #   export route-policy rm-policy
    #   export to vrf allow-imported-vpn
    #   export to default-vrf route-policy rm-policy
    #   export route-target
    #    192.0.2.2:400
    #   !
    #   maximum prefix 200

    # Using overridden
    #
    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:iosxr(config)#show running-config vrf
    # vrf VRF7
    #  address-family ipv4 unicast
    #   import route-policy test-policy
    #   import from bridge-domain advertise-as-vpn
    #   import from default-vrf route-policy test-policy
    #   import from vrf advertise-as-vpn
    #   import route-target
    #    192.0.2.4:400
    #   !
    #   export route-policy rm-policy
    #   export to vrf allow-imported-vpn
    #   export to default-vrf route-policy rm-policy
    #   export route-target
    #    192.0.2.2:400
    #   !
    #   maximum prefix 200

    - name: Override the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_vrf_address_family:
        state: overridden
        config:
          - name: VRF6
            address_families:
              - afi: "ipv4"
                safi: "unicast"
                export:
                  route_target: "192.0.2.8:200"
                  route_policy: "rm-policy1"
                  to:
                    default_vrf:
                      route_policy: "rm-policy"
                    vrf:
                      allow_imported_vpn: "true"
                import_config:
                  route_target: "192.0.2.2:200"
                  route_policy: "test-policy"
                  from_config:
                    bridge_domain:
                      advertise_as_vpn: "true"
                    default_vrf:
                      route_policy: "test-policy"
                    vrf:
                      advertise_as_vpn: "true"
                maximum:
                  prefix: 500
    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF7
    #   address_families:
    #     - afi: "ipv4"
    #       safi: "unicast"
    #       export:
    #         route_target: "192.0.2.2:400"
    #         route_policy: "rm-policy"
    #         to:
    #           default_vrf:
    #             route_policy: "rm-policy"
    #           vrf:
    #             allow_imported_vpn: true
    #       import_config:
    #         route_target: "192.0.2.4:400"
    #         route_policy: "test-policy"
    #         from_config:
    #           bridge_domain:
    #             advertise_as_vpn: true
    #           default_vrf:
    #             route_policy: "test-policy"
    #           vrf:
    #             advertise_as_vpn: true
    #       maximum:
    #         prefix: 200
    #
    # commands:
    # - vrf VRF7
    # - address-family ipv4 unicast
    # - no import route-policy test-policy
    # - no import from bridge-domain advertise-as-vpn
    # - no import from default-vrf route-policy test-policy
    # - no import from vrf advertise-as-vpn
    # - no import route-target 192.0.2.4:400
    # - no export route-policy rm-policy
    # - no export route-target 192.0.2.2:400
    # - no export to default-vrf route-policy rm-policy
    # - no export to vrf allow-imported-vpn
    # - no maximum prefix 200
    # - vrf VRF6
    # - address-family ipv4 unicast
    # - export route-policy rm-policy1
    # - export route-target 192.0.2.8:200
    # - export to default-vrf route-policy rm-policy
    # - export to vrf allow-imported-vpn
    # - import route-target 192.0.2.2:200
    # - import route-policy test-policy
    # - import from bridge-domain advertise-as-vpn
    # - import from default-vrf route-policy test-policy
    # - import from vrf advertise-as-vpn
    # - maximum prefix 500
    #
    # after:
    # - name: VRF4
    # - name: VRF6
    #   address_families:
    #     - afi: "ipv4"
    #       safi: "unicast"
    #       export:
    #         route_target: "192.0.2.8:200"
    #         route_policy: "rm-policy1"
    #         to:
    #           default_vrf:
    #             route_policy: "rm-policy"
    #           vrf:
    #             allow_imported_vpn: "true"
    #       import_config:
    #         route_target: "192.0.2.2:200"
    #         route_policy: "test-policy"
    #         from_config:
    #           bridge_domain:
    #             advertise_as_vpn: "true"
    #           default_vrf:
    #             route_policy: "test-policy"
    #           vrf:
    #             advertise_as_vpn: "true"
    #       maximum:
    #         prefix: 500
    # - name: VRF7
    #
    # After state:
    # -------------
    # RP/0/RP0/CPU0:iosxr(config)#show running-config vrf
    # vrf VRF4
    # vrf VRF6
    #  address-family ipv4 unicast
    #   import route-policy test-policy
    #   import from bridge-domain advertise-as-vpn
    #   import from default-vrf route-policy test-policy
    #   import from vrf advertise-as-vpn
    #   import route-target
    #    192.0.2.2:200
    #   export route-policy rm-policy1
    #   export to vrf allow-imported-vpn
    #   export to default-vrf route-policy rm-policy
    #   export route-target
    #    192.0.2.8:200
    #   maximum prefix 500
    # vrf VRF7

    # Using deleted
    #
    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:iosxr(config)#show running-config vrf
    # vrf VRF4
    # vrf VRF6
    #  address-family ipv4 unicast
    #   import route-policy test-policy
    #   import from bridge-domain advertise-as-vpn
    #   import from default-vrf route-policy test-policy
    #   import from vrf advertise-as-vpn
    #   import route-target
    #    192.0.2.2:200
    #   export route-policy rm-policy1
    #   export to vrf allow-imported-vpn
    #   export to default-vrf route-policy rm-policy
    #   export route-target
    #    192.0.2.8:200
    #   maximum prefix 500
    # vrf VRF7

    - name: Delete the provided configuration
      cisco.iosxr.iosxr_vrf_address_family:
        config:
        state: deleted

    # Task Output:
    # ------------
    #
    # before:
    # - name: VRF4
    # - name: VRF6
    #   address_families:
    #     - afi: "ipv4"
    #       safi: "unicast"
    #       export:
    #         route_target: "192.0.2.8:200"
    #         route_policy: "rm-policy1"
    #         to:
    #           default_vrf:
    #             route_policy: "rm-policy"
    #           vrf:
    #             allow_imported_vpn: "true"
    #       import_config:
    #         route_target: "192.0.2.2:200"
    #         route_policy: "test-policy"
    #         from_config:
    #           bridge_domain:
    #             advertise_as_vpn: "true"
    #           default_vrf:
    #             route_policy: "test-policy"
    #           vrf:
    #             advertise_as_vpn: "true"
    #       maximum:
    #         prefix: 500
    # - name: VRF7

    # commands:
    # - vrf VRF4
    # - vrf VRF6
    # - no address-family ipv4 unicast
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
    # RP/0/RP0/CPU0:iosxr(config)#show running-config vrf
    # vrf VRF4
    # vrf VRF6
    # vrf VRF7

    # Using rendered
    #
    - name: Render provided configuration with device configuration
      cisco.iosxr.iosxr_vrf_address_family:
        config:
          - name: VRF4
            address_families:
              - afi: "ipv4"
                safi: "unicast"
                export:
                  route_target: "192.0.2.1:400"
                  route_policy: "rm-policy"
                  to:
                    default_vrf:
                      route_policy: "rm-policy"
                    vrf:
                      allow_imported_vpn: true
                import_config:
                  route_target: "192.0.2.6:200"
                  route_policy: "test-policy"
                  from_config:
                    bridge_domain:
                      advertise_as_vpn: true
                    default_vrf:
                      route_policy: "test-policy"
                    vrf:
                      advertise_as_vpn: true
                maximum:
                  prefix: 100
        state: rendered

    # Task Output:
    # ------------
    #
    # rendered:
    # - vrf VRF4
    # - address-family ipv4 unicast
    # - export route-policy rm-policy
    # - export route-target 192.0.2.1:400
    # - export to default-vrf route-policy rm-policy
    # - export to vrf allow-imported-vpn
    # - import route-target 192.0.2.6:200
    # - import route-policy test-policy
    # - import from bridge-domain advertise-as-vpn
    # - import from default-vrf route-policy test-policy
    # - import from vrf advertise-as-vpn
    # - maximum prefix 100

    # Using gathered
    #
    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:iosxr(config)#show running-config vrf
    # vrf VRF4
    #  address-family ipv4 unicast
    #   export route-policy rm-policy
    #   export route-target 192.0.2.1:400
    #   export to default-vrf route-policy rm-policy
    #   export to vrf allow-imported-vpn
    #   import route-target 192.0.2.6:200
    #   import route-policy test-policy
    #   import from bridge-domain advertise-as-vpn
    #   import from default-vrf route-policy test-policy
    #   import from vrf advertise-as-vpn
    #   maximum prefix 100

    - name: Gather existing running configuration
      cisco.iosxr.iosxr_vrf_address_family:
        state: gathered

    # Task Output:
    # ------------
    #
    # gathered:
    # - name: VRF4
    #   address_families:
    #     - afi: "ipv4"
    #       safi: "unicast"
    #       export:
    #         route_target: "192.0.2.1:400"
    #         route_policy: "rm-policy"
    #         to:
    #           default_vrf:
    #             route_policy: "rm-policy"
    #           vrf:
    #             allow_imported_vpn: true
    #       import_config:
    #         route_target: "192.0.2.6:200"
    #         route_policy: "test-policy"
    #         from_config:
    #           bridge_domain:
    #             advertise_as_vpn: true
    #           default_vrf:
    #             route_policy: "test-policy"
    #           vrf:
    #             advertise_as_vpn: true
    #       maximum:
    #         prefix: 100

    # Using parsed
    #
    # File: parsed.cfg
    # ----------------
    #
    # vrf test
    #  address-family ipv4 unicast
    #   export to default-vrf route-policy "rm-policy"
    #   export to vrf allow-imported-vpn
    #   export route-policy "export-policy"
    #   export route-target
    #    192.0.2.1:400
    #   import route-target
    #    192.0.2.2:200
    #   import route-policy "test-policy"
    #   import from bridge-domain advertise-as-vpn
    #   import from default-vrf route-policy "new-policy"
    #   import from vrf advertise-as-vpn
    #   maximum prefix 23

    - name: Parse the provided configuration
      cisco.iosxr.iosxr_vrf_address_family:
        running_config: "{{ lookup('file', 'parsed.cfg') }}"
        state: parsed

    # Task Output:
    # ------------
    #
    # parsed:
    #   - address_families:
    #     - afi: ipv4
    #       export:
    #         route_policy: export-policy
    #         route_target: 192.0.2.1:400
    #         to:
    #           default_vrf:
    #             route_policy: rm-policy
    #           vrf:
    #             allow_imported_vpn: true
    #       import_config:
    #         from_config:
    #           bridge_domain:
    #             advertise_as_vpn: true
    #           default_vrf:
    #             route_policy: new-policy
    #           vrf:
    #             advertise_as_vpn: true
    #         route_policy: test-policy
    #         route_target: 192.0.2.2:200
    #       maximum:
    #         prefix: 23
    #       safi: unicast
    #     name: test



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;vrf VRF7&#x27;, &#x27;address-family ipv4 unicast&#x27;, &#x27;export route-policy rm-policy&#x27;, &#x27;import route-policy test-policy&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;vrf VRF4&#x27;, &#x27;address-family ipv4 unicast&#x27;, &#x27;export route-policy rm-policy&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ruchi Pakhle (@Ruchip16)
