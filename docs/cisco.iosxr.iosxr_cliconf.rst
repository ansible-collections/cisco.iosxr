.. _cisco.iosxr.iosxr_cliconf:


*****************
cisco.iosxr.iosxr
*****************

**Use iosxr cliconf to run command on Cisco IOS XR platform**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This iosxr plugin provides low level abstraction apis for sending and receiving CLI commands from Cisco IOS XR network devices.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                <th>Configuration</th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>commit_confirmed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"no"</div>
                </td>
                    <td>
                                <div>env:ANSIBLE_IOSXR_COMMIT_CONFIRMED</div>
                                <div>var: ansible_iosxr_commit_confirmed</div>
                    </td>
                <td>
                        <div>enable or disable commit confirmed mode</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>commit_confirmed_comment</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>env:ANSIBLE_IOSXR_COMMIT_CONFIRMED_COMMENT</div>
                                <div>var: ansible_iosxr_commit_confirmed_comment</div>
                    </td>
                <td>
                        <div>Adds comment to commit confirmed..</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>commit_confirmed_label</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>env:ANSIBLE_IOSXR_COMMIT_CONFIRMED_LABEL</div>
                                <div>var: ansible_iosxr_commit_confirmed_label</div>
                    </td>
                <td>
                        <div>Adds label to commit confirmed.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>commit_confirmed_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>env:ANSIBLE_IOSXR_COMMIT_CONFIRMED_TIMEOUT</div>
                                <div>var: ansible_iosxr_commit_confirmed_timeout</div>
                    </td>
                <td>
                        <div>Commits the configuration on a trial basis for the time specified in seconds or minutes.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config_commands</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 2.0.0</div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">[]</div>
                </td>
                    <td>
                                <div>var: ansible_iosxr_config_commands</div>
                    </td>
                <td>
                        <div>Specifies a list of commands that can make configuration changes to the target device.</div>
                        <div>When `ansible_network_single_user_mode` is enabled, if a command sent to the device is present in this list, the existing cache is invalidated.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>config_mode_exclusive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"no"</div>
                </td>
                    <td>
                                <div>env:ANSIBLE_IOSXR_CONFIG_MODE_EXCLUSIVE</div>
                                <div>var: ansible_iosxr_config_mode_exclusive</div>
                    </td>
                <td>
                        <div>enable or disable config mode exclusive</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    - name: Commit confirmed with a task
      vars:
        ansible_iosxr_commit_confirmed: True
        ansible_iosxr_commit_confirmed_timeout: 50
        ansible_iosxr_commit_confirmed_label: TestLabel
        ansible_iosxr_commit_confirmed_comment: I am a test comment
      cisco.iosxr.iosxr_logging_global:
        state: merged
        config:
          buffered:
            severity: errors #alerts #informational
          correlator:
            buffer_size: 2024

    # Commands (cliconf specific)
    # ["commit confirmed 50 label TestLabel comment I am a test comment"]

    - name: Configure exclusive mode with a task
      vars:
        ansible_iosxr_config_mode_exclusive: True
      cisco.iosxr.iosxr_interfaces:
        config:
            - name: GigabitEthernet0/0/0/2
            description: Configured via Ansible
            - name: GigabitEthernet0/0/0/3
            description: Configured via Ansible
        state: merged

    # Commands (cliconf specific)
    # ["configure exclusive"]




Status
------


Authors
~~~~~~~

- Ansible Networking Team (@ansible-network)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
