# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
#
# Copyright (c) 2015 Peter Sprygada, <psprygada@ansible.com>
# Copyright (c) 2017 Red Hat Inc.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type
import json
import re

from difflib import Differ

from ansible.module_utils._text import to_bytes, to_text
from ansible.module_utils.connection import Connection, ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.netconf import (
    NetconfConnection,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import to_list


try:
    from ncclient.xml_ import to_xml

    HAS_NCCLIENT = True
except ImportError:
    HAS_NCCLIENT = False

try:
    from lxml import etree

    HAS_XML = True
except ImportError:
    HAS_XML = False

_EDIT_OPS = frozenset(["merge", "create", "replace", "delete"])

BASE_1_0 = "{urn:ietf:params:xml:ns:netconf:base:1.0}"

NS_DICT = {
    "BASE_NSMAP": {"xc": "urn:ietf:params:xml:ns:netconf:base:1.0"},
    "BANNERS_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-infra-infra-cfg"},
    "INTERFACES_NSMAP": {None: "http://openconfig.net/yang/interfaces"},
    "INSTALL_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-spirit-install-instmgr-oper"},
    "INSTALL_OLD_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-installmgr-admin-oper"},
    "HOST-NAMES_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-cfg"},
    "M:TYPE_NSMAP": {"idx": "urn:ietf:params:xml:ns:yang:iana-if-type"},
    "ETHERNET_NSMAP": {None: "http://openconfig.net/yang/interfaces/ethernet"},
    "CETHERNET_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-drivers-media-eth-cfg"},
    "INTERFACE-CONFIGURATIONS_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"},
    "INFRA-STATISTICS_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-infra-statsd-oper"},
    "INTERFACE-PROPERTIES_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-oper"},
    "IP-DOMAIN_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-cfg"},
    "SYSLOG_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-infra-syslog-cfg"},
    "AAA_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-aaa-lib-cfg"},
    "AAA_LOCALD_NSMAP": {None: "http://cisco.com/ns/yang/Cisco-IOS-XR-aaa-locald-cfg"},
}


command_spec = {"command": dict(), "prompt": dict(default=None), "answer": dict(default=None)}

CONFIG_MISPLACED_CHILDREN = [re.compile(r"^end-\s*(.+)$")]

# Objects defined in Route-policy Language guide of IOS_XR.
# Reconfiguring these objects replace existing configurations.
# Hence these objects should be played direcly from candidate
# configurations
CONFIG_BLOCKS_FORCED_IN_DIFF = [
    {"start": re.compile(r"^route-policy"), "end": re.compile(r"end-policy$")},
    {"start": re.compile(r"^prefix-set"), "end": re.compile(r"end-set$")},
    {"start": re.compile(r"^as-path-set"), "end": re.compile(r"end-set$")},
    {"start": re.compile(r"^community-set"), "end": re.compile(r"end-set$")},
    {"start": re.compile(r"^rd-set"), "end": re.compile(r"end-set$")},
    {"start": re.compile(r"^extcommunity-set"), "end": re.compile(r"end-set$")},
]


def get_connection(module):
    if hasattr(module, "connection"):
        return module.connection

    capabilities = get_capabilities(module)
    network_api = capabilities.get("network_api")
    if network_api in ["cliconf", "ansible.netcommon.grpc"]:
        module.connection = Connection(module._socket_path)
    elif network_api == "netconf":
        module.connection = NetconfConnection(module._socket_path)
    else:
        module.fail_json(msg="Invalid connection type {0!s}".format(network_api))

    return module.connection


def get_capabilities(module):
    if hasattr(module, "capabilities"):
        return module.capabilities
    try:
        capabilities = Connection(module._socket_path).get_capabilities()
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
    module.capabilities = json.loads(capabilities)

    return module.capabilities


