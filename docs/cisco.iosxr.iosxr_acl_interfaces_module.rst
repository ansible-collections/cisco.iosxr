.. _cisco.iosxr.iosxr_acl_interfaces_module:


********************************
cisco.iosxr.iosxr_acl_interfaces
********************************

**ACL interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages adding and removing Access Control Lists (ACLs) from interfaces on devices running IOS-XR software.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="4">
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
                        <div>A dictionary of ACL options for interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies ACLs attached to the interfaces.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>acls</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the ACLs for the provided AFI.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>direction</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>in</li>
                                    <li>out</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the direction of packets that the ACL will be applied on.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specifies the name of the IPv4/IPv6 ACL for the interface.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Specifies the AFI for the ACL(s) to be configured on this interface.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Name/Identifier for the interface</div>
                </td>
            </tr>

            <tr>
                <td colspan="4">
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
                <td colspan="4">
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
                                    <li>parsed</li>
                                    <li>rendered</li>
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

    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:22:32.911 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !

    - name: Merge the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_acl_interfaces:
        config:
        - name: GigabitEthernet0/0/0/0
          access_groups:
          - afi: ipv4
            acls:
            - name: acl_1
              direction: in
            - name: acl_2
              direction: out
          - afi: ipv6
            acls:
            - name: acl6_1
              direction: in
            - name: acl6_2
              direction: out

        - name: GigabitEthernet0/0/0/1
          access_groups:
          - afi: ipv4
            acls:
            - name: acl_1
              direction: out
        state: merged

    # After state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:27:49.378 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 egress
    # !

    # Using merged to update interface ACL configuration

    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:27:49.378 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 egress
    # !
    #

    - name: Update acl_interfaces configuration using merged
      cisco.iosxr.iosxr_acl_interfaces:
        config:
        - name: GigabitEthernet0/0/0/1
          access_groups:
          - afi: ipv4
            acls:
            - name: acl_2
              direction: out
            - name: acl_1
              direction: in
        state: merged

    # After state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:27:49.378 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    # !
    #

    # Using replaced

    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:34:56.689 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 egress
    # !

    - name: Replace device configurations of listed interface with provided configurations
      cisco.iosxr.iosxr_acl_interfaces:
        config:
        - name: GigabitEthernet0/0/0/0
          access_groups:
          - afi: ipv6
            acls:
            - name: acl6_3
              direction: in
        state: replaced

    # After state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:34:56.689 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv6 access-group acl6_3 ingress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 egress
    # !
    #

    # Using overridden

    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:34:56.689 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 egress
    # !
    #

    - name: Overridde all interface ACL configuration with provided configuration
      cisco.iosxr.iosxr_acl_interfaces:
        config:
        - name: GigabitEthernet0/0/0/1
          access_groups:
          - afi: ipv4
            acls:
            - name: acl_2
              direction: in
          - afi: ipv6
            acls:
            - name: acl6_3
              direction: out
        state: overridden

    # After state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:34:56.689 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_2 ingress
    #  ipv6 access-group acl6_3 egress
    # !
    #

    # Using 'deleted' to delete all ACL attributes of a single interface

    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:34:56.689 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 egress
    # !
    #

    - name: Delete all ACL attributes of GigabitEthernet0/0/0/1
      cisco.iosxr.iosxr_acl_interfaces:
        config:
        - name: GigabitEthernet0/0/0/1
        state: deleted

    # After state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:34:56.689 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    #

    # Using 'deleted' to remove all ACLs attached to all the interfaces in the device

    # Before state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:34:56.689 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 egress
    # !
    #

    - name: Delete all ACL interfaces configuration from the device
      cisco.iosxr.iosxr_acl_interfaces:
        state: deleted

    # After state:
    # -------------
    #
    # RP/0/RP0/CPU0:ios#sh running-config interface
    # Wed Jan 15 12:34:56.689 UTC
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    # !
    #

    # Using parsed

    # parsed.cfg
    # ------------
    #
    # interface MgmtEth0/RP0/CPU0/0
    #  ipv4 address dhcp
    # !
    # interface GigabitEthernet0/0/0/0
    #  shutdown
    #  ipv4 access-group acl_1 ingress
    #  ipv4 access-group acl_2 egress
    #  ipv6 access-group acl6_1 ingress
    #  ipv6 access-group acl6_2 egress
    # !
    # interface GigabitEthernet0/0/0/1
    #  shutdown
    #  ipv4 access-group acl_1 egress
    # !

    # - name: Convert ACL interfaces config to argspec without connecting to the appliance
    #   cisco.iosxr.iosxr_acl_interfaces:
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


    # Using gathered

    - name: Gather ACL interfaces facts using gathered state
      cisco.iosxr.iosxr_acl_interfaces:
        state: gathered


    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": [
    #   {
    #      "name": "MgmtEth0/RP0/CPU0/0"
    #   },
    #   {
    #      "access_groups": [
    #          {
    #              "acls": [
    #                  {
    #                      "direction": "in",
    #                      "name": "acl_1"
    #                  },
    #                  {
    #                      "direction": "out",
    #                      "name": "acl_2"
    #                  }
    #              ],
    #              "afi": "ipv4"
    #          }
    #      "name": "GigabitEthernet0/0/0/0"
    #  },
    #  {
    #      "access_groups": [
    #          {
    #              "acls": [
    #                  {
    #                      "direction": "in",
    #                      "name": "acl6_1"
    #                  }
    #              ],
    #              "afi": "ipv6"
    #          }
    #       "name": "GigabitEthernet0/0/0/1"
    #   }
    # ]


    # Using rendered

    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_acl_interfaces:
        config:
        - name: GigabitEthernet0/0/0/0
          access_groups:
          - afi: ipv4
            acls:
            - name: acl_1
              direction: in
            - name: acl_2
              direction: out
        state: rendered

    # Task Output (redacted)
    # -----------------------

    # "rendered": [
    #     "interface GigabitEthernet0/0/0/0",
    #     "ipv4 access-group acl_1 ingress",
    #     "ipv4 access-group acl_2 egress"
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface GigabitEthernet0/0/0/1&#x27;, &#x27;ipv4 access-group acl_1 ingress&#x27;, &#x27;ipv4 access-group acl_2 egress&#x27;, &#x27;ipv6 access-group acl6_1 ingress&#x27;, &#x27;interface GigabitEthernet0/0/0/2&#x27;, &#x27;no ipv4 access-group acl_3 ingress&#x27;, &#x27;ipv4 access-group acl_4 egress&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nilashish Chakraborty (@NilashishC)
