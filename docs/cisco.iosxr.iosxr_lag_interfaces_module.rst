.. _cisco.iosxr.iosxr_lag_interfaces_module:


********************************
cisco.iosxr.iosxr_lag_interfaces
********************************

**LAG interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the attributes of LAG/Ether-Bundle interfaces on IOS-XR devices.




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
                        <div>A provided Link Aggregation Group (LAG) configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>links</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This dict contains configurable options related to LAG/Ether-Bundle links.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_active</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the limit on the number of links that can be active in the LAG/Ether-Bundle.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>min_active</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the minimum number of active links needed to bring up the LAG/Ether-Bundle.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_balancing_hash</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>dst-ip</li>
                                    <li>src-ip</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the hash function used for traffic forwarded over the LAG/Ether-Bundle.</div>
                        <div>Option &#x27;dst-ip&#x27; uses the destination IP as the hash function.</div>
                        <div>Option &#x27;src-ip&#x27; uses the source IP as the hash function.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>members</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of member interfaces for the LAG/Ether-Bundle.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>member</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the member interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>on</li>
                                    <li>active</li>
                                    <li>passive</li>
                                    <li>inherit</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the mode of the operation for the member interface.</div>
                        <div>Mode &#x27;active&#x27; runs LACP in active mode.</div>
                        <div>Mode &#x27;on&#x27; does not run LACP over the port.</div>
                        <div>Mode &#x27;passive&#x27; runs LACP in passive mode over the port.</div>
                        <div>Mode &#x27;inherit&#x27; runs LACP as configured in the bundle.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>on</li>
                                    <li>active</li>
                                    <li>passive</li>
                        </ul>
                </td>
                <td>
                        <div>LAG mode.</div>
                        <div>Mode &#x27;active&#x27; runs LACP in active mode over the port.</div>
                        <div>Mode &#x27;on&#x27; does not run LACP over the port.</div>
                        <div>Mode &#x27;passive&#x27; runs LACP in passive mode over the port.</div>
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
                        <div>Name/Identifier of the LAG/Ether-Bundle to configure.</div>
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
                        <div>The value of this option should be the output received from the IOS-XR device by executing the command <b>show running-config int</b>.</div>
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
                        <div>The state of the configuration after module completion.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against IOS-XR 6.1.3.
   - This module works with connection ``network_cli``. See `the IOS-XR Platform Options <../network/user_guide/platform_iosxr.html>`_.



Examples
--------

