#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for iosxr_prefix_lists
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
module: iosxr_prefix_lists
short_description: Prefix-Lists resource module.
description:
- This module manages prefix-lists configuration on devices running Cisco IOSXR.
version_added: 2.3.0
notes:
- Tested against IOSXR 7.0.2.
- This module works with connection C(network_cli).
author: Ashwini Mhatre (@amhatre)
options:
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the Iosxr device by
        executing the command B(show running-config prefix-list).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  config:
    description: A list of prefix-lists configuration.
    type: list
    elements: dict
    suboptions:
      afi:
        description:
        - The Address Family Identifier (AFI) for the prefix-lists.
        type: str
        choices: ["ipv4", "ipv6"]
      prefix_lists:
        description: List of prefix-list configurations.
        type: list
        elements: dict
        suboptions:
          name:
            description: Name of the prefix-list.
            type: str
          entries:
            description: List of configurations for the specified prefix-list
            type: list
            elements: dict
            suboptions:
              sequence:
                description: Sequence Number.
                type: int
              action:
                description: Prefix-List permit or deny.
                type: str
                choices: ["permit", "deny", "remark"]
              description:
                description: Description of the prefix list. only applicable for action "remark".
                type: str
              prefix:
                description: IP or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format. only applicable for action "permit" and "deny"
                type: str
  state:
    description:
    - The state the configuration should be left in.
    - Refer to examples for more details.
    - With state I(replaced), for the listed prefix-lists,
      sequences that are in running-config but not in the task are negated.
    - With state I(overridden), all prefix-lists that are in running-config but
      not in the task are negated.
    - Please refer to examples for more details.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - parsed
    - gathered
    - rendered
    default: merged
"""
EXAMPLES = """
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.prefix_lists.prefix_lists import (
    Prefix_listsArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.prefix_lists.prefix_lists import (
    Prefix_lists,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=Prefix_listsArgs.argument_spec,
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

    result = Prefix_lists(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