def build_xml_subtree(container_ele, xmap, param=None, opcode=None):
    sub_root = container_ele
    meta_subtree = list()

    for key, meta in xmap.items():
        candidates = meta.get("xpath", "").split("/")
        if container_ele.tag == candidates[-2]:
            parent = container_ele
        elif sub_root.tag == candidates[-2]:
            parent = sub_root
        else:
            parent = sub_root.find(
                ".//" + meta.get("xpath", "").split(sub_root.tag + "/", 1)[1].rsplit("/", 1)[0],
            )

        if (
            opcode in ("delete", "merge") and meta.get("operation", "unknown") == "edit"
        ) or meta.get("operation", None) is None:

            if meta.get("tag", False) is True:
                if parent.tag == container_ele.tag:
                    if meta.get("ns", False) is True:
                        child = etree.Element(candidates[-1], nsmap=NS_DICT[key.upper() + "_NSMAP"])
                    else:
                        child = etree.Element(candidates[-1])
                    meta_subtree.append(child)
                    sub_root = child
                else:
                    if meta.get("ns", False) is True:
                        child = etree.SubElement(
                            parent,
                            candidates[-1],
                            nsmap=NS_DICT[key.upper() + "_NSMAP"],
                        )
                    else:
                        child = etree.SubElement(parent, candidates[-1])

                if meta.get("attrib", None) is not None and opcode in ("delete", "merge"):
                    child.set(BASE_1_0 + meta.get("attrib"), opcode)

                continue

            text = None
            param_key = key.split(":")
            if param_key[0] == "a":
                if param is not None and param.get(param_key[1], None) is not None:
                    text = param.get(param_key[1])
            elif param_key[0] == "m":
                if meta.get("value", None) is not None:
                    text = meta.get("value")

            if text:
                if meta.get("ns", False) is True:
                    child = etree.SubElement(
                        parent,
                        candidates[-1],
                        nsmap=NS_DICT[key.upper() + "_NSMAP"],
                    )
                else:
                    child = etree.SubElement(parent, candidates[-1])
                child.text = text

                if meta.get("attrib", None) is not None and opcode in ("delete", "merge"):
                    child.set(BASE_1_0 + meta.get("attrib"), opcode)

    if len(meta_subtree) > 1:
        for item in meta_subtree:
            container_ele.append(item)

    if sub_root == container_ele:
        return None
    else:
        return sub_root


def build_xml(container, xmap=None, params=None, opcode=None, namespace=None):
    """
    Builds netconf xml rpc document from meta-data

    Args:
        container: the YANG container within the namespace
        xmap: meta-data map to build xml tree
        params: Input params that feed xml tree values
        opcode: operation to be performed (merge, delete etc.)

    Example:
        Module inputs:
            banner_params = [{'banner':'motd', 'text':'Ansible banner example', 'state':'present'}]

        Meta-data definition:
            bannermap = collections.OrderedDict()
            bannermap.update([
                ('banner', {'xpath' : 'banners/banner', 'tag' : True, 'attrib' : "operation"}),
                ('a:banner', {'xpath' : 'banner/banner-name'}),
                ('a:text', {'xpath' : 'banner/banner-text', 'operation' : 'edit'})
            ])

            Fields:
                key: exact match to the key in arg_spec for a parameter
                   (prefixes --> a: value fetched from arg_spec, m: value fetched from meta-data)
                xpath: xpath of the element (based on YANG model)
                tag: True if no text on the element
                attrib: attribute to be embedded in the element (e.g. xc:operation="merge")
                operation: if edit --> includes the element in edit_config() query else ignores for get() queries
                value: if key is prefixed with "m:", value is required in meta-data

        Output:
            <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
              <banners xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-infra-infra-cfg">
                <banner xc:operation="merge">
                  <banner-name>motd</banner-name>
                  <banner-text>Ansible banner example</banner-text>
                </banner>
              </banners>
            </config>
    :returns: xml rpc document as a string
    """
    if not namespace:
        namespace = container
    if opcode == "filter":
        root = etree.Element("filter", type="subtree")
    elif opcode in ("delete", "merge"):
        root = etree.Element("config", nsmap=NS_DICT["BASE_NSMAP"])

    container_ele = etree.SubElement(root, container, nsmap=NS_DICT[namespace.upper() + "_NSMAP"])

    if xmap is not None:
        if params is None:
            build_xml_subtree(container_ele, xmap, opcode=opcode)
        else:
            subtree_list = list()
            for param in to_list(params):
                subtree_ele = build_xml_subtree(container_ele, xmap, param=param, opcode=opcode)
                if subtree_ele is not None:
                    subtree_list.append(subtree_ele)

            for item in subtree_list:
                container_ele.append(item)

    return etree.tostring(root, encoding="unicode")


