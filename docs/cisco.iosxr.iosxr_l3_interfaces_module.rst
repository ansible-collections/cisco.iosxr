.. _cisco.iosxr.iosxr_l3_interfaces_module:


*******************************
cisco.iosxr.iosxr_l3_interfaces
*******************************

**Resource module to configure L3 interfaces.**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module provides declarative management of Layer-3 interface on Cisco IOS-XR devices.




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
                        <div>A dictionary of Layer-3 interface options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv4 address to be set for the Layer-3 interface mentioned in <em>name</em> option.</div>
                        <div>The address format is &lt;ipv4 address&gt;/&lt;mask&gt;, the mask is number in range 0-32 eg. 192.168.0.1/24</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures the IPv4 address for Interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>secondary</b>
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
                        <div>Configures the IP address as a secondary address.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IPv6 address to be set for the Layer-3 interface mentioned in <em>name</em> option.</div>
                        <div>The address format is &lt;ipv6 address&gt;/&lt;mask&gt;, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures the IPv6 address for Interface.</div>
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
                        <div>Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1.</div>
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
                                    <li>parsed</li>
                                    <li>rendered</li>
                                    <li>gathered</li>
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

    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    # !

    - name: Merge provided configuration with device configuration
      cisco.iosxr.iosxr_l3_interfaces:
        config:
          - name: GigabitEthernet0/0/0/2
            ipv4:
              - address: 192.168.0.1/24
          - name: GigabitEthernet0/0/0/3
            ipv4:
              - address: 192.168.2.1/24
                secondary: true
        state: merged

    # Task Output
    # -----------
    #
    # before:
    # - name: Loopback888
    # - name: Loopback999
    # - name: GigabitEthernet0/0/0/2
    # - name: GigabitEthernet0/0/0/3
    # commands:
    # - interface GigabitEthernet0/0/0/2
    # - ipv4 address 192.168.0.1 255.255.255.0
    # - interface GigabitEthernet0/0/0/3
    # - ipv4 address 192.168.2.1 255.255.255.0 secondary
    # after:
    # - name: Loopback888
    # - name: Loopback999
    # - ipv4:
    #   - address: 192.168.0.1/24
    #   name: GigabitEthernet0/0/0/2
    # - ipv4:
    #   - address: 192.168.2.1/24
    #     secondary: true
    #   name: GigabitEthernet0/0/0/3

    # After state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  ipv4 address 192.168.0.1 255.255.255.0
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    #  ipv4 address 192.168.2.1 255.255.255.0 secondary
    # !

    # Using overridden

    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  ipv4 address 192.168.0.1 255.255.255.0
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    #  ipv4 address 192.168.2.1 255.255.255.0 secondary
    # !

    - name: Override device configuration of all interfaces with provided configuration
      cisco.iosxr.iosxr_l3_interfaces:
        config:
          - name: GigabitEthernet0/0/0/3
            ipv4:
              - address: 192.168.0.2/24
              - address: 192.168.2.1/24
                secondary: true
        state: overridden


    # Task Output
    # -----------
    #
    # before:
    # - name: Loopback888
    # - name: Loopback999
    # - ipv4:
    #   - address: 192.168.0.1/24
    #   name: GigabitEthernet0/0/0/2
    # - ipv4:
    #   - address: 192.168.2.1/24
    #     secondary: true
    #   name: GigabitEthernet0/0/0/3
    # commands:
    # - interface GigabitEthernet0/0/0/2
    # - no ipv4 address
    # - interface GigabitEthernet0/0/0/3
    # - ipv4 address 192.168.0.2 255.255.255.0
    # - ipv4 address 192.168.0.1 255.255.255.0
    # after:
    # - name: Loopback888
    # - name: Loopback999
    # - name: GigabitEthernet0/0/0/2
    # - ipv4:
    #   - address: 192.168.0.1/24
    #   - address: 192.168.2.1/24
    #     secondary: true
    #   name: GigabitEthernet0/0/0/3

    # After state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    #  ipv4 address 192.168.0.1 255.255.255.0
    #  ipv4 address 192.168.2.1 255.255.255.0 secondary
    # !

    # Using replaced

    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    #  ipv4 address 192.168.0.1 255.255.255.0
    #  ipv4 address 192.168.2.1 255.255.255.0 secondary
    # !

    - name: >-
        Replaces device configuration of listed interfaces with provided
        configuration
      cisco.iosxr.iosxr_l3_interfaces:
        config:
          - name: GigabitEthernet0/0/0/3
            ipv6:
              - address: 'fd5d:12c9:2201:1::1/64'
          - name: GigabitEthernet0/0/0/2
            ipv4:
              - address: 192.168.0.2/24
        state: replaced


    # Task Output
    # -----------
    #
    # before:
    # - name: Loopback888
    # - name: Loopback999
    # - name: GigabitEthernet0/0/0/2
    # - ipv4:
    #   - address: 192.168.0.1/24
    #   - address: 192.168.2.1/24
    #     secondary: true
    #   name: GigabitEthernet0/0/0/3
    # commands:
    # - interface GigabitEthernet0/0/0/3
    # - no ipv4 address
    # - ipv6 address fd5d:12c9:2201:1::1/64
    # - interface GigabitEthernet0/0/0/2
    # - ipv4 address 192.168.0.2 255.255.255.0
    # after:
    # - name: Loopback888
    # - name: Loopback999
    # - ipv4:
    #   - address: 192.168.0.2/24
    #   name: GigabitEthernet0/0/0/2
    # - ipv6:
    #   - address: fd5d:12c9:2201:1::1/64
    #   name: GigabitEthernet0/0/0/3

    # After state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  ipv4 address 192.168.0.2 255.255.255.0
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    #  ipv6 address fd5d:12c9:2201:1::1/64
    # !

    # Using deleted

    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  ipv4 address 192.168.0.2 255.255.255.0
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    #  ipv6 address fd5d:12c9:2201:1::1/64
    # !

    - name: Delete attributes for interfaces (This won't delete the interface itself)
      cisco.iosxr.iosxr_l3_interfaces:
        config:
          - name: GigabitEthernet0/0/0/3
          - name: GigabitEthernet0/0/0/4
          - name: GigabitEthernet0/0/0/3.700
        state: deleted


    # Task Output
    # -----------
    #
    # before:
    # - name: Loopback888
    # - name: Loopback999
    # - ipv4:
    #   - address: 192.168.0.2/24
    #   name: GigabitEthernet0/0/0/2
    # - ipv6:
    #   - address: fd5d:12c9:2201:1::1/64
    #   name: GigabitEthernet0/0/0/3
    # commands:
    # - interface GigabitEthernet0/0/0/3
    # - no ipv6 address
    # after:
    # - name: Loopback888
    # - name: Loopback999
    # - ipv4:
    #   - address: 192.168.0.2/24
    #   name: GigabitEthernet0/0/0/2
    # - name: GigabitEthernet0/0/0/3

    # After state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  ipv4 address 192.168.0.2 255.255.255.0
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    # !

    # Using deleted - will delete all interface configuration and not interface

    # Before state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  ipv4 address 192.168.2.1 255.255.255.0
    #  shutdown
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  ipv4 address 192.168.3.1 255.255.255.0
    #  shutdown
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    #  ipv4 address 192.168.0.2 255.255.255.0
    #  shutdown
    # !
    # interface preconfigure GigabitEthernet0/0/0/3.700
    #  ipv4 address 192.168.0.1 255.255.255.0
    # !
    # interface preconfigure GigabitEthernet0/0/0/4
    #  ipv6 address fd5d:12c9:2201:1::1/64
    #  shutdown
    # !

    - name: "Delete L3 config of all interfaces (This won't delete the interface itself)"
      cisco.iosxr.iosxr_l3_interfaces:
        state: deleted

    # Task Output
    # -----------
    #
    # before:
    # - name: Loopback888
    # - name: Loopback999
    # - ipv4:
    #   - address: 192.168.2.1/24
    #   name: GigabitEthernet0/0/0/1
    # - ipv4:
    #   - address: 192.168.3.1/24
    #   name: GigabitEthernet0/0/0/2
    # - ipv4:
    #   - address: 192.168.0.2/24
    #   name: GigabitEthernet0/0/0/3
    # - ipv4:
    #   - address: 192.168.0.1/24
    #   name: GigabitEthernet0/0/0/3.700
    # - ipv6:
    #   - address: fd5d:12c9:2201:1::1/64
    #   name: GigabitEthernet0/0/0/4
    # commands:
    # - interface GigabitEthernet0/0/0/1
    # - no ipv4 address
    # - interface GigabitEthernet0/0/0/2
    # - no ipv4 address
    # - interface GigabitEthernet0/0/0/3
    # - no ipv4 address
    # - interface GigabitEthernet0/0/0/3.700
    # - no ipv4 address
    # - interface GigabitEthernet0/0/0/4
    # - no ipv6 address
    # after:
    # - name: Loopback888
    # - name: Loopback999
    # - name: GigabitEthernet0/0/0/1
    # - name: GigabitEthernet0/0/0/2
    # - name: GigabitEthernet0/0/0/3
    # - name: GigabitEthernet0/0/0/3.700
    # - name: GigabitEthernet0/0/0/4

    # After state:
    # -------------
    #
    # viosxr#show running-config interface
    # interface Loopback888
    # !
    # interface Loopback999
    # !
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  shutdown
    # !
    # interface preconfigure GigabitEthernet0/0/0/3
    #  shutdown
    # !
    # interface preconfigure GigabitEthernet0/0/0/3.700
    # !
    # interface preconfigure GigabitEthernet0/0/0/4
    #  shutdown
    # !


    # Using parsed

    # File: parsed.cfg
    # ----------------
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
    #  mtu 66
    #  ipv4 address 192.0.2.1 255.255.255.0
    #  ipv4 address 192.0.2.2 255.255.255.0 secondary
    #  ipv6 address 2001:db8:0:3::/64
    #  duplex half
    # !
    # interface GigabitEthernet0/0/0/1
    #  description Configured and Merged by Ansible-Network
    #  mtu 66
    #  speed 100
    #  duplex full
    #  dot1q native vlan 10
    #  l2transport
    #   l2protocol cdp forward
    #   l2protocol pvst tunnel
    #   propagate remote-status
    #  !
    # !
    # interface GigabitEthernet0/0/0/3
    #  ipv4 address 192.0.22.1 255.255.255.0
    #  ipv4 address 192.0.23.1 255.255.255.0
    # !

    - name: Convert L3 interfaces config to argspec without connecting to the appliance
      cisco.iosxr.iosxr_l3_interfaces:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # Task Output
    # -----------
    #
    # parsed:
    # - ipv4:
    #   - address: 192.0.2.1 255.255.255.0
    #   - address: 192.0.2.2 255.255.255.0
    #     secondary: true
    #   ipv6:
    #   - address: 2001:db8:0:3::/64
    #   name: GigabitEthernet0/0/0/0
    # - name: GigabitEthernet0/0/0/1
    # - ipv4:
    #   - address: 192.0.22.1 255.255.255.0
    #   - address: 192.0.23.1 255.255.255.0
    #   name: GigabitEthernet0/0/0/3

    # Using rendered

    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_l3_interfaces:
        config:
          - name: GigabitEthernet0/0/0/0
            ipv4:
              - address: 198.51.100.1/24
          - name: GigabitEthernet0/0/0/1
            ipv6:
              - address: '2001:db8:0:3::/64'
            ipv4:
              - address: 192.0.2.1/24
              - address: 192.0.2.2/24
                secondary: true
        state: rendered


    # Task Output
    # -----------
    #
    # rendered:
    # - interface GigabitEthernet0/0/0/0
    # - ipv4 address 198.51.100.1 255.255.255.0
    # - interface GigabitEthernet0/0/0/1
    # - ipv4 address 192.0.2.2 255.255.255.0 secondary
    # - ipv4 address 192.0.2.1 255.255.255.0
    # - ipv6 address 2001:db8:0:3::/64

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
    #  mtu 66
    #  ipv4 address 192.0.2.1 255.255.255.0
    #  ipv4 address 192.0.2.2 255.255.255.0 secondary
    #  ipv6 address 2001:db8:0:3::/64
    #  duplex half
    # !
    # interface GigabitEthernet0/0/0/1
    #  description Configured and Merged by Ansible-Network
    #  mtu 66
    #  speed 100
    #  duplex full
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
    # interface GigabitEthernet0/0/0/4
    #  shutdown
    #  dot1q native vlan 40
    # !

    - name: Gather l3 interfaces facts
      cisco.iosxr.iosxr_l3_interfaces:
        config:
        state: gathered

    # Task Output
    # -----------
    #
    # gathered:
    # - name: Loopback888
    # - ipv4:
    #   - address: 192.0.2.1 255.255.255.0
    #   - address: 192.0.2.2 255.255.255.0
    #     secondary: true
    #   ipv6:
    #   - address: 2001:db8:0:3::/64
    #   name: GigabitEthernet0/0/0/0
    # - name: GigabitEthernet0/0/0/1
    # - name: GigabitEthernet0/0/0/3
    # - name: GigabitEthernet0/0/0/4



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface GigabitEthernet0/0/0/1&#x27;, &#x27;ipv4 address 192.168.0.1 255.255.255.0&#x27;]</div>
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
