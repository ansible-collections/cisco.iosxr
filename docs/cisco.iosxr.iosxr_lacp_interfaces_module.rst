.. _cisco.iosxr.iosxr_lacp_interfaces_module:


*********************************
cisco.iosxr.iosxr_lacp_interfaces
*********************************

**LACP interfaces resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages Link Aggregation Control Protocol (LACP) attributes of interfaces on IOS-XR devices.




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
                        <div>A dictionary of LACP interfaces options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>churn_logging</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>actor</li>
                                    <li>partner</li>
                                    <li>both</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the parameter for logging of LACP churn events.</div>
                        <div>Valid only for ether-bundles.</div>
                        <div>Mode &#x27;actor&#x27; logs actor churn events only.</div>
                        <div>Mode &#x27;partner&#x27; logs partner churn events only.</div>
                        <div>Mode &#x27;both&#x27; logs actor and partner churn events only.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>collector_max_delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the collector max delay to be signaled to the LACP partner.</div>
                        <div>Valid only for ether-bundles.</div>
                        <div>Refer to vendor documentation for valid values.</div>
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
                    <b>period</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the rate at which packets are sent or received.</div>
                        <div>For ether-bundles, this specifies the period to be used by its member links.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>switchover_suppress_flaps</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the time for which to suppress flaps during a LACP switchover.</div>
                        <div>Valid only for ether-bundles.</div>
                        <div>Refer to vendor documentation for valid values.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>This dict object contains configurable options related to LACP system parameters for ether-bundles.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the system ID to use in LACP negotiations for the bundle, encoded as a MAC address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the system priority to use in LACP negotiations for the bundle.</div>
                        <div>Refer to vendor documentation for valid values.</div>
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
                                    <li>gathered</li>
                                    <li>rendered</li>
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
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh running-config interface
    # Sun Jul 21 18:01:35.079 UTC
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
    #  description 'GigabitEthernet - 1'
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
      cisco.iosxr.iosxr_lacp_interfaces:
        config:
        - name: Bundle-Ether10
          churn_logging: actor
          collector_max_delay: 100
          switchover_suppress_flaps: 500

        - name: Bundle-Ether11
          system:
            mac: 00c2.4c00.bd15

        - name: GigabitEthernet0/0/0/1
          period: 200
        state: merged

    #
    #
    # -----------
    # After state
    # -----------
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh run int
    # Sun Jul 21 18:24:52.413 UTC
    # interface Bundle-Ether10
    #  lacp churn logging actor
    #  lacp switchover suppress-flaps 500
    #  lacp collector-max-delay 100
    # !
    # interface Bundle-Ether11
    #  lacp system mac 00c2.4c00.bd15
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
    #  lacp period 200
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


    # Using replaced
    #
    #
    # ------------
    # Before state
    # ------------
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh run int
    # Sun Jul 21 18:24:52.413 UTC
    # interface Bundle-Ether10
    #  lacp churn logging actor
    #  lacp switchover suppress-flaps 500
    #  lacp collector-max-delay 100
    # !
    # interface Bundle-Ether11
    #  lacp system mac 00c2.4c00.bd15
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
    #  lacp period 200
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

    - name: Replace LACP configuration of listed interfaces with provided configuration
      cisco.iosxr.iosxr_lacp_interfaces:
        config:
        - name: Bundle-Ether10
          churn_logging: partner

        - name: GigabitEthernet0/0/0/2
          period: 300
        state: replaced

    #
    #
    # -----------
    # After state
    # -----------
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh run int
    # Sun Jul 21 18:50:21.929 UTC
    # interface Bundle-Ether10
    #  lacp churn logging partner
    # !
    # interface Bundle-Ether11
    #  lacp system mac 00c2.4c00.bd15
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
    #  lacp period 200
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #  lacp period 300
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
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
    # RP/0/0/CPU0:an-iosxr#sh run int
    # Sun Jul 21 18:24:52.413 UTC
    # interface Bundle-Ether10
    #  lacp churn logging actor
    #  lacp switchover suppress-flaps 500
    #  lacp collector-max-delay 100
    # !
    # interface Bundle-Ether11
    #  lacp system mac 00c2.4c00.bd15
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
    #  lacp period 200
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #  lacp period 200
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    # !
    #
    #

    - name: Override all interface LACP configuration with provided configuration
      cisco.iosxr.iosxr_lacp_interfaces:
        config:
        - name: Bundle-Ether12
          churn_logging: both
          collector_max_delay: 100
          switchover_suppress_flaps: 500

        - name: GigabitEthernet0/0/0/1
          period: 300
        state: overridden

    #
    #
    # -----------
    # After state
    # -----------
    #
    #
    # RP/0/0/CPU0:an-iosxr(config-if)#do sh run int
    # Sun Jul 21 19:32:36.115 UTC
    # interface Bundle-Ether10
    # !
    # interface Bundle-Ether11
    # !
    # interface Bundle-Ether12
    #  lacp churn logging both
    #  lacp switchover suppress-flaps 500
    #  lacp collector-max-delay 100
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
    #  lacp period 300
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


    # Using deleted
    #
    #
    # ------------
    # Before state
    # ------------
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh run int
    # Sun Jul 21 18:24:52.413 UTC
    # interface Bundle-Ether10
    #  lacp churn logging actor
    #  lacp switchover suppress-flaps 500
    #  lacp collector-max-delay 100
    # !
    # interface Bundle-Ether11
    #  lacp non-revertive
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
    #  lacp period 200
    # !
    # interface GigabitEthernet0/0/0/2
    #  description "GigabitEthernet - 2"
    #   lacp period 300
    # !
    # interface GigabitEthernet0/0/0/3
    #  description "GigabitEthernet - 3"
    # !
    # interface GigabitEthernet0/0/0/4
    #  description "GigabitEthernet - 4"
    # !
    #

    - name: Deleted LACP configurations of provided interfaces (Note - This won't delete
        the interface itself)
      cisco.iosxr.iosxr_lacp_interfaces:
        config:
        - name: Bundle-Ether10
        - name: Bundle-Ether11
        - name: GigabitEthernet0/0/0/1
        - name: GigabitEthernet0/0/0/2
        state: deleted

    #
    #
    # -----------
    # After state
    # -----------
    #
    #
    # Using parsed:

    # parsed.cfg
    # interface Bundle-Ether10
    #  lacp churn logging actor
    #  lacp switchover suppress-flaps 500
    #  lacp collector-max-delay 100
    # !
    # interface Bundle-Ether11
    #  lacp system mac 00c2.4c00.bd15
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  lacp period 200
    # !
    #

    - name: Convert lacp interfaces config to argspec without connecting to the appliance
      cisco.iosxr.iosxr_lacp_interfaces:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # --------------
    # Output:
    # --------------

    #    parsed:
    #      - name: Bundle-Ether10
    #        churn_logging: actor
    #        collector_max_delay: 100
    #        switchover_suppress_flaps: 500
    #
    #      - name: Bundle-Ether11
    #        system:
    #          mac: 00c2.4c00.bd15
    #
    #      - name: GigabitEthernet0/0/0/1
    #        period: 200
    #
    #

    # Using gathered:

    # Native config:
    # interface Bundle-Ether10
    #  lacp churn logging actor
    #  lacp switchover suppress-flaps 500
    #  lacp collector-max-delay 100
    # !
    # interface Bundle-Ether11
    #  lacp system mac 00c2.4c00.bd15
    # !
    # interface MgmtEth0/0/CPU0/0
    #  ipv4 address 192.0.2.11 255.255.255.0
    # !
    # interface GigabitEthernet0/0/0/1
    #  lacp period 200
    # !
    #

    - name: Gather IOSXR lacp interfaces configuration
      cisco.iosxr.iosxr_lacp_interfaces:
        config:
        state: gathered

    # ----------
    # Output
    # ---------
    #    gathered:
    #      - name: Bundle-Ether10
    #        churn_logging: actor
    #        collector_max_delay: 100
    #        switchover_suppress_flaps: 500
    #
    #      - name: Bundle-Ether11
    #        system:
    #          mac: 00c2.4c00.bd15
    #
    #      - name: GigabitEthernet0/0/0/1
    #        period: 200

    # Using rendered:

    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_lacp_interfaces:
        config:
        - name: Bundle-Ether10
          churn_logging: actor
          collector_max_delay: 100
          switchover_suppress_flaps: 500

        - name: Bundle-Ether11
          system:
            mac: 00c2.4c00.bd15

        - name: GigabitEthernet0/0/0/1
          period: 200
        state: rendered

    # -------------
    # Output
    # -------------
    # rendered: [
    #     - "interface Bundle-Ether10"
    #     - " lacp churn logging actor"
    #     - " lacp switchover suppress-flaps 500"
    #     - " lacp collector-max-delay 100"
    #     - "interface Bundle-Ether11"
    #     - " lacp system mac 00c2.4c00.bd15"
    #     - "interface MgmtEth0/0/CPU0/0"
    #     - " ipv4 address 192.0.2.11 255.255.255.0"
    #     - "interface GigabitEthernet0/0/0/1"
    #     - " lacp period 200"
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface Bundle-Ether10&#x27;, &#x27;lacp churn logging partner&#x27;, &#x27;lacp period 150&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nilashish Chakraborty (@nilashishc)
