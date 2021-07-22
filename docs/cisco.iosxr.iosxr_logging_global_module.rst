.. _cisco.iosxr.iosxr_logging_global_module:


********************************
cisco.iosxr.iosxr_logging_global
********************************

**Manages logging attributes of Cisco IOSXR network devices**


Version added: 2.4.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module manages the logging attributes of Cisco IOSXR network devices




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
                        <div>A dictionary of logging options.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>archive</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>logging to a persistent device(disk/harddisk)</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>archive_length</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The maximum no of weeks of log to maintain.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>archive_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The total size of the archive.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>device</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure the archive device</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>file_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The maximum file size for a single log file..</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>frequency</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>daily</li>
                                    <li>weekly</li>
                        </ul>
                </td>
                <td>
                        <div>The collection interval for logs.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>informational</li>
                                    <li>notifications</li>
                                    <li>warnings</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Threshold percent &lt;1-99&gt;.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>buffered</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set buffered logging parameters</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>discriminator</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Establish MD-Buffer association</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_params</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>match1</li>
                                    <li>match2</li>
                                    <li>match3</li>
                                    <li>nomatch1</li>
                                    <li>nomatch2</li>
                                    <li>nomatch3</li>
                        </ul>
                </td>
                <td>
                        <div>Set match/no-match discriminator.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>discriminator name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>informational</li>
                                    <li>notifications</li>
                                    <li>warnings</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Logging buffer size</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>console</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set console logging parameters</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>discriminator</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Establish MD-Buffer association</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_params</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>match1</li>
                                    <li>match2</li>
                                    <li>match3</li>
                                    <li>nomatch1</li>
                                    <li>nomatch2</li>
                                    <li>nomatch3</li>
                        </ul>
                </td>
                <td>
                        <div>Set match/no-match discriminator.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>discriminator name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>informational</li>
                                    <li>notifications</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable logging.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>correlator</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure properties of the event correlator</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>buffer_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure size of the correlator buffer.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rule_sets</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a specified correlation ruleset.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the ruleset</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rulename</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the rule</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rules</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure a specified correlation rule.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>context_correlation</b>
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
                        <div>Specify enable correlation on context.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>reissue_nonbistate</b>
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
                        <div>Specify reissue of non-bistate alarms on parent clear.This option is allowed for the rules whose type is stateful.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>reparent</b>
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
                        <div>Specify reparent of alarm on parent clear.This option is allowed for the rules whose type is stateful.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rule_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>name of rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>rule_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>stateful</li>
                                    <li>nonstateful</li>
                        </ul>
                </td>
                <td>
                        <div>type of rule - stateful or nonstateful.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specify timeout.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timeout_rootcause</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify timeout for root-cause.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>events</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure event monitoring parameters.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>buffer_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set size of the local event buffer.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>display_location</b>
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
                        <div>Include alarm source location in message text.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filter_match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure filter.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>informational</li>
                                    <li>notifications</li>
                                    <li>warnings</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>threshold</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Capacity alarm threshold.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>facility</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>auth</li>
                                    <li>cron</li>
                                    <li>daemon</li>
                                    <li>kern</li>
                                    <li>local0</li>
                                    <li>local1</li>
                                    <li>local2</li>
                                    <li>local3</li>
                                    <li>local4</li>
                                    <li>local5</li>
                                    <li>local6</li>
                                    <li>local7</li>
                                    <li>lpr</li>
                                    <li>mail</li>
                                    <li>news</li>
                                    <li>sys10</li>
                                    <li>sys11</li>
                                    <li>sys12</li>
                                    <li>sys13</li>
                                    <li>sys14</li>
                                    <li>sys9</li>
                                    <li>syslog</li>
                                    <li>user</li>
                                    <li>uucp</li>
                        </ul>
                </td>
                <td>
                        <div>Facility parameter for syslog messages</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>files</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set file logging.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maxfilesize</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set max file size.</div>
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
                        <div>name of file.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>info</li>
                                    <li>notifications</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>format</b>
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
                        <div>Enable to send the syslog message rfc5424 format .</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>history</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure syslog history table</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>informational</li>
                                    <li>notifications</li>
                                    <li>warnings</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Logging buffer size</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable logging.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Hostname prefix to add on msgs to servers.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hosts</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set syslog server IP address and parameters</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>IPv4/Ipv6 address or hostname of the syslog server</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"default"</div>
                </td>
                <td>
                        <div>Set &lt;0-65535&gt;  non-default Port.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>error</li>
                                    <li>info</li>
                                    <li>notifications</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                        <div>Set VRF option</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv4</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mark the dscp/precedence bit for ipv4 packets.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dscp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>precedence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set precedence Please refer vendor document for valid entries.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ipv6</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Mark the dscp/precedence bit for ipv4 packets.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dscp</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>precedence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set precedence Please refer vendor document for valid entries.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>localfilesize</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set size of the local log file</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>monitor</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set terminal line (monitor) logging parameters</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>discriminator</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Establish MD-Buffer association</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>match_params</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>match1</li>
                                    <li>match2</li>
                                    <li>match3</li>
                                    <li>nomatch1</li>
                                    <li>nomatch2</li>
                                    <li>nomatch3</li>
                        </ul>
                </td>
                <td>
                        <div>Set match/no-match discriminator.</div>
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
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>discriminator name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>informational</li>
                                    <li>notifications</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable logging.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify interface for source address in logging transactions</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface name with number</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>VPN Routing/Forwarding instance name</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>suppress</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Suppress logging behaviour.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>apply_rule</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Apply suppression rule.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>duplicates</b>
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
                        <div>Suppress consecutive duplicate messages.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tls_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Secure server over tls.</div>
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
                        <div>Name for the tls peer configuration.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>informational</li>
                                    <li>notifications</li>
                                    <li>warnings</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tls_hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the logging host.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trustpoint</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the trustpoint configured.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>name of vrf.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trap</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set syslog server logging level</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>severity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>alerts</li>
                                    <li>critical</li>
                                    <li>debugging</li>
                                    <li>emergencies</li>
                                    <li>errors</li>
                                    <li>informational</li>
                                    <li>notifications</li>
                                    <li>warning</li>
                        </ul>
                </td>
                <td>
                        <div>Logging severity level</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
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
                                    <li>enabled</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>Enable or disable logging.</div>
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
                        <div>The value of this option should be the output received from the IOS device by executing the command <b>show running-config | include logging</b>.</div>
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
                        <div>The state the configuration should be left in</div>
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
    #-----------------
    # Before state
    #RP/0/0/CPU0:10#show running-config logging
    #Thu Feb  4 09:38:36.245 UTC
    #% No such configuration item(s)
    #RP/0/0/CPU0:10#
    #
    #
    #  - name: Merge the provided configuration with the existing running configuration
    #    cisco.iosxr.iosxr_logging_global:
    #         config:
    #           buffered:
    #             size: 2097152
    #             severity: warnings
    #           correlator:
    #             buffer_size: 1024
    #           events:
    #             display_location: True
    #           files:
    #             - maxfilesize: '1024'
    #               name: test
    #               path: test
    #               severity: info
    #           hostnameprefix: test
    #           hosts:
    #             - host: 1.1.1.1
    #               port: default
    #               severity: critical
    #               vrf: default
    #           ipv4:
    #             dscp: af11
    #           localfilesize: 1024
    #           monitor:
    #             severity: errors
    #           source_interfaces:
    #             - interface: GigabitEthernet0/0/0/0
    #               vrf: test
    #           tls_servers:
    #             - name: test
    #               tls_hostname: test2
    #               trustpoint: test2
    #               vrf: test
    #           trap:
    #             severity: informational
    #         state: merged
    #
    #
    # After state:
    #-------------------------------------------
    #RP/0/0/CPU0:10#show running-config logging
    # Tue Jul 20 18:09:18.491 UTC
    # logging tls-server test
    #  vrf test
    #  trustpoint test2
    #  tls-hostname test2
    # !
    # logging file test path test maxfilesize 1024 severity info
    # logging ipv4 dscp af11
    # logging trap informational
    # logging events display-location
    # logging monitor errors
    # logging buffered 2097152
    # logging buffered warnings
    # logging 1.1.1.1 vrf default severity critical port default
    # logging correlator buffer-size 1024
    # logging localfilesize 1024
    # logging source-interface GigabitEthernet0/0/0/0 vrf test
    # logging hostnameprefix test
    #------------------------------------------------
    #Module execution
    #
    #     "after": {
    #         "buffered": {
    #             "severity": "errors"
    #         },
    #         "correlator": {
    #             "buffer_size": 1024
    #         },
    #         "files": [
    #             {
    #                 "maxfilesize": "1024",
    #                 "name": "test",
    #                 "path": "test1",
    #                 "severity": "info"
    #             }
    #         ],
    #         "hostnameprefix": "test1",
    #         "hosts": [
    #             {
    #                 "host": "1.1.1.3",
    #                 "port": "default",
    #                 "severity": "critical",
    #                 "vrf": "default"
    #             }
    #         ],
    #         "ipv6": {
    #             "dscp": "af11"
    #         },
    #         "localfilesize": 1024,
    #         "source_interfaces": [
    #             {
    #                 "interface": "GigabitEthernet0/0/0/0",
    #                 "vrf": "test1"
    #             }
    #         ],
    #         "tls_servers": [
    #             {
    #                 "name": "test",
    #                 "tls_hostname": "test2",
    #                 "trustpoint": "test",
    #                 "vrf": "test"
    #             }
    #         ]
    #     },
    #     "before": {},
    #     "changed": true,
    #     "commands": [
    #         "logging buffered errors",
    #         "logging correlator buffer-size 1024",
    #         "logging hostnameprefix test1",
    #         "logging ipv6 dscp af11",
    #         "logging localfilesize 1024",
    #         "logging trap disable",
    #         "logging monitor disable",
    #         "logging history disable",
    #         "logging console disable",
    #         "logging 1.1.1.3 vrf default severity critical port default",
    #         "logging file test path test1 maxfilesize 1024 severity info",
    #         "logging source-interface GigabitEthernet0/0/0/0 vrf test1",
    #         "logging tls-server test tls-hostname test2",
    #         "logging tls-server test trustpoint test",
    #         "logging tls-server test vrf test"
    #     ],
    #     "invocation": {
    #         "module_args": {
    #             "config": {
    #                 "archive": null,
    #                 "buffered": {
    #                     "discriminator": null,
    #                     "severity": "errors",
    #                     "size": null
    #                 },
    #                 "console": {
    #                     "discriminator": null,
    #                     "severity": null,
    #                     "state": "disabled"
    #                 },
    #                 "correlator": {
    #                     "buffer_size": 1024,
    #                     "rule_set": null,
    #                     "rules": null
    #                 },
    #                 "events": null,
    #                 "facility": null,
    #                 "files": [
    #                     {
    #                         "maxfilesize": "1024",
    #                         "name": "test",
    #                         "path": "test1",
    #                         "severity": "info"
    #                     }
    #                 ],
    #                 "format": null,
    #                 "history": {
    #                     "severity": null,
    #                     "size": null,
    #                     "state": "disabled"
    #                 },
    #                 "hostnameprefix": "test1",
    #                 "hosts": [
    #                     {
    #                         "host": "1.1.1.3",
    #                         "port": "default",
    #                         "severity": "critical",
    #                         "vrf": "default"
    #                     }
    #                 ],
    #                 "ipv4": null,
    #                 "ipv6": {
    #                     "dscp": "af11",
    #                     "precedence": null
    #                 },
    #                 "localfilesize": 1024,
    #                 "monitor": {
    #                     "discriminator": null,
    #                     "severity": null,
    #                     "state": "disabled"
    #                 },
    #                 "source_interfaces": [
    #                     {
    #                         "interface": "GigabitEthernet0/0/0/0",
    #                         "vrf": "test1"
    #                     }
    #                 ],
    #                 "suppress": null,
    #                 "tls_servers": [
    #                     {
    #                         "name": "test",
    #                         "severity": null,
    #                         "tls_hostname": "test2",
    #                         "trustpoint": "test",
    #                         "vrf": "test"
    #                     }
    #                 ],
    #                 "trap": {
    #                     "severity": null,
    #                     "state": "disabled"
    #                 }
    #             },
    #             "running_config": null,
    #             "state": "merged"
    #         }
    #     }
    # }
    #
    # Using replaced:
    # -----------------------------------------------------------
    #
    #Before state
    #RP/0/0/CPU0:10#show running-config logging
    # Tue Jul 20 18:09:18.491 UTC
    # logging tls-server test
    #  vrf test
    #  trustpoint test2
    #  tls-hostname test2
    # !
    # logging file test path test maxfilesize 1024 severity info
    # logging ipv4 dscp af11
    # logging trap informational
    # logging events display-location
    # logging monitor errors
    # logging buffered 2097152
    # logging buffered warnings
    # logging 1.1.1.1 vrf default severity critical port default
    # logging correlator buffer-size 1024
    # logging localfilesize 1024
    # logging source-interface GigabitEthernet0/0/0/0 vrf test
    # logging hostnameprefix test
    #-----------------------------------------------------------
    #
    # - name: Replace BGP configuration with provided configuration
    #   cisco.iosxr.iosxr_logging_global:
    #     state: replaced
    #     config:
    #           buffered:
    #             severity: errors
    #           correlator:
    #             buffer_size: 1024
    #           files:
    #             - maxfilesize: '1024'
    #               name: test
    #               path: test1
    #               severity: info
    #           hostnameprefix: test1
    #           hosts:
    #             - host: 1.1.1.3
    #               port: default
    #               severity: critical
    #               vrf: default
    #           ipv6:
    #             dscp: af11
    #           localfilesize: 1024
    #           monitor:
    #             severity: errors
    #           tls_servers:
    #             - name: test
    #               tls_hostname: test2
    #               trustpoint: test
    #               vrf: test
    #           trap:
    #             severity: critical
    #
    # After state:
    #RP/0/0/CPU0:10#show running-config logging
    # Tue Jul 20 18:31:51.709 UTC
    # logging tls-server test
    #  vrf test
    #  trustpoint test
    #  tls-hostname test2
    # !
    # logging file test path test1 maxfilesize 1024 severity info
    # logging ipv6 dscp af11
    # logging trap critical
    # logging monitor errors
    # logging buffered errors
    # logging 1.1.1.3 vrf default severity critical port default
    # logging correlator buffer-size 1024
    # logging localfilesize 1024
    # logging hostnameprefix test1
    #-----------------------------------------------------------------
    #
    # Module Execution:
    # "after": {
    #         "buffered": {
    #             "severity": "errors"
    #         },
    #         "correlator": {
    #             "buffer_size": 1024
    #         },
    #         "files": [
    #             {
    #                 "maxfilesize": "1024",
    #                 "name": "test",
    #                 "path": "test1",
    #                 "severity": "info"
    #             }
    #         ],
    #         "hostnameprefix": "test1",
    #         "hosts": [
    #             {
    #                 "host": "1.1.1.3",
    #                 "port": "default",
    #                 "severity": "critical",
    #                 "vrf": "default"
    #             }
    #         ],
    #         "ipv6": {
    #             "dscp": "af11"
    #         },
    #         "localfilesize": 1024,
    #         "monitor": {
    #             "severity": "errors"
    #         },
    #         "tls_servers": [
    #             {
    #                 "name": "test",
    #                 "tls_hostname": "test2",
    #                 "trustpoint": "test",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "trap": {
    #             "severity": "critical"
    #         }
    #     },
    #     "before": {
    #         "buffered": {
    #             "severity": "warnings",
    #             "size": 2097152
    #         },
    #         "correlator": {
    #             "buffer_size": 1024
    #         },
    #         "events": {
    #             "display_location": true
    #         },
    #         "files": [
    #             {
    #                 "maxfilesize": "1024",
    #                 "name": "test",
    #                 "path": "test",
    #                 "severity": "info"
    #             }
    #         ],
    #         "hostnameprefix": "test",
    #         "hosts": [
    #             {
    #                 "host": "1.1.1.1",
    #                 "port": "default",
    #                 "severity": "critical",
    #                 "vrf": "default"
    #             }
    #         ],
    #         "ipv4": {
    #             "dscp": "af11"
    #         },
    #         "localfilesize": 1024,
    #         "monitor": {
    #             "severity": "errors"
    #         },
    #         "source_interfaces": [
    #             {
    #                 "interface": "GigabitEthernet0/0/0/0",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "tls_servers": [
    #             {
    #                 "name": "test",
    #                 "tls_hostname": "test2",
    #                 "trustpoint": "test2",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "trap": {
    #             "severity": "informational"
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #         "no logging buffered 2097152",
    #         "no logging events display-location",
    #         "no logging ipv4 dscp af11",
    #         "no logging 1.1.1.1 vrf default severity critical port default",
    #         "no logging source-interface GigabitEthernet0/0/0/0 vrf test",
    #         "logging buffered errors",
    #         "logging hostnameprefix test1",
    #         "logging ipv6 dscp af11",
    #         "logging trap critical",
    #         "logging 1.1.1.3 vrf default severity critical port default",
    #         "logging file test path test1 maxfilesize 1024 severity info",
    #         "logging tls-server test trustpoint test"
    #     ],
    #
    #
    #
    # Using deleted:
    # -----------------------------------------------------------
    # Before state:
    #RP/0/0/CPU0:10#show running-config logging
    # Tue Jul 20 18:09:18.491 UTC
    # logging tls-server test
    #  vrf test
    #  trustpoint test2
    #  tls-hostname test2
    # !
    # logging file test path test maxfilesize 1024 severity info
    # logging ipv4 dscp af11
    # logging trap informational
    # logging events display-location
    # logging monitor errors
    # logging buffered 2097152
    # logging buffered warnings
    # logging 1.1.1.1 vrf default severity critical port default
    # logging correlator buffer-size 1024
    # logging localfilesize 1024
    # logging source-interface GigabitEthernet0/0/0/0 vrf test
    # logging hostnameprefix test
    #
    #-----------------------------------------------------------
    # - name: Delete given logging_global configuration
    #   cisco.iosxr.iosxr_logging_global:
    #     state: deleted
    #
    # After state:
    #RP/0/0/CPU0:10#show running-config
    #
    #-------------------------------------------------------------
    # Module Execution:
    #
    # "after": {},
    #     "before": {
    #         "buffered": {
    #             "severity": "warnings",
    #             "size": 2097152
    #         },
    #         "correlator": {
    #             "buffer_size": 1024
    #         },
    #         "events": {
    #             "display_location": true
    #         },
    #         "files": [
    #             {
    #                 "maxfilesize": "1024",
    #                 "name": "test",
    #                 "path": "test",
    #                 "severity": "info"
    #             }
    #         ],
    #         "hostnameprefix": "test",
    #         "hosts": [
    #             {
    #                 "host": "1.1.1.1",
    #                 "port": "default",
    #                 "severity": "critical",
    #                 "vrf": "default"
    #             }
    #         ],
    #         "ipv4": {
    #             "dscp": "af11"
    #         },
    #         "localfilesize": 1024,
    #         "monitor": {
    #             "severity": "errors"
    #         },
    #         "source_interfaces": [
    #             {
    #                 "interface": "GigabitEthernet0/0/0/0",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "tls_servers": [
    #             {
    #                 "name": "test",
    #                 "tls_hostname": "test2",
    #                 "trustpoint": "test2",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "trap": {
    #             "severity": "informational"
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #         "no logging buffered 2097152",
    #         "no logging buffered warnings",
    #         "no logging correlator buffer-size 1024",
    #         "no logging events display-location",
    #         "no logging hostnameprefix test",
    #         "no logging ipv4 dscp af11",
    #         "no logging localfilesize 1024",
    #         "no logging monitor errors",
    #         "no logging trap informational",
    #         "no logging 1.1.1.1 vrf default severity critical port default",
    #         "no logging file test path test maxfilesize 1024 severity info",
    #         "no logging source-interface GigabitEthernet0/0/0/0 vrf test",
    #         "no logging tls-server test"
    #     ],
    #     "invocation": {
    #         "module_args": {
    #             "config": null,
    #             "running_config": null,
    #             "state": "deleted"
    #         }
    #     }
    #
    #
    #
    # using gathered:
    # ------------------------------------------------------------
    # Before state:
    #RP/0/0/CPU0:10#show running-config logging
    # Tue Jul 20 18:09:18.491 UTC
    # logging tls-server test
    #  vrf test
    #  trustpoint test2
    #  tls-hostname test2
    # !
    # logging file test path test maxfilesize 1024 severity info
    # logging ipv4 dscp af11
    # logging trap informational
    # logging events display-location
    # logging monitor errors
    # logging buffered 2097152
    # logging buffered warnings
    # logging 1.1.1.1 vrf default severity critical port default
    # logging correlator buffer-size 1024
    # logging localfilesize 1024
    # logging source-interface GigabitEthernet0/0/0/0 vrf test
    # logging hostnameprefix test
    #
    #
    # - name: Gather iosxr_logging_global facts using gathered state
    #   cisco.iosxr.iosxr_logging_global:
    #     state: gathered
    #
    #-------------------------------------------------------------
    # Module Execution:
    #
    # "changed": false,
    # "gathered": {
    #         "buffered": {
    #             "severity": "warnings",
    #             "size": 2097152
    #         },
    #         "correlator": {
    #             "buffer_size": 1024
    #         },
    #         "events": {
    #             "display_location": true
    #         },
    #         "files": [
    #             {
    #                 "maxfilesize": "1024",
    #                 "name": "test",
    #                 "path": "test",
    #                 "severity": "info"
    #             }
    #         ],
    #         "hostnameprefix": "test",
    #         "hosts": [
    #             {
    #                 "host": "1.1.1.1",
    #                 "port": "default",
    #                 "severity": "critical",
    #                 "vrf": "default"
    #             }
    #         ],
    #         "ipv4": {
    #             "dscp": "af11"
    #         },
    #         "localfilesize": 1024,
    #         "monitor": {
    #             "severity": "errors"
    #         },
    #         "source_interfaces": [
    #             {
    #                 "interface": "GigabitEthernet0/0/0/0",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "tls_servers": [
    #             {
    #                 "name": "test",
    #                 "tls_hostname": "test2",
    #                 "trustpoint": "test2",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "trap": {
    #             "severity": "informational"
    #         }
    #     },
    #     "invocation": {
    #         "module_args": {
    #             "config": null,
    #             "running_config": null,
    #             "state": "gathered"
    #         }
    # }
    #
    #
    # Using parsed:
    #---------------------------------------------------------------
    #
    # parsed.cfg
    #
    # logging tls-server test
    #  vrf test
    #  trustpoint test2
    #  tls-hostname test2
    # !
    # logging file test path test maxfilesize 1024 severity info
    # logging ipv4 dscp af11
    # logging trap informational
    # logging events display-location
    # logging monitor errors
    # logging buffered 2097152
    # logging buffered warnings
    # logging 1.1.1.1 vrf default severity critical port default
    # logging correlator buffer-size 1024
    # logging localfilesize 1024
    # logging source-interface GigabitEthernet0/0/0/0 vrf test
    # logging hostnameprefix test
    #
    #
    # - name: Parse externally provided Prefix_lists config to agnostic model
    #   cisco.iosxr.iosxr_prefix_lists:
    #     running_config: "{{ lookup('file', './fixtures/parsed.cfg') }}"
    #     state: parsed
    #----------------------------------------------------------------
    # Module execution:
    # "changed": false,
    # "parsed": {
    #         "buffered": {
    #             "severity": "warnings",
    #             "size": 2097152
    #         },
    #         "correlator": {
    #             "buffer_size": 1024
    #         },
    #         "events": {
    #             "display_location": true
    #         },
    #         "files": [
    #             {
    #                 "maxfilesize": "1024",
    #                 "name": "test",
    #                 "path": "test",
    #                 "severity": "info"
    #             }
    #         ],
    #         "hostnameprefix": "test",
    #         "hosts": [
    #             {
    #                 "host": "1.1.1.1",
    #                 "port": "default",
    #                 "severity": "critical",
    #                 "vrf": "default"
    #             }
    #         ],
    #         "ipv4": {
    #             "dscp": "af11"
    #         },
    #         "localfilesize": 1024,
    #         "monitor": {
    #             "severity": "errors"
    #         },
    #         "source_interfaces": [
    #             {
    #                 "interface": "GigabitEthernet0/0/0/0",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "tls_servers": [
    #             {
    #                 "name": "test",
    #                 "tls_hostname": "test2",
    #                 "trustpoint": "test2",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "trap": {
    #             "severity": "informational"
    #         }
    #     }
    #
    #
    # Using rendered:
    # ----------------------------------------------------------------------------
    # - name: Render platform specific configuration lines with state rendered (without connecting to the device)
    #   cisco.iosxr.iosxr_logging_global:
    #     state: rendered
    #     config:
    #       buffered:
    #         size: 2097152
    #         severity: warnings
    #       correlator:
    #         buffer_size: 1024
    #       events:
    #         display_location: True
    #       files:
    #         - maxfilesize: '1024'
    #           name: test
    #           path: test
    #           severity: info
    #       hostnameprefix: test
    #       hosts:
    #         - host: 1.1.1.1
    #           port: default
    #           severity: critical
    #           vrf: default
    #       ipv4:
    #         dscp: af11
    #       localfilesize: 1024
    #       monitor:
    #         severity: errors
    #       source_interfaces:
    #         - interface: GigabitEthernet0/0/0/0
    #           vrf: test
    #       tls_servers:
    #         - name: test
    #           tls_hostname: test2
    #           trustpoint: test2
    #           vrf: test
    #       trap:
    #         severity: informational
    #----------------------------------------------------------------
    # Module Execution:
    # "rendered": [
    #         "logging buffered errors",
    #         "logging correlator buffer-size 1024",
    #         "logging hostnameprefix test1",
    #         "logging ipv6 dscp af11",
    #         "logging localfilesize 1024",
    #         "logging trap disable",
    #         "logging monitor disable",
    #         "logging history disable",
    #         "logging console disable",
    #         "logging 1.1.1.3 vrf default severity critical port default",
    #         "logging file test path test1 maxfilesize 1024 severity info",
    #         "logging source-interface GigabitEthernet0/0/0/0 vrf test1",
    #         "logging tls-server test tls-hostname test2",
    #         "logging tls-server test trustpoint test",
    #         "logging tls-server test vrf test"
    #     ]
    #
    # Using overridden:
    # ---------------------------------------------------------------------------------
    # Before state:
    #RP/0/0/CPU0:10#show running-config logging
    # Tue Jul 20 18:09:18.491 UTC
    # logging tls-server test
    #  vrf test
    #  trustpoint test2
    #  tls-hostname test2
    # !
    # logging file test path test maxfilesize 1024 severity info
    # logging ipv4 dscp af11
    # logging trap informational
    # logging events display-location
    # logging monitor errors
    # logging buffered 2097152
    # logging buffered warnings
    # logging 1.1.1.1 vrf default severity critical port default
    # logging correlator buffer-size 1024
    # logging localfilesize 1024
    # logging source-interface GigabitEthernet0/0/0/0 vrf test
    # logging hostnameprefix test
    #
    #-----------------------------------------------------------
    #
    # - name: Overridde BGP configuration with provided configuration
    #   cisco.iosxr.iosxr_logging_global: &id002
    #     state: overridden
    #     config:
    #           buffered:
    #             severity: errors
    #           correlator:
    #             buffer_size: 1024
    #           files:
    #             - maxfilesize: '1024'
    #               name: test
    #               path: test1
    #               severity: info
    #           hostnameprefix: test1
    #           hosts:
    #             - host: 1.1.1.3
    #               port: default
    #               severity: critical
    #               vrf: default
    #           ipv6:
    #             dscp: af11
    #           localfilesize: 1024
    #           monitor:
    #             severity: errors
    #           tls_servers:
    #             - name: test
    #               tls_hostname: test2
    #               trustpoint: test
    #               vrf: test
    #           trap:
    #             severity: critical
    #
    # After state:
    #RP/0/0/CPU0:10#show running-config logging
    # Tue Jul 20 18:31:51.709 UTC
    # logging tls-server test
    #  vrf test
    #  trustpoint test
    #  tls-hostname test2
    # !
    # logging file test path test1 maxfilesize 1024 severity info
    # logging ipv6 dscp af11
    # logging trap critical
    # logging monitor errors
    # logging buffered errors
    # logging 1.1.1.3 vrf default severity critical port default
    # logging correlator buffer-size 1024
    # logging localfilesize 1024
    # logging hostnameprefix test1
    #-----------------------------------------------------------------
    #
    # Module Execution:
    # "after": {
    #         "buffered": {
    #             "severity": "errors"
    #         },
    #         "correlator": {
    #             "buffer_size": 1024
    #         },
    #         "files": [
    #             {
    #                 "maxfilesize": "1024",
    #                 "name": "test",
    #                 "path": "test1",
    #                 "severity": "info"
    #             }
    #         ],
    #         "hostnameprefix": "test1",
    #         "hosts": [
    #             {
    #                 "host": "1.1.1.3",
    #                 "port": "default",
    #                 "severity": "critical",
    #                 "vrf": "default"
    #             }
    #         ],
    #         "ipv6": {
    #             "dscp": "af11"
    #         },
    #         "localfilesize": 1024,
    #         "monitor": {
    #             "severity": "errors"
    #         },
    #         "tls_servers": [
    #             {
    #                 "name": "test",
    #                 "tls_hostname": "test2",
    #                 "trustpoint": "test",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "trap": {
    #             "severity": "critical"
    #         }
    #     },
    #     "before": {
    #         "buffered": {
    #             "severity": "warnings",
    #             "size": 2097152
    #         },
    #         "correlator": {
    #             "buffer_size": 1024
    #         },
    #         "events": {
    #             "display_location": true
    #         },
    #         "files": [
    #             {
    #                 "maxfilesize": "1024",
    #                 "name": "test",
    #                 "path": "test",
    #                 "severity": "info"
    #             }
    #         ],
    #         "hostnameprefix": "test",
    #         "hosts": [
    #             {
    #                 "host": "1.1.1.1",
    #                 "port": "default",
    #                 "severity": "critical",
    #                 "vrf": "default"
    #             }
    #         ],
    #         "ipv4": {
    #             "dscp": "af11"
    #         },
    #         "localfilesize": 1024,
    #         "monitor": {
    #             "severity": "errors"
    #         },
    #         "source_interfaces": [
    #             {
    #                 "interface": "GigabitEthernet0/0/0/0",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "tls_servers": [
    #             {
    #                 "name": "test",
    #                 "tls_hostname": "test2",
    #                 "trustpoint": "test2",
    #                 "vrf": "test"
    #             }
    #         ],
    #         "trap": {
    #             "severity": "informational"
    #         }
    #     },
    #     "changed": true,
    #     "commands": [
    #         "no logging buffered 2097152",
    #         "no logging events display-location",
    #         "no logging ipv4 dscp af11",
    #         "no logging 1.1.1.1 vrf default severity critical port default",
    #         "no logging source-interface GigabitEthernet0/0/0/0 vrf test",
    #         "logging buffered errors",
    #         "logging hostnameprefix test1",
    #         "logging ipv6 dscp af11",
    #         "logging trap critical",
    #         "logging 1.1.1.3 vrf default severity critical port default",
    #         "logging file test path test1 maxfilesize 1024 severity info",
    #         "logging tls-server test trustpoint test"
    #     ],
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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em>, <em>deleted</em> or <em>purged</em></td>
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
                <td>when state is <em>merged</em>, <em>replaced</em>, <em>overridden</em>, <em>deleted</em> or <em>purged</em></td>
                <td>
                            <div>The set of commands pushed to the remote device.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;logging file test path test1 maxfilesize 1024 severity info&#x27;, &#x27;logging ipv6 dscp af11&#x27;, &#x27;logging trap critical&#x27;, &#x27;logging monitor errors&#x27;, &#x27;logging buffered errors&#x27;, &#x27;logging 1.1.1.3 vrf default severity critical port default&#x27;]</div>
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
                <td>when state is <em>gathered</em></td>
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
                <td>when state is <em>parsed</em></td>
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
                <td>when state is <em>rendered</em></td>
                <td>
                            <div>The provided configuration in the task rendered in device-native format (offline).</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;logging buffered errors&#x27;, &#x27;logging correlator buffer-size 1024&#x27;, &#x27;logging hostnameprefix test1&#x27;, &#x27;logging ipv6 dscp af11&#x27;, &#x27;logging localfilesize 1024&#x27;, &#x27;logging trap disable&#x27;, &#x27;logging monitor disable&#x27;, &#x27;logging history disable&#x27;, &#x27;logging console disable&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ashwini Mhatre (@amhatre)
