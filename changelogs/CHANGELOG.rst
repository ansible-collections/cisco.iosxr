====================================
Cisco Iosxr Collection Release Notes
====================================

.. contents:: Topics


v1.2.1
======

Bugfixes
--------

- Update docs to clarify the idemptonecy releated caveat and add it in the output warnings (https://github.com/ansible-collections/ansible.netcommon/pull/189)

v1.2.0
======

Minor Changes
-------------

- Added iosxr ospf_interfaces resource module (https://github.com/ansible-collections/cisco.iosxr/pull/84).

Bugfixes
--------

- Add version key to galaxy.yaml to work around ansible-galaxy bug
- Fix iosxr_acls throwing a traceback with overridden (https://github.com/ansible-collections/cisco.iosxr/issues/87).
- require one to specify a banner delimiter in order to fix a timeout when using multi-line strings

New Modules
-----------

- iosxr_ospf_interfaces - OSPF Interfaces Resource Module.

v1.1.0
======

Minor Changes
-------------

- Added iosxr ospfv3 resource module (https://github.com/ansible-collections/cisco.iosxr/pull/81).
- Platform supported coments token to be provided when invoking the object.

New Modules
-----------

- iosxr_ospfv3 - ospfv3 resource module

v1.0.5
======

Bugfixes
--------

- Confirmed commit fails with TypeError in IOS XR netconf plugin (https://github.com/ansible-collections/cisco.iosxr/issues/74)
- running config data for interface split when substring interface starts with newline

v1.0.4
======

Release Summary
---------------

- Rereleased 1.0.3 with updated changelog.

v1.0.3
======

Release Summary
---------------

- Rereleased 1.0.2 with regenerated documentation.

v1.0.2
======

Bugfixes
--------

- Make `src`, `backup` and `backup_options` in iosxr_config work when module alias is used (https://github.com/ansible-collections/cisco.iosxr/pull/63).
- Makes sure that docstring and argspec are in sync and removes sanity ignores (https://github.com/ansible-collections/cisco.iosxr/pull/62).
- Update docs after sanity fixes to modules.

v1.0.1
======

Minor Changes
-------------

- Bring plugin table to correct position (https://github.com/ansible-collections/cisco.iosxr/pull/44)

v1.0.0
======

New Plugins
-----------

Cliconf
~~~~~~~

- iosxr - Use iosxr cliconf to run command on Cisco IOS XR platform

Netconf
~~~~~~~

- iosxr - Use iosxr netconf plugin to run netconf commands on Cisco IOSXR platform

New Modules
-----------

- iosxr_acl_interfaces - ACL interfaces resource module
- iosxr_acls - ACLs resource module
- iosxr_banner - Manage multiline banners on Cisco IOS XR devices
- iosxr_bgp - Configure global BGP protocol settings on Cisco IOS-XR
- iosxr_command - Run commands on remote devices running Cisco IOS XR
- iosxr_config - Manage Cisco IOS XR configuration sections
- iosxr_facts - Get facts about iosxr devices.
- iosxr_interface - (deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS XR network devices
- iosxr_interfaces - Interfaces resource module
- iosxr_l2_interfaces - L2 interfaces resource module
- iosxr_l3_interfaces - L3 interfaces resource module
- iosxr_lacp - LACP resource module
- iosxr_lacp_interfaces - LACP interfaces resource module
- iosxr_lag_interfaces - LAG interfaces resource module
- iosxr_lldp_global - LLDP resource module
- iosxr_lldp_interfaces - LLDP interfaces resource module
- iosxr_logging - Configuration management of system logging services on network devices
- iosxr_netconf - Configures NetConf sub-system service on Cisco IOS-XR devices
- iosxr_ospfv2 - OSPFv2 resource module
- iosxr_static_routes - Static routes resource module
- iosxr_system - Manage the system attributes on Cisco IOS XR devices
- iosxr_user - Manage the aggregate of local users on Cisco IOS XR device
