.. _cisco.iosxr.iosxr_prefix_lists_module:


******************************
cisco.iosxr.iosxr_prefix_lists
******************************

**Prefix-Lists resource module.**


Version added: 2.3.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages prefix-lists configuration on devices running Cisco IOSXR.




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
                        <div>A list of prefix-lists configuration.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>afi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ipv4</li>
                                    <li>ipv6</li>
                        </ul>
                </td>
                <td>
                        <div>The Address Family Identifier (AFI) for the prefix-lists.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix_lists</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of prefix-list configurations.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>entries</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of configurations for the specified prefix-list</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>action</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>permit</li>
                                    <li>deny</li>
                                    <li>remark</li>
                        </ul>
                </td>
                <td>
                        <div>Prefix-List permit or deny.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Description of the prefix list. only applicable for action &quot;remark&quot;.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>IP or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format. only applicable for action &quot;permit&quot; and &quot;deny&quot;</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sequence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Sequence Number.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Name of the prefix-list.</div>
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
                        <div>The value of this option should be the output received from the Iosxr device by executing the command <b>show running-config prefix-list</b>.</div>
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
                                    <li>parsed</li>
                                    <li>gathered</li>
                                    <li>rendered</li>
                        </ul>
                </td>
                <td>
                        <div>The state the configuration should be left in.</div>
                        <div>Refer to examples for more details.</div>
                        <div>With state <em>replaced</em>, for the listed prefix-lists, sequences that are in running-config but not in the task are negated.</div>
                        <div>With state <em>overridden</em>, all prefix-lists that are in running-config but not in the task are negated.</div>
                        <div>Please refer to examples for more details.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested against IOSXR 7.0.2.
   - This module works with connection ``network_cli``.



Examples
--------

