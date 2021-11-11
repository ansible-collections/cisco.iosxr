.. _cisco.iosxr.iosxr_logging_module:


*************************
cisco.iosxr.iosxr_logging
*************************

**Configuration management of system logging services on network devices**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1

DEPRECATED
----------
:Removed in collection release after 2023-08-01
:Why: Updated module released with more functionality.
:Alternative: iosxr_logging_global



Synopsis
--------
- This module provides declarative management configuration of system logging (syslog) on Cisco IOS XR devices.



Requirements
------------
The below requirements are needed on the host that executes this module.

- ncclient >= 0.5.3 when using netconf
- lxml >= 4.1.1 when using netconf


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
                    <b>aggregate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of syslog logging configuration definitions.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dest</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>host</li>
                                    <li>console</li>
                                    <li>monitor</li>
                                    <li>buffered</li>
                                    <li>file</li>
                        </ul>
                </td>
                <td>
                        <div>Destination for system logging (syslog) messages.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>To configure the type of syslog facility in which system logging (syslog) messages are sent to syslog servers Optional config for <code>dest</code> = <code>host</code></div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostnameprefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>To append a hostname prefix to system logging (syslog) messages logged to syslog servers. Optional config for <code>dest</code> = <code>host</code></div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emergencies</li>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>errors</li>
                                    <li>warning</li>
                                    <li>notifications</li>
                                    <li>informational</li>
                                    <li>debugging</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the severity level for the logging.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: severity</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>When <code>dest</code> = <em>file</em> name indicates file-name</div>
                        <div>When <code>dest</code> = <em>host</em> name indicates the host-name or ip-address of syslog server.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set file path.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Size of buffer when <code>dest</code> = <code>buffered</code>. The acceptable value is in the range <em>307200 to 125000000 bytes</em>. Default 307200</div>
                        <div>Size of file when <code>dest</code> = <code>file</code>. The acceptable value is in the range <em>1 to 2097152</em>KB. Default 2 GB</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>present</li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>Existential state of the logging configuration on the node.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>vrf name when syslog server is configured, <code>dest</code> = <code>host</code></div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dest</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>host</li>
                                    <li>console</li>
                                    <li>monitor</li>
                                    <li>buffered</li>
                                    <li>file</li>
                        </ul>
                </td>
                <td>
                        <div>Destination for system logging (syslog) messages.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"local7"</div>
                </td>
                <td>
                        <div>To configure the type of syslog facility in which system logging (syslog) messages are sent to syslog servers Optional config for <code>dest</code> = <code>host</code></div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostnameprefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>To append a hostname prefix to system logging (syslog) messages logged to syslog servers. Optional config for <code>dest</code> = <code>host</code></div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>emergencies</li>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>errors</li>
                                    <li>warning</li>
                                    <li>notifications</li>
                                    <li>informational</li>
                                    <li><div style="color: blue"><b>debugging</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the severity level for the logging.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: severity</div>
                </td>
            </tr>
            <tr>
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
                        <div>When <code>dest</code> = <em>file</em> name indicates file-name</div>
                        <div>When <code>dest</code> = <em>host</em> name indicates the host-name or ip-address of syslog server.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set file path.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>provider</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div><b>Deprecated</b></div>
                        <div>Starting with Ansible 2.5 we recommend using <code>connection: network_cli</code>.</div>
                        <div>For more information please see the <a href='../network/getting_started/network_differences.html#multiple-communication-protocols'>Network Guide</a>.</div>
                        <div><hr/></div>
                        <div>A dict object containing connection details.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable <code>ANSIBLE_NET_PASSWORD</code> will be used instead.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the port to use when building the connection to the remote device.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ssh_keyfile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable <code>ANSIBLE_NET_SSH_KEYFILE</code> will be used instead.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>transport</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>cli</b>&nbsp;&larr;</div></li>
                                    <li>netconf</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of connection based transport.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable <code>ANSIBLE_NET_USERNAME</code> will be used instead.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Size of buffer when <code>dest</code> = <code>buffered</code>. The acceptable value is in the range <em>307200 to 125000000 bytes</em>. Default 307200</div>
                        <div>Size of file when <code>dest</code> = <code>file</code>. The acceptable value is in the range <em>1 to 2097152</em>KB. Default 2 GB</div>
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
                                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>Existential state of the logging configuration on the node.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"default"</div>
                </td>
                <td>
                        <div>vrf name when syslog server is configured, <code>dest</code> = <code>host</code></div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module works with connection ``network_cli`` and ``netconf``. See `the IOS-XR Platform Options <../network/user_guide/platform_iosxr.html>`_.
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
   - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <https://www.ansible.com/integrations/networks/cisco>`_.



