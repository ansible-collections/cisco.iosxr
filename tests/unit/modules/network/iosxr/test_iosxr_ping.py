#
# (c) 2022, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from textwrap import dedent

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_ping
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule


class TestIosxrPingModule(TestIosxrModule):
    module = iosxr_ping

    def setUp(self):
        super(TestIosxrPingModule, self).setUp()
        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.ping.ping.Ping.run_command",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrPingModule, self).tearDown()
        self.mock_execute_show_command.stop()

    def test_iosxr_ping_count(self):
        self.execute_show_command.return_value = dedent(
            """\
            Type escape sequence to abort.
            ending 2, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
            !
            Success rate is 100 percent (2/2), round-trip min/avg/max = 25/25/25 ms
            """,
        )
        set_module_args(dict(count=2, dest="8.8.8.8"))
        result = self.execute_module()
        mock_res = {
            "commands": "ping ipv4 8.8.8.8 count 2",
            "packet_loss": "0%",
            "packets_rx": 2,
            "packets_tx": 2,
            "rtt": {"min": 25, "avg": 25, "max": 25},
            "changed": False,
        }
        self.assertEqual(result, mock_res)

    def test_iosxr_ping_v6(self):
        self.execute_show_command.return_value = dedent(
            """\
            Type escape sequence to abort.
            ending 2, 100-byte ICMP Echos to 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff, timeout is 2 seconds:
            !
            Success rate is 100 percent (2/2), round-trip min/avg/max = 25/25/25 ms
            """,
        )
        set_module_args(
            dict(
                count=2,
                dest="2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
                afi="ipv6",
            ),
        )
        result = self.execute_module()
        mock_res = {
            "commands": "ping ipv6 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff count 2",
            "packet_loss": "0%",
            "packets_rx": 2,
            "packets_tx": 2,
            "rtt": {"min": 25, "avg": 25, "max": 25},
            "changed": False,
        }
        self.assertEqual(result, mock_res)

    def test_iosxr_ping_options_all(self):
        self.execute_show_command.return_value = dedent(
            """\
            Type escape sequence to abort.
            ending 2, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
            !
            Success rate is 100 percent (2/2), round-trip min/avg/max = 25/25/25 ms
            """,
        )
        set_module_args(
            {
                "afi": "ipv4",
                "count": 4,
                "dest": "8.8.8.8",
                "df_bit": True,
                "size": "10",
                "source": "Loopback88",
                "state": "present",
                "sweep": True,
                "validate": True,
                "vrf": "DummyVrf",
            },
        )
        result = self.execute_module()
        mock_res = {
            "commands": "ping vrf DummyVrf ipv4 8.8.8.8 count 4 df-bit sweep validate size 10 source Loopback88",
            "packet_loss": "0%",
            "packets_rx": 2,
            "packets_tx": 2,
            "rtt": {"min": 25, "avg": 25, "max": 25},
            "changed": False,
        }
        self.assertEqual(result, mock_res)

    def test_iosxr_ping_state_absent_pass(self):
        self.execute_show_command.return_value = dedent(
            """\
            Type escape sequence to abort.
            ending 2, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
            !
            Success rate is 90 percent (2/2), round-trip min/avg/max = 25/25/25 ms
            """,
        )
        set_module_args(dict(count=2, dest="8.8.8.8", state="absent"))
        result = self.execute_module(failed=True)
        mock_res = {
            "msg": "Ping succeeded unexpectedly",
            "commands": "ping ipv4 8.8.8.8 count 2",
            "packet_loss": "10%",
            "packets_rx": 2,
            "packets_tx": 2,
            "rtt": {"min": 25, "avg": 25, "max": 25},
            "failed": True,
        }
        self.assertEqual(result, mock_res)

    def test_iosxr_ping_state_absent_pass(self):
        self.execute_show_command.return_value = dedent(
            """\
            Type escape sequence to abort.
            Sending 5, 100-byte ICMP Echos to 192.0.2.1, timeout is 2 seconds:
            .....
            Success rate is 0 percent (0/5)
            """,
        )
        set_module_args(dict(count=2, dest="192.0.2.1", state="absent"))
        result = self.execute_module(failed=False)
        print(result)
        mock_res = {
            "commands": "ping ipv4 192.0.2.1 count 2",
            "packet_loss": "100%",
            "packets_rx": 0,
            "packets_tx": 5,
            "rtt": {},
            "changed": False,
        }
        self.assertEqual(result, mock_res)

    def test_iosxr_ping_state_absent_present_fail(self):
        self.execute_show_command.return_value = dedent(
            """\
            Type escape sequence to abort.
            ending 2, 100-byte ICMP Echos to 8.8.8.8, timeout is 12 seconds:
            !
            Success rate is 0 percent (0/2), round-trip min/avg/max = 25/25/25 ms
            """,
        )
        set_module_args(dict(count=2, dest="8.8.8.8", state="present"))
        result = self.execute_module(failed=True)
        mock_res = {
            "msg": "Ping failed unexpectedly",
            "commands": "ping ipv4 8.8.8.8 count 2",
            "packet_loss": "100%",
            "packets_rx": 0,
            "packets_tx": 2,
            "rtt": {"min": 25, "avg": 25, "max": 25},
            "failed": True,
        }
        self.assertEqual(result, mock_res)
