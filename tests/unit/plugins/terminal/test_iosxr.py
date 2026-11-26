from __future__ import absolute_import, division, print_function


__metaclass__ = type

import pytest

from ansible_collections.cisco.iosxr.plugins.terminal.iosxr import TerminalModule


def is_error(output):
    return any(r.search(output) for r in TerminalModule.terminal_stderr_re)


@pytest.mark.parametrize(
    "output",
    [
        b"connection timed out",
        b"\r\n% Connection timed out\r\n",
    ],
)
def test_connection_timed_out_error_is_detected(output):
    assert is_error(output)


@pytest.mark.parametrize(
    "output",
    [
        # issue 632: a syslog line in "show logging" is not a CLI error
        b"RP/0/RP0/CPU0:Jun 19 13:42:57.617 UTC: tacacsd[1144]: %SECURITY-TACACSD-6-SERVER_DOWN : "
        b"TACACS+ server 192.0.2.50/49 is DOWN - Socket 1013555: Connection timed out\r\n",
        b"some text (connection timed out)",
    ],
)
def test_connection_timed_out_in_log_text_is_not_an_error(output):
    assert not is_error(output)
