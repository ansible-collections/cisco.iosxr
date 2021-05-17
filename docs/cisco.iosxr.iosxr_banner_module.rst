.. _cisco.iosxr.iosxr_banner_module:


************************
cisco.iosxr.iosxr_banner
************************

**Manage multiline banners on Cisco IOS XR devices**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module will configure both exec and motd banners on remote device running Cisco IOS XR. It allows playbooks to add or remove banner text from the running configuration.



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
                    <b>banner</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>login</li>
                                    <li>motd</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the type of banner to configure on remote device.</div>
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
                        <div>Existential state of the configuration on the device.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>text</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Banner text to be configured. Accepts multi line string, without empty lines. When using a multi line string, the first and last characters must be the start and end delimiters for the banner Requires <em>state=present</em>.</div>
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

    - name: configure the login banner
      cisco.iosxr.iosxr_banner:
        banner: login
        text: |
          @this is my login banner
          that contains a multiline
          string@
        state: present
    - name: remove the motd banner
      cisco.iosxr.iosxr_banner:
        banner: motd
        state: absent
    - name: Configure banner from file
      cisco.iosxr.iosxr_banner:
        banner: motd
        text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
        state: present



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
                            <div>The list of configuration mode commands sent to device with transport <code>cli</code></div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;banner login&#x27;, &#x27;@this is my login banner&#x27;, &#x27;that contains a multiline&#x27;, &#x27;string@&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;config xmlns:xc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;banners xmlns=&quot;http://cisco.com/ns/yang/Cisco-IOS-XR-infra-infra-cfg&quot;&gt; &lt;banner xc:operation=&quot;merge&quot;&gt; &lt;banner-name&gt;motd&lt;/banner-name&gt; &lt;banner-text&gt;Ansible banner example&lt;/banner-text&gt; &lt;/banner&gt; &lt;/banners&gt; &lt;/config&gt;&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Trishna Guha (@trishnaguha)
- Kedar Kekan (@kedarX)