def etree_find(root, node):
    try:
        root = etree.fromstring(to_bytes(root))
    except (ValueError, etree.XMLSyntaxError):
        pass

    return root.find(".//%s" % node.strip())


def etree_findall(root, node):
    try:
        root = etree.fromstring(to_bytes(root))
    except (ValueError, etree.XMLSyntaxError):
        pass

    return root.findall(".//%s" % node.strip())


def is_cliconf(module):
    capabilities = get_capabilities(module)
    return capabilities.get("network_api") == "cliconf"


def is_netconf(module):
    capabilities = get_capabilities(module)
    network_api = capabilities.get("network_api")
    if network_api == "netconf":
        if not HAS_NCCLIENT:
            module.fail_json(msg="ncclient is not installed")
        if not HAS_XML:
            module.fail_json(msg="lxml is not installed")
        return True

    return False


def get_config_diff(module, running=None, candidate=None):
    conn = get_connection(module)

    if is_cliconf(module):
        try:
            response = conn.get("show commit changes diff")
        except ConnectionError as exc:
            module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
        return response
    elif is_netconf(module):
        if running and candidate:
            # ignore rpc-reply root node and diff from data element onwards
            running_data_ele = etree.fromstring(to_bytes(running.strip())).getchildren()[0]
            candidate_data_ele = etree.fromstring(to_bytes(candidate.strip())).getchildren()[0]

            running_data = to_text(etree.tostring(running_data_ele)).strip()
            candidate_data = to_text(etree.tostring(candidate_data_ele)).strip()
            if running_data != candidate_data:
                d = Differ()
                diff = list(d.compare(running_data.splitlines(), candidate_data.splitlines()))
                return "\n".join(diff).strip()

    return None


def discard_config(module):
    conn = get_connection(module)
    try:
        if is_netconf(module):
            conn.discard_changes(remove_ns=True)
        else:
            conn.discard_changes()
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))


def commit_config(
    module,
    comment=None,
    confirmed=False,
    confirm_timeout=None,
    persist=False,
    check=False,
    label=None,
):
    conn = get_connection(module)
    reply = None
    try:
        if is_netconf(module):
            if check:
                reply = conn.validate(remove_ns=True)
            else:
                reply = conn.commit(
                    confirmed=confirmed,
                    timeout=confirm_timeout,
                    persist=persist,
                    remove_ns=True,
                )
        elif is_cliconf(module):
            if check:
                module.fail_json(
                    msg="Validate configuration is not supported with network_cli connection type",
                )
            else:
                reply = conn.commit(comment=comment, label=label)
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))

    return reply


def get_oper(module, filter=None):
    conn = get_connection(module)

    if filter is not None:
        try:
            if is_netconf(module):
                response = conn.get(filter=filter, remove_ns=True)
            else:
                response = conn.get(filter)
        except ConnectionError as exc:
            module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
    else:
        return None

    return to_bytes(etree.tostring(response), errors="surrogate_then_replace").strip()


def get_config(module, config_filter=None, source="running"):
    conn = get_connection(module)

    # Note: Does not cache config in favour of latest config on every get operation.
    try:
        if is_netconf(module):
            out = to_xml(conn.get_config(source=source, filter=config_filter, remove_ns=True))
        elif is_cliconf(module):
            out = conn.get_config(source=source, flags=config_filter)
        cfg = out.strip()
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
    return cfg


def check_existing_commit_labels(conn, label):
    out = conn.get(command="show configuration history detail | include %s" % label)
    label_exist = re.search(label, out, re.M)
    if label_exist:
        return True
    else:
        return False


