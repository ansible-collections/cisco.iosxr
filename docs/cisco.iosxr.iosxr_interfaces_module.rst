.. _cisco.iosxr.iosxr_interfaces_module:


****************************
cisco.iosxr.iosxr_interfaces
****************************

**Interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the interface attributes on Cisco IOS-XR network devices.




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
                        <div>A dictionary of interface options</div>
                </td>
            </tr>
                                <tr>
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
                        <div>Interface description.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>duplex</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>full</li>
                                    <li>half</li>
                        </ul>
                </td>
                <td>
                        <div>Configures the interface duplex mode. Default is auto-negotiation when not configured.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Administrative state of the interface.</div>
                        <div>Set the value to <code>True</code> to administratively enable the interface or <code>False</code> to disable it.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mtu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Sets the MTU value for the interface. Applicable for Ethernet interfaces only.</div>
                        <div>Refer to vendor documentation for valid values.</div>
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
                        <div>Full name of the interface to configure in <code>type + path</code> format. e.g. <code>GigabitEthernet0/0/0/0</code></div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the speed for an interface. Default is auto-negotiation when not configured.</div>
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
                        <div>The value of this option should be the output received from the IOS-XR device by executing the command <b>show running-config interface</b>.</div>
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
                                    <li>parsed</li>
                                    <li>deleted</li>
                                    <li>replaced</li>
                                    <li>rendered</li>
                                    <li>gathered</li>
                                    <li>overridden</li>
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
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf custB
    #  ipv4 address 178.18.169.23 255.255.255.0
    #  dot1q native vlan 30
    # !
    # interface GigabitEthernet0/0/0/3
    #  description Replaced by Ansible Team
    #  mtu 2000
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  dot1q native vlan 1021
    # !
    - name: Configure Ethernet interfaces
      cisco.iosxr.iosxr_interfaces:
        config:
        - name: GigabitEthernet0/0/0/2
          description: Configured by Ansible
          enabled: true
        - name: GigabitEthernet0/0/0/3
          description: Configured by Ansible Network
          enabled: false
          duplex: full
        state: merged
    # After state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  description Configured and Merged by Ansible Network
    #  vrf custB
    #  ipv4 address 178.18.169.23 255.255.255.0
    #  dot1q native vlan 30
    # !
    # interface GigabitEthernet0/0/0/3
    #  description Configured and Merged by Ansible Network
    #  mtu 2600
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex full
    #  shutdown
    #  dot1q native vlan 1021
    # !
    # Using replaced
    # Before state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/1
    #  description Configured by Ansible
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  description Test
    #  vrf custB
    #  ipv4 address 178.18.169.23 255.255.255.0
    #  dot1q native vlan 30
    # !
    # interface GigabitEthernet0/0/0/3
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  dot1q native vlan 1021
    # !
    - name: Configure following interfaces and replace their existing config
      cisco.iosxr.iosxr_interfaces:
        config:
        - name: GigabitEthernet0/0/0/2
          description: Configured by Ansible
          enabled: true
          mtu: 2000
        - name: GigabitEthernet0/0/0/3
          description: Configured by Ansible Network
          enabled: false
          duplex: auto
        state: replaced
    # After state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/1
    #  description Configured by Ansible
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  description Configured and Replaced by Ansible
    #  mtu 2000
    #  vrf custB
    #  ipv4 address 178.18.169.23 255.255.255.0
    #  dot1q native vlan 30
    # !
    # interface GigabitEthernet0/0/0/3
    #  description Configured and Replaced by Ansible Network
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex half
    #  shutdown
    #  dot1q native vlan 1021
    # !
    # Using overridden
    # Before state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  description Configured by Ansible
    #  vrf custB
    #  ipv4 address 178.18.169.23 255.255.255.0
    #  dot1q native vlan 30
    # !
    # interface GigabitEthernet0/0/0/3
    #  description Configured by Ansible
    #  mtu 2600
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex full
    #  shutdown
    #  dot1q native vlan 1021
    # !
    - name: Override interfaces
      cisco.iosxr.iosxr_interfaces:
        config:
        - name: GigabitEthernet0/0/0/2
          description: Configured by Ansible
          enabled: true
          duplex: auto
        - name: GigabitEthernet0/0/0/3
          description: Configured by Ansible Network
          enabled: false
          speed: 1000
        state: overridden
    # After state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  description Configured and Overridden by Ansible Network
    #  vrf custB
    #  ipv4 address 178.18.169.23 255.255.255.0
    #  speed 1000
    #  dot1q native vlan 30
    # !
    # interface GigabitEthernet0/0/0/3
    #  description Configured and Overridden by Ansible Network
    #  mtu 2000
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex full
    #  shutdown
    #  dot1q native vlan 1021
    # !
    # Using deleted
    # Before state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  description Configured and Overridden by Ansible Network
    #  vrf custB
    #  ipv4 address 178.18.169.23 255.255.255.0
    #  speed 1000
    #  dot1q native vlan 30
    # !
    # interface GigabitEthernet0/0/0/3
    #  description Configured and Overridden by Ansible Network
    #  mtu 2000
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  duplex full
    #  shutdown
    #  dot1q native vlan 1021
    # !
    - name: Delete IOSXR interfaces as in given arguments
      cisco.iosxr.iosxr_interfaces:
        config:
        - name: GigabitEthernet0/0/0/2
        - name: GigabitEthernet0/0/0/3
        state: deleted
    # After state:
    # ------------
    #
    # viosxr#show running-config interface
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/2
    #  vrf custB
    #  ipv4 address 178.18.169.23 255.255.255.0
    #  dot1q native vlan 30
    # !
    # interface GigabitEthernet0/0/0/3
    #  vrf custB
    #  ipv4 address 10.10.0.2 255.255.255.0
    #  dot1q native vlan 1021
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
    # interface GigabitEthernet0/0/0/3
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/4
    #  shutdown
    # !
    # - name: Convert ACL interfaces config to argspec without connecting to the appliance
    #   cisco.iosxr.iosxr_interfaces:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed
    # Task Output (redacted)
    # -----------------------
    # "parsed": [
    #        {
    #            "name": "MgmtEth0/RP0/CPU0/0"
    #        },
    #        {
    #            "access_groups": [
    #                {
    #                    "acls": [
    #                        {
    #                            "direction": "in",
    #                            "name": "acl_1"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "acl_2"
    #                        }
    #                    ],
    #                    "afi": "ipv4"
    #                },
    #                {
    #                    "acls": [
    #                        {
    #                            "direction": "in",
    #                            "name": "acl6_1"
    #                        },
    #                        {
    #                            "direction": "out",
    #                            "name": "acl6_2"
    #                        }
    #                    ],
    #                    "afi": "ipv6"
    #                }
    #            ],
    #            "name": "GigabitEthernet0/0/0/0"
    #        },
    #        {
    #            "access_groups": [
    #                {
    #                    "acls": [
    #                        {
    #                            "direction": "out",
    #                            "name": "acl_1"
    #                        }
    #                    ],
    #                    "afi": "ipv4"
    #                }
    #            ],
    #            "name": "GigabitEthernet0/0/0/1"
    #        }
    #    ]
    # }
    # Using rendered
    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_interfaces:
        config:
        - name: GigabitEthernet0/0/0/0
          description: Configured and Merged by Ansible-Network
          mtu: 110
          enabled: true
          duplex: half
        - name: GigabitEthernet0/0/0/1
          description: Configured and Merged by Ansible-Network
          mtu: 2800
          enabled: false
          speed: 100
          duplex: full
        state: rendered
    # Task Output (redacted)
    # -----------------------
    # "rendered": [
    #         "interface GigabitEthernet0/0/0/0",
    #         "description Configured and Merged by Ansible-Network",
    #         "mtu 110",
    #         "duplex half",
    #         "no shutdown",
    #         "interface GigabitEthernet0/0/0/1",
    #         "description Configured and Merged by Ansible-Network",
    #         "mtu 2800",
    #         "speed 100",
    #         "duplex full",
    #         "shutdown"
    #     ]
    # Using gathered
    # Before state:
    # ------------
    #
    # RP/0/0/CPU0:an-iosxr-02#show running-config  interface
    # interface Loopback888
    # description test for ansible
    # shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    # ipv4 address 10.8.38.70 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/0
    # description Configured and Merged by Ansible-Network
    # mtu 110
    # ipv4 address 172.31.1.1 255.255.255.0
    # duplex half
    # !
    # interface GigabitEthernet0/0/0/3
    # shutdown
    # !
    # interface GigabitEthernet0/0/0/4
    # shutdown
    # !
    - name: Gather IOSXR interfaces as in given arguments
      cisco.iosxr.iosxr_interfaces:
        config:
        state: gathered
    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": [
    #         {
    #             "description": "test for ansible",
    #             "enabled": false,
    #             "name": "Loopback888"
    #         },
    #         {
    #             "description": "Configured and Merged by Ansible-Network",
    #             "duplex": "half",
    #             "enabled": true,
    #             "mtu": 110,
    #             "name": "GigabitEthernet0/0/0/0"
    #         },
    #         {
    #             "enabled": false,
    #             "name": "GigabitEthernet0/0/0/3"
    #         },
    #         {
    #             "enabled": false,
    #             "name": "GigabitEthernet0/0/0/4"
    #         }
    #     ]
    # After state:
    # ------------
    #
    # RP/0/0/CPU0:an-iosxr-02#show running-config  interface
    # interface Loopback888
    # description test for ansible
    # shutdown
    # !
    # interface MgmtEth0/0/CPU0/0
    # ipv4 address 10.8.38.70 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/0
    # description Configured and Merged by Ansible-Network
    # mtu 110
    # ipv4 address 172.31.1.1 255.255.255.0
    # duplex half
    # !
    # interface GigabitEthernet0/0/0/3
    # shutdown
    # !
    # interface GigabitEthernet0/0/0/4
    # shutdown
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface GigabitEthernet0/0/0/2&#x27;, &#x27;description: Configured by Ansible&#x27;, &#x27;shutdown&#x27;]</div>
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
