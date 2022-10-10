# Cisco IOSXR Collection
[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/project/github.com/ansible-collections/cisco.iosxr) <!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/vyos)](https://codecov.io/gh/ansible-collections/cisco.iosxr)-->

The Ansible Cisco IOSXR collection includes a variety of Ansible content to help automate the management of Cisco IOSXR network appliances.

This collection has been tested against Cisco IOSXR version 7.0.2.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

For collections that support Ansible 2.9, please ensure you update your `network_os` to use the
fully qualified collection name (for example, `cisco.ios.ios`).
Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

### Supported connections
The Cisco IOSXR collection supports ``network_cli``  and ``netconf`` connections.

## Included content
<!--start collection content-->
### Cliconf plugins
Name | Description
--- | ---
[cisco.iosxr.iosxr](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_cliconf.rst)|Use iosxr cliconf to run command on Cisco IOS XR platform

### Netconf plugins
Name | Description
--- | ---
[cisco.iosxr.iosxr](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_netconf.rst)|Use iosxr netconf plugin to run netconf commands on Cisco IOSXR platform

### Modules
Name | Description
--- | ---
[cisco.iosxr.iosxr_acl_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_acl_interfaces_module.rst)|Resource module to configure ACL interfaces.
[cisco.iosxr.iosxr_acls](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_acls_module.rst)|Resource module to configure ACLs.
[cisco.iosxr.iosxr_banner](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_banner_module.rst)|Module to configure multiline banners.
[cisco.iosxr.iosxr_bgp](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_module.rst)|Module to configure BGP protocol settings.
[cisco.iosxr.iosxr_bgp_address_family](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_address_family_module.rst)|Resource module to configure BGP Address family.
[cisco.iosxr.iosxr_bgp_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_global_module.rst)|Resource module to configure BGP.
[cisco.iosxr.iosxr_bgp_neighbor_address_family](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_neighbor_address_family_module.rst)|Resource module to configure BGP Neighbor Address family.
[cisco.iosxr.iosxr_command](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_command_module.rst)|Module to run commands on remote devices.
[cisco.iosxr.iosxr_config](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_config_module.rst)|Module to manage configuration sections.
[cisco.iosxr.iosxr_facts](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_facts_module.rst)|Module to collect facts from remote devices.
[cisco.iosxr.iosxr_hostname](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_hostname_module.rst)|Resource module to configure hostname.
[cisco.iosxr.iosxr_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_interfaces_module.rst)|Resource module to configure interfaces.
[cisco.iosxr.iosxr_l2_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_l2_interfaces_module.rst)|Resource Module to configure L2 interfaces.
[cisco.iosxr.iosxr_l3_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_l3_interfaces_module.rst)|Resource module to configure L3 interfaces.
[cisco.iosxr.iosxr_lacp](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lacp_module.rst)|Resource module to configure LACP.
[cisco.iosxr.iosxr_lacp_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lacp_interfaces_module.rst)|Resource module to configure LACP interfaces.
[cisco.iosxr.iosxr_lag_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lag_interfaces_module.rst)|Resource module to configure LAG interfaces.
[cisco.iosxr.iosxr_lldp_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lldp_global_module.rst)|Resource module to configure LLDP.
[cisco.iosxr.iosxr_lldp_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_lldp_interfaces_module.rst)|Resource module to configure LLDP interfaces.
[cisco.iosxr.iosxr_logging](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_logging_module.rst)|(deprecated, removed after 2023-08-01) Configuration management of system logging services on network devices
[cisco.iosxr.iosxr_logging_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_logging_global_module.rst)|Resource module to configure logging.
[cisco.iosxr.iosxr_netconf](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_netconf_module.rst)|Configures NetConf sub-system service on Cisco IOS-XR devices
[cisco.iosxr.iosxr_ntp_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ntp_global_module.rst)|Resource module to configure NTP.
[cisco.iosxr.iosxr_ospf_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospf_interfaces_module.rst)|Resource module to configure OSPF interfaces.
[cisco.iosxr.iosxr_ospfv2](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospfv2_module.rst)|Resource module to configure OSPFv2.
[cisco.iosxr.iosxr_ospfv3](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospfv3_module.rst)|Resource module to configure OSPFv3.
[cisco.iosxr.iosxr_ping](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ping_module.rst)|Tests reachability using ping from IOSXR switch.
[cisco.iosxr.iosxr_prefix_lists](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_prefix_lists_module.rst)|Resource module to configure prefix lists.
[cisco.iosxr.iosxr_snmp_server](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_snmp_server_module.rst)|Resource module to configure snmp server.
[cisco.iosxr.iosxr_static_routes](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_static_routes_module.rst)|Resource module to configure static routes.
[cisco.iosxr.iosxr_system](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_system_module.rst)|Module to manage the system attributes.
[cisco.iosxr.iosxr_user](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_user_module.rst)|Module to manage the aggregates of local users.

<!--end collection content-->

Click the ``Content`` button to see the list of content included in this collection.

## Installing this collection

You can install the Cisco IOSXR collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install cisco.iosxr

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: cisco.iosxr
```
## Using this collection


This collection includes [network resource modules](https://docs.ansible.com/ansible/latest/network/user_guide/network_resource_modules.html).

### Using modules from the Cisco IOSXR collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `cisco.iosxr.iosxr_l2_interfaces`.
The following example task replaces configuration changes in the existing configuration on a Cisco IOSXR network device, using the FQCN:

```yaml
---
 - name: Replace device configuration of specified L2 interfaces with provided configuration.
   cisco.iosxr.iosxr_l2_interfaces:
     config:
       - name: GigabitEthernet0/0/0/4
         native_vlan: 40
         l2transport: True
         l2protocol:
         - stp: forward
       - name: GigabitEthernet0/0/0/3.900
         q_vlan:
         - 20
         - any
     state: replaced

```

**NOTE**: For Ansible 2.9, you may not see deprecation warnings when you run your playbooks with this collection. Use this documentation to track when a module is deprecated.


### See Also:

* [Cisco IOSXR Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_iosxr.html)
* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Cisco IOSXR collection repository](https://github.com/ansible-collections/cisco.iosxr). See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for complete details.

You can also join us on:

- IRC - the ``#ansible-network`` [libera.chat](https://libera.chat/) channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

### Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Release notes

Release notes are available [here](https://github.com/ansible-collections/cisco.iosxr/blob/main/CHANGELOG.rst).

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
