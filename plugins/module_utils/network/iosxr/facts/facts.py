#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The facts class for iosxr
this file validates each subset of facts and selectively
calls the appropriate facts gathering function
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts import (
    FactsBase,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.legacy.base import (
    Default,
    Hardware,
    Interfaces,
    Config,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lacp.lacp import (
    LacpFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lacp_interfaces.lacp_interfaces import (
    Lacp_interfacesFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lldp_global.lldp_global import (
    Lldp_globalFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lldp_interfaces.lldp_interfaces import (
    Lldp_interfacesFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.interfaces.interfaces import (
    InterfacesFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.lag_interfaces.lag_interfaces import (
    Lag_interfacesFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.l2_interfaces.l2_interfaces import (
    L2_InterfacesFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.l3_interfaces.l3_interfaces import (
    L3_InterfacesFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.acl_interfaces.acl_interfaces import (
    Acl_interfacesFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.acls.acls import (
    AclsFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.static_routes.static_routes import (
    Static_routesFacts,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.facts.ospfv2.ospfv2 import (
    Ospfv2Facts,
)


FACT_LEGACY_SUBSETS = dict(
    default=Default, hardware=Hardware, interfaces=Interfaces, config=Config
)
FACT_RESOURCE_SUBSETS = dict(
    lacp=LacpFacts,
    lacp_interfaces=Lacp_interfacesFacts,
    lldp_global=Lldp_globalFacts,
    lldp_interfaces=Lldp_interfacesFacts,
    interfaces=InterfacesFacts,
    l2_interfaces=L2_InterfacesFacts,
    lag_interfaces=Lag_interfacesFacts,
    l3_interfaces=L3_InterfacesFacts,
    acl_interfaces=Acl_interfacesFacts,
    acls=AclsFacts,
    static_routes=Static_routesFacts,
    ospfv2=Ospfv2Facts,
)


class Facts(FactsBase):
    """ The fact class for iosxr
    """

    VALID_LEGACY_GATHER_SUBSETS = frozenset(FACT_LEGACY_SUBSETS.keys())
    VALID_RESOURCE_SUBSETS = frozenset(FACT_RESOURCE_SUBSETS.keys())

    def __init__(self, module):
        super(Facts, self).__init__(module)

    def get_facts(
        self, legacy_facts_type=None, resource_facts_type=None, data=None
    ):
        """ Collect the facts for iosxr

        :param legacy_facts_type: List of legacy facts types
        :param resource_facts_type: List of resource fact types
        :param data: previously collected conf
        :rtype: dict
        :return: the facts gathered
        """
        if self.VALID_RESOURCE_SUBSETS:
            self.get_network_resources_facts(
                FACT_RESOURCE_SUBSETS, resource_facts_type, data
            )

        if self.VALID_LEGACY_GATHER_SUBSETS:
            self.get_network_legacy_facts(
                FACT_LEGACY_SUBSETS, legacy_facts_type
            )

        return self.ansible_facts, self._warnings
