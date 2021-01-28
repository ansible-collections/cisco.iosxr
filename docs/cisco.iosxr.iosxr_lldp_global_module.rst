.. _cisco.iosxr.iosxr_lldp_global_module:


*****************************
cisco.iosxr.iosxr_lldp_global
*****************************

**LLDP resource module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages Global Link Layer Discovery Protocol (LLDP) settings on IOS-XR devices.




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The provided global LLDP configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>holdtime</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the holdtime (in sec) to be sent in packets.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>reinit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the delay (in sec) for LLDP initialization on any interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>subinterfaces</b>
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
                        <div>Enable or disable LLDP over sub-interfaces.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the rate at which LLDP packets are sent (in sec).</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tlv_select</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the LLDP TLVs to enable or disable.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>management_address</b>
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
                        <div>Enable or disable management address TLV.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port_description</b>
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
                        <div>Enable or disable port description TLV.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_capabilities</b>
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
                        <div>Enable or disable system capabilities TLV.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_description</b>
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
                        <div>Enable or disable system description TLV.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>system_name</b>
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
                        <div>Enable or disable system name TLV.</div>
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
                        <div>The value of this option should be the output received from the IOS-XR device by executing the command <b>show running-config lldp</b>.</div>
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
    # -------------
    # Before State
    # -------------
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh run lldp
    # Tue Aug  6 19:27:54.933 UTC
    # % No such configuration item(s)
    #
    #

    - name: Merge provided LLDP configuration with the existing configuration
      cisco.iosxr.iosxr_lldp_global:
        config:
          holdtime: 100
          reinit: 2
          timer: 3000
          subinterfaces: true
          tlv_select:
            management_address: false
            system_description: false
        state: merged

    #
    #
    # ------------------------
    # Module Execution Result
    # ------------------------
    #
    #  "before": {}
    #
    #  "commands": [
    #        "lldp subinterfaces enable",
    #        "lldp holdtime 100",
    #        "lldp reinit 2",
    #        "lldp tlv-select system-description disable",
    #        "lldp tlv-select management-address disable",
    #        "lldp timer 3000"
    #  ]
    #
    #  "after": {
    #        "holdtime": 100,
    #        "reinit": 2,
    #        "subinterfaces": true,
    #        "timer": 3000,
    #        "tlv_select": {
    #            "management_address": false,
    #            "system_description": false
    #        }
    #  }
    #
    #
    # ------------
    # After state
    # ------------
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh run lldp
    # Tue Aug  6 21:31:10.587 UTC
    # lldp
    #  timer 3000
    #  reinit 2
    #  subinterfaces enable
    #  holdtime 100
    #  tlv-select
    #   management-address disable
    #   system-description disable
    #  !
    # !
    #
    #


    # Using replaced
    #
    #
    # -------------
    # Before State
    # -------------
    #
    # RP/0/0/CPU0:an-iosxr#sh run lldp
    # Tue Aug  6 21:31:10.587 UTC
    # lldp
    #  timer 3000
    #  reinit 2
    #  subinterfaces enable
    #  holdtime 100
    #  tlv-select
    #   management-address disable
    #   system-description disable
    #  !
    # !
    #
    #

    - name: Replace existing LLDP device configuration with provided configuration
      cisco.iosxr.iosxr_lldp_global:
        config:
          holdtime: 100
          tlv_select:
            port_description: false
            system_description: true
            management_description: true
        state: replaced

    #
    #
    # ------------------------
    # Module Execution Result
    # ------------------------
    #
    #  "before": {
    #        "holdtime": 100,
    #        "reinit": 2,
    #        "subinterfaces": true,
    #        "timer": 3000,
    #        "tlv_select": {
    #            "management_address": false,
    #            "system_description": false
    #        }
    #  }
    #
    #  "commands": [
    #        "no lldp reinit 2",
    #        "no lldp subinterfaces enable",
    #        "no lldp timer 3000",
    #        "no lldp tlv-select management-address disable",
    #        "no lldp tlv-select system-description disable",
    #        "lldp tlv-select port-description disable"
    #  ]
    #
    #  "after": {
    #        "holdtime": 100,
    #        "tlv_select": {
    #            "port_description": false
    #        }
    #  }
    #
    #
    # ------------
    # After state
    # ------------
    #
    # RP/0/0/CPU0:an-iosxr#sh run lldp
    # Tue Aug  6 21:53:08.407 UTC
    # lldp
    #  holdtime 100
    #  tlv-select
    #   port-description disable
    #  !
    # !
    #
    #


    # Using deleted
    #
    # ------------
    # Before state
    # ------------
    #
    #
    # RP/0/0/CPU0:an-iosxr#sh run lldp
    # Tue Aug  6 21:31:10.587 UTC
    # lldp
    #  timer 3000
    #  reinit 2
    #  subinterfaces enable
    #  holdtime 100
    #  tlv-select
    #   management-address disable
    #   system-description disable
    #  !
    # !
    #
    #

    - name: Deleted existing LLDP configurations from the device
      cisco.iosxr.iosxr_lldp_global:
        state: deleted

    #
    #
    # ------------------------
    # Module Execution Result
    # ------------------------
    #
    #  "before": {
    #        "holdtime": 100,
    #        "reinit": 2,
    #        "subinterfaces": true,
    #        "timer": 3000,
    #        "tlv_select": {
    #            "management_address": false,
    #            "system_description": false
    #        }
    #  },
    #
    #  "commands": [
    #        "no lldp holdtime 100",
    #        "no lldp reinit 2",
    #        "no lldp subinterfaces enable",
    #        "no lldp timer 3000",
    #        "no lldp tlv-select management-address disable",
    #        "no lldp tlv-select system-description disable"
    #  ]
    #
    #  "after": {}
    #
    #
    # -----------
    # After state
    # -----------
    #
    # RP/0/0/CPU0:an-iosxr#sh run lldp
    # Tue Aug  6 21:38:31.187 UTC
    # lldp
    # !
    #
    # Using parsed:

    # parsed.cfg
    # lldp
    #  timer 3000
    #  reinit 2
    #  subinterfaces enable
    #  holdtime 100
    #  tlv-select
    #   management-address disable
    #   system-description disable
    #  !
    # !

    - name: Convert lldp global config to argspec without connecting to the appliance
      cisco.iosxr.iosxr_lldp_global:
        running_config: "{{ lookup('file', './parsed.cfg') }}"
        state: parsed

    # ------------------------
    # Module Execution Result
    # ------------------------
    # parsed:
    #     holdtime: 100
    #     reinit: 2
    #     timer: 3000
    #     subinterfaces: True
    #     tlv_select:
    #       management_address: False
    #       system_description: False

    # using gathered:

    # Device config:
    # lldp
    #  timer 3000
    #  reinit 2
    #  subinterfaces enable
    #  holdtime 100
    #  tlv-select
    #   management-address disable
    #   system-description disable
    #  !
    # !

    - name: Gather IOSXR lldp global configuration
      cisco.iosxr.iosxr_lldp_global:
        config:
        state: gathered


    # ------------------------
    # Module Execution Result
    # ------------------------
    # gathered:
    #     holdtime: 100
    #     reinit: 2
    #     timer: 3000
    #     subinterfaces: True
    #     tlv_select:
    #       management_address: False
    #       system_description: False

    # using rendered:

    - name: Render platform specific commands from task input using rendered state
      cisco.iosxr.iosxr_lldp_global:
        config:
          holdtime: 100
          reinit: 2
          timer: 3000
          subinterfaces: true
          tlv_select:
            management_address: false
            system_description: false
        state: rendered

    #
    #
    # ------------------------
    # Module Execution Result
    # ------------------------
    #
    #  "rendered": [
    #        "lldp subinterfaces enable",
    #        "lldp holdtime 100",
    #        "lldp reinit 2",
    #        "lldp tlv-select system-description disable",
    #        "lldp tlv-select management-address disable",
    #        "lldp timer 3000"
    #  ]



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;lldp subinterfaces enable&#x27;, &#x27;lldp holdtime 100&#x27;, &#x27;no lldp tlv-select management-address disable&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Nilashish Chakraborty (@NilashishC)