Examples
--------

.. code-block:: yaml

    - name: configure logging for syslog server host
      cisco.iosxr.iosxr_logging:
        dest: host
        name: 10.10.10.1
        level: critical
        state: present

    - name: add hostnameprefix configuration
      cisco.iosxr.iosxr_logging:
        hostnameprefix: host1
        state: absent

    - name: add facility configuration
      cisco.iosxr.iosxr_logging:
        facility: local1
        state: present

    - name: configure console logging level
      cisco.iosxr.iosxr_logging:
        dest: console
        level: debugging
        state: present

    - name: configure monitor logging level
      cisco.iosxr.iosxr_logging:
        dest: monitor
        level: errors
        state: present

    - name: configure syslog to a file
      cisco.iosxr.iosxr_logging:
        dest: file
        name: file_name
        size: 2048
        level: errors
        state: present

    - name: configure buffered logging with size
      cisco.iosxr.iosxr_logging:
        dest: buffered
        size: 5100000

    - name: Configure logging using aggregate
      cisco.iosxr.iosxr_logging:
        aggregate:
        - {dest: console, level: warning}
        - {dest: buffered, size: 4800000}
        - {dest: file, name: file3, size: 2048}
        - {dest: host, name: host3, level: critical}

    - name: Delete logging using aggregate
      cisco.iosxr.iosxr_logging:
        aggregate:
        - {dest: console, level: warning}
        - {dest: buffered, size: 4800000}
        - {dest: file, name: file3, size: 2048}
        - {dest: host, name: host3, level: critical}
        state: absent



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
                    <b>commands</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always (empty list when no commands to send)</td>
                <td>
                            <div>The list of configuration mode commands to send to the device</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;logging 10.10.10.1 vrf default severity debugging&#x27;, &#x27;logging facility local7&#x27;, &#x27;logging hostnameprefix host1&#x27;, &#x27;logging console critical&#x27;, &#x27;logging buffered 2097153&#x27;, &#x27;logging buffered warnings&#x27;, &#x27;logging monitor errors&#x27;, &#x27;logging file log_file maxfilesize 1024 severity info&#x27;]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>xml</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always (empty list when no xml rpc to send)</td>
                <td>
                            <div>NetConf rpc xml sent to device with transport <code>netconf</code></div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;config xmlns:xc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;syslog xmlns=&quot;http://cisco.com/ns/yang/Cisco-IOS-XR-infra-syslog-cfg&quot;&gt; &lt;files&gt; &lt;file xc:operation=&quot;delete&quot;&gt; &lt;file-name&gt;file1&lt;/file-name&gt; &lt;file-log-attributes&gt; &lt;max-file-size&gt;2097152&lt;/max-file-size&gt; &lt;severity&gt;2&lt;/severity&gt; &lt;/file-log-attributes&gt; &lt;/file&gt; &lt;/files&gt; &lt;/syslog&gt; &lt;/config&gt;&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


- This module will be removed in a release after 2023-08-01. *[deprecated]*
- For more information see `DEPRECATED`_.


Authors
~~~~~~~

- Trishna Guha (@trishnaguha)
- Kedar Kekan (@kedarX)
