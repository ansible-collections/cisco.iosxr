.. _cisco.iosxr.iosxr_l2_interfaces_module:


*******************************
cisco.iosxr.iosxr_l2_interfaces
*******************************

**L2 interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the Layer-2 interface attributes on Cisco IOS-XR devices.




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
                        <div>A dictionary of Layer-2 interface options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encapsulation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify which packets will be matched by this sub-interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dot1q</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IEEE 802.1Q VLAN-tagged packets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>second_dot1q</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IEEE 802.1Q VLAN-tagged packets.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>l2protocol</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures Layer 2 protocol tunneling and protocol data unit (PDU) filtering on an interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cdp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>drop</li>
                                    <li>forward</li>
                                    <li>tunnel</li>
                        </ul>
                </td>
                <td>
                        <div>Cisco Discovery Protocol (CDP) tunneling and data unit parameters.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cpsv</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>drop</li>
                                    <li>reverse-tunnel</li>
                                    <li>tunnel</li>
                        </ul>
                </td>
                <td>
                        <div>CDP, PVST+, STP, and VTP protocols.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pvst</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>drop</li>
                                    <li>forward</li>
                                    <li>tunnel</li>
                        </ul>
                </td>
                <td>
                        <div>Configures the per-VLAN Spanning Tree Protocol (PVST) tunneling and data unit parameters.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>drop</li>
                                    <li>forward</li>
                                    <li>tunnel</li>
                        </ul>
                </td>
                <td>
                        <div>Spanning Tree Protocol (STP) tunneling and data unit parameters.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vtp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>drop</li>
                                    <li>forward</li>
                                    <li>tunnel</li>
                        </ul>
                </td>
                <td>
                        <div>VLAN Trunk Protocol (VTP) tunneling and data unit parameters.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>l2transport</b>
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
                        <div>Switchport mode access command to configure the interface as a layer 2 access</div>
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
                        <div>Full name of the interface/sub-interface excluding any logical unit number, e.g. GigabitEthernet0/0/0/1 or GigabitEthernet0/0/0/1.100.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>native_vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a native VLAN ID for the trunk</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>propagate</b>
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
                        <div>Propagate Layer 2 transport events. Note that it will work only when the <em>l2tranport</em> option is set to TRUE</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>q_vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>802.1Q VLAN configuration. Note that it can accept either 2 VLAN IDs when configuring Q-in-Q VLAN, or it will accept 1 VLAN ID and &#x27;any&#x27; as input list when configuring Q-in-any vlan as input. Note, that this option is valid only with respect to Sub-Interface and is not valid when configuring for Interface.</div>
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
                        <div>The value of this option should be the output received from the IOS-XR device by executing the command <b>show running-config interface</b>.</div>
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
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>replaced</li>
                                    <li>overridden</li>
                                    <li>deleted</li>
                                    <li>rendered</li>
                                    <li>gathered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state of the configuration after module completion</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module works with connection ``network_cli``. See `the IOS-XR Platform Options <../network/user_guide/platform_iosxr.html>`_.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/4
    #  description Test description
    # !

    - name: Merge provided configuration with device configuration
      cisco.iosxr.iosxr_l2_interfaces:
        config:
        - name: GigabitEthernet0/0/0/3
          native_vlan: 20
        - name: GigabitEthernet0/0/0/4
          native_vlan: 40
          l2transport: true
          l2protocol:
          - stp: tunnel
        - name: GigabitEthernet0/0/0/3.900
          l2transport: true
          q_vlan:
          - 20
          - 40
        state: merged

    # After state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    #  dot1q native vlan 20
    # !
    # interface GigabitEthernet0/0/0/4
    # description Test description
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol stp tunnel
    #  !
    # !
    # interface GigabitEthernet0/0/0/3.900 l2transport
    #  dot1q vlan 20 40
    # !

    # Using replaced
    #
    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    #  dot1q native vlan 20
    # !
    # interface GigabitEthernet0/0/0/4
    # description Test description
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol stp tunnel
    #  !
    # !
    # interface GigabitEthernet0/0/0/3.900 l2transport
    #  dot1q vlan 20 40
    # !

    - name: Replaces device configuration of listed interfaces with provided configuration
      cisco.iosxr.iosxr_l2_interfaces:
        config:
        - name: GigabitEthernet0/0/0/4
          native_vlan: 40
          l2transport: true
          l2protocol:
          - stp: forward
        - name: GigabitEthernet0/0/0/3.900
          q_vlan:
          - 20
          - any
        state: replaced

    # After state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    #  dot1q native vlan 20
    # !
    # interface GigabitEthernet0/0/0/4
    # description Test description
    #  dot1q native vlan 40
    #  l2transport
    #   l2protocol stp forward
    #  !
    # !
    # interface GigabitEthernet0/0/0/3.900 l2transport
    #  dot1q vlan 20 any
    # !

    # Using overridden
    #
    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    #  dot1q native vlan 20
    # !
    # interface GigabitEthernet0/0/0/4
    # description Test description
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol stp tunnel
    #  !
    # !
    # interface GigabitEthernet0/0/0/3.900 l2transport
    #  dot1q vlan 20 40
    # !

    - name: Override device configuration of all interfaces with provided configuration
      cisco.iosxr.iosxr_l2_interfaces:
        config:
        - name: GigabitEthernet0/0/0/4
          native_vlan: 40
          l2transport: true
          l2protocol:
          - stp: forward
        - name: GigabitEthernet0/0/0/3.900
          q_vlan:
          - 20
          - any
        state: overridden

    # After state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/4
    # description Test description
    #  dot1q native vlan 40
    #  l2transport
    #   l2protocol stp forward
    #  !
    # !
    # interface GigabitEthernet0/0/0/3.900
    #  dot1q vlan 20 any
    # !

    # Using deleted
    #
    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    #  dot1q native vlan 20
    # !
    # interface GigabitEthernet0/0/0/4
    #  description Test description
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol stp tunnel
    #  !
    # !
    #

    - name: "Delete L2 attributes of given interfaces (Note: This won't delete the interface itself)"
      cisco.iosxr.iosxr_l2_interfaces:
        config:
        - name: GigabitEthernet0/0/0/4
        state: deleted

    # After state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    #  dot1q native vlan 20
    # !
    # interface GigabitEthernet0/0/0/4
    #  description Test description
    # !

    # Using Deleted without any config passed
    # "(NOTE: This will delete all of configured resource module attributes from each configured interface)"
    #
    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    #  dot1q native vlan 20
    # !
    # interface GigabitEthernet0/0/0/4
    #  description Test description
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol stp tunnel
    #  !
    # !

    - name: "Delete L2 attributes of all interfaces (Note: This won't delete the interface itself)"
      cisco.iosxr.iosxr_l2_interfaces:
        state: deleted

    # After state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/3
    #  description Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/4
    #  description Test description
    # !


    # Using parsed
    # parsed.cfg
    # ------------
    #
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 10.8.38.70 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/0
    #  description Configured and Merged by Ansible-Network
    #  mtu 110
    #  ipv4 address 172.31.1.1 255.255.255.0
    #  duplex half
    # !
    # interface GigabitEthernet0/0/0/1
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol cdp forward
    #   l2protocol pvst tunnel
    #   propagate remote-status
    #  !
    # !
    # interface GigabitEthernet0/0/0/3
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/3.900
    #  encapsulation dot1q 20 second-dot1q 40
    # !
    # interface GigabitEthernet0/0/0/4
    #  shutdown
    #  dot1q native vlan 40
    # !
    - name: Convert L2 interfaces config to argspec without connecting to the appliance
      cisco.iosxr.iosxr_l2_interfaces:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed
    # Task Output (redacted)
    # -----------------------
    # "parsed": [
    #         {
    #             "name": "GigabitEthernet0/0/0/0"
    #         },
    #         {
    #             "l2protocol": [
    #                 {
    #                     "cdp": "forward"
    #                 },
    #                 {
    #                     "pvst": "tunnel"
    #                 }
    #             ],
    #             "l2transport": true,
    #             "name": "GigabitEthernet0/0/0/1",
    #             "native_vlan": 10,
    #             "propagate": true
    #         },
    #         {
    #             "name": "GigabitEthernet0/0/0/3"
    #         },
    #         {
    #             "name": "GigabitEthernet0/0/0/3.900",
    #             "q_vlan": [
    #                 20,
    #                 40
    #             ]
    #         },
    #         {
    #             "name": "GigabitEthernet0/0/0/4",
    #             "native_vlan": 40
    #         }
    #     ]


    # Using rendered
    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_l2_interfaces:
        config:

        - name: GigabitEthernet0/0/0/1
          native_vlan: 10
          l2transport: true
          l2protocol:

          - pvst: tunnel

          - cdp: forward
          propagate: true

        - name: GigabitEthernet0/0/0/3.900
          q_vlan:
          - 20
          - 40

        - name: GigabitEthernet0/0/0/4
          native_vlan: 40
        state: rendered
    # Task Output (redacted)
    # -----------------------
    # "rendered": [
    #         "interface GigabitEthernet0/0/0/1",
    #         "dot1q native vlan 10",
    #         "l2transport l2protocol pvst tunnel",
    #         "l2transport l2protocol cdp forward",
    #         "l2transport propagate remote-status",
    #         "interface GigabitEthernet0/0/0/3.900",
    #         "dot1q vlan 20 40",
    #         "interface GigabitEthernet0/0/0/4",
    #         "dot1q native vlan 40"
    #     ]


    # Using gathered
    # Before state:
    # ------------
    #
    # RP/0/0/CPU0:an-iosxr-02#show running-config  interface
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 10.8.38.70 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/0
    #  description Configured and Merged by Ansible-Network
    #  mtu 110
    #  ipv4 address 172.31.1.1 255.255.255.0
    #  duplex half
    # !
    # interface GigabitEthernet0/0/0/1
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol cdp forward
    #   l2protocol pvst tunnel
    #   propagate remote-status
    #  !
    # !
    # interface GigabitEthernet0/0/0/3
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/3.900
    #  encapsulation dot1q 20 second-dot1q 40
    # !
    # interface GigabitEthernet0/0/0/4
    #  shutdown
    #  dot1q native vlan 40
    # !
    - name: Gather IOSXR l2 interfaces as in given arguments
      cisco.iosxr.iosxr_l2_interfaces:
        config:
        state: gathered
    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": [
    #         {
    #             "name": "GigabitEthernet0/0/0/0"
    #         },
    #         {
    #             "l2protocol": [
    #                 {
    #                     "cdp": "forward"
    #                 },
    #                 {
    #                     "pvst": "tunnel"
    #                 }
    #             ],
    #             "l2transport": true,
    #             "name": "GigabitEthernet0/0/0/1",
    #             "native_vlan": 10,
    #             "propagate": true
    #         },
    #         {
    #             "name": "GigabitEthernet0/0/0/3"
    #         },
    #         {
    #             "name": "GigabitEthernet0/0/0/3.900",
    #             "q_vlan": [
    #                 20,
    #                 40
    #             ]
    #         },
    #         {
    #             "name": "GigabitEthernet0/0/0/4",
    #             "native_vlan": 40
    #         }
    #     ]
    # After state:
    # ------------
    #
    # RP/0/0/CPU0:an-iosxr-02#show running-config  interface
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 10.8.38.70 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/0
    #  description Configured and Merged by Ansible-Network
    #  mtu 110
    #  ipv4 address 172.31.1.1 255.255.255.0
    #  duplex half
    # !
    # interface GigabitEthernet0/0/0/1
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol cdp forward
    #   l2protocol pvst tunnel
    #   propagate remote-status
    #  !
    # !
    # interface GigabitEthernet0/0/0/3
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/3.900
    #  encapsulation dot1q 20 second-dot1q 40
    # !
    # interface GigabitEthernet0/0/0/4
    #  shutdown
    #  dot1q native vlan 40
    # !



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
                            <div>The configuration as structured data after module completion.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
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
                            <div>The configuration as structured data prior to module invocation.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">The configuration returned will always be in the same format of the parameters above.</div>
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
                            <div>The set of commands pushed to the remote device</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface GigabitEthernet0/0/0/2&#x27;, &#x27;l2transport l2protocol pvst tunnel&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Sumit Jaiswal (@justjais)
- Rohit Thakur (@rohitthakur2590)
