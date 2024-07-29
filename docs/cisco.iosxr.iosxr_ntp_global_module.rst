.. _cisco.iosxr.iosxr_ntp_global_module:


****************************
cisco.iosxr.iosxr_ntp_global
****************************

**Resource module to configure NTP.**


Version added: 2.5.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module configures and manages the attributes of  ntp on Cisco IOSXR platforms.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="5">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="5">
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
                        <div>A dictionary of ntp options</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>access_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Control NTP access</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Configure IPv4 access</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide full access</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>query_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allow only control queries.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide server and query access.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide only server access.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Configure IPv6 access</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide full access</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>query_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allow only control queries.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide server and query access.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide only server access.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vrfs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify non-default VRF.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configure IPv4 access</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide full access</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>query_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allow only control queries.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide server and query access.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide only server access.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
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
                        <div>Configure IPv6 access</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide full access</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>query_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Allow only control queries.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide server and query access.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>serve_only</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Provide only server access.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Specify non-default VRF.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authenticate</b>
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
                        <div>Authenticate time sources</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>authentication_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Authentication key for trusted time sources</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>encryption</b>
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
                        <div>Type of key encrypted or clear-text.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>&lt;1-65535&gt;  Key number</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Authentication key.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>broadcastdelay</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Estimated round-trip delay in microseconds.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>drift</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Drift(cisco-support)</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>aging_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Aging time in hours.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>file</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>File for drift values.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interfaces</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NTP on an interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>broadcast_client</b>
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
                        <div>Listen to NTP broadcasts</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>broadcast_destination</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure broadcast destination address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>broadcast_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Broadcast key number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>broadcast_version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>&lt;2-4&gt;  NTP version number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multicast_client</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure multicast client</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multicast_destination</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure multicast destination</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multicast_key</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure multicast authentication key.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multicast_ttl</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure TTL to use.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multicast_version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>&lt;2-4&gt;  NTP version number.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Name of the interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Name of the vrf.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                <td colspan="3">
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
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>precedence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>critical</li>
                                    <li>flash</li>
                                    <li>flash-override</li>
                                    <li>immediate</li>
                                    <li>internet</li>
                                    <li>network</li>
                                    <li>priority</li>
                                    <li>routine</li>
                        </ul>
                </td>
                <td>
                        <div>Set precedence Please refer vendor document for valid entries.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
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
                <td colspan="3">
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
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>precedence</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>critical</li>
                                    <li>flash</li>
                                    <li>flash-override</li>
                                    <li>immediate</li>
                                    <li>internet</li>
                                    <li>network</li>
                                    <li>priority</li>
                                    <li>routine</li>
                        </ul>
                </td>
                <td>
                        <div>Set precedence Please refer vendor document for valid entries.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_internal_sync</b>
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
                        <div>Logs internal synchronization changes.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>master</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Act as NTP master clock</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>stratum</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use NTP as clock source with stratum number &lt;1-15&gt;</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_associations</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>&lt;0-4294967295&gt;  Number of associations.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>passive</b>
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
                        <div>Enable the passive associations.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NTP peer.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>burst</b>
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
                        <div>Use burst mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>iburst</b>
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
                        <div>Use initial burst mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SConfigure peer authentication key</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maxpoll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure Maximum poll interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>minpoll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure Minimum poll interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>peer</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Hostname or A.B.C.D or A:B:C:D:E:F:G:H.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefer</b>
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
                        <div>Prefer this peer when possible</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface for source address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP version.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>vrf name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure NTP server.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>burst</b>
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
                        <div>Use burst mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>iburst</b>
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
                        <div>Use initial burst mode.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>SConfigure peer authentication key</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>maxpoll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure Maximum poll interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>minpoll</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>configure Minimum poll interval.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>prefer</b>
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
                        <div>Prefer this peer when possible</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>server</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Hostname or A.B.C.D or A:B:C:D:E:F:G:H.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Interface for source address.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>NTP version.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>vrf name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_interface</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure default interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>source_vrfs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Configure default interface.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>Name of source interface.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        <div>vrf name.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>trusted_keys</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>list of Key numbers for trusted time sources.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>key_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Key numbers for trusted time sources.</div>
                </td>
            </tr>

            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>update_calendar</b>
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
                        <div>Periodically update calendar with NTP time.</div>
                </td>
            </tr>

            <tr>
                <td colspan="5">
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
                        <div>The value of this option should be the output received from the IOSXR device by executing the command <b>show running-config ntp</b>.</div>
                        <div>The state <em>parsed</em> reads the configuration from <code>running_config</code> option and transforms it into Ansible structured data as per the resource module&#x27;s argspec and the value is then returned in the <em>parsed</em> key within the result.</div>
                </td>
            </tr>
            <tr>
                <td colspan="5">
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
                        <div>The state the configuration should be left in.</div>
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

    # Using state: merged
    # Before state:
    # -------------
    # RP/0/0/CPU0:10#show running-config ntp
    # --------------------- EMPTY -----------------
    # Merged play:
    # ------------
    - name: Merge the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_ntp_global:
        config:
          access_group:
            ipv4:
              peer: PeerAcl1
              query_only: QueryOnlyAcl1
              serve: ServeAcl1
              serve_only: ServeOnlyAcl1
            vrfs:
              - ipv4:
                  peer: PeerAcl3
                  serve: ServeAcl2
                name: siteA
          authenticate: true
          broadcastdelay: 1
          drift:
            aging_time: 0
            file: apphost
          interfaces:
            - name: GigabitEthernet0/0/0/0
              multicast_client: 224.0.0.8
              multicast_destination: 224.0.0.8
              broadcast_client: true
          ipv4:
            dscp: af11
          ipv6:
            precedence: routine
          log_internal_sync: true
          master: 1
          max_associations: 10
          passive: true
          peers:
            - iburst: true
              peer: 192.0.2.1
              vrf: siteC
          servers:
            - burst: true
              server: 192.0.2.2
              vrf: siteD
          source: GigabitEthernet0/0/0/0
          source_vrfs:
            - name: GigabitEthernet0/0/0/0
              vrf: siteE
          trusted_keys:
            - key_id: 1
          update_calendar: true
    # Commands Fired:
    # ------------
    # "commands": [
    #         "ntp peer vrf siteC 192.0.2.1 iburst ",
    #         "ntp server vrf siteD 192.0.2.2 burst ",
    #         "ntp trusted-key 1",
    #         "ntp interface GigabitEthernet0/0/0/0 broadcast client",
    #         "ntp interface GigabitEthernet0/0/0/0 multicast destination 224.0.0.8",
    #         "ntp interface GigabitEthernet0/0/0/0 multicast client 224.0.0.8",
    #         "ntp vrf siteE source GigabitEthernet0/0/0/0",
    #         "ntp access-group vrf siteA ipv4 serve ServeAcl2",
    #         "ntp access-group vrf siteA ipv4 peer PeerAcl3",
    #         "ntp access-group ipv4 peer PeerAcl1",
    #         "ntp access-group ipv4 serve ServeAcl1",
    #         "ntp access-group ipv4 serve-only ServeOnlyAcl1",
    #         "ntp access-group ipv4 query-only QueryOnlyAcl1",
    #         "ntp authenticate",
    #         "ntp log-internal-sync",
    #         "ntp broadcastdelay 1",
    #         "ntp drift aging time 0",
    #         "ntp drift file apphost",
    #         "ntp ipv4 dscp af11",
    #         "ntp ipv6 precedence routine",
    #         "ntp max-associations 10",
    #         "ntp master 1",
    #         "ntp passive",
    #         "ntp update-calendar",
    #         "ntp source GigabitEthernet0/0/0/0"
    #     ],
    # After state:
    # ------------
    # RP/0/0/CPU0:10#show running-config ntp
    # ntp
    #  max-associations 10
    #  interface GigabitEthernet0/0/0/0
    #   broadcast client
    #   multicast client 224.0.0.8
    #   multicast destination 224.0.0.8
    #  !
    #  authenticate
    #  trusted-key 1
    #  ipv4 dscp af11
    #  ipv6 precedence routine
    #  peer vrf siteC 192.0.2.1 iburst
    #  server vrf siteD 192.0.2.2 burst
    #  drift file apphost
    #  drift aging time 0
    #  master 1
    #  access-group vrf siteA ipv4 peer PeerAcl3
    #  access-group vrf siteA ipv4 serve ServeAcl2
    #  access-group ipv4 peer PeerAcl1
    #  access-group ipv4 serve ServeAcl1
    #  access-group ipv4 serve-only ServeOnlyAcl1
    #  access-group ipv4 query-only QueryOnlyAcl1
    #  source vrf siteE GigabitEthernet0/0/0/0
    #  source GigabitEthernet0/0/0/0
    #  passive
    #  broadcastdelay 1
    #  update-calendar
    #  log-internal-sync
    # !
    # Using state: deleted
    # Before state:
    # -------------
    # RP/0/0/CPU0:10#show running-config ntp
    # ntp
    #  max-associations 10
    #  interface GigabitEthernet0/0/0/0
    #   broadcast client
    #   multicast client 224.0.0.8
    #   multicast destination 224.0.0.8
    #  !
    #  authenticate
    #  trusted-key 1
    #  ipv4 dscp af11
    #  ipv6 precedence routine
    #  peer vrf siteC 192.0.2.1 iburst
    #  server vrf siteD 192.0.2.2 burst
    #  drift file apphost
    #  drift aging time 0
    #  master 1
    #  access-group vrf siteA ipv4 peer PeerAcl3
    #  access-group vrf siteA ipv4 serve ServeAcl2
    #  access-group ipv4 peer PeerAcl1
    #  access-group ipv4 serve ServeAcl1
    #  access-group ipv4 serve-only ServeOnlyAcl1
    #  access-group ipv4 query-only QueryOnlyAcl1
    #  source vrf siteE GigabitEthernet0/0/0/0
    #  source GigabitEthernet0/0/0/0
    #  passive
    #  broadcastdelay 1
    #  update-calendar
    #  log-internal-sync
    # !
    # Deleted play:
    # -------------
    - name: Remove all existing configuration
      cisco.iosxr.iosxr_ntp_global:
        state: deleted
    # Commands Fired:
    # ---------------
    # "commands": [
    #         "no ntp peer vrf siteC 192.0.2.1 iburst ",
    #         "no ntp server vrf siteD 192.0.2.2 burst ",
    #         "no ntp trusted-key 1",
    #         "no ntp interface GigabitEthernet0/0/0/0",
    #         "no ntp vrf siteE source GigabitEthernet0/0/0/0",
    #         "no ntp access-group vrf siteA ipv4 serve ServeAcl2",
    #         "no ntp access-group vrf siteA ipv4 peer PeerAcl3",
    #         "no ntp access-group ipv4 peer PeerAcl1",
    #         "no ntp access-group ipv4 serve ServeAcl1",
    #         "no ntp access-group ipv4 serve-only ServeOnlyAcl1",
    #         "no ntp access-group ipv4 query-only QueryOnlyAcl1",
    #         "no ntp authenticate",
    #         "no ntp log-internal-sync",
    #         "no ntp broadcastdelay 1",
    #         "no ntp drift aging time 0",
    #         "no ntp drift file apphost",
    #         "no ntp ipv4 dscp af11",
    #         "no ntp ipv6 precedence routine",
    #         "no ntp max-associations 10",
    #         "no ntp master 1",
    #         "no ntp passive",
    #         "no ntp update-calendar",
    #         "no ntp source GigabitEthernet0/0/0/0"
    #     ],
    # After state:
    # ------------
    # RP/0/0/CPU0:10#show running-config ntp
    # --------------------- EMPTY -----------------
    # Using state: overridden
    # Before state:
    # -------------
    # RP/0/0/CPU0:10#show running-config ntp
    # ntp
    #  max-associations 10
    #  interface GigabitEthernet0/0/0/0
    #   broadcast client
    #   multicast client 224.0.0.8
    #   multicast destination 224.0.0.8
    #  !
    #  authenticate
    #  trusted-key 1
    #  ipv4 dscp af11
    #  ipv6 precedence routine
    #  peer vrf siteC 192.0.2.1 iburst
    #  server vrf siteD 192.0.2.2 burst
    #  drift file apphost
    #  drift aging time 0
    #  master 1
    #  access-group vrf siteA ipv4 peer PeerAcl3
    #  access-group vrf siteA ipv4 serve ServeAcl2
    #  access-group ipv4 peer PeerAcl1
    #  access-group ipv4 serve ServeAcl1
    #  access-group ipv4 serve-only ServeOnlyAcl1
    #  access-group ipv4 query-only QueryOnlyAcl1
    #  source vrf siteE GigabitEthernet0/0/0/0
    #  source GigabitEthernet0/0/0/0
    #  passive
    #  broadcastdelay 1
    #  update-calendar
    #  log-internal-sync
    # !
    # Overridden play:
    # ----------------
    - name: Override BGP configuration with provided configuration
      cisco.iosxr.iosxr_ntp_global:
        state: overridden
        config:
          access_group:
            ipv4:
              peer: PeerAcl1
              query_only: QueryOnlyAcl1
              serve: ServeAcl4
              serve_only: ServeOnlyAcl1
            vrfs:
              - ipv4:
                  peer: PeerAcl3
                  serve: ServeAcl2
                name: siteA
          authenticate: true
          broadcastdelay: 1
          drift:
            aging_time: 0
            file: apphost
          interfaces:
            - name: GigabitEthernet0/0/0/1
              multicast_client: 224.0.0.8
              multicast_destination: 224.0.0.8
              broadcast_client: true
          ipv4:
            dscp: af12
          ipv6:
            precedence: routine
          log_internal_sync: true
          master: 1
          max_associations: 10
          passive: true
          peers:
            - iburst: true
              peer: 192.0.2.3
              vrf: siteC
          servers:
            - burst: true
              server: 192.0.2.2
              vrf: siteD
          source: GigabitEthernet0/0/0/1
          source_vrfs:
            - name: GigabitEthernet0/0/0/0
              vrf: siteE
          trusted_keys:
            - key_id: 1
          update_calendar: true
    # Commands Fired:
    # ---------------
    # "commands": [
    #         "no ntp peer vrf siteC 192.0.2.1 iburst ",
    #         "no ntp interface GigabitEthernet0/0/0/0",
    #         "ntp peer vrf siteC 192.0.2.3 iburst ",
    #         "ntp interface GigabitEthernet0/0/0/1 broadcast client",
    #         "ntp interface GigabitEthernet0/0/0/1 multicast destination 224.0.0.8",
    #         "ntp interface GigabitEthernet0/0/0/1 multicast client 224.0.0.8",
    #         "ntp access-group ipv4 serve ServeAcl4",
    #         "ntp ipv4 dscp af12",
    #         "ntp source GigabitEthernet0/0/0/1"
    #     ],
    # After state:
    # ------------
    # RP/0/RP0/CPU0:ios#show running-config ntp
    # Mon Sep 13 10:38:22.690 UTC
    # ntp
    #  max-associations 10
    #  interface GigabitEthernet0/0/0/1
    #   broadcast client
    #   multicast client 224.0.0.8
    #   multicast destination 224.0.0.8
    #  !
    #  authentication-key 1 md5 encrypted testkey
    #  authenticate
    #  trusted-key 1
    #  ipv4 dscp af12
    #  ipv6 precedence routine
    #  peer vrf siteC 192.0.2.3 iburst
    #  server vrf siteD 192.0.2.2 burst
    #  drift file apphost
    #  drift aging time 0
    #  master 1
    #  access-group vrf siteA ipv4 peer PeerAcl3
    #  access-group vrf siteA ipv4 serve ServeAcl2
    #  access-group ipv4 peer PeerAcl1
    #  access-group ipv4 serve ServeAcl4
    #  access-group ipv4 serve-only ServeOnlyAcl1
    #  access-group ipv4 query-only QueryOnlyAcl1
    #  source vrf siteE GigabitEthernet0/0/0/0
    #  source GigabitEthernet0/0/0/1
    #  passive
    #  broadcastdelay 1
    #  update-calendar
    #  log-internal-sync
    # !
    #
    # Using state: replaced
    # Before state:
    # -------------
    # RP/0/0/CPU0:10#show running-config ntp
    # ntp
    #  max-associations 10
    #  interface GigabitEthernet0/0/0/0
    #   broadcast client
    #   multicast client 224.0.0.8
    #   multicast destination 224.0.0.8
    #  !
    #  authenticate
    #  trusted-key 1
    #  ipv4 dscp af11
    #  ipv6 precedence routine
    #  peer vrf siteC 192.0.2.1 iburst
    #  server vrf siteD 192.0.2.2 burst
    #  drift file apphost
    #  drift aging time 0
    #  master 1
    #  access-group vrf siteA ipv4 peer PeerAcl3
    #  access-group vrf siteA ipv4 serve ServeAcl2
    #  access-group ipv4 peer PeerAcl1
    #  access-group ipv4 serve ServeAcl1
    #  access-group ipv4 serve-only ServeOnlyAcl1
    #  access-group ipv4 query-only QueryOnlyAcl1
    #  source vrf siteE GigabitEthernet0/0/0/0
    #  source GigabitEthernet0/0/0/0
    #  passive
    #  broadcastdelay 1
    #  update-calendar
    #  log-internal-sync
    # !
    # Replaced play:
    # ----------------
    - name: Replaced BGP configuration with provided configuration
      cisco.iosxr.iosxr_ntp_global:
        state: replaced
        config:
          access_group:
            ipv4:
              peer: PeerAcl1
              query_only: QueryOnlyAcl1
              serve: ServeAcl4
              serve_only: ServeOnlyAcl1
            vrfs:
              - ipv4:
                  peer: PeerAcl3
                  serve: ServeAcl2
                name: siteA
          authenticate: true
          broadcastdelay: 1
          drift:
            aging_time: 0
            file: apphost
          interfaces:
            - name: GigabitEthernet0/0/0/1
              multicast_client: 224.0.0.8
              multicast_destination: 224.0.0.8
              broadcast_client: true
          ipv4:
            dscp: af12
          ipv6:
            precedence: routine
          log_internal_sync: true
          master: 1
          max_associations: 10
          passive: true
          peers:
            - iburst: true
              peer: 192.0.2.3
              vrf: siteC
          servers:
            - burst: true
              server: 192.0.2.2
              vrf: siteD
          source: GigabitEthernet0/0/0/1
          source_vrfs:
            - name: GigabitEthernet0/0/0/0
              vrf: siteE
          trusted_keys:
            - key_id: 1
          update_calendar: true
    # Commands Fired:
    # ---------------
    # "commands": [
    #         "no ntp peer vrf siteC 192.0.2.1 iburst ",
    #         "no ntp interface GigabitEthernet0/0/0/0",
    #         "ntp peer vrf siteC 192.0.2.3 iburst ",
    #         "ntp interface GigabitEthernet0/0/0/1 broadcast client",
    #         "ntp interface GigabitEthernet0/0/0/1 multicast destination 224.0.0.8",
    #         "ntp interface GigabitEthernet0/0/0/1 multicast client 224.0.0.8",
    #         "ntp access-group ipv4 serve ServeAcl4",
    #         "ntp ipv4 dscp af12",
    #         "ntp source GigabitEthernet0/0/0/1"
    #     ],
    # After state:
    # ------------
    # RP/0/RP0/CPU0:ios#show running-config ntp
    # Mon Sep 13 10:38:22.690 UTC
    # ntp
    #  max-associations 10
    #  interface GigabitEthernet0/0/0/1
    #   broadcast client
    #   multicast client 224.0.0.8
    #   multicast destination 224.0.0.8
    #  !
    #  authentication-key 1 md5 encrypted testkey
    #  authenticate
    #  trusted-key 1
    #  ipv4 dscp af12
    #  ipv6 precedence routine
    #  peer vrf siteC 192.0.2.3 iburst
    #  server vrf siteD 192.0.2.2 burst
    #  drift file apphost
    #  drift aging time 0
    #  master 1
    #  access-group vrf siteA ipv4 peer PeerAcl3
    #  access-group vrf siteA ipv4 serve ServeAcl2
    #  access-group ipv4 peer PeerAcl1
    #  access-group ipv4 serve ServeAcl4
    #  access-group ipv4 serve-only ServeOnlyAcl1
    #  access-group ipv4 query-only QueryOnlyAcl1
    #  source vrf siteE GigabitEthernet0/0/0/0
    #  source GigabitEthernet0/0/0/1
    #  passive
    #  broadcastdelay 1
    #  update-calendar
    #  log-internal-sync
    # !
    # Using state: gathered
    # Before state:
    # -------------
    # RP/0/0/CPU0:10#show running-config ntp
    # ntp
    #  max-associations 10
    #  interface GigabitEthernet0/0/0/0
    #   broadcast client
    #   multicast client 224.0.0.8
    #   multicast destination 224.0.0.8
    #  !
    #  authenticate
    #  trusted-key 1
    #  ipv4 dscp af11
    #  ipv6 precedence routine
    #  peer vrf siteC 192.0.2.1 iburst
    #  server vrf siteD 192.0.2.2 burst
    #  drift file apphost
    #  drift aging time 0
    #  master 1
    #  access-group vrf siteA ipv4 peer PeerAcl3
    #  access-group vrf siteA ipv4 serve ServeAcl2
    #  access-group ipv4 peer PeerAcl1
    #  access-group ipv4 serve ServeAcl1
    #  access-group ipv4 serve-only ServeOnlyAcl1
    #  access-group ipv4 query-only QueryOnlyAcl1
    #  source vrf siteE GigabitEthernet0/0/0/0
    #  source GigabitEthernet0/0/0/0
    #  passive
    #  broadcastdelay 1
    #  update-calendar
    #  log-internal-sync
    # !
    # Gathered play:
    # --------------
    - name: Gather listed ntp config
      cisco.iosxr.iosxr_ntp_global:
        state: gathered
    # Module Execution Result:
    # ------------------------
    # "gathered":{
    #         "access_group": {
    #             "ipv4": {
    #                 "peer": "PeerAcl1",
    #                 "query_only": "QueryOnlyAcl1",
    #                 "serve": "ServeAcl1",
    #                 "serve_only": "ServeOnlyAcl1"
    #             },
    #             "vrfs": [
    #                 {
    #                     "ipv4": {
    #                         "peer": "PeerAcl3",
    #                         "serve": "ServeAcl2"
    #                     },
    #                     "name": "siteA"
    #                 }
    #             ]
    #         },
    #         "authenticate": true,
    #         "broadcastdelay": 1,
    #         "drift": {
    #             "aging_time": 0,
    #             "file": "apphost"
    #         },
    #         "interfaces": [
    #             {
    #                 "broadcast_client": true,
    #                 "multicast_client": "224.0.0.8",
    #                 "multicast_destination": "224.0.0.8",
    #                 "name": "GigabitEthernet0/0/0/0"
    #             }
    #         ],
    #         "ipv4": {
    #             "dscp": "af11"
    #         },
    #         "ipv6": {
    #             "precedence": "routine"
    #         },
    #         "log_internal_sync": true,
    #         "master": 1,
    #         "max_associations": 10,
    #         "passive": true,
    #         "peers": [
    #             {
    #                 "iburst": true,
    #                 "peer": "192.0.2.1",
    #                 "vrf": "siteC"
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "burst": true,
    #                 "server": "192.0.2.2",
    #                 "vrf": "siteD"
    #             }
    #         ],
    #         "source": "GigabitEthernet0/0/0/0",
    #         "source_vrfs": [
    #             {
    #                 "name": "GigabitEthernet0/0/0/0",
    #                 "vrf": "siteE"
    #             }
    #         ],
    #         "trusted_keys": [
    #             {
    #                 "key_id": 1
    #             }
    #         ],
    #         "update_calendar": true
    #     }
    # Using state: rendered
    # Rendered play:
    # --------------
    - name: >-
        Render platform specific configuration lines with state rendered (without
        connecting to the device)
      cisco.iosxr.iosxr_ntp_global:
        state: rendered
        config:
          access_group:
            ipv4:
              peer: PeerAcl1
              query_only: QueryOnlyAcl1
              serve: ServeAcl1
              serve_only: ServeOnlyAcl1
            vrfs:
              - ipv4:
                  peer: PeerAcl3
                  serve: ServeAcl2
                name: siteA
          authenticate: true
          broadcastdelay: 1
          drift:
            aging_time: 0
            file: apphost
          interfaces:
            - name: GigabitEthernet0/0/0/0
              multicast_client: 224.0.0.8
              multicast_destination: 224.0.0.8
              broadcast_client: true
          ipv4:
            dscp: af11
          ipv6:
            precedence: routine
          log_internal_sync: true
          master: 1
          max_associations: 10
          passive: true
          peers:
            - iburst: true
              peer: 192.0.2.1
              vrf: siteC
          servers:
            - burst: true
              server: 192.0.2.2
              vrf: siteD
          source: GigabitEthernet0/0/0/0
          source_vrfs:
            - name: GigabitEthernet0/0/0/0
              vrf: siteE
          trusted_keys:
            - key_id: 1
          update_calendar: true
      register: result
    # Module Execution Result:
    # ------------------------
    # "rendered": [
    #         "ntp peer vrf siteC 192.0.2.1 iburst ",
    #         "ntp server vrf siteD 192.0.2.2 burst ",
    #         "ntp trusted-key 1",
    #         "ntp interface GigabitEthernet0/0/0/0 broadcast client",
    #         "ntp interface GigabitEthernet0/0/0/0 multicast destination 224.0.0.8",
    #         "ntp interface GigabitEthernet0/0/0/0 multicast client 224.0.0.8",
    #         "ntp vrf siteE source GigabitEthernet0/0/0/0",
    #         "ntp access-group vrf siteA ipv4 serve ServeAcl2",
    #         "ntp access-group vrf siteA ipv4 peer PeerAcl3",
    #         "ntp access-group ipv4 peer PeerAcl1",
    #         "ntp access-group ipv4 serve ServeAcl1",
    #         "ntp access-group ipv4 serve-only ServeOnlyAcl1",
    #         "ntp access-group ipv4 query-only QueryOnlyAcl1",
    #         "ntp authenticate",
    #         "ntp log-internal-sync",
    #         "ntp broadcastdelay 1",
    #         "ntp drift aging time 0",
    #         "ntp drift file apphost",
    #         "ntp ipv4 dscp af11",
    #         "ntp ipv6 precedence routine",
    #         "ntp max-associations 10",
    #         "ntp master 1",
    #         "ntp passive",
    #         "ntp update-calendar",
    #         "ntp source GigabitEthernet0/0/0/0"
    #     ],
    # Using state: parsed
    # File: parsed.cfg
    # ----------------
    # ntp
    #  max-associations 10
    #  interface GigabitEthernet0/0/0/0
    #   broadcast client
    #   multicast client 224.0.0.8
    #   multicast destination 224.0.0.8
    #  !
    #  authenticate
    #  trusted-key 1
    #  ipv4 dscp af11
    #  ipv6 precedence routine
    #  peer vrf siteC 192.0.2.1 iburst
    #  server vrf siteD 192.0.2.2 burst
    #  drift file apphost
    #  drift aging time 0
    #  master 1
    #  access-group vrf siteA ipv4 peer PeerAcl3
    #  access-group vrf siteA ipv4 serve ServeAcl2
    #  access-group ipv4 peer PeerAcl1
    #  access-group ipv4 serve ServeAcl1
    #  access-group ipv4 serve-only ServeOnlyAcl1
    #  access-group ipv4 query-only QueryOnlyAcl1
    #  source vrf siteE GigabitEthernet0/0/0/0
    #  source GigabitEthernet0/0/0/0
    #  passive
    #  broadcastdelay 1
    #  update-calendar
    #  log-internal-sync
    # !
    # Parsed play:
    # ------------
    - name: Parse the provided configuration with the existing running configuration
      cisco.iosxr.iosxr_ntp_global:
        running_config: "{{ lookup('file', 'parsed.cfg') }}"
        state: parsed
    # Module Execution Result:
    # ------------------------
    # "parsed":{
    #         "access_group": {
    #             "ipv4": {
    #                 "peer": "PeerAcl1",
    #                 "query_only": "QueryOnlyAcl1",
    #                 "serve": "ServeAcl1",
    #                 "serve_only": "ServeOnlyAcl1"
    #             },
    #             "vrfs": [
    #                 {
    #                     "ipv4": {
    #                         "peer": "PeerAcl3",
    #                         "serve": "ServeAcl2"
    #                     },
    #                     "name": "siteA"
    #                 }
    #             ]
    #         },
    #         "authenticate": true,
    #         "broadcastdelay": 1,
    #         "drift": {
    #             "aging_time": 0,
    #             "file": "apphost"
    #         },
    #         "interfaces": [
    #             {
    #                 "broadcast_client": true,
    #                 "multicast_client": "224.0.0.8",
    #                 "multicast_destination": "224.0.0.8",
    #                 "name": "GigabitEthernet0/0/0/0"
    #             }
    #         ],
    #         "ipv4": {
    #             "dscp": "af11"
    #         },
    #         "ipv6": {
    #             "precedence": "routine"
    #         },
    #         "log_internal_sync": true,
    #         "master": 1,
    #         "max_associations": 10,
    #         "passive": true,
    #         "peers": [
    #             {
    #                 "iburst": true,
    #                 "peer": "192.0.2.1",
    #                 "vrf": "siteC"
    #             }
    #         ],
    #         "servers": [
    #             {
    #                 "burst": true,
    #                 "server": "192.0.2.2",
    #                 "vrf": "siteD"
    #             }
    #         ],
    #         "source": "GigabitEthernet0/0/0/0",
    #         "source_vrfs": [
    #             {
    #                 "name": "GigabitEthernet0/0/0/0",
    #                 "vrf": "siteE"
    #             }
    #         ],
    #         "trusted_keys": [
    #             {
    #                 "key_id": 1
    #             }
    #         ],
    #         "update_calendar": true
    #     }



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;sample command 1&#x27;, &#x27;sample command 2&#x27;, &#x27;sample command 3&#x27;]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;sample command 1&#x27;, &#x27;sample command 2&#x27;, &#x27;sample command 3&#x27;]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Ashwini Mhatre (@amhatre)
