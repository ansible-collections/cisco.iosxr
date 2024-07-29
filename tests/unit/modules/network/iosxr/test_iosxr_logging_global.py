# (c) 2021 Red Hat Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent
from unittest.mock import patch

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_logging_global
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrLoggingGlobalModule(TestIosxrModule):
    module = iosxr_logging_global

    def setUp(self):
        super(TestIosxrLoggingGlobalModule, self).setUp()

        self.mock_get_resource_connection = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.resource_module_base."
            "get_resource_connection",
        )
        self.get_resource_connection = self.mock_get_resource_connection.start()

        self.mock_get_config = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.logging_global.logging_global."
            "Logging_globalFacts.get_config",
        )
        self.get_config = self.mock_get_config.start()

    def tearDown(self):
        super(TestIosxrLoggingGlobalModule, self).tearDown()
        self.get_resource_connection.stop()
        self.get_config.stop()

    def test_iosxr_logging_global_merged_idempotent(self):
        run_cfg = dedent(
            """\
                logging tls-server test
                 vrf test
                 trustpoint test2
                 tls-hostname test2
                !
                logging file test path test maxfilesize 1024 severity info
                logging file test2 path test1 maxfilesize 1024 severity debugging
                logging ipv4 dscp af11
                logging ipv6 precedence routine
                logging trap informational
                logging events filter
                 match test
                 match test1
                !
                logging events threshold 10
                logging events buffer-size 1024
                logging events display-location
                logging events level warnings
                logging format rfc5424
                logging archive
                 device disk0
                 severity alerts
                 file-size 1
                 frequency daily
                 archive-size 1
                 archive-length 1
                !
                logging console warning
                logging console discriminator
                 match1 test
                 nomatch1 test3
                !
                logging history size 10
                logging monitor errors
                logging monitor discriminator
                 match1 test1
                !
                logging buffered 2097152
                logging buffered warnings
                logging buffered discriminator
                 match2 test
                !
                logging 1.1.1.1 vrf default severity critical port default
                logging correlator rule test type stateful
                 reissue-nonbistate
                 timeout 5
                 reparent
                 context-correlation
                !
                logging correlator rule test1 type nonstateful
                 timeout 6
                 context-correlation
                !
                logging correlator ruleset test
                 rulename test
                 rulename test1
                !
                logging correlator buffer-size 1024
                logging localfilesize 1024
                logging source-interface GigabitEthernet0/0/0/0 vrf test
                logging hostnameprefix test
                logging suppress duplicates
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    archive=dict(
                        archive_length=1,
                        archive_size=1,
                        device="disk0",
                        file_size=1,
                        frequency="daily",
                        severity="alerts",
                    ),
                    buffered=dict(
                        size=2097152,
                        severity="warnings",
                        discriminator=[
                            dict(match_params="match2", name="test"),
                        ],
                    ),
                    console=dict(
                        severity="warning",
                        discriminator=[
                            dict(match_params="match1", name="test"),
                            dict(match_params="nomatch1", name="test3"),
                        ],
                    ),
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[
                            dict(name="test", rulename=["test1", "test"]),
                        ],
                        rules=[
                            dict(
                                rule_name="test",
                                rule_type="stateful",
                                timeout=5,
                                context_correlation=True,
                                reissue_nonbistate=True,
                                reparent=True,
                            ),
                            dict(
                                rule_name="test1",
                                rule_type="nonstateful",
                                timeout=6,
                                context_correlation=True,
                            ),
                        ],
                    ),
                    events=dict(
                        severity="warnings",
                        display_location=True,
                        buffer_size=1024,
                        filter_match=["test1", "test"],
                        threshold=10,
                    ),
                    format=True,
                    files=[
                        dict(
                            maxfilesize=1024,
                            name="test",
                            path="test",
                            severity="info",
                        ),
                        dict(
                            maxfilesize=1024,
                            name="test2",
                            path="test1",
                            severity="debugging",
                        ),
                    ],
                    history=dict(size=10),
                    hostnameprefix="test",
                    hosts=[
                        dict(
                            host="1.1.1.1",
                            port="default",
                            severity="critical",
                            vrf="default",
                        ),
                    ],
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    localfilesize=1024,
                    monitor=dict(
                        severity="errors",
                        discriminator=[
                            dict(match_params="match1", name="test1"),
                        ],
                    ),
                    source_interfaces=[
                        dict(interface="GigabitEthernet0/0/0/0", vrf="test"),
                    ],
                    suppress=dict(duplicates=True),
                    tls_servers=[
                        dict(
                            name="test",
                            tls_hostname="test2",
                            trustpoint="test2",
                            vrf="test",
                        ),
                    ],
                    trap=dict(severity="informational"),
                ),
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_logging_global_merged(self):
        set_module_args(
            dict(
                config=dict(
                    archive=dict(
                        archive_length=1,
                        archive_size=1,
                        device="disk0",
                        file_size=1,
                        frequency="daily",
                        severity="alerts",
                    ),
                    buffered=dict(
                        size=2097152,
                        severity="warnings",
                        discriminator=[
                            dict(match_params="match2", name="test"),
                        ],
                    ),
                    console=dict(
                        severity="warning",
                        discriminator=[
                            dict(match_params="match1", name="test"),
                            dict(match_params="nomatch1", name="test3"),
                        ],
                    ),
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[
                            dict(name="test", rulename=["test1", "test"]),
                        ],
                        rules=[
                            dict(
                                rule_name="test",
                                rule_type="stateful",
                                timeout=5,
                                context_correlation=True,
                                reissue_nonbistate=True,
                                reparent=True,
                            ),
                            dict(
                                rule_name="test1",
                                rule_type="nonstateful",
                                timeout=6,
                                context_correlation=True,
                            ),
                        ],
                    ),
                    events=dict(
                        severity="warnings",
                        display_location=True,
                        buffer_size=1024,
                        filter_match=["test1", "test"],
                        threshold=10,
                    ),
                    format=True,
                    files=[
                        dict(
                            maxfilesize=1024,
                            name="test",
                            path="test",
                            severity="info",
                        ),
                        dict(
                            maxfilesize=1024,
                            name="test2",
                            path="test1",
                            severity="debugging",
                        ),
                    ],
                    history=dict(state="disabled", size=10),
                    hostnameprefix="test",
                    hosts=[
                        dict(
                            host="1.1.1.1",
                            port="default",
                            severity="critical",
                            vrf="default",
                        ),
                    ],
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    localfilesize=1024,
                    monitor=dict(
                        severity="errors",
                        discriminator=[
                            dict(match_params="match1", name="test1"),
                        ],
                    ),
                    source_interfaces=[
                        dict(interface="GigabitEthernet0/0/0/0", vrf="test"),
                    ],
                    suppress=dict(duplicates=True),
                    tls_servers=[
                        dict(
                            name="test",
                            tls_hostname="test2",
                            trustpoint="test2",
                            vrf="test",
                        ),
                    ],
                    trap=dict(severity="informational"),
                ),
                state="merged",
            ),
        )
        commands = [
            "logging archive device disk0",
            "logging archive frequency daily",
            "logging archive severity alerts",
            "logging archive archive-size 1",
            "logging archive archive-length 1",
            "logging archive file-size 1",
            "logging buffered 2097152",
            "logging buffered warnings",
            "logging console warning",
            "logging correlator buffer-size 1024",
            "logging events threshold 10",
            "logging events buffer-size 1024",
            "logging events display-location",
            "logging events level warnings",
            "logging hostnameprefix test",
            "logging format rfc5424",
            "logging ipv4 dscp af11",
            "logging ipv6 precedence routine",
            "logging localfilesize 1024",
            "logging suppress duplicates",
            "logging monitor errors",
            "logging history size 10",
            "logging history disable",
            "logging trap informational",
            "logging 1.1.1.1 vrf default severity critical port default",
            "logging file test path test maxfilesize 1024 severity info",
            "logging file test2 path test1 maxfilesize 1024 severity debugging",
            "logging source-interface GigabitEthernet0/0/0/0 vrf test",
            "logging tls-server test tls-hostname test2",
            "logging tls-server test trustpoint test2",
            "logging tls-server test vrf test",
            "logging correlator ruleset  test  rulename test1",
            "logging correlator ruleset  test  rulename test",
            "logging correlator rule test type stateful timeout 5",
            "logging correlator rule test type stateful reissue-nonbistate",
            "logging correlator rule test type stateful reparent",
            "logging correlator rule test type stateful context-correlation",
            "logging correlator rule test1 type nonstateful timeout 6",
            "logging correlator rule test1 type nonstateful context-correlation",
            "logging events filter match test1",
            "logging events filter match test",
            "logging buffered discriminator match2 test",
            "logging monitor discriminator match1 test1",
            "logging console discriminator match1 test",
            "logging console discriminator nomatch1 test3",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_logging_global_deleted(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                logging tls-server test
                 vrf test
                 trustpoint test2
                 tls-hostname test2
                !
                logging file test path test maxfilesize 1024 severity info
                logging file test2 path test1 maxfilesize 1024 severity debugging
                logging ipv4 dscp af11
                logging ipv6 precedence routine
                logging trap informational
                logging events filter
                 match test
                 match test1
                !
                logging events threshold 10
                logging events buffer-size 1024
                logging events display-location
                logging events level warnings
                logging format rfc5424
                logging archive
                 device disk0
                 severity alerts
                 file-size 1
                 frequency daily
                 archive-size 1
                 archive-length 1
                !
                logging console warning
                logging console discriminator
                 match1 test
                 nomatch1 test3
                !
                logging history size 10
                logging history disable
                logging monitor errors
                logging monitor discriminator
                 match1 test1
                !
                logging buffered 2097152
                logging buffered warnings
                logging buffered discriminator
                 match2 test
                !
                logging 1.1.1.1 vrf default severity critical port default
                logging correlator rule test type stateful
                 reissue-nonbistate
                 timeout 5
                 reparent
                 context-correlation
                !
                logging correlator rule test1 type nonstateful
                 timeout 6
                 context-correlation
                !
                logging correlator ruleset test
                 rulename test
                 rulename test1
                !
                logging correlator buffer-size 1024
                logging localfilesize 1024
                logging source-interface GigabitEthernet0/0/0/0 vrf test
                logging hostnameprefix test
                logging suppress duplicates
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="deleted"))
        commands = [
            "no logging archive device disk0",
            "no logging archive frequency daily",
            "no logging archive severity alerts",
            "no logging archive archive-size 1",
            "no logging archive archive-length 1",
            "no logging archive file-size 1",
            "no logging buffered 2097152",
            "no logging buffered warnings",
            "no logging console warning",
            "no logging correlator buffer-size 1024",
            "no logging events threshold 10",
            "no logging events buffer-size 1024",
            "no logging events display-location",
            "no logging events level warnings",
            "no logging hostnameprefix test",
            "no logging format rfc5424",
            "no logging ipv4 dscp af11",
            "no logging ipv6 precedence routine",
            "no logging localfilesize 1024",
            "no logging suppress duplicates",
            "no logging monitor errors",
            "no logging history size 10",
            "no logging history disable",
            "no logging trap informational",
            "no logging 1.1.1.1 vrf default severity critical port default",
            "no logging file test path test maxfilesize 1024 severity info",
            "no logging file test2 path test1 maxfilesize 1024 severity debugging",
            "no logging source-interface GigabitEthernet0/0/0/0 vrf test",
            "no logging tls-server test",
            "no logging correlator ruleset  test  rulename test",
            "no logging correlator ruleset  test  rulename test1",
            "no logging correlator rule test type stateful timeout 5",
            "no logging correlator rule test type stateful reissue-nonbistate",
            "no logging correlator rule test type stateful reparent",
            "no logging correlator rule test type stateful context-correlation",
            "no logging correlator rule test1 type nonstateful timeout 6",
            "no logging correlator rule test1 type nonstateful context-correlation",
            "no logging events filter match test",
            "no logging events filter match test1",
            "no logging buffered discriminator match2 test",
            "no logging monitor discriminator match1 test1",
            "no logging console discriminator match1 test",
            "no logging console discriminator nomatch1 test3",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_logging_global_replaced(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                logging tls-server test
                 vrf test
                 trustpoint test2
                 tls-hostname test2
                !
                logging file test path test maxfilesize 1024 severity info
                logging file test2 path test1 maxfilesize 1024 severity debugging
                logging ipv4 dscp af11
                logging ipv6 precedence routine
                logging trap informational
                logging events filter
                 match test
                 match test1
                !
                logging events threshold 10
                logging events buffer-size 1024
                logging events display-location
                logging events level warnings
                logging format rfc5424
                logging archive
                 device disk0
                 severity alerts
                 file-size 1
                 frequency daily
                 archive-size 1
                 archive-length 1
                !
                logging console warning
                logging console discriminator
                 match1 test
                 nomatch1 test3
                !
                logging history size 10
                logging history disable
                logging monitor errors
                logging monitor discriminator
                 match1 test1
                !
                logging buffered 2097152
                logging buffered warnings
                logging buffered discriminator
                 match2 test
                !
                logging 1.1.1.1 vrf default severity critical port default
                logging correlator rule test type stateful
                 reissue-nonbistate
                 timeout 5
                 reparent
                 context-correlation
                !
                logging correlator rule test1 type nonstateful
                 timeout 6
                 context-correlation
                !
                logging correlator ruleset test
                 rulename test
                 rulename test1
                !
                logging correlator buffer-size 1024
                logging localfilesize 1024
                logging source-interface GigabitEthernet0/0/0/0 vrf test
                logging hostnameprefix test
                logging suppress duplicates
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    archive=dict(
                        archive_length=1,
                        archive_size=1,
                        device="disk0",
                        file_size=1,
                        severity="alerts",
                    ),
                    buffered=dict(size=2097152, severity="warnings"),
                    console=dict(
                        severity="warning",
                        discriminator=[
                            dict(match_params="match1", name="test1"),
                        ],
                    ),
                    correlator=dict(
                        buffer_size=1024,
                        rules=[
                            dict(
                                rule_name="test",
                                rule_type="stateful",
                                timeout=6,
                                context_correlation=True,
                                reissue_nonbistate=True,
                                reparent=True,
                            ),
                        ],
                    ),
                    events=dict(
                        severity="warnings",
                        display_location=True,
                        buffer_size=1024,
                        filter_match=["test1"],
                        threshold=12,
                    ),
                    format=True,
                    files=[
                        dict(
                            maxfilesize=1024,
                            name="test",
                            path="test1",
                            severity="info",
                        ),
                    ],
                    history=dict(state="disabled", size=10),
                    hostnameprefix="test",
                    hosts=[
                        dict(
                            host="1.1.1.2",
                            port="default",
                            severity="critical",
                            vrf="default",
                        ),
                    ],
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    localfilesize=1024,
                    source_interfaces=[
                        dict(interface="GigabitEthernet0/0/0/0", vrf="test"),
                    ],
                    tls_servers=[
                        dict(
                            name="test",
                            tls_hostname="test2",
                            trustpoint="test3",
                            vrf="test",
                        ),
                    ],
                ),
                state="replaced",
            ),
        )
        commands = [
            "logging console discriminator match1 test1",
            "logging correlator rule test type stateful timeout 6",
            "logging events threshold 12",
            "logging 1.1.1.2 vrf default severity critical port default",
            "logging file test path test1 maxfilesize 1024 severity info",
            "logging tls-server test trustpoint test3",
            "no logging 1.1.1.1 vrf default severity critical port default",
            "no logging archive frequency daily",
            "no logging buffered discriminator match2 test",
            "no logging console discriminator match1 test",
            "no logging console discriminator nomatch1 test3",
            "no logging correlator rule test1 type nonstateful context-correlation",
            "no logging correlator rule test1 type nonstateful timeout 6",
            "no logging correlator ruleset  test  rulename test",
            "no logging correlator ruleset  test  rulename test1",
            "no logging events filter match test",
            "no logging file test2 path test1 maxfilesize 1024 severity debugging",
            "no logging monitor discriminator match1 test1",
            "no logging monitor errors",
            "no logging suppress duplicates",
            "no logging trap informational",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_logging_global_rendered(self):
        self.maxDiff = None
        set_module_args(
            dict(
                config=dict(
                    archive=dict(
                        archive_length=1,
                        archive_size=1,
                        device="disk0",
                        file_size=1,
                        frequency="daily",
                        severity="alerts",
                    ),
                    buffered=dict(
                        size=2097152,
                        severity="warnings",
                        discriminator=[
                            dict(match_params="match2", name="test"),
                        ],
                    ),
                    console=dict(
                        severity="warning",
                        discriminator=[
                            dict(match_params="match1", name="test"),
                            dict(match_params="nomatch1", name="test3"),
                        ],
                    ),
                    correlator=dict(
                        buffer_size=1024,
                        rule_sets=[
                            dict(name="test", rulename=["test1", "test"]),
                        ],
                        rules=[
                            dict(
                                rule_name="test",
                                rule_type="stateful",
                                timeout=5,
                                context_correlation=True,
                                reissue_nonbistate=True,
                                reparent=True,
                            ),
                            dict(
                                rule_name="test1",
                                rule_type="nonstateful",
                                timeout=6,
                                context_correlation=True,
                            ),
                        ],
                    ),
                    events=dict(
                        severity="warnings",
                        display_location=True,
                        buffer_size=1024,
                        filter_match=["test1", "test"],
                        threshold=10,
                    ),
                    format=True,
                    files=[
                        dict(
                            maxfilesize=1024,
                            name="test",
                            path="test",
                            severity="info",
                        ),
                        dict(
                            maxfilesize=1024,
                            name="test2",
                            path="test1",
                            severity="debugging",
                        ),
                    ],
                    history=dict(state="disabled", size=10),
                    hostnameprefix="test",
                    hosts=[
                        dict(
                            host="1.1.1.1",
                            port="default",
                            severity="critical",
                            vrf="default",
                        ),
                    ],
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    localfilesize=1024,
                    monitor=dict(
                        severity="errors",
                        discriminator=[
                            dict(match_params="match1", name="test1"),
                        ],
                    ),
                    source_interfaces=[
                        dict(interface="GigabitEthernet0/0/0/0", vrf="test"),
                    ],
                    suppress=dict(duplicates=True),
                    tls_servers=[
                        dict(
                            name="test",
                            tls_hostname="test2",
                            trustpoint="test2",
                            vrf="test",
                        ),
                    ],
                    trap=dict(severity="informational"),
                ),
                state="rendered",
            ),
        )
        commands = [
            "logging archive device disk0",
            "logging archive frequency daily",
            "logging archive severity alerts",
            "logging archive archive-size 1",
            "logging archive archive-length 1",
            "logging archive file-size 1",
            "logging buffered 2097152",
            "logging buffered warnings",
            "logging console warning",
            "logging correlator buffer-size 1024",
            "logging events threshold 10",
            "logging events buffer-size 1024",
            "logging events display-location",
            "logging events level warnings",
            "logging hostnameprefix test",
            "logging format rfc5424",
            "logging ipv4 dscp af11",
            "logging ipv6 precedence routine",
            "logging localfilesize 1024",
            "logging suppress duplicates",
            "logging monitor errors",
            "logging history size 10",
            "logging history disable",
            "logging trap informational",
            "logging 1.1.1.1 vrf default severity critical port default",
            "logging file test path test maxfilesize 1024 severity info",
            "logging file test2 path test1 maxfilesize 1024 severity debugging",
            "logging source-interface GigabitEthernet0/0/0/0 vrf test",
            "logging tls-server test tls-hostname test2",
            "logging tls-server test trustpoint test2",
            "logging tls-server test vrf test",
            "logging correlator ruleset  test  rulename test1",
            "logging correlator ruleset  test  rulename test",
            "logging correlator rule test type stateful timeout 5",
            "logging correlator rule test type stateful reissue-nonbistate",
            "logging correlator rule test type stateful reparent",
            "logging correlator rule test type stateful context-correlation",
            "logging correlator rule test1 type nonstateful timeout 6",
            "logging correlator rule test1 type nonstateful context-correlation",
            "logging events filter match test1",
            "logging events filter match test",
            "logging buffered discriminator match2 test",
            "logging monitor discriminator match1 test1",
            "logging console discriminator match1 test",
            "logging console discriminator nomatch1 test3",
        ]
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(commands))

    def test_iosxr_logging_global_overridden(self):
        self.maxDiff = None
        run_cfg = dedent(
            """\
                logging tls-server test
                 vrf test
                 trustpoint test2
                 tls-hostname test2
                !
                logging file test path test maxfilesize 1024 severity info
                logging file test2 path test1 maxfilesize 1024 severity debugging
                logging ipv4 dscp af11
                logging ipv6 precedence routine
                logging trap informational
                logging events filter
                 match test
                 match test1
                !
                logging events threshold 10
                logging events buffer-size 1024
                logging events display-location
                logging events level warnings
                logging format rfc5424
                logging archive
                 device disk0
                 severity alerts
                 file-size 1
                 frequency daily
                 archive-size 1
                 archive-length 1
                !
                logging console warning
                logging console discriminator
                 match1 test
                 nomatch1 test3
                !
                logging history size 10
                logging history disable
                logging monitor errors
                logging monitor discriminator
                 match1 test1
                !
                logging buffered 2097152
                logging buffered warnings
                logging buffered discriminator
                 match2 test
                !
                logging 1.1.1.1 vrf default severity critical port default
                logging correlator rule test type stateful
                 reissue-nonbistate
                 timeout 5
                 reparent
                 context-correlation
                !
                logging correlator rule test1 type nonstateful
                 timeout 6
                 context-correlation
                !
                logging correlator ruleset test
                 rulename test
                 rulename test1
                !
                logging correlator buffer-size 1024
                logging localfilesize 1024
                logging source-interface GigabitEthernet0/0/0/0 vrf test
                logging hostnameprefix test
                logging suppress duplicates
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(
            dict(
                config=dict(
                    archive=dict(
                        archive_length=1,
                        archive_size=1,
                        device="disk0",
                        file_size=1,
                        severity="alerts",
                    ),
                    buffered=dict(size=2097152, severity="warnings"),
                    console=dict(
                        severity="warning",
                        discriminator=[
                            dict(match_params="match1", name="test1"),
                        ],
                    ),
                    correlator=dict(
                        buffer_size=1024,
                        rules=[
                            dict(
                                rule_name="test",
                                rule_type="stateful",
                                timeout=6,
                                context_correlation=True,
                                reissue_nonbistate=True,
                                reparent=True,
                            ),
                        ],
                    ),
                    events=dict(
                        severity="warnings",
                        display_location=True,
                        buffer_size=1024,
                        filter_match=["test1"],
                        threshold=12,
                    ),
                    format=True,
                    files=[
                        dict(
                            maxfilesize=1024,
                            name="test",
                            path="test1",
                            severity="info",
                        ),
                    ],
                    history=dict(state="disabled", size=10),
                    hostnameprefix="test",
                    hosts=[
                        dict(
                            host="1.1.1.2",
                            port="default",
                            severity="critical",
                            vrf="default",
                        ),
                    ],
                    ipv6=dict(precedence="routine"),
                    ipv4=dict(dscp="af11"),
                    localfilesize=1024,
                    source_interfaces=[
                        dict(interface="GigabitEthernet0/0/0/0", vrf="test"),
                    ],
                    tls_servers=[
                        dict(
                            name="test",
                            tls_hostname="test2",
                            trustpoint="test3",
                            vrf="test",
                        ),
                    ],
                ),
                state="overridden",
            ),
        )
        commands = [
            "logging console discriminator match1 test1",
            "logging correlator rule test type stateful timeout 6",
            "logging events threshold 12",
            "logging 1.1.1.2 vrf default severity critical port default",
            "logging file test path test1 maxfilesize 1024 severity info",
            "logging tls-server test trustpoint test3",
            "no logging 1.1.1.1 vrf default severity critical port default",
            "no logging archive frequency daily",
            "no logging buffered discriminator match2 test",
            "no logging console discriminator match1 test",
            "no logging console discriminator nomatch1 test3",
            "no logging correlator rule test1 type nonstateful context-correlation",
            "no logging correlator rule test1 type nonstateful timeout 6",
            "no logging correlator ruleset  test  rulename test",
            "no logging correlator ruleset  test  rulename test1",
            "no logging events filter match test",
            "no logging file test2 path test1 maxfilesize 1024 severity debugging",
            "no logging monitor discriminator match1 test1",
            "no logging monitor errors",
            "no logging suppress duplicates",
            "no logging trap informational",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_iosxr_logging_global_gathered(self):
        run_cfg = dedent(
            """\
                logging tls-server test
                 vrf test
                 trustpoint test2
                 tls-hostname test2
                !
                logging file test path test maxfilesize 1024 severity info
                logging ipv4 dscp af11
                logging ipv6 precedence routine
                logging trap informational
                logging events filter
                 match test
                !
                logging events threshold 10
                logging events buffer-size 1024
                logging events display-location
                logging events level warnings
                logging format rfc5424
                logging archive
                 device disk0
                 severity alerts
                 file-size 1
                 frequency daily
                 archive-size 1
                 archive-length 1
                !
                logging console warning
                logging console discriminator
                 match1 test
                !
                logging history size 10
                logging history disable
                logging monitor errors
                logging monitor discriminator
                 match1 test1
                !
                logging buffered 2097152
                logging buffered warnings
                logging buffered discriminator
                 match2 test
                !
                logging 1.1.1.1 vrf default severity critical port default
                logging correlator rule test type stateful
                 reissue-nonbistate
                 timeout 5
                 reparent
                 context-correlation
                !
                logging correlator ruleset test
                 rulename test
                !
                logging correlator buffer-size 1024
                logging localfilesize 1024
                logging source-interface GigabitEthernet0/0/0/0 vrf test
                logging hostnameprefix test
                logging suppress duplicates
                !
            """,
        )
        self.get_config.return_value = run_cfg
        set_module_args(dict(state="gathered"))
        gathered = {
            "archive": {
                "archive_length": 1,
                "archive_size": 1,
                "device": "disk0",
                "file_size": 1,
                "frequency": "daily",
                "severity": "alerts",
            },
            "buffered": {
                "discriminator": [{"match_params": "match2", "name": "test"}],
                "severity": "warnings",
                "size": 2097152,
            },
            "console": {
                "discriminator": [{"match_params": "match1", "name": "test"}],
                "severity": "warning",
            },
            "correlator": {
                "buffer_size": 1024,
                "rule_sets": [{"name": "test", "rulename": ["test"]}],
                "rules": [
                    {
                        "context_correlation": True,
                        "reissue_nonbistate": True,
                        "reparent": True,
                        "rule_name": "test",
                        "rule_type": "stateful",
                        "timeout": 5,
                    },
                ],
            },
            "events": {
                "buffer_size": 1024,
                "display_location": True,
                "filter_match": ["test"],
                "severity": "warnings",
                "threshold": 10,
            },
            "files": [
                {
                    "maxfilesize": 1024,
                    "name": "test",
                    "path": "test",
                    "severity": "info",
                },
            ],
            "format": True,
            "history": {"state": "disabled", "size": 10},
            "hostnameprefix": "test",
            "hosts": [
                {
                    "host": "1.1.1.1",
                    "port": "default",
                    "severity": "critical",
                    "vrf": "default",
                },
            ],
            "ipv4": {"dscp": "af11"},
            "ipv6": {"precedence": "routine"},
            "localfilesize": 1024,
            "monitor": {
                "discriminator": [{"match_params": "match1", "name": "test1"}],
                "severity": "errors",
            },
            "source_interfaces": [
                {"interface": "GigabitEthernet0/0/0/0", "vrf": "test"},
            ],
            "suppress": {"duplicates": True},
            "tls_servers": [
                {
                    "name": "test",
                    "tls_hostname": "test2",
                    "trustpoint": "test2",
                    "vrf": "test",
                },
            ],
            "trap": {"severity": "informational"},
        }
        result = self.execute_module(changed=False)
        self.assertEqual(gathered, result["gathered"])

    def test_iosxr_logging_global_parsed(self):
        set_module_args(
            dict(
                running_config="logging tls-server test\n vrf test\n trustpoint test2\n tls-hostname test2"
                "\n!\nlogging file test path test maxfilesize 1024 severity info\nlogging ipv4 dscp"
                " af11\nlogging ipv6 precedence routine\nlogging trap informational\nlogging events"
                " filter\n match test1\n!\nlogging events threshold "
                "10\nlogging events buffer-size 1024\nlogging events display-location"
                "\nlogging events level warnings"
                "\nlogging format rfc5424\nlogging archive\n device disk0"
                "\n severity alerts\n file-size 1\n frequency "
                "daily\n archive-size 1\n archive-length 1\n!\nlogging console "
                "warning\nlogging console discriminator\n "
                "match1 test\n!\nlogging history size "
                "10\nlogging history disable\nlogging monitor errors"
                "\nlogging monitor discriminator\n match1 test1\n!"
                "\nlogging buffered 2097152\nlogging buffered warnings\n"
                "logging buffered discriminator\n match2 test\n!\nlogging "
                "1.1.1.1 vrf default severity critical port default"
                "\nlogging correlator rule test type stateful\n reissue-nonbistate\n "
                "timeout 5\n reparent\n context-correlation\n!"
                "\n!\nlogging correlator ruleset test\n rulename test1"
                "\n!\nlogging correlator buffer-size 1024\nlogging "
                "localfilesize 1024\nlogging source-interface"
                " GigabitEthernet0/0/0/0 vrf test\nlogging hostnameprefix "
                "test\nlogging suppress duplicates",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = {
            "archive": {
                "archive_length": 1,
                "archive_size": 1,
                "device": "disk0",
                "file_size": 1,
                "frequency": "daily",
                "severity": "alerts",
            },
            "buffered": {
                "discriminator": [{"match_params": "match2", "name": "test"}],
                "severity": "warnings",
                "size": 2097152,
            },
            "console": {
                "discriminator": [{"match_params": "match1", "name": "test"}],
                "severity": "warning",
            },
            "correlator": {
                "buffer_size": 1024,
                "rule_sets": [{"name": "test", "rulename": ["test1"]}],
                "rules": [
                    {
                        "context_correlation": True,
                        "reissue_nonbistate": True,
                        "reparent": True,
                        "rule_name": "test",
                        "rule_type": "stateful",
                        "timeout": 5,
                    },
                ],
            },
            "events": {
                "buffer_size": 1024,
                "display_location": True,
                "filter_match": ["test1"],
                "severity": "warnings",
                "threshold": 10,
            },
            "files": [
                {
                    "maxfilesize": 1024,
                    "name": "test",
                    "path": "test",
                    "severity": "info",
                },
            ],
            "format": True,
            "history": {"state": "disabled", "size": 10},
            "hostnameprefix": "test",
            "hosts": [
                {
                    "host": "1.1.1.1",
                    "port": "default",
                    "severity": "critical",
                    "vrf": "default",
                },
            ],
            "ipv4": {"dscp": "af11"},
            "ipv6": {"precedence": "routine"},
            "localfilesize": 1024,
            "monitor": {
                "discriminator": [{"match_params": "match1", "name": "test1"}],
                "severity": "errors",
            },
            "source_interfaces": [
                {"interface": "GigabitEthernet0/0/0/0", "vrf": "test"},
            ],
            "suppress": {"duplicates": True},
            "tls_servers": [
                {
                    "name": "test",
                    "tls_hostname": "test2",
                    "trustpoint": "test2",
                    "vrf": "test",
                },
            ],
            "trap": {"severity": "informational"},
        }

        self.assertEqual(parsed_list, result["parsed"])
