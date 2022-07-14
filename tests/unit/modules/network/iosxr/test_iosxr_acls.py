#
# (c) 2019, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible_collections.cisco.iosxr.plugins.modules import iosxr_acls
from ansible_collections.cisco.iosxr.tests.unit.compat.mock import patch
from ansible_collections.cisco.iosxr.tests.unit.modules.utils import set_module_args

from .iosxr_module import TestIosxrModule, load_fixture


class TestIosxrAclsModule(TestIosxrModule):
    module = iosxr_acls

    def setUp(self):
        super(TestIosxrAclsModule, self).setUp()

        self.mock_get_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.get_config",
        )
        self.get_config = self.mock_get_config.start()

        self.mock_load_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.network.Config.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_get_resource_connection_config = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.cfg.base.get_resource_connection",
        )
        self.get_resource_connection_config = self.mock_get_resource_connection_config.start()

        self.mock_get_resource_connection_facts = patch(
            "ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts.get_resource_connection",
        )
        self.get_resource_connection_facts = self.mock_get_resource_connection_facts.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.acls.acls.AclsFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestIosxrAclsModule, self).tearDown()
        self.mock_get_resource_connection_config.stop()
        self.mock_get_resource_connection_facts.stop()
        self.mock_get_config.stop()
        self.mock_load_config.stop()
        self.mock_execute_show_command.stop()

    def _prepare(self):
        def load_from_file(*args, **kwargs):
            return load_fixture("iosxr_acls_config.cfg")

        self.execute_show_command.side_effect = load_from_file

    def test_iosxr_acls_merged(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        acls=[
                            dict(
                                name="acl_1",
                                aces=[
                                    dict(
                                        sequence="30",
                                        grant="permit",
                                        protocol="ospf",
                                        source=dict(prefix="192.168.1.0/24"),
                                        destination=dict(any="true"),
                                        log="true",
                                    ),
                                    dict(
                                        sequence="40",
                                        grant="deny",
                                        protocol="ipv4",
                                        source=dict(
                                            address="10.233.0.0",
                                            wildcard_bits="0.0.255.255",
                                        ),
                                        destination=dict(
                                            net_group="netgroup1",
                                        ),
                                    ),
                                    dict(
                                        sequence="50",
                                        grant="deny",
                                        protocol="ipv4",
                                        source=dict(
                                            address="10.233.0.0",
                                            wildcard_bits="0.0.255.255",
                                        ),
                                        destination=dict(
                                            port_group="portgroup1",
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            "ipv4 access-list acl_1",
            "30 permit ospf 192.168.1.0 0.0.0.255 any log",
            "40 deny ipv4 10.233.0.0 0.0.255.255 net-group netgroup1",
            "50 deny ipv4 10.233.0.0 0.0.255.255 port-group portgroup1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_iosxr_acls_merged_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        acls=[
                            dict(
                                name="acl_2",
                                aces=[
                                    dict(
                                        sequence="10",
                                        grant="deny",
                                        protocol="ipv4",
                                        destination=dict(any="true"),
                                        source=dict(any="true"),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_acls_replaced(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        acls=[
                            dict(
                                name="acl_2",
                                aces=[
                                    dict(
                                        sequence="30",
                                        grant="permit",
                                        protocol="ospf",
                                        source=dict(prefix="10.0.0.0/8"),
                                        destination=dict(any="true"),
                                        log="true",
                                    ),
                                    dict(
                                        sequence="40",
                                        grant="deny",
                                        protocol="ipv4",
                                        source=dict(
                                            address="10.233.0.0",
                                            wildcard_bits="0.0.255.255",
                                        ),
                                        destination=dict(
                                            net_group="netgroup1",
                                        ),
                                    ),
                                    dict(
                                        sequence="50",
                                        grant="deny",
                                        protocol="ipv4",
                                        source=dict(
                                            address="10.233.0.0",
                                            wildcard_bits="0.0.255.255",
                                        ),
                                        destination=dict(
                                            port_group="portgroup1",
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            "ipv4 access-list acl_2",
            "no 10",
            "no 20",
            "30 permit ospf 10.0.0.0 0.255.255.255 any log",
            "40 deny ipv4 10.233.0.0 0.0.255.255 net-group netgroup1",
            "50 deny ipv4 10.233.0.0 0.0.255.255 port-group portgroup1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_iosxr_acls_replaced_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        acls=[
                            dict(
                                name="acl_2",
                                aces=[
                                    dict(
                                        sequence="10",
                                        grant="deny",
                                        protocol="ipv4",
                                        destination=dict(any="true"),
                                        source=dict(any="true"),
                                    ),
                                    dict(
                                        sequence="20",
                                        grant="permit",
                                        protocol="tcp",
                                        destination=dict(any="true"),
                                        source=dict(host="192.168.1.100"),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="replaced",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_acls_overridden(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        acls=[
                            dict(
                                name="acl_2",
                                aces=[
                                    dict(
                                        sequence="40",
                                        grant="permit",
                                        protocol="ospf",
                                        source=dict(any="true"),
                                        destination=dict(any="true"),
                                        log="true",
                                    ),
                                    dict(
                                        sequence="50",
                                        grant="deny",
                                        protocol="ipv4",
                                        source=dict(
                                            address="10.233.0.0",
                                            wildcard_bits="0.0.255.255",
                                        ),
                                        destination=dict(
                                            net_group="netgroup1",
                                        ),
                                    ),
                                    dict(
                                        sequence="60",
                                        grant="deny",
                                        protocol="ipv4",
                                        source=dict(
                                            address="10.233.0.0",
                                            wildcard_bits="0.0.255.255",
                                        ),
                                        destination=dict(
                                            port_group="portgroup1",
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            "no ipv6 access-list acl6_1",
            "no ipv4 access-list acl_1",
            "ipv4 access-list acl_2",
            "no 10",
            "no 20",
            "40 permit ospf any any log",
            "50 deny ipv4 10.233.0.0 0.0.255.255 net-group netgroup1",
            "60 deny ipv4 10.233.0.0 0.0.255.255 port-group portgroup1",
        ]
        self.execute_module(changed=True, commands=commands)

    def test_iosxr_acls_overridden_idempotent(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        acls=[
                            dict(
                                name="acl_1",
                                aces=[
                                    dict(
                                        sequence="10",
                                        grant="deny",
                                        protocol="ipv4",
                                        source=dict(
                                            address="10.233.0.0",
                                            wildcard_bits="0.0.255.255",
                                        ),
                                        destination=dict(
                                            net_group="netgroup1",
                                        ),
                                    ),
                                    dict(
                                        sequence="20",
                                        grant="deny",
                                        protocol="ipv4",
                                        source=dict(
                                            address="10.233.0.0",
                                            wildcard_bits="0.0.255.255",
                                        ),
                                        destination=dict(
                                            port_group="portgroup1",
                                        ),
                                    ),
                                ],
                            ),
                            dict(
                                name="acl_2",
                                aces=[
                                    dict(
                                        sequence="10",
                                        grant="deny",
                                        protocol="ipv4",
                                        destination=dict(any="true"),
                                        source=dict(any="true"),
                                    ),
                                    dict(
                                        sequence="20",
                                        grant="permit",
                                        protocol="tcp",
                                        destination=dict(any="true"),
                                        source=dict(host="192.168.1.100"),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    dict(
                        afi="ipv6",
                        acls=[
                            dict(
                                name="acl6_1",
                                aces=[
                                    dict(
                                        sequence="10",
                                        grant="deny",
                                        protocol="icmpv6",
                                        destination=dict(any="true"),
                                        source=dict(any="true"),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        self.execute_module(changed=False, commands=[])

    def test_iosxr_acls_deletedacls(self):
        self._prepare()
        set_module_args(
            dict(
                config=[dict(afi="ipv6", acls=[dict(name="acl6_1")])],
                state="deleted",
            ),
        )
        commands = ["no ipv6 access-list acl6_1"]
        self.execute_module(changed=True, commands=commands)

    def test_iosxr_acls_deletedafis(self):
        self._prepare()
        set_module_args(dict(config=[dict(afi="ipv4")], state="deleted"))
        commands = ["no ipv4 access-list acl_2", "no ipv4 access-list acl_1"]
        self.execute_module(changed=True, commands=commands)

    def test_iosxr_acls_rendered(self):
        self._prepare()
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        acls=[
                            dict(
                                name="acl_2",
                                aces=[
                                    dict(
                                        grant="permit",
                                        source=dict(any="true"),
                                        destination=dict(any="true"),
                                        protocol="igmp",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="rendered",
            ),
        )
        commands = ["ipv4 access-list acl_2", "permit igmp any any"]
        result = self.execute_module(changed=False)
        self.assertEqual(
            sorted(result["rendered"]),
            sorted(commands),
            result["rendered"],
        )

    def test_iosxr_acls_overridden_on_empty_config(self):
        self.execute_show_command.return_value = ""
        set_module_args(
            dict(
                config=[
                    dict(
                        afi="ipv4",
                        acls=[
                            dict(
                                name="acl_1",
                                aces=[
                                    dict(
                                        sequence="10",
                                        grant="deny",
                                        source=dict(any=True),
                                        destination=dict(any=True),
                                        protocol="ip",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
                state="overridden",
            ),
        )
        cmds = ["ipv4 access-list acl_1", "10 deny ip any any"]
        self.execute_module(changed=True, commands=cmds)

    def test_iosxr_acls_parsed_matches(self):
        set_module_args(
            dict(
                running_config="""ipv4 access-list ACL_NAME\n5 permit ipv4 host x.x.x.x any (409 matches)""",
                state="parsed",
            ),
        )
        result = self.execute_module(changed=False)
        parsed_list = [
            {
                "acls": [
                    {
                        "name": "ACL_NAME",
                        "aces": [
                            {
                                "sequence": 5,
                                "grant": "permit",
                                "protocol": "ipv4",
                                "source": {"host": "x.x.x.x"},
                                "destination": {"any": True},
                            },
                        ],
                    },
                ],
                "afi": "ipv4",
            },
        ]
        self.assertEqual(parsed_list, result["parsed"])