def load_config(
    module,
    command_filter,
    commit=False,
    replace=False,
    comment=None,
    admin=False,
    exclusive=False,
    running=None,
    nc_get_filter=None,
    label=None,
):

    conn = get_connection(module)

    diff = None
    if is_netconf(module):
        # FIXME: check for platform behaviour and restore this
        # conn.lock(target = 'candidate')
        # conn.discard_changes()

        try:
            for filter in to_list(command_filter):
                conn.edit_config(config=filter, remove_ns=True)

            candidate = get_config(module, source="candidate", config_filter=nc_get_filter)
            diff = get_config_diff(module, running, candidate)

            if commit and diff:
                commit_config(module)
            else:
                discard_config(module)
        except ConnectionError as exc:
            module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))
        finally:
            # conn.unlock(target = 'candidate')
            pass

    elif is_cliconf(module):
        try:
            if label:
                old_label = check_existing_commit_labels(conn, label)
                if old_label:
                    module.fail_json(
                        msg="commit label {%s} is already used for"
                        " an earlier commit, please choose a different label"
                        " and rerun task" % label,
                    )

            response = conn.edit_config(
                candidate=command_filter,
                commit=commit,
                admin=admin,
                exclusive=exclusive,
                replace=replace,
                comment=comment,
                label=label,
            )
            if module._diff:
                diff = response.get("diff")

            # Overwrite the default diff by the IOS XR commit diff.
            # See plugins/cliconf/iosxr.py for this key set: show_commit_config_diff
            diff = response.get("show_commit_config_diff")

        except ConnectionError as exc:
            module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))

    return diff


def run_commands(module, commands, check_rc=True):
    connection = get_connection(module)
    try:
        return connection.run_commands(commands=commands, check_rc=check_rc)
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc))


def copy_file(module, src, dst, proto="scp"):
    conn = get_connection(module)
    try:
        conn.copy_file(source=src, destination=dst, proto=proto)
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))


def get_file(module, src, dst, proto="scp"):
    conn = get_connection(module)
    try:
        conn.get_file(source=src, destination=dst, proto=proto)
    except ConnectionError as exc:
        module.fail_json(msg=to_text(exc, errors="surrogate_then_replace"))


# A list of commands like {end-set, end-policy, ...} are part of configuration
# block like { prefix-set, as-path-set , ... } but they are not indented properly
# to be included with their parent. sanitize_config will add indentation to
# end-* commands so they are included with their parents
def sanitize_config(config, force_diff_prefix=None):
    conf_lines = config.split("\n")
    for regex in CONFIG_MISPLACED_CHILDREN:
        for index, line in enumerate(conf_lines):
            m = regex.search(line)
            if m and m.group(0):
                if force_diff_prefix:
                    conf_lines[index] = "  " + m.group(0) + force_diff_prefix
                else:
                    conf_lines[index] = "  " + m.group(0)
    conf = ("\n").join(conf_lines)
    return conf


def mask_config_blocks_from_diff(config, candidate, force_diff_prefix):
    conf_lines = config.split("\n")
    candidate_lines = candidate.split("\n")

    for regex in CONFIG_BLOCKS_FORCED_IN_DIFF:
        block_index_start_end = []
        start_index = None
        for index, line in enumerate(candidate_lines):
            startre = regex["start"].search(line)
            if startre and startre.group(0):
                start_index = index
            else:
                endre = regex["end"].search(line)
                if endre and endre.group(0) and start_index:
                    end_index = index
                    new_block = True
                    for prev_start, prev_end in block_index_start_end:
                        if start_index == prev_start:
                            # This might be end-set of another regex
                            # otherwise we would be having new start
                            new_block = False
                            break
                    if new_block and end_index:
                        block_index_start_end.append((start_index, end_index))

        for start, end in block_index_start_end:
            diff = False
            if candidate_lines[start] in conf_lines:
                run_conf_start_index = conf_lines.index(candidate_lines[start])
            else:
                diff = False
                continue
            for i in range(start, end + 1):
                if conf_lines[run_conf_start_index] == candidate_lines[i]:
                    run_conf_start_index = run_conf_start_index + 1
                else:
                    diff = True
                    break
            if diff:
                run_conf_start_index = conf_lines.index(candidate_lines[start])
                for i in range(start, end + 1):
                    conf_lines[run_conf_start_index] = (
                        conf_lines[run_conf_start_index] + force_diff_prefix
                    )
                    run_conf_start_index = run_conf_start_index + 1

    conf = ("\n").join(conf_lines)
    return conf


def get_os_version(module):
    connection = get_connection(module)
    if connection.get_device_info():
        os_version = connection.get_device_info()["network_os_version"]
        return os_version
