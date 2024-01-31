.. _cisco.iosxr.iosxr_lacp_module:


**********************
cisco.iosxr.iosxr_lacp
**********************

**Resource module to configure LACP.**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages Global Link Aggregation Control Protocol (LACP) on IOS-XR devices.




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The provided configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>This option sets the default system parameters for LACP bundles.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The system MAC related configuration for LACP.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>The system ID to use in LACP negotiations.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>The system priority to use in LACP negotiations.</div>
                        <div>Lower value is higher priority.</div>
                        <div>Refer to vendor documentation for valid values.</div>
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
                        <div>The value of this option should be the output received from the IOS-XR device by executing the command <b>show running-config lacp</b>.</div>
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
                                    <li>deleted</li>
                                    <li>parsed</li>
                                    <li>rendered</li>
                                    <li>gathered</li>
                                    <li>overridden</li>
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
    # RP/0/0/CPU0:iosxr01#show running-config lacp
    # Tue Jul 16 17:46:08.147 UTC
    # % No such configuration item(s)
    #
    #

    - name: Merge provided configuration with device configuration
      cisco.iosxr.iosxr_lacp:
        config:
          system:
            priority: 10
            mac:
              address: 00c1.4c00.bd15
        state: merged

    #
    #
    # -----------------------
    # Module Execution Result
    # -----------------------
    #
    # "before": {}
    #
    #
    # "commands": [
    #    "lacp system priority 10",
    #    "lacp system mac 00c1.4c00.bd15"
    #  ]
    #
    #
    # "after": {
    #    "system": {
    #       "mac": {
    #          "address": "00c1.4c00.bd15"
    #       },
    #       "priority": 10
    #     }
    #  }
    #
    # -----------
    # After state
    # -----------
    #
    #
    # RP/0/0/CPU0:iosxr01#sh run lacp
    # Tue Jul 16 17:51:29.365 UTC
    # lacp system mac 00c1.4c00.bd15
    # lacp system priority 10
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
    # RP/0/0/CPU0:iosxr01#sh run lacp
    # Tue Jul 16 17:53:59.904 UTC
    # lacp system mac 00c1.4c00.bd15
    # lacp system priority 10
    #

    - name: Replace device global lacp configuration with the given configuration
      cisco.iosxr.iosxr_lacp:
        config:
          system:
            priority: 11
        state: replaced
    #
    #
    # -----------------------
    # Module Execution Result
    # -----------------------
    # "before": {
    #    "system": {
    #       "mac": {
    #         "address": "00c1.4c00.bd15"
    #       },
    #       "priority": 10
    #    }
    #  }
    #
    #
    # "commands": [
    #    "no lacp system mac",
    #    "lacp system priority 11"
    #  ]
    #
    #
    # "after": {
    #    "system": {
    #       "priority": 11
    #    }
    # }
    #
    # -----------
    # After state
    # -----------
    #
    #
    # RP/0/0/CPU0:iosxr01#sh run lacp
    # Tue Jul 16 18:02:40.379 UTC
    # lacp system priority 11
    #
    #

    # Using deleted
    #
    #
    # ------------
    # Before state
    # ------------
    #
    #
    # RP/0/0/CPU0:iosxr01#sh run lacp
    # Tue Jul 16 18:37:09.727 UTC
    # lacp system mac 00c1.4c00.bd15
    # lacp system priority 11
    #
    #

    - name: Delete global LACP configurations from the device
      cisco.iosxr.iosxr_lacp:
        state: deleted

    #
    #
    # -----------------------
    # Module Execution Result
    # -----------------------
    # "before": {
    #    "system": {
    #       "mac": {
    #         "address": "00c1.4c00.bd15"
    #       },
    #       "priority": 11
    #    }
    # }
    #
    #
    # "commands": [
    #     "no lacp system mac",
    #     "no lacp system priority"
    # ]
    #
    #
    # "after": {}
    #
    # ------------
    # After state
    # ------------
    #
    #
    # RP/0/0/CPU0:iosxr01#sh run lacp
    # Tue Jul 16 18:39:44.116 UTC
    # % No such configuration item(s)
    #
    #


    # Using parsed
    # parsed.cfg
    # ------------
    #
    # lacp system mac 00c1.4c00.bd15
    # lacp system priority 11
    # - name: Convert LACP config to argspec without connecting to the appliance
    #   cisco.iosxr.iosxr_lacp:
    #     running_config: "{{ lookup('file', './parsed.cfg') }}"
    #     state: parsed
    # Task Output (redacted)
    # -----------------------
    # "parsed": {
    #         "system": {
    #             "mac": {
    #                 "address": "00c1.4c00.bd15"
    #             },
    #             "priority": 11
    #         }
    #     }


    # Using rendered
    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_lacp:
        config:
          system:
            priority: 11
            mac:
              address: 00c1.4c00.bd15
        state: rendered
    # Task Output (redacted)
    # -----------------------
    # "rendered": [
    #         "lacp system priority 11",
    #         "lacp system mac 00c1.4c00.bd15"
    #     ]


    # Using gathered
    # Before state:
    # ------------
    #
    # RP/0/0/CPU0:an-iosxr-02#show running-config lacp
    # lacp system mac 00c1.4c00.bd15
    # lacp system priority 11
    - name: Gather IOSXR LACP configuration
      cisco.iosxr.iosxr_lacp:
        config:
        state: gathered
    # Task Output (redacted)
    # -----------------------
    #
    # "gathered": {
    #         "system": {
    #             "mac": {
    #                 "address": "00c1.4c00.bd15"
    #             },
    #             "priority": 11
    #         }
    #     }
    # After state:
    # ------------
    #
    # RP/0/0/CPU0:an-iosxr-02#show running-config lacp
    # lacp system mac 00c1.4c00.bd15
    # lacp system priority



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
                      <span style="color: purple">dictionary</span>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;lacp system priority 10&#x27;, &#x27;lacp system mac 00c1.4c00.bd15&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nilashish Chakraborty (@nilashishc)
- Rohit Thakur (@rohitthakur2590)
