.. _cisco.iosxr.iosxr_lldp_interfaces_module:


*********************************
cisco.iosxr.iosxr_lldp_interfaces
*********************************

**Resource module to configure LLDP interfaces.**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages Link Layer Discovery Protocol (LLDP) attributes of interfaces on IOS-XR devices.




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
                        <div>A dictionary of LLDP interfaces options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>destination</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies LLDP destination configuration on the interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ieee-nearest-bridge</li>
                                    <li>ieee-nearest-non-tmpr-bridge</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the LLDP destination mac address on the interface.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name/Identifier of the interface or Ether-Bundle.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>receive</b>
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
                        <div>Enable/disable LLDP RX on an interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transmit</b>
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
                        <div>Enable/disable LLDP TX on an interface.</div>
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
    #
    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 12:40:23.104 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    # !
    #
    #

    - name: Merge provided configuration with running configuration
      cisco.iosxr.iosxr_lldp_interfaces:
        config:
          - name: GigabitEthernet0/0/0/1
            destination:
              mac_address: ieee-nearest-non-tmpr-bridge
            transmit: false
          - name: GigabitEthernet0/0/0/2
            destination:
              mac_address: ieee-nearest-bridge
            receive: false
        state: merged


    #
    #
    # ------------------------
    # Module Execution Result
    # ------------------------
    #
    #
    # "before": [
    #        {
    #            "name": "TenGigE0/0/0/0"
    #        },
    #        {
    #            "name": "GigabitEthernet0/0/0/1"
    #        },
    #        {
    #            "name": "GigabitEthernet0/0/0/2"
    #        }
    # ]
    #
    # "commands": [
    #        "interface GigabitEthernet0/0/0/2",
    #        "lldp destination mac-address ieee-nearest-non-tmpr-bridge",
    #        "lldp transmit disable",
    #        "interface GigabitEthernet0/0/0/1",
    #        "lldp receive disable",
    #        "lldp destination mac-address ieee-nearest-bridge"
    # ]
    #
    # "after": [
    #        {
    #            "name": "TenGigE0/0/0/0"
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/1",
    #            "receive": false
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-non-tmpr-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/2",
    #            "transmit": false
    #        }
    # ]
    #
    #
    # ------------
    # After state
    # ------------
    #
    #
    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 12:49:51.517 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  lldp
    #   receive disable
    #   destination mac-address
    #    ieee-nearest-bridge
    #   !
    #  !
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  lldp
    #   transmit disable
    #   destination mac-address
    #    ieee-nearest-non-tmpr-bridge
    #   !
    #  !
    # !
    #
    #


    # Using replaced
    #
    #
    # -------------
    # Before state
    # -------------
    #
    #
    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 12:49:51.517 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  lldp
    #   receive disable
    #   destination mac-address
    #    ieee-nearest-bridge
    #   !
    #  !
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  lldp
    #   transmit disable
    #   destination mac-address
    #    ieee-nearest-non-tmpr-bridge
    #   !
    #  !
    # !
    #
    #

    - name: >-
        Replace existing LLDP configurations of specified interfaces with provided
        configuration
      cisco.iosxr.iosxr_lldp_interfaces:
        config:
          - name: GigabitEthernet0/0/0/1
            destination:
              mac_address: ieee-nearest-non-tmpr-bridge
        state: replaced


    #
    #
    # ------------------------
    # Module Execution Result
    # ------------------------
    #
    # "before": [
    #        {
    #            "name": "TenGigE0/0/0/0"
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/1",
    #            "receive": false
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-non-tmpr-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/2",
    #            "transmit": false
    #        }
    # ]
    #
    #
    # "commands": [
    #        "interface GigabitEthernet0/0/0/1",
    #        "no lldp receive disable",
    #        "lldp destination mac-address ieee-nearest-non-tmpr-bridge"
    # ]
    #
    #
    # "after": [
    #        {
    #            "name": "TenGigE0/0/0/0"
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-non-tmpr-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/1"
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-non-tmpr-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/2",
    #            "transmit": false
    #        }
    # ]
    #
    #
    # ------------
    # After state
    # ------------
    #
    #
    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 13:02:57.062 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  lldp
    #   destination mac-address
    #    ieee-nearest-non-tmpr-bridge
    #   !
    #  !
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  lldp
    #   transmit disable
    #   destination mac-address
    #    ieee-nearest-non-tmpr-bridge
    #   !
    #  !
    # !
    #
    #


    # Using overridden
    #
    #
    # -------------
    # Before state
    # -------------
    #
    #
    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 13:15:40.465 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  lldp
    #   receive disable
    #   destination mac-address
    #    ieee-nearest-bridge
    #   !
    #  !
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  lldp
    #   transmit disable
    #   destination mac-address
    #    ieee-nearest-non-tmpr-bridge
    #   !
    #  !
    # !
    #
    #

    - name: >-
        Override the LLDP configurations of all the interfaces with provided
        configurations
      cisco.iosxr.iosxr_lldp_interfaces:
        config:
          - name: GigabitEthernet0/0/0/1
            transmit: false
        state: overridden


    #
    #
    # ------------------------
    # Module Execution Result
    # ------------------------
    #
    #
    # "before": [
    #        {
    #            "name": "TenGigE0/0/0/0"
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/1",
    #            "receive": false
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-non-tmpr-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/2",
    #            "transmit": false
    #        }
    # ]
    #
    # "commands": [
    #        "interface GigabitEthernet0/0/0/2",
    #        "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
    #        "no lldp transmit disable",
    #        "interface GigabitEthernet0/0/0/1",
    #        "no lldp destination mac-address ieee-nearest-bridge",
    #        "no lldp receive disable",
    #        "lldp transmit disable"
    # ]
    #
    #
    # "after": [
    #        {
    #            "name": "TenGigE0/0/0/0"
    #        },
    #        {
    #            "name": "GigabitEthernet0/0/0/1",
    #            "transmit": false
    #        },
    #        {
    #            "name": "GigabitEthernet0/0/0/2"
    #        }
    # ]
    #
    #
    # ------------
    # After state
    # ------------
    #
    #
    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 13:22:25.604 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  lldp
    #   transmit disable
    #  !
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    # !
    #
    #


    # Using deleted
    #
    #
    # -------------
    # Before state
    # -------------
    #
    #
    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 13:26:21.498 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  lldp
    #   receive disable
    #   destination mac-address
    #    ieee-nearest-bridge
    #   !
    #  !
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  lldp
    #   transmit disable
    #   destination mac-address
    #    ieee-nearest-non-tmpr-bridge
    #   !
    #  !
    # !
    #
    #

    - name: Delete LLDP configurations of all interfaces (Note - This won't delete the
        interfaces themselves)
      cisco.iosxr.iosxr_lldp_interfaces:
        state: deleted

    #
    #
    #
    # ------------------------
    # Module Execution Result
    # ------------------------
    #
    #
    # "before": [
    #        {
    #            "name": "TenGigE0/0/0/0"
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/1",
    #            "receive": false
    #        },
    #        {
    #            "destination": {
    #                "mac_address": "ieee-nearest-non-tmpr-bridge"
    #            },
    #            "name": "GigabitEthernet0/0/0/2",
    #            "transmit": false
    #        }
    # ]
    #
    #
    # "commands": [
    #        "interface GigabitEthernet0/0/0/1",
    #        "no lldp destination mac-address ieee-nearest-bridge",
    #        "no lldp receive disable",
    #        "interface GigabitEthernet0/0/0/2",
    #        "no lldp destination mac-address ieee-nearest-non-tmpr-bridge",
    #        "no lldp transmit disable"
    # ]
    #
    #
    # "after": [
    #        {
    #            "name": "TenGigE0/0/0/0"
    #        },
    #        {
    #            "name": "GigabitEthernet0/0/0/1"
    #        },
    #        {
    #            "name": "GigabitEthernet0/0/0/2"
    #        }
    # ]
    #
    #
    # ------------
    # After state
    # ------------
    #
    #
    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 13:30:14.618 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    # !
    #
    #
    # Using parsed:
    # parsed.cfg

    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  lldp
    #   receive disable
    #   destination mac-address
    #    ieee-nearest-bridge
    #   !
    #  !
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  lldp
    #   transmit disable
    #   destination mac-address
    #    ieee-nearest-non-tmpr-bridge

    - name: Convert lacp interfaces config to argspec without connecting to the appliance
      cisco.iosxr.iosxr_lldp_interfaces:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # ------------------------
    # Module Execution Result
    # ------------------------

    # parsed: [
    #   - name: GigabitEthernet0/0/0/1
    #       destination:
    #         mac_address: ieee-nearest-non-tmpr-bridge
    #       transmit: False

    #     - name: GigabitEthernet0/0/0/2
    #       destination:
    #         mac_address: ieee-nearest-bridge
    #       receive: False
    #   ]

    # Using gathered:
    # Device config:

    # RP/0/RP0/CPU0:ios#sh run int
    # Mon Aug 12 12:49:51.517 UTC
    # interface TenGigE0/0/0/0
    #  ipv4 address 192.0.2.11 255.255.255.192
    # !
    # interface preconfigure GigabitEthernet0/0/0/1
    #  lldp
    #   receive disable
    #   destination mac-address
    #    ieee-nearest-bridge
    #   !
    #  !
    # !
    # interface preconfigure GigabitEthernet0/0/0/2
    #  lldp
    #   transmit disable
    #   destination mac-address
    #    ieee-nearest-non-tmpr-bridge

    - name: Gather IOSXR lldp interfaces configuration
      cisco.iosxr.iosxr_lldp_interfaces:
        config:
        state: gathered

    # ------------------------
    # Module Execution Result
    # ------------------------

    #   gathered:
    #     - name: GigabitEthernet0/0/0/1
    #       destination:
    #         mac_address: ieee-nearest-non-tmpr-bridge
    #       transmit: False

    #     - name: GigabitEthernet0/0/0/2
    #       destination:
    #         mac_address: ieee-nearest-bridge
    #       receive: False

    # Using rendred:
    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_lldp_interfaces:
        config:
          - name: GigabitEthernet0/0/0/1
            destination:
              mac_address: ieee-nearest-non-tmpr-bridge
            transmit: false
          - name: GigabitEthernet0/0/0/2
            destination:
              mac_address: ieee-nearest-bridge
            receive: false
        state: rendered
    # ------------------------
    # Module Execution Result
    # ------------------------

    # "rendered": [
    #        "interface GigabitEthernet0/0/0/2",
    #        "lldp destination mac-address ieee-nearest-non-tmpr-bridge",
    #        "lldp transmit disable",
    #        "interface GigabitEthernet0/0/0/1",
    #        "lldp receive disable",
    #        "lldp destination mac-address ieee-nearest-bridge"
    # ]



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface GigabitEthernet0/0/0/1&#x27;, &#x27;lldp destination mac-address ieee-nearest-non-tmpr-bridge&#x27;, &#x27;no lldp transmit disable&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nilashish Chakraborty (@nilashishc)
