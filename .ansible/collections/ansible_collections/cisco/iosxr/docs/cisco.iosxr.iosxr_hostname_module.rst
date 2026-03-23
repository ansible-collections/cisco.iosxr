.. _cisco.iosxr.iosxr_hostname_module:


**************************
cisco.iosxr.iosxr_hostname
**************************

**Resource module to configure hostname.**


Version added: 2.7.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages the attributes of hostname on Cisco IOSXR platforms.




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
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Hostname configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>hostname of iosxr box.</div>
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
                        <div>The value of this option should be the output received from the IOSXR device by executing the command <b>show running-config hostname</b>.</div>
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
                                    <li>deleted</li>
                                    <li><div style="color: blue"><b>merged</b>&nbsp;&larr;</div></li>
                                    <li>overridden</li>
                                    <li>replaced</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                                    <li>parsed</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in</div>
                        <div>The states <em>rendered</em>, <em>gathered</em> and <em>parsed</em> does not perform any change on the device.</div>
                        <div>The state <em>rendered</em> will transform the configuration in <code>config</code> option to platform specific CLI commands which will be returned in the <em>rendered</em> key within the result. For state <em>rendered</em> active connection to remote host is not required.</div>
                        <div>The states <em>merged</em>, <em>replaced</em> and <em>overridden</em> have identical behaviour for this module.</div>
                        <div>The state <em>gathered</em> will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the <em>gathered</em> key within the result.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into JSON format as per the resource module parameters and the value is returned in the <em>parsed</em> key within the result. The value of <code>running_config</code> option should be the same format as the output of command <em>show running-config hostname</em> executed on device. For state <em>parsed</em> active connection to remote host is not required.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against Cisco Iosxr 7.0.2
   - This module works with connection ``network_cli``.



Examples
--------

.. code-block:: yaml

    # Using state: merged
    # Before state:
    # -------------

    # RP/0/RP0/CPU0:ios#show running-config hostname
    # Thu Jan 20 19:48:56.011 UTC
    # hostname ios

    # Merged play:
    # ------------

    - name: Apply the provided configuration
      cisco.iosxr.iosxr_hostname:
        config:
          hostname: Router1
        state: merged

    # Commands Fired:
    # ---------------
    # "commands": [
    #         "hostname Router1",
    # ],

    # After state:
    # ------------

    # RP/0/0/CPU0:Router1#show running-config hostname
    # Thu Jan 20 19:48:56.011 UTC
    # hostname Router1


    # Using state: deleted
    # Before state:
    # -------------

    # RP/0/0/CPU0:Router1#show running-config hostname
    # Thu Jan 20 19:48:56.011 UTC
    # hostname Router1

    # Deleted play:
    # -------------

    - name: Remove all existing configuration
      cisco.iosxr.iosxr_hostname:
        state: deleted

    # Commands Fired:
    # ---------------

    # "commands": [
    #     "no hostname Router1",
    # ],

    # After state:
    # ------------
    # RP/0/RP0/CPU0:ios#show running-config hostname
    # Thu Jan 20 19:55:12.971 UTC
    # hostname ios

    # Using state: overridden
    # Before state:
    # -------------

    # RP/0/0/CPU0:ios#show running-config hostname
    # hostname ios

    # Overridden play:
    # ----------------

    - name: Override commands with provided configuration
      cisco.iosxr.iosxr_hostname:
        config:
          hostname: RouterTest
        state: overridden

    # Commands Fired:
    # ---------------
    # "commands": [
    #       "hostname RouterTest",
    #     ],

    # After state:
    # ------------

    # RP/0/RP0/CPU0:RouterTest#show running-config hostname
    # Thu Jan 20 19:48:56.011 UTC
    # hostname RouterTest

    # Using state: replaced
    # Before state:
    # -------------

    # RP/0/RP0/CPU0:RouterTest#show running-config hostname
    # Thu Jan 20 19:48:56.011 UTC
    # hostname RouterTest

    # Replaced play:
    # --------------

    - name: Replace commands with provided configuration
      cisco.iosxr.iosxr_hostname:
        config:
          hostname: RouterTest
        state: replaced

    # Commands Fired:
    # ---------------
    # "commands": [],

    # After state:
    # ------------
    # RP/0/0/CPU0:RouterTest#show running-config hostname
    # hostname RouterTest

    # Using state: gathered
    # Before state:
    # -------------

    # RP/0/RP0/CPU0:RouterTest#show running-config hostname
    # Thu Jan 20 19:48:56.011 UTC
    # hostname RouterTest

    # Gathered play:
    # --------------

    - name: Gather listed hostname config
      cisco.iosxr.iosxr_hostname:
        state: gathered

    # Module Execution Result:
    # ------------------------
    #   "gathered": {
    #      "hostname": "RouterTest"
    #     },

    # Using state: rendered
    # Rendered play:
    # --------------

    - name: Render the commands for provided configuration
      cisco.iosxr.iosxr_hostname:
        config:
          hostname: RouterTest
        state: rendered

    # Module Execution Result:
    # ------------------------
    # "rendered": [
    #     "hostname RouterTest",
    # ]

    # Using state: parsed
    # File: parsed.cfg
    # ----------------

    # hostname RouterTest
    # Parsed play:
    # ------------

    - name: Parse the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_hostname:
        running_config: "{{ lookup('file', 'parsed.cfg') }}"
        state: parsed

    # Module Execution Result:
    # ------------------------
    #  "parsed": {
    #     "hostname": "RouterTest"
    # }



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;hostname Router1&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;hostname Router1&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ashwini Mhatre (@amhatre)
