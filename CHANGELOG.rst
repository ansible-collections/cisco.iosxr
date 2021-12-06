====================================
Cisco Iosxr Collection Release Notes
====================================

.. contents:: Topics

v2.6.0
======

Minor Changes
-------------

- Add iosxr_snmp_server resource module.
- Added support for keys net_group, port_group to resolve issue with fact gathering against IOS-XR 6.6.3.

Bugfixes
--------

- fix issue of local variable 'start_index' referenced before assignment with cisco.iosxr.iosxr_config.
- iosxr_user - replaced custom paramiko sftp and ssh usage with native "copy_file" and "send_command" functions. Fixed issue when ssh key copying doesn't work with network_cli or netconf plugin by deleting "provider" usage. Fixed improper handling of "No such configuration item" when getting data for username section, without that ansible always tried to delete user "No" when purging if there is no any user in config. Fixed one-line admin mode commands not work anymore for ssh key management on IOS XR Software, Version 7.1.3, and add support of "admin" module property (https://github.com/ansible-collections/cisco.iosxr/pull/15)

Documentation Changes
---------------------

- Update valid docs for iosxr_logging_global and prefix_list

New Modules
-----------

- iosxr_snmp_server - Manages snmp-server resource module

v2.5.0
======

Minor Changes
-------------

- Added iosxr ntp_global resource module.

Documentation Changes
---------------------

- Update valid deprecation date in bgp module.

v2.4.0
======

Minor Changes
-------------

- Add iosxr_logging_global resource module.

Deprecated Features
-------------------

- The iosxr_logging module has been deprecated in favor of the new iosxr_logging_global resource module and will be removed in a release after '2023-08-01'.

Bugfixes
--------

- fix issue in prefix-lists facts code when prefix-lists facts are empty. (https://github.com/ansible-collections/cisco.iosxr/pull/161)

New Modules
-----------

- iosxr_logging_global - Manages logging attributes of Cisco IOSXR network devices

v2.3.0
======

Minor Changes
-------------

- Add `iosxr_prefix_lists` resource module.

Bugfixes
--------

- To add updated route policy params to Bgp nbr AF RM
- fix backword compatibility issue for iosxr 6.x.
- fix intermittent issue on CI for iosxr_banner module.
- fix iosxr_config issue for prefix-set,route-policy config
- fix static routes interface parsing issue.

New Modules
-----------

- iosxr_prefix_lists - Prefix-Lists resource module.

v2.2.0
======

Minor Changes
-------------

- Add new keys for iosxr_l2_interface, iosxr_logging.
- Fix integration tests for iosxr_config, iosxr_smoke,iosxr_facts,iosxr_l2_interfaces,iosxr_lag_interfaces, iosxr_logging,iosxr_user.

Bugfixes
--------

- Add warning when comment is not supported by IOSXR.
- Fix issue of commit operation which was not failing for invalid inputs.

v2.1.0
======

Minor Changes
-------------

- Add support for available_network_resources key, which allows to fetch the available resources for a platform (https://github.com/ansible-collections/cisco.iosxr/issues/119).
- Update psudo-atomic operation scenario tests with correct assertion.

Bugfixes
--------

- Avoid using default value for comment for iosxr version > 7.2(Module=iosxr_config)
- Avoid using default value for comment when "comment is not supported" by device.

v2.0.2
======

Bugfixes
--------

- For versions >=2.0.1, this collection requires ansible.netcommon >=2.0.1.
- Re-releasing this collection with ansible.netcommon dependency requirements updated.

v2.0.1
======

Security Fixes
--------------

- Properly mask values of sensitive keys in module result.

Bugfixes
--------

- Add fix for interfaces which are not in running config should get merged when state is merged. (https://github.com/ansible-collections/cisco.iosxr/issues/106)
- Update valid hostname info in iosxr_facs using show running-conf hostname command. (https://github.com/ansible-collections/cisco.iosxr/issues/103)

v2.0.0
======

Major Changes
-------------
- Requires ansible.netcommon v2.0.0+ to support `ansible_network_single_user_mode` and `ansible_network_import_modules`.
- Please refer to ansible.netcommon `changelog <https://github.com/ansible-collections/ansible.netcommon/blob/main/changelogs/CHANGELOG.rst#ansible-netcommon-collection-release-notes>`_ for more details.
- ipaddress is no longer in ansible.netcommon. For Python versions without ipaddress (< 3.0), the ipaddress package is now required.

Minor Changes
-------------

- Add iosxr_bgp_address_family resource module (https://github.com/ansible-collections/cisco.iosxr/pull/105.).
- Add iosxr_bgp_global resource module (https://github.com/ansible-collections/cisco.iosxr/pull/101.).
- Add iosxr_bgp_neighbor_address_family resource module (https://github.com/ansible-collections/cisco.iosxr/pull/107.).
- Add missing examples for bgp_address_family module.
- Add support for single_user_mode.
- Fix integration testcases for bgp_address_family and bgp_neighbor_address_family.
- Fix issue in delete state in bgp_address_family (https://github.com/ansible-collections/cisco.iosxr/pull/109).
- Move iosxr_config idempotent warning message with the task response under `warnings` key if `changed` is `True`
- Re-use device_info dict instead of building it every time.

Bugfixes
--------

- Fix to accurately report configuration failure during pseudo-atomic operation fior iosxr-6.6.3 (https://github.com/ansible-collections/cisco.iosxr/issues/92).

New Modules
-----------

- iosxr_bgp_address_family - Manages BGP Address Family resource module.
- iosxr_bgp_global - Manages BGP global resource module.
- iosxr_bgp_neighbor_address_family - Manages BGP neighbor address family resource module.

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
