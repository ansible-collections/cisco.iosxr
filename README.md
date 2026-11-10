# Cisco IOSXR Collection
<!--[![Codecov](https://img.shields.io/codecov/c/github/ansible-collections/vyos)](https://codecov.io/gh/ansible-collections/cisco.iosxr)-->
[![CI](https://github.com/ansible-collections/cisco.iosxr/actions/workflows/tests.yml/badge.svg?branch=main&event=schedule)](https://github.com/ansible-collections/cisco.iosxr/actions/workflows/tests.yml)
[![Integration tests 💻](https://github.com/ansible-collections/cisco.iosxr/actions/workflows/integration-libssh.yml/badge.svg?branch=main)](https://github.com/ansible-collections/cisco.iosxr/actions/workflows/integration-libssh.yml)

The Ansible Cisco IOSXR collection includes a variety of Ansible content to help automate the management of Cisco IOSXR network appliances.

This collection has been tested against Cisco IOS-XR version 7.0.2

## Requirements

- Ansible Core 2.16.0 or later.
- Python 3.10 or later.
- The `ansible.netcommon` collection, version 8.5.2 or later.
- The `ansible.utils` collection, required transitively by `ansible.netcommon` as declared in its [collection metadata](https://github.com/ansible-collections/ansible.netcommon/blob/main/galaxy.yml).
- Python packages declared in this collection's [`requirements.txt`](https://github.com/ansible-collections/cisco.iosxr/blob/main/requirements.txt) and [`ansible.netcommon`'s requirements.txt](https://github.com/ansible-collections/ansible.netcommon/blob/main/requirements.txt): `ansible-pylibssh` 1.4.0 or later, `jxmlease`, `ncclient`, `paramiko`, `xmltodict`, `grpcio` 1.48.4 or later, and `protobuf` 3.20.0 or later.

`ansible-pylibssh` provides the libssh backend for `ansible.netcommon.network_cli`. The `paramiko` backend is now deprecated. Refer to the following [forum post](https://forum.ansible.com/t/deprecation-notice-paramiko-deprecated-for-network-cli-migrate-to-libssh-ansible-pylibssh/45782) for more information.

## Communication

* Join the Ansible forum:
  * [Get Help](https://forum.ansible.com/c/help/6): get help or help others.
  * [Posts tagged with 'network'](https://forum.ansible.com/tag/network): subscribe to participate in collection-related conversations.
  * [Ansible Network Automation Working Group](https://forum.ansible.com/g/network-wg): by joining the team you will automatically get subscribed to the posts tagged with [network](https://forum.ansible.com/tags/network).
  * [Social Spaces](https://forum.ansible.com/c/chat/4): gather and interact with fellow enthusiasts.
  * [News & Announcements](https://forum.ansible.com/c/news/5): track project-wide announcements including social events.

* The Ansible [Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn): is used to announce releases and important changes.

For more information about communication, see the [Ansible communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against the following Ansible versions: **>=2.16.0**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

### Supported connections

The Cisco IOS-XR collection supports ``network_cli``  and ``netconf`` connections. A detailed platform guide can be found [here](https://github.com/ansible-collections/cisco.iosxr/blob/main/platform_guide.rst).

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
[cisco.iosxr.iosxr_bgp_address_family](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_address_family_module.rst)|Resource module to configure BGP Address family.
[cisco.iosxr.iosxr_bgp_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_global_module.rst)|Resource module to configure BGP.
[cisco.iosxr.iosxr_bgp_neighbor_address_family](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_neighbor_address_family_module.rst)|Resource module to configure BGP Neighbor Address family.
[cisco.iosxr.iosxr_bgp_templates](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_bgp_templates_module.rst)|Manages BGP templates resource module.
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
[cisco.iosxr.iosxr_logging_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_logging_global_module.rst)|Resource module to configure logging.
[cisco.iosxr.iosxr_netconf](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_netconf_module.rst)|Configures NetConf sub-system service on Cisco IOS-XR devices
[cisco.iosxr.iosxr_ntp_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ntp_global_module.rst)|Resource module to configure NTP.
[cisco.iosxr.iosxr_ospf_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospf_interfaces_module.rst)|Resource module to configure OSPF interfaces.
[cisco.iosxr.iosxr_ospfv2](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospfv2_module.rst)|Resource module to configure OSPFv2.
[cisco.iosxr.iosxr_ospfv3](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ospfv3_module.rst)|Resource module to configure OSPFv3.
[cisco.iosxr.iosxr_ping](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_ping_module.rst)|Tests reachability using ping from IOSXR switch.
[cisco.iosxr.iosxr_prefix_lists](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_prefix_lists_module.rst)|Resource module to configure prefix lists.
[cisco.iosxr.iosxr_route_maps](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_route_maps_module.rst)|Resource module to configure route maps.
[cisco.iosxr.iosxr_snmp_server](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_snmp_server_module.rst)|Resource module to configure snmp server.
[cisco.iosxr.iosxr_static_routes](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_static_routes_module.rst)|Resource module to configure static routes.
[cisco.iosxr.iosxr_system](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_system_module.rst)|Module to manage the system attributes.
[cisco.iosxr.iosxr_user](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_user_module.rst)|Module to manage the aggregates of local users.
[cisco.iosxr.iosxr_vrf_address_family](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_vrf_address_family_module.rst)|Resource module to configure VRF Address family.
[cisco.iosxr.iosxr_vrf_global](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_vrf_global_module.rst)|Manages global VRF configuration.
[cisco.iosxr.iosxr_vrf_interfaces](https://github.com/ansible-collections/cisco.iosxr/blob/main/docs/cisco.iosxr.iosxr_vrf_interfaces_module.rst)|Resource module to configure VRF interfaces.

<!--end collection content-->

Click the ``Content`` button to see the list of content included in this collection.

## Installation

Install the certified Cisco IOS-XR collection from Red Hat Ansible Automation Hub. Access to certified content requires a Red Hat account with an active Ansible Automation Platform subscription and an Automation Hub offline token. In the Red Hat Hybrid Cloud Console, go to **Automation Hub > Connect Hub**, load the offline token, and store it securely. See the [Red Hat token management instructions](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-token_management_hub).

Configure your `ansible.cfg` to use the hosted Automation Hub service:

```ini
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url = https://console.redhat.com/api/automation-hub/content/published/
auth_url = https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token = <your_automation_hub_token>
```

Keep the token secret and out of source control. Then install the collection:

```bash
ansible-galaxy collection install cisco.iosxr --server automation_hub
```

For a `requirements.yml` file, identify Automation Hub as the source:

```yaml
---
collections:
  - name: cisco.iosxr
    source: automation_hub
```

Install the requirements with `ansible-galaxy collection install -r requirements.yml`.

### Installing from Ansible Galaxy for community use

For community use outside Red Hat supported environments, you can install the collection from Ansible Galaxy:

```bash
ansible-galaxy collection install cisco.iosxr
```

You can also add it to a `requirements.yml` file:

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
- Slack - [Ansible Network](https://ansiblenetwork.slack.com)

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

## Support

As Red Hat Ansible [Certified Content](https://catalog.redhat.com/software/search?target_platforms=Red%20Hat%20Ansible%20Automation%20Platform), this collection is entitled to support through [Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible) (AAP). Open a support case using the **Create issue** button in the top-right corner of this collection's page in Red Hat Ansible Automation Hub.

Community help is also available on [#network:ansible.com](https://matrix.to/#/#network:ansible.com) or the [Ansible Forum Network Working Group](https://forum.ansible.com/g/network-wg).

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
