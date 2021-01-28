.. _cisco.iosxr.iosxr_interface_module:


***************************
cisco.iosxr.iosxr_interface
***************************

**(deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS XR network devices**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1

DEPRECATED
----------
:Removed in collection release after 2022-06-01
:Why: Newer and updated modules released with more functionality in Ansible 2.9
:Alternative: iosxr_interfaces



Synopsis
--------
- This module provides declarative management of Interfaces on Cisco IOS XR network devices.



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
                    <b>active</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>active</b>&nbsp;&larr;</div></li>
                                    <li>preconfigure</li>
                        </ul>
                </td>
                <td>
                        <div>Whether the interface is <code>active</code> or <code>preconfigured</code>. Preconfiguration allows you to configure modular services cards before they are inserted into the router. When the cards are inserted, they are instantly configured. Active cards are the ones already inserted.</div>
                </td>
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
                        <div>List of interfaces definition</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>active</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>active</li>
                                    <li>preconfigure</li>
                        </ul>
                </td>
                <td>
                        <div>Whether the interface is <code>active</code> or <code>preconfigured</code>. Preconfiguration allows you to configure modular services cards before they are inserted into the router. When the cards are inserted, they are instantly configured. Active cards are the ones already inserted.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are <em>state</em> with values <code>up</code>/<code>down</code>, <em>tx_rate</em> and <em>rx_rate</em>.</div>
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
                        <div>Description of Interface being configured.</div>
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
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Removes the shutdown configuration, which removes the forced administrative down on the interface, enabling it to move to an up or down state.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mtu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Sets the MTU value for the interface. Range is between 64 and 65535&#x27;</div>
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
                        <div>Name of the interface to configure in <code>type + path</code> format. e.g. <code>GigabitEthernet0/0/0/0</code></div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rx_rate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Receiver rate in bits per second (bps).</div>
                        <div>This is state check parameter only.</div>
                        <div>Supports conditionals, see <a href='../network/user_guide/network_working_with_command_output.html'>Conditionals in Networking Modules</a></div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>10</li>
                                    <li>100</li>
                                    <li>1000</li>
                        </ul>
                </td>
                <td>
                        <div>Configure the speed for an interface. Default is auto-negotiation when not configured.</div>
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
                                    <li>up</li>
                                    <li>down</li>
                        </ul>
                </td>
                <td>
                        <div>State of the Interface configuration, <code>up</code> means present and operationally up and <code>down</code> means present and operationally <code>down</code></div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tx_rate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Transmit rate in bits per second (bps).</div>
                        <div>This is state check parameter only.</div>
                        <div>Supports conditionals, see <a href='../network/user_guide/network_working_with_command_output.html'>Conditionals in Networking Modules</a></div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>delay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">10</div>
                </td>
                <td>
                        <div>Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are <em>state</em> with values <code>up</code>/<code>down</code>, <em>tx_rate</em> and <em>rx_rate</em>.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
                        <div>Description of Interface being configured.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
                <td colspan="2">
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
                        <div>Removes the shutdown configuration, which removes the forced administrative down on the interface, enabling it to move to an up or down state.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mtu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Sets the MTU value for the interface. Range is between 64 and 65535&#x27;</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
                        <div>Name of the interface to configure in <code>type + path</code> format. e.g. <code>GigabitEthernet0/0/0/0</code></div>
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
                    <b>rx_rate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Receiver rate in bits per second (bps).</div>
                        <div>This is state check parameter only.</div>
                        <div>Supports conditionals, see <a href='../network/user_guide/network_working_with_command_output.html'>Conditionals in Networking Modules</a></div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>speed</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>10</li>
                                    <li>100</li>
                                    <li>1000</li>
                        </ul>
                </td>
                <td>
                        <div>Configure the speed for an interface. Default is auto-negotiation when not configured.</div>
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
                                    <li>up</li>
                                    <li>down</li>
                        </ul>
                </td>
                <td>
                        <div>State of the Interface configuration, <code>up</code> means present and operationally up and <code>down</code> means present and operationally <code>down</code></div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tx_rate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Transmit rate in bits per second (bps).</div>
                        <div>This is state check parameter only.</div>
                        <div>Supports conditionals, see <a href='../network/user_guide/network_working_with_command_output.html'>Conditionals in Networking Modules</a></div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - This module works with connection ``network_cli`` and ``netconf``. See `the IOS-XR Platform Options <../network/user_guide/platform_iosxr.html>`_.
   - Tested against IOS XRv 6.1.3.
   - Preconfiguration of physical interfaces is not supported with ``netconf`` transport.
   - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
   - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <https://www.ansible.com/integrations/networks/cisco>`_.



Examples
--------

.. code-block:: yaml

    - name: configure interface
      cisco.iosxr.iosxr_interface:
        name: GigabitEthernet0/0/0/2
        description: test-interface
        speed: 100
        duplex: half
        mtu: 512

    - name: remove interface
      cisco.iosxr.iosxr_interface:
        name: GigabitEthernet0/0/0/2
        state: absent

    - name: make interface up
      cisco.iosxr.iosxr_interface:
        name: GigabitEthernet0/0/0/2
        enabled: true

    - name: make interface down
      cisco.iosxr.iosxr_interface:
        name: GigabitEthernet0/0/0/2
        enabled: false

    - name: Create interface using aggregate
      cisco.iosxr.iosxr_interface:
        aggregate:
        - name: GigabitEthernet0/0/0/3
        - name: GigabitEthernet0/0/0/2
        speed: 100
        duplex: full
        mtu: 512
        state: present

    - name: Create interface using aggregate along with additional params in aggregate
      cisco.iosxr.iosxr_interface:
        aggregate:
        - {name: GigabitEthernet0/0/0/3, description: test-interface 3}
        - {name: GigabitEthernet0/0/0/2, description: test-interface 2}
        speed: 100
        duplex: full
        mtu: 512
        state: present

    - name: Delete interface using aggregate
      cisco.iosxr.iosxr_interface:
        aggregate:
        - name: GigabitEthernet0/0/0/3
        - name: GigabitEthernet0/0/0/2
        state: absent

    - name: Check intent arguments
      cisco.iosxr.iosxr_interface:
        name: GigabitEthernet0/0/0/5
        state: up
        delay: 20

    - name: Config + intent
      cisco.iosxr.iosxr_interface:
        name: GigabitEthernet0/0/0/5
        enabled: false
        state: down
        delay: 20



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;interface GigabitEthernet0/0/0/2&#x27;, &#x27;description test-interface&#x27;, &#x27;duplex half&#x27;, &#x27;mtu 512&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;&lt;config xmlns:xc=&quot;urn:ietf:params:xml:ns:netconf:base:1.0&quot;&gt; &lt;interface-configurations xmlns=&quot;http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg&quot;&gt; &lt;interface-configuration xc:operation=&quot;merge&quot;&gt; &lt;active&gt;act&lt;/active&gt; &lt;interface-name&gt;GigabitEthernet0/0/0/0&lt;/interface-name&gt; &lt;description&gt;test-interface-0&lt;/description&gt; &lt;mtus&gt;&lt;mtu&gt; &lt;owner&gt;GigabitEthernet&lt;/owner&gt; &lt;mtu&gt;512&lt;/mtu&gt; &lt;/mtu&gt;&lt;/mtus&gt; &lt;ethernet xmlns=&quot;http://cisco.com/ns/yang/Cisco-IOS-XR-drivers-media-eth-cfg&quot;&gt; &lt;speed&gt;100&lt;/speed&gt; &lt;duplex&gt;half&lt;/duplex&gt; &lt;/ethernet&gt; &lt;/interface-configuration&gt; &lt;/interface-configurations&gt;&lt;/config&gt;&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


- This module will be removed in version . *[deprecated]*
- For more information see `DEPRECATED`_.


Authors
~~~~~~~

- Ganesh Nalawade (@ganeshrn)
- Kedar Kekan (@kedarX)
