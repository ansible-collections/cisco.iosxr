#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_logging_global
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: iosxr_logging_global
version_added: 2.4.0
short_description: Manages logging attributes of Cisco IOSXR network devices
description: This module manages the logging attributes of Cisco IOSXR network devices
notes:
- Tested against IOSXR 7.0.2.
- This module works with connection C(network_cli).
author: Ashwini Mhatre (@amhatre)
options:
  config:
    description: A dictionary of logging options.
    type: dict
    suboptions:
      archive:
        description: logging to a persistent device(disk/harddisk)
        type: dict
        suboptions:
          device:
            type: str
            description: Configure the archive device
          archive_length:
            type: int
            description: The maximum no of weeks of log to maintain.
          archive_size:
            type: int
            description: The total size of the archive.
          file_size:
            type: int
            description: The maximum file size for a single log file..
          frequency:
            type: str
            description: The collection interval for logs.
            choices: ["daily", "weekly"]
          severity: &severity
            description: Logging severity level
            type: str
            choices:
              - alerts
              - critical
              - debugging
              - emergencies
              - errors
              - informational
              - notifications
              - warnings
          threshold:
            type: int
            description: Threshold percent <1-99>.
      buffered:
        description: Set buffered logging parameters
        type: dict
        suboptions:
          size: &size
            description: Logging buffer size
            type: int
          severity: *severity
          discriminator: &discriminator
            description: Establish MD-Buffer association
            type: list
            elements: dict
            suboptions:
              match_params:
                type: str
                description: Set match/no-match discriminator.
                choices: ["match1", "match2", "match3", "nomatch1", "nomatch2", "nomatch3"]
              name:
                type: str
                description: discriminator name.
      console:
        description: Set console logging parameters
        type: dict
        suboptions:
          severity: &severity1
            description: Logging severity level
            type: str
            choices:
              - alerts
              - critical
              - debugging
              - emergencies
              - errors
              - informational
              - notifications
              - warning
              - disable
          discriminator: *discriminator
      correlator:
        description: Configure properties of the event correlator
        type: dict
        suboptions:
          buffer_size:
            type: int
            description: Configure size of the correlator buffer.
          rules:
            type: list
            elements: dict
            description: Configure a specified correlation rule.
            suboptions:
              rule_name:
                type: str
                description: name of rule.
              rule_type:
                type: str
                choices: ["stateful", "nonstateful"]
                description: type of rule - stateful or nonstateful.
              timeout:
                type: int
                description: Specify timeout.
              timeout_rootcause:
                type: int
                description: Specify timeout for root-cause.
              context_correlation:
                type: bool
                description: Specify enable correlation on context.
              reissue_nonbistate:
                type: bool
                description: Specify reissue of non-bistate alarms on parent clear.This option is allowed for the rules whose type is stateful.
              reparent:
                type: bool
                description: Specify reparent of alarm on parent clear.This option is allowed for the rules whose type is stateful.
          rule_set:
            type: list
            elements: dict
            description: Configure a specified correlation ruleset.
            suboptions:
              name:
                type: str
                description: Name of the ruleset
              rulename:
                type: list
                elements: str
                description: Name of the rule
      events:
        type: dict
        description: Configure event monitoring parameters.
        suboptions:
          buffer_size:
            type: int
            description: Set size of the local event buffer.
          display_location:
            type: bool
            description: Include alarm source location in message text.
          filter_match:
            type: list
            elements: str
            description: Configure filter.
          severity: *severity
          threshold:
            type: int
            description: Capacity alarm threshold.
      facility:
        description: Facility parameter for syslog messages
        type: str
        choices:
          - auth
          - cron
          - daemon
          - kern
          - local0
          - local1
          - local2
          - local3
          - local4
          - local5
          - local6
          - local7
          - lpr
          - mail
          - news
          - sys10
          - sys11
          - sys12
          - sys13
          - sys14
          - sys9
          - syslog
          - user
          - uucp
      files:
        type: list
        elements: dict
        description: Set file logging.
        suboptions:
          name:
            description: name of file.
            type: str
          path:
            description: Set file path.
            type: str
          maxfilesize:
            description: Set max file size.
          severity:
            description: Logging severity level
            type: str
            choices:
              - alerts
              - critical
              - debugging
              - emergencies
              - errors
              - info
              - notifications
              - warning
      format:
        type: bool
        description: Enable to send the syslog message rfc5424 format .
      history:
        description: Configure syslog history table
        type: dict
        suboptions:
          size: *size
          severity:
            description: Logging severity level
            type: str
            choices:
              - alerts
              - critical
              - debugging
              - emergencies
              - errors
              - informational
              - notifications
              - warnings
              - disable
      hostnameprefix:
        type: str
        description: Hostname prefix to add on msgs to servers.
      ipv4: &ip
        description: Mark the dscp/precedence bit for ipv4 packets.
        type: dict
        suboptions:
          dscp:
            description: Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries.
            type: str
          precedence:
            description: Set precedence Please refer vendor document for valid entries.
            type: str
      ipv6: *ip
      localfilesize:
        type: int
        description: Set size of the local log file
      monitor:
        description: Set terminal line (monitor) logging parameters
        type: dict
        suboptions:
          discriminator: *discriminator
          severity: *severity1
      source_interfaces:
        description: Specify interface for source address in logging transactions
        type: list
        elements: dict
        suboptions:
          interface:
            description: Interface name with number
            type: str
          vrf:
            description: VPN Routing/Forwarding instance name
            type: str
      suppress:
        type: dict
        description: Suppress logging behaviour.
        suboptions:
          apply_rule:
            type: str
            description: Apply suppression rule.
          duplicates:
            type: bool
            description: Suppress consecutive duplicate messages.
      tls_servers:
        type: list
        elements: dict
        description: Secure server over tls.
        suboptions:
          name:
            type: str
            description: Name for the tls peer configuration.
          severity: *severity
          tls_hostname:
            type: str
            description: Name of the logging host.
          trustpoint:
            type: str
            description: Name of the trustpoint configured.
          vrf:
            type: str
            description: name of vrf.
      trap:
        description: Set syslog server logging level
        type: dict
        suboptions:
          severity: *severity1
      hosts:
        description: Set syslog server IP address and parameters
        type: list
        elements: dict
        suboptions:
          severity:
            description: Logging severity level
            type: str
            choices:
              - alerts
              - critical
              - debugging
              - emergencies
              - error
              - info
              - notifications
              - warning
          host:
            description: IPv4/Ipv6 address or hostname of the syslog server
            type: str
          port:
            description: Set <0-65535>  non-default Port.
            type: str
          vrf:
            description: Set VRF option
            type: str
            default: default
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the IOS device by
        executing the command B(show running-config | include logging).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    choices:
      - merged
      - replaced
      - overridden
      - deleted
      - gathered
      - parsed
      - rendered
    default: merged
    description:
      - The state the configuration should be left in
    type: str
required_if:
  - ["state", "merged", ["config"]]
  - ["state", "replaced", ["config"]]
  - ["state", "overridden", ["config"]]
  - ["state", "rendered", ["config"]]
  - ["state", "parsed", ["running_config"]]
mutually_exclusive:
  - ["config", "running_config"]
supports_check_mode: True
"""
EXAMPLES = """

"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.logging_global.logging_global import (
    Logging_globalArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.logging_global.logging_global import (
    Logging_global,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Logging_globalArgs.argument_spec,
        mutually_exclusive=[["config", "running_config"]],
        required_if=[
            ["state", "merged", ["config"]],
            ["state", "replaced", ["config"]],
            ["state", "overridden", ["config"]],
            ["state", "rendered", ["config"]],
            ["state", "parsed", ["running_config"]],
        ],
        supports_check_mode=True,
    )

    result = Logging_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