.. code-block:: yaml

    # Using merged
    # Before state
    #RP/0/0/CPU0:10#show running-config
    #Thu Feb  4 09:38:36.245 UTC
    #% No such configuration item(s)
    #RP/0/0/CPU0:10#
    #
    - name: Merge the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_prefix_lists:
             state: merged
             config:
               - afi: ipv6
                 prefix_lists:
                   - name: pl_1
                     entries:
                       - prefix: 2001:db8:1234::/48
                         action: deny
                         sequence: 1
                   - name: pl_2
                     entries:
                       - sequence: 2
                         action: remark
                         description: TEST_PL_2_REMARK
               - afi: ipv4
                 prefix_lists:
                   - name: pl1
                     entries:
                       - sequence: 3
                         action: remark
                         description: TEST_PL1_2_REMARK
                       - sequence: 4
                         action: permit
                         prefix: 10.0.0.0/24
                   - name: pl2
                     entries:
                       - sequence: 5
                         action: remark
                         description: TEST_PL2_REMARK
    #
    # After state:
    #
    #RP/0/0/CPU0:10#show running-config
    # ipv6 prefix-list pl_1
    #  1 deny 2001:db8:1234::/48
    # !
    # ipv6 prefix-list pl_2
    #  2 remark TEST_PL_2_REMARK
    # !
    # ipv4 prefix-list pl1
    #  3 remark TEST_PL1_2_REMARK
    #  4 permit 10.0.0.0/24
    # !
    # ipv4 prefix-list pl2
    #  5 remark TEST_PL2_REMARK
    # !
    #Module execution
    #
    # "after": [
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "prefix": "2001:db8:1234::/48",
    #                             "sequence": 1
    #                         }
    #                     ],
    #                     "name": "pl_1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL_2_REMARK",
    #                             "sequence": 2
    #                         }
    #                     ],
    #                     "name": "pl_2"
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL1_2_REMARK",
    #                             "sequence": 3
    #                         },
    #                         {
    #                             "action": "permit",
    #                             "prefix": "10.0.0.0/24",
    #                             "sequence": 4
    #                         }
    #                     ],
    #                     "name": "pl1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL2_REMARK",
    #                             "sequence": 5
    #                         }
    #                     ],
    #                     "name": "pl2"
    #                 }
    #             ]
    #         }
    #     ],
    #     "before": [],
    #     "changed": true,
    #     "commands": [
    #         "ipv6 prefix-list pl_1 1 deny 2001:db8:1234::/48",
    #         "ipv6 prefix-list pl_2 2 remark TEST_PL_2_REMARK",
    #         "ipv4 prefix-list pl1 3 remark TEST_PL1_2_REMARK",
    #         "ipv4 prefix-list pl1 4 permit 10.0.0.0/24",
    #         "ipv4 prefix-list pl2 5 remark TEST_PL2_REMARK"
    #     ]
    #-----------------------------------------------------------------------
    # Using replaced:
    # --------------
    # Before state
    #RP/0/0/CPU0:10#show running-config
    #
    # ipv6 prefix-list pl_1
    #  1 deny 2001:db8:1234::/48
    # !
    # ipv6 prefix-list pl_2
    #  2 remark TEST_PL_2_REMARK
    # !
    # ipv4 prefix-list pl1
    #  3 remark TEST_PL1_2_REMARK
    #  4 permit 10.0.0.0/24
    # !
    # ipv4 prefix-list pl2
    #  5 remark TEST_PL2_REMARK
    # !
    #
    #
    - name: Replace device configurations of listed prefix lists with provided configurations
      register: result
      cisco.iosxr.iosxr_prefix_lists: &id001
        config:
               - afi: ipv4
                 prefix_lists:
                   - name: pl1
                     entries:
                       - sequence: 3
                         action: permit
                         prefix: 10.0.0.0/24
               - afi: ipv6
                 prefix_lists:
                   - name: pl_1
                     entries:
                       - prefix: 2001:db8:1234::/48
                         action: permit
                         sequence: 1
                   - name: pl_2
                     entries:
                       - sequence: 2
                         action: remark
                         description: TEST_PL1_2
        state: replaced
    # After state:
    #RP/0/0/CPU0:10#show running-config
    #
    # ipv6 prefix-list pl_1
    #  1 deny 2001:db8:1234::/48
    # !
    # ipv6 prefix-list pl_2
    #  2 remark TEST_PL1_2
    # !
    # ipv4 prefix-list pl1
    #  3 permit 10.0.0.0/24
    # !
    # ipv4 prefix-list pl2
    #  5 remark TEST_PL2_REMARK
    #
    # Module Execution:
    #
    # "after": [
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "prefix": "2001:db8:1234::/48",
    #                             "sequence": 1
    #                         }
    #                     ],
    #                     "name": "pl_1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL1_2",
    #                             "sequence": 2
    #                         }
    #                     ],
    #                     "name": "pl_2"
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "prefix": "10.0.0.0/24",
    #                             "sequence": 3
    #                         }
    #                     ],
    #                     "name": "pl1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL2_REMARK",
    #                             "sequence": 5
    #                         }
    #                     ],
    #                     "name": "pl2"
    #                 }
    #             ]
    #         }
    #     ],
    #     "before": [
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "prefix": "2001:db8:1234::/48",
    #                             "sequence": 1
    #                         }
    #                     ],
    #                     "name": "pl_1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL_2_REMARK",
    #                             "sequence": 2
    #                         }
    #                     ],
    #                     "name": "pl_2"
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL1_2_REMARK",
    #                             "sequence": 3
    #                         },
    #                         {
    #                             "action": "permit",
    #                             "prefix": "10.0.0.0/24",
    #                             "sequence": 4
    #                         }
    #                     ],
    #                     "name": "pl1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL2_REMARK",
    #                             "sequence": 5
    #                         }
    #                     ],
    #                     "name": "pl2"
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "no ipv4 prefix-list pl1 3 remark TEST_PL1_2_REMARK",
    #         "no ipv4 prefix-list pl1 4 permit 10.0.0.0/24",
    #         "ipv4 prefix-list pl1 3 permit 10.0.0.0/24",
    #         "ipv6 prefix-list pl_2 2 remark TEST_PL1_2"
    #     ],
    #     "invocation": {
    #         "module_args": {
    #             "config": [
    #                 {
    #                     "afi": "ipv4",
    #                     "prefix_lists": [
    #                         {
    #                             "entries": [
    #                                 {
    #                                     "action": "permit",
    #                                     "description": null,
    #                                     "prefix": "10.0.0.0/24",
    #                                     "sequence": 3
    #                                 }
    #                             ],
    #                             "name": "pl1"
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "afi": "ipv6",
    #                     "prefix_lists": [
    #                         {
    #                             "entries": [
    #                                 {
    #                                     "action": "permit",
    #                                     "description": null,
    #                                     "prefix": "2001:db8:1234::/48",
    #                                     "sequence": 1
    #                                 }
    #                             ],
    #                             "name": "pl_1"
    #                         },
    #                         {
    #                             "entries": [
    #                                 {
    #                                     "action": "remark",
    #                                     "description": "TEST_PL1_2",
    #                                     "prefix": null,
    #                                     "sequence": 2
    #                                 }
    #                             ],
    #                             "name": "pl_2"
    #                         }
    #                     ]
    #                 }
    #             ],
    #             "running_config": null,
    #             "state": "replaced"
    #         }
    #     }
    # }
    #------------------------------------------------------------------
    # Using deleted:
    # -------------
    # Before state:
    #RP/0/0/CPU0:10#show running-config
    #
    # ipv6 prefix-list pl_1
    #  1 deny 2001:db8:1234::/48
    # !
    # ipv6 prefix-list pl_2
    #  2 remark TEST_PL_2_REMARK
    # !
    # ipv4 prefix-list pl1
    #  3 remark TEST_PL1_2_REMARK
    #  4 permit 10.0.0.0/24
    # !
    # ipv4 prefix-list pl2
    #  5 remark TEST_PL2_REMARK

    - name: Delete all prefix-lists from the device
      cisco.iosxr.iosxr_prefix_lists:
        state: deleted

    # After state:
    #RP/0/0/CPU0:10#show running-config
    #
    #
    # Module Execution:
    #
    # "after": [],
    #     "before": [
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "prefix": "2001:db8:1234::/48",
    #                             "sequence": 1
    #                         }
    #                     ],
    #                     "name": "pl_1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL1_2",
    #                             "sequence": 2
    #                         }
    #                     ],
    #                     "name": "pl_2"
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "permit",
    #                             "prefix": "10.0.0.0/24",
    #                             "sequence": 3
    #                         }
    #                     ],
    #                     "name": "pl1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL2_REMARK",
    #                             "sequence": 5
    #                         }
    #                     ],
    #                     "name": "pl2"
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "no ipv6 prefix-list pl_1",
    #         "no ipv6 prefix-list pl_2",
    #         "no ipv4 prefix-list pl1",
    #         "no ipv4 prefix-list pl2"
    #     ],
    #     "invocation": {
    #         "module_args": {
    #             "config": null,
    #             "running_config": null,
    #             "state": "deleted"
    #         }
    #     }
    # }
    #---------------------------------------------------------------------------------
    #
    # using gathered:
    # --------------
    # Before state:
    #RP/0/0/CPU0:10#show running-config
    #
    # ipv6 prefix-list pl_1
    #  1 deny 2001:db8:1234::/48
    # !
    # ipv6 prefix-list pl_2
    #  2 remark TEST_PL_2_REMARK
    # !
    # ipv4 prefix-list pl1
    #  3 remark TEST_PL1_2_REMARK
    #  4 permit 10.0.0.0/24
    # !
    # ipv4 prefix-list pl2
    #  5 remark TEST_PL2_REMARK
    #
    - name: Gather ACL interfaces facts using gathered state
      cisco.iosxr.iosxr_prefix_lists:
         state: gathered
    #
    # Module Execution:
    #
    # "gathered": [
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "prefix": "2001:db8:1234::/48",
    #                             "sequence": 1
    #                         }
    #                     ],
    #                     "name": "pl_1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL_2_REMARK",
    #                             "sequence": 2
    #                         }
    #                     ],
    #                     "name": "pl_2"
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL1_2_REMARK",
    #                             "sequence": 3
    #                         },
    #                         {
    #                             "action": "permit",
    #                             "prefix": "10.0.0.0/24",
    #                             "sequence": 4
    #                         }
    #                     ],
    #                     "name": "pl1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL2_REMARK",
    #                             "sequence": 5
    #                         }
    #                     ],
    #                     "name": "pl2"
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": false,
    #--------------------------------------------------------------------------
    # Using parsed:
    # --------------
    #
    # parsed.cfg
    #------------------------------
    # ipv6 prefix-list pl_1
    #  1 deny 2001:db8:1234::/48
    # !
    # ipv6 prefix-list pl_2
    #  2 remark TEST_PL_2_REMARK
    # !
    # ipv4 prefix-list pl1
    #  3 remark TEST_PL1_2_REMARK
    #  4 permit 10.0.0.0/24
    # !
    # ipv4 prefix-list pl2
    #  5 remark TEST_PL2_REMARK
    #
    #
    - name: Parse externally provided Prefix_lists config to agnostic model
      cisco.iosxr.iosxr_prefix_lists:
         running_config: "{{ lookup('file', './fixtures/parsed.cfg') }}"
         state: parsed
    #
    # Module execution:
    #"parsed": [
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "prefix": "2001:db8:1234::/48",
    #                             "sequence": 1
    #                         }
    #                     ],
    #                     "name": "pl_1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL_2_REMARK",
    #                             "sequence": 2
    #                         }
    #                     ],
    #                     "name": "pl_2"
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL1_2_REMARK",
    #                             "sequence": 3
    #                         },
    #                         {
    #                             "action": "permit",
    #                             "prefix": "10.0.0.0/24",
    #                             "sequence": 4
    #                         }
    #                     ],
    #                     "name": "pl1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL2_REMARK",
    #                             "sequence": 5
    #                         }
    #                     ],
    #                     "name": "pl2"
    #                 }
    #             ]
    #         }
    #     ]
    #
    #----------------------------------------------------------------------------
    # Using rendered:
    # --------------
    #
    - name: Render platform specific commands from task input using rendered state
      register: result
      cisco.iosxr.iosxr_prefix_lists:
         config:
           - afi: ipv6
             prefix_lists:
               - name: pl_1
                 entries:
                   - prefix: 2001:db8:1234::/48
                     action: deny
                     sequence: 1
               - name: pl_2
                 entries:
                   - sequence: 2
                     action: remark
                     description: TEST_PL_2_REMARK
           - afi: ipv4
             prefix_lists:
               - name: pl1
                 entries:
                   - sequence: 3
                     action: remark
                     description: TEST_PL1_2_REMARK
                   - sequence: 4
                     action: permit
                     prefix: 10.0.0.0/24
               - name: pl2
                 entries:
                   - sequence: 5
                     action: remark
                     description: TEST_PL2_REMARK

         state: rendered
    # After state:
    # Module Execution:
    # "rendered": [
    #         "ipv6 prefix-list pl_1 1 deny 2001:db8:1234::/48",
    #         "ipv6 prefix-list pl_2 2 remark TEST_PL_2_REMARK",
    #         "ipv4 prefix-list pl1 3 remark TEST_PL1_2_REMARK",
    #         "ipv4 prefix-list pl1 4 permit 10.0.0.0/24",
    #         "ipv4 prefix-list pl2 5 remark TEST_PL2_REMARK"
    #     ]
    #
    #---------------------------------------------------------------------------------
    # Using overridden:
    # --------------
    # Before state:
    #RP/0/0/CPU0:10#show running-config
    #
    # ipv6 prefix-list pl_1
    #  1 deny 2001:db8:1234::/48
    # !
    # ipv6 prefix-list pl_2
    #  2 remark TEST_PL_2_REMARK
    # !
    # ipv4 prefix-list pl1
    #  3 remark TEST_PL1_2_REMARK
    #  4 permit 10.0.0.0/24
    # !
    # ipv4 prefix-list pl2
    #  5 remark TEST_PL2_REMARK
    #
    - name: Overridde all Prefix_lists configuration with provided configuration
      cisco.iosxr.iosxr_prefix_lists:
            config:
               - afi: ipv4
                 prefix_lists:
                   - name: pl3
                     entries:
                       - sequence: 3
                         action: remark
                         description: TEST_PL1_3_REMARK
                       - sequence: 4
                         action: permit
                         prefix: 10.0.0.0/24
            state: overridden

    # After state:
    #RP/0/0/CPU0:10#show running-config
    #
    #ipv4 prefix-list pl3
    # 3 remark TEST_PL1_3_REMARK
    # 4 permit 10.0.0.0/24
    #!
    # # Module Execution:
    # "after": [
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL1_3_REMARK",
    #                             "sequence": 3
    #                         },
    #                         {
    #                             "action": "permit",
    #                             "prefix": "10.0.0.0/24",
    #                             "sequence": 4
    #                         }
    #                     ],
    #                     "name": "pl3"
    #                 }
    #             ]
    #         }
    #     ],
    #     "before": [
    #         {
    #             "afi": "ipv6",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "deny",
    #                             "prefix": "2001:db8:1234::/48",
    #                             "sequence": 1
    #                         }
    #                     ],
    #                     "name": "pl_1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL_2_REMARK",
    #                             "sequence": 2
    #                         }
    #                     ],
    #                     "name": "pl_2"
    #                 }
    #             ]
    #         },
    #         {
    #             "afi": "ipv4",
    #             "prefix_lists": [
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL1_2_REMARK",
    #                             "sequence": 3
    #                         },
    #                         {
    #                             "action": "permit",
    #                             "prefix": "10.0.0.0/24",
    #                             "sequence": 4
    #                         }
    #                     ],
    #                     "name": "pl1"
    #                 },
    #                 {
    #                     "entries": [
    #                         {
    #                             "action": "remark",
    #                             "description": "TEST_PL2_REMARK",
    #                             "sequence": 5
    #                         }
    #                     ],
    #                     "name": "pl2"
    #                 }
    #             ]
    #         }
    #     ],
    #     "changed": true,
    #     "commands": [
    #         "no ipv6 prefix-list pl_1",
    #         "no ipv6 prefix-list pl_2",
    #         "no ipv4 prefix-list pl1",
    #         "no ipv4 prefix-list pl2",
    #         "ipv4 prefix-list pl3 3 remark TEST_PL1_3_REMARK",
    #         "ipv4 prefix-list pl3 4 permit 10.0.0.0/24"
    #     ],
    #     "invocation": {
    #         "module_args": {
    #             "config": [
    #                 {
    #                     "afi": "ipv4",
    #                     "prefix_lists": [
    #                         {
    #                             "entries": [
    #                                 {
    #                                     "action": "remark",
    #                                     "description": "TEST_PL1_3_REMARK",
    #                                     "prefix": null,
    #                                     "sequence": 3
    #                                 },
    #                                 {
    #                                     "action": "permit",
    #                                     "description": null,
    #                                     "prefix": "10.0.0.0/24",
    #                                     "sequence": 4
    #                                 }
    #                             ],
    #                             "name": "pl3"
    #                         }
    #                     ]
    #                 }
    #             ],
    #             "running_config": null,
    #             "state": "overridden"
    #         }
    #     }
    # }
    #




Status
------


Authors
~~~~~~~

- Ashwini Mhatre (@amhatre)
