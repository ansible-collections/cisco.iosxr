.. _cisco.iosxr.iosxr_vrf_interfaces_module:


********************************
cisco.iosxr.iosxr_vrf_interfaces
********************************

**Resource module to configure VRF interfaces.**


Version added: 10.3.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages the VRF configuration in interface on IOS XR platforms.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
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
                        <div>A list of VRF interfaces options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
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
                        <div>Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/0/0/1.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Vrf that is to be added to the interface.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
                        <div>The value of this option should be the output received from the IOS device by executing the command <b>sh running-config interface</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
                        <div>The state the configuration should be left in</div>
                        <div>The states <em>rendered</em>, <em>gathered</em> and <em>parsed</em> does not perform any change on the device.</div>
                        <div>The state <em>rendered</em> will transform the configuration in <code>config</code> option to platform specific CLI commands which will be returned in the <em>rendered</em> key within the result. For state <em>rendered</em> active connection to remote host is not required.</div>
                        <div>The state <em>gathered</em> will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into JSON format as per the resource module parameters and the value is returned in the <em>parsed</em> key within the result. The value of <code>running_config</code> option should be the same format as the output of command <em>show running-config | include ip route|ipv6 route</em> executed on device. For state <em>parsed</em> active connection to remote host is not required.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Cisco IOS-XR 7.2.2.
   - This module works with connection ``network_cli``.



Examples
--------

.. code-block:: yaml

    # Using merged

    # Before state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  shutdown
    # !

    - name: Simple merge selective
      cisco.iosxr.iosxr_vrf_interfaces:
        state: merged
        config:
          - name: MgmtEth0/RP0/CPU0/0
          - name: GigabitEthernet0/0/0/0
          - name: GigabitEthernet0/0/0/1
            vrf_name: vrf_C
          - name: GigabitEthernet0/0/0/2
            vrf_name: vrf_D

    # Task Output
    # -----------
    #
    # before:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #   - name: GigabitEthernet0/0/0/2
    # commands:
    #   - interface GigabitEthernet0/0/0/1
    #   - vrf vrf_C
    #   - interface GigabitEthernet0/0/0/2
    #   - vrf vrf_D
    # after:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #     vrf_name: vrf_C
    #   - name: GigabitEthernet0/0/0/2
    #     vrf_name: vrf_D

    # After state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  vrf vrf_C
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf vrf_D
    #  shutdown
    # !

    # Using replaced

    # Before state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  vrf vrf_C
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf vrf_D
    #  shutdown
    # !

    - name: Simple replaced selective
      cisco.iosxr.iosxr_vrf_interfaces:
        state: replaced
        config:
          - name: MgmtEth0/RP0/CPU0/0
          - name: GigabitEthernet0/0/0/0
          - name: GigabitEthernet0/0/0/1
            vrf_name: vrf_E
          - name: GigabitEthernet0/0/0/2
            vrf_name: vrf_D

    # Task Output
    # -----------
    #
    # before:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #     vrf_name: vrf_C
    #   - name: GigabitEthernet0/0/0/2
    #     vrf_name: vrf_D
    # commands:
    #   - interface GigabitEthernet0/0/0/1
    #   - vrf vrf_E
    # after:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #     vrf_name: vrf_E
    #   - name: GigabitEthernet0/0/0/2
    #     vrf_name: vrf_D

    # After state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  vrf vrf_E
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf vrf_D
    #  shutdown
    # !

    # Using overridden

    # Before state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  vrf vrf_C
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf vrf_D
    #  shutdown
    # !

    - name: Simple overridden selective
      cisco.iosxr.iosxr_vrf_interfaces:
        state: overridden
        config:
          - name: MgmtEth0/RP0/CPU0/0
          - name: GigabitEthernet0/0/0/0
          - name: GigabitEthernet0/0/0/1
            vrf_name: vrf_E

    # Task Output
    # -----------
    #
    # before:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #     vrf_name: vrf_C
    #   - name: GigabitEthernet0/0/0/2
    #     vrf_name: vrf_D
    # commands:
    #   - interface GigabitEthernet0/0/0/1
    #   - vrf vrf_E
    #   - interface GigabitEthernet0/0/0/2
    #   - no vrf vrf_E
    # after:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #     vrf_name: vrf_E
    #   - name: GigabitEthernet0/0/0/2

    # After state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  vrf vrf_E
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  shutdown
    # !

    # Using deleted

    # Before state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  vrf vrf_E
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf vrf_D
    #  shutdown
    # !

    - name: Simple deleted selective
      cisco.iosxr.iosxr_vrf_interfaces:
        state: deleted
        config:
          - name: GigabitEthernet0/0/0/1
            vrf_name: vrf_E

    # Task Output
    # -----------
    #
    # before:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #     vrf_name: vrf_E
    #   - name: GigabitEthernet0/0/0/2
    #     vrf_name: vrf_D
    # commands:
    #   - interface GigabitEthernet0/0/0/1
    #   - no vrf vrf_E
    # after:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #   - name: GigabitEthernet0/0/0/2
    #     vrf_name: vrf_D

    # After state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf vrf_D
    #  shutdown
    # !

    # Using gathered

    # Before state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  vrf vrf_C
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf vrf_D
    #  shutdown
    # !

    - name: Simple gathered selective
      cisco.iosxr.iosxr_vrf_interfaces:
        state: gathered

    # Task Output
    # -----------
    #
    # gathered:
    #   - name: MgmtEth0/RP0/CPU0/0
    #   - name: GigabitEthernet0/0/0/0
    #   - name: GigabitEthernet0/0/0/1
    #     vrf_name: vrf_C
    #   - name: GigabitEthernet0/0/0/2
    #     vrf_name: vrf_D

    # Using rendered

    # Before state:
    # -------------
    #
    # viosxr#show running-config interfaces
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  description this is interface0
    #  cdp
    # !
    # interface GigabitEthernet0/0/0/1
    #  vrf vrf_C
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf vrf_D
    #  shutdown
    # !

    - name: Simple rendered selective
      cisco.iosxr.iosxr_vrf_interfaces:
        state: rendered

    # Task Output
    # -----------
    #
    # commands:
    #   - interface GigabitEthernet0/0/0/1
    #   - vrf vrf_C
    #   - interface GigabitEthernet0/0/0/2
    #   - vrf vrf_D



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
                            <div>The resulting configuration after module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
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
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The configuration prior to the module execution.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">This output will always be in the same format as the module argspec.</div>
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
                <td>when <em>state</em> is <code>merged</code>, <code>replaced</code>, <code>overridden</code>, <code>deleted</code> or <code>purged</code></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface GigabitEthernet0/0/0/1&#x27;, &#x27;no vrf test_vrf1&#x27;, &#x27;vrf test_vrf2&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface GigabitEthernet0/0/0/1&#x27;, &#x27;no vrf test_vrf1&#x27;, &#x27;vrf test_vrf2&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Sagar Paul (@KB-perByte)