.. code-block:: yaml

    # Using merged
    #
    #
    # ------------
    # Before state
    # ------------
    #
    # RP/0/0/CPU0:iosxr01#show run int
    # Sun Jul  7 19:42:59.416 UTC
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description "GigabitEthernet - 1"
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    # !
    #
    #
    - name: Merge provided configuration with device configuration
      cisco.iosxr.iosxr_lag_interfaces:
        config:
        - name: Bundle-Ether10
          members:
          - member: GigabitEthernet0/0/0/1
            mode: inherit
          - member: GigabitEthernet0/0/0/3
            mode: inherit
          mode: active
          links:
            max_active: 5
            min_active: 2
          load_balancing_hash: src-ip

        - name: Bundle-Ether12
          members:
          - member: GigabitEthernet0/0/0/2
            mode: passive
          - member: GigabitEthernet0/0/0/4
            mode: passive
          load_balancing_hash: dst-ip
        state: merged
    #
    #
    # -----------
    # After state
    # -----------
    #
    # RP/0/0/CPU0:iosxr01#show run int
    # Sun Jul  7 20:51:17.685 UTC
    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash src-ip
    #  bundle maximum-active links 5
    #  bundle minimum-active links 2
    # !
    # interface Bundle-Ether12
    #  bundle load-balancing hash dst-ip
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #   bundle id 12 mode passive
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    #  bundle id 12 mode passive
    # !
    #


    # Using replaced
    #
    #
    # -------------
    # Before state
    # -------------
    #
    #
    # RP/0/0/CPU0:iosxr01#sho run int
    # Sun Jul  7 20:58:06.527 UTC
    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash src-ip
    #  bundle maximum-active links 5
    #  bundle minimum-active links 2
    # !
    # interface Bundle-Ether12
    #  bundle load-balancing hash dst-ip
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #  bundle id 12 mode passive
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    #  bundle id 12 mode passive
    # !
    #
    #
    - name: Replace device configuration of listed Bundles with provided configurations
      cisco.iosxr.iosxr_lag_interfaces:
        config:
        - name: Bundle-Ether12
          members:
          - name: GigabitEthernet0/0/0/2
          mode: passive

        - name: Bundle-Ether11
          members:
          - name: GigabitEthernet0/0/0/4
          load_balancing_hash: src-ip
        state: replaced
    #
    #
    # -----------
    # After state
    # -----------
    #
    #
    # RP/0/0/CPU0:iosxr01#sh run int
    # Sun Jul  7 21:22:27.397 UTC
    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash src-ip
    #  bundle maximum-active links 5
    #  bundle minimum-active links 2
    # !
    # interface Bundle-Ether11
    #  bundle load-balancing hash src-ip
    # !
    # interface Bundle-Ether12
    #  lacp mode passive
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #  bundle id 12 mode on
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    #  bundle id 11 mode on
    # !
    #
    #


    # Using overridden
    #
    #
    # ------------
    # Before state
    # ------------
    #
    #
    # RP/0/0/CPU0:iosxr01#sh run int
    # Sun Jul  7 21:22:27.397 UTC
    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash src-ip
    #  bundle maximum-active links 5
    #  bundle minimum-active links 2
    # !
    # interface Bundle-Ether11
    #  bundle load-balancing hash src-ip
    # !
    # interface Bundle-Ether12
    #  lacp mode passive
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #  bundle id 12 mode on
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    #  bundle id 11 mode on
    # !
    #
    #

    - name: Overrides all device configuration with provided configuration
      cisco.iosxr.iosxr_lag_interfaces:
        config:
        - name: Bundle-Ether10
          members:
          - member: GigabitEthernet0/0/0/1
            mode: inherit
          - member: GigabitEthernet0/0/0/2
            mode: inherit
          mode: active
          load_balancing_hash: dst-ip
        state: overridden
    #
    #
    # ------------
    # After state
    # ------------
    #
    #
    # RP/0/0/CPU0:iosxr01#sh run int
    # Sun Jul  7 21:43:04.802 UTC
    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash dst-ip
    # !
    # interface Bundle-Ether11
    # !
    # interface Bundle-Ether12
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    # !
    #
    #


    # Using deleted
    #
    #
    # ------------
    # Before state
    # ------------
    #
    # RP/0/0/CPU0:iosxr01#sh run int
    # Sun Jul  7 21:22:27.397 UTC
    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash src-ip
    #  bundle maximum-active links 5
    #  bundle minimum-active links 2
    # !
    # interface Bundle-Ether11
    #  bundle load-balancing hash src-ip
    # !
    # interface Bundle-Ether12
    #  lacp mode passive
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #  bundle id 12 mode on
    # !n
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    #  bundle id 11 mode on
    # !
    #
    #

    - name: Delete attributes of given bundles and removes member interfaces from them
        (Note - This won't delete the bundles themselves)
      cisco.iosxr.iosxr_lag_interfaces:
        config:
        - name: Bundle-Ether10
        - name: Bundle-Ether11
        - name: Bundle-Ether12
        state: deleted

    #
    #
    # ------------
    # After state
    # ------------
    #
    # RP/0/0/CPU0:iosxr01#sh run int
    # Sun Jul  7 21:49:50.004 UTC
    # interface Bundle-Ether10
    # !
    # interface Bundle-Ether11
    # !
    # interface Bundle-Ether12
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    # !
    #
    #

    # Using deleted (without config)
    #
    #
    # ------------
    # Before state
    # ------------
    #
    # RP/0/0/CPU0:an-iosxr#sh run int
    # Sun Aug 18 19:49:51.908 UTC
    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash src-ip
    #  bundle maximum-active links 10
    #  bundle minimum-active links 2
    # !
    # interface Bundle-Ether11
    #  bundle load-balancing hash dst-ip
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/1
    #  bundle id 10 mode inherit
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  bundle id 10 mode passive
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/3
    #  bundle id 11 mode passive
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/4
    #  bundle id 11 mode passive
    #  shutdown
    # !
    #

    - name: Delete attributes of all bundles and removes member interfaces from them (Note
        - This won't delete the bundles themselves)
      cisco.iosxr.iosxr_lag_interfaces:
        state: deleted

    #
    #
    # ------------
    # After state
    # ------------
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh run int
    # Sun Aug 18 19:54:22.389 UTC
    # interface Bundle-Ether10
    # !
    # interface Bundle-Ether11
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 10.8.38.69 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/3
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/4
    #  shutdown
    # !

    # Using parsed:

    # parsed.cfg

    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash src-ip
    #  bundle maximum-active links 5
    #  bundle minimum-active links 2
    # !
    # interface Bundle-Ether12
    #  bundle load-balancing hash dst-ip
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #   bundle id 12 mode passive
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    #  bundle id 12 mode passive
    # !
    #
    - name: Convert lag interfaces config to argspec without connecting to the appliance
      cisco.iosxr.iosxr_lag_interfaces:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # --------------
    # Output
    # --------------
    #   parsed:
    #     - name: Bundle-Ether10
    #       members:
    #         - member: GigabitEthernet0/0/0/1
    #           mode: inherit
    #         - member: GigabitEthernet0/0/0/3
    #           mode: inherit
    #       mode: active
    #       links:
    #         max_active: 5
    #         min_active: 2
    #       load_balancing_hash: src-ip

    #     - name: Bundle-Ether12
    #       members:
    #         - member: GigabitEthernet0/0/0/2
    #           mode: passive
    #         - member: GigabitEthernet0/0/0/4
    #           mode: passive
    #       load_balancing_hash: dst-ip

    # using gathered

    # Device Config:
    # -------------

    # interface Bundle-Ether10
    #  lacp mode active
    #  bundle load-balancing hash src-ip
    #  bundle maximum-active links 5
    #  bundle minimum-active links 2
    # !
    # interface Bundle-Ether12
    #  bundle load-balancing hash dst-ip
    # !
    # interface Loopback888
    #  description test for ansible
    #  shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  description 'GigabitEthernet - 1"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #   bundle id 12 mode passive
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    #  bundle id 10 mode inherit
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    #  bundle id 12 mode passive
    # !
    #

    - name: Gather IOSXR lag interfaces configuration
      cisco.iosxr.iosxr_lag_interfaces:
        config:
        state: gathered

    # --------------
    # Output
    # --------------
    #   gathered:
    #     - name: Bundle-Ether10
    #       members:
    #         - member: GigabitEthernet0/0/0/1
    #           mode: inherit
    #         - member: GigabitEthernet0/0/0/3
    #           mode: inherit
    #       mode: active
    #       links:
    #         max_active: 5
    #         min_active: 2
    #       load_balancing_hash: src-ip

    #     - name: Bundle-Ether12
    #       members:
    #         - member: GigabitEthernet0/0/0/2
    #           mode: passive
    #         - member: GigabitEthernet0/0/0/4
    #           mode: passive
    #       load_balancing_hash: dst-ip

    # Using rendered:
    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_lag_interfaces:
        config:
        - name: Bundle-Ether10
          members:
          - member: GigabitEthernet0/0/0/1
            mode: inherit
          - member: GigabitEthernet0/0/0/3
            mode: inherit
          mode: active
          links:
            max_active: 5
            min_active: 2
          load_balancing_hash: src-ip

        - name: Bundle-Ether12
          members:
          - member: GigabitEthernet0/0/0/2
            mode: passive
          - member: GigabitEthernet0/0/0/4
            mode: passive
          load_balancing_hash: dst-ip
        state: rendered

    # Output:

    # rendered:
    #    [
    #         - "interface Bundle-Ether10"
    #         - " lacp mode active"
    #         - " bundle load-balancing hash src-ip"
    #         - " bundle maximum-active links 5"
    #         - " bundle minimum-active links 2"
    #         - "interface Bundle-Ether12"
    #         - " bundle load-balancing hash dst-ip"
    #         - "interface Loopback888"
    #         - " description test for ansible"
    #         - " shutdown"
    #         - "interface MgmtEth0/0/CPU0/0"
    #         - " ipv4 address 192.0.2.11 255.255.255.0"
    #         - "interface GigabitEthernet0/0/0/1"
    #         - " description 'GigabitEthernet - 1""
    #         - " bundle id 10 mode inherit"
    #         - "interface GigabitEthernet0/0/0/2"
    #         - " description "GigabitEthernet - 2""
    #         - "  bundle id 12 mode passive"
    #         - "interface GigabitEthernet0/0/0/3"
    #         - " description "GigabitEthernet - 3""
    #         - " bundle id 10 mode inherit"
    #         - "interface GigabitEthernet0/0/0/4"
    #         - " description "GigabitEthernet - 4""
    #         - " bundle id 12 mode passive"
    #    ]
    #
    #



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
                            <div>The configuration as structured data prior to module invocation.</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface Bundle-Ether10&#x27;, &#x27;bundle minimum-active links 2&#x27;, &#x27;bundle load-balancing hash src-ip&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nilashish Chakraborty (@NilashishC)
