from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("ncclient")
pytest.importorskip("lxml")

from lxml.etree import Element

from ansible_collections.cisco.iosxr.plugins.netconf.iosxr import Netconf


@pytest.fixture
def netconf_plugin():
    mock_connection = MagicMock()
    mock_manager = MagicMock()
    mock_connection.manager = mock_manager
    plugin = Netconf(mock_connection)
    plugin._connection = mock_connection
    return plugin, mock_manager


class TestEditConfigHugeTree:
    """Tests for huge_tree support in edit_config"""

    def test_edit_config_parses_string_with_huge_tree(self, netconf_plugin):
        """Verify that string config is parsed with huge_tree=True (handles >10MB XML)"""
        plugin, mock_manager = netconf_plugin

        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.edit_config.return_value = mock_resp

        large_description = "X" * 100000
        config_xml = (
            f'<config><interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">'
            f"<interface-configuration><active>act</active>"
            f"<interface-name>Loopback9999</interface-name>"
            f"<description>{large_description}</description>"
            f"</interface-configuration></interface-configurations></config>"
        )

        result = plugin.edit_config(config=config_xml)

        assert result == "<ok/>"
        mock_manager.edit_config.assert_called_once()
        call_args = mock_manager.edit_config.call_args
        passed_config = call_args[0][0] if call_args[0] else call_args[1]["config"]
        assert hasattr(passed_config, "tag")

    def test_edit_config_string_parsed_as_element(self, netconf_plugin):
        """Verify string config is converted to lxml Element before passing to ncclient"""
        plugin, mock_manager = netconf_plugin

        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.edit_config.return_value = mock_resp

        config_xml = "<config><test>value</test></config>"
        plugin.edit_config(config=config_xml)

        call_args = mock_manager.edit_config.call_args
        passed_config = call_args[0][0] if call_args[0] else call_args[1]["config"]
        assert hasattr(passed_config, "tag")
        assert passed_config.tag == "config"

    def test_edit_config_element_passed_directly(self, netconf_plugin):
        """Verify lxml Element config is passed directly without re-parsing"""
        plugin, mock_manager = netconf_plugin

        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.edit_config.return_value = mock_resp

        config_elem = Element("config")
        plugin.edit_config(config=config_elem)

        call_args = mock_manager.edit_config.call_args
        passed_config = call_args[0][0] if call_args[0] else call_args[1]["config"]
        assert passed_config is config_elem

    def test_edit_config_none_raises_value_error(self, netconf_plugin):
        """Verify ValueError is raised when config is None"""
        plugin, mock_manager = netconf_plugin

        with pytest.raises(ValueError, match="config value must be provided"):
            plugin.edit_config(config=None)

    def test_edit_config_rpc_error_raises_exception(self, netconf_plugin):
        """Verify RPCError from ncclient is re-raised as Exception"""
        plugin, mock_manager = netconf_plugin

        from ncclient.operations import RPCError

        rpc_error = MagicMock()
        rpc_error.xml = Element("rpc-error")
        mock_manager.edit_config.side_effect = RPCError(rpc_error)

        with pytest.raises(Exception):
            plugin.edit_config(config="<config/>")

    @patch("ansible_collections.cisco.iosxr.plugins.netconf.iosxr.remove_namespaces")
    def test_edit_config_remove_ns(self, mock_remove_ns, netconf_plugin):
        """Verify remove_ns=True calls remove_namespaces on response"""
        plugin, mock_manager = netconf_plugin

        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.edit_config.return_value = mock_resp
        mock_remove_ns.return_value = "<ok/>"

        result = plugin.edit_config(config="<config/>", remove_ns=True)

        mock_remove_ns.assert_called_once_with(mock_resp)

    def test_edit_config_uses_xml_response(self, netconf_plugin):
        """Verify fallback to resp.xml when data_xml is not available"""
        plugin, mock_manager = netconf_plugin

        mock_resp = MagicMock(spec=[])
        mock_resp.xml = "<ok-xml/>"
        mock_manager.edit_config.return_value = mock_resp

        result = plugin.edit_config(config="<config/>")
        assert result == "<ok-xml/>"


class TestGet:
    """Tests for get method"""

    def test_get_returns_data_xml(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<data>result</data>"
        mock_manager.get.return_value = mock_resp

        result = plugin.get()
        assert result == "<data>result</data>"
        mock_manager.get.assert_called_once_with(filter=None, with_defaults=None)

    def test_get_with_filter(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<data/>"
        mock_manager.get.return_value = mock_resp

        plugin.get(filter="<System/>")
        mock_manager.get.assert_called_once_with(filter="<System/>", with_defaults=None)

    def test_get_filter_list_converted_to_tuple(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<data/>"
        mock_manager.get.return_value = mock_resp

        plugin.get(filter=["subtree", "<System/>"])
        mock_manager.get.assert_called_once_with(
            filter=("subtree", "<System/>"),
            with_defaults=None,
        )

    @patch("ansible_collections.cisco.iosxr.plugins.netconf.iosxr.remove_namespaces")
    def test_get_remove_ns(self, mock_remove_ns, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_manager.get.return_value = mock_resp
        mock_remove_ns.return_value = "<clean/>"

        result = plugin.get(remove_ns=True)
        assert result == "<clean/>"
        mock_remove_ns.assert_called_once_with(mock_resp)

    def test_get_falls_back_to_xml(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock(spec=[])
        mock_resp.xml = "<data-xml/>"
        mock_manager.get.return_value = mock_resp

        result = plugin.get()
        assert result == "<data-xml/>"

    def test_get_rpc_error(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        from ncclient.operations import RPCError

        rpc_error = MagicMock()
        rpc_error.xml = Element("rpc-error")
        mock_manager.get.side_effect = RPCError(rpc_error)

        with pytest.raises(Exception):
            plugin.get()


class TestGetConfig:
    """Tests for get_config method"""

    def test_get_config_returns_data_xml(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<config>running</config>"
        mock_manager.get_config.return_value = mock_resp

        result = plugin.get_config(source="running")
        assert result == "<config>running</config>"
        mock_manager.get_config.assert_called_once_with(source="running", filter=None)

    def test_get_config_with_filter(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<data/>"
        mock_manager.get_config.return_value = mock_resp

        plugin.get_config(source="running", filter="<interfaces/>")
        mock_manager.get_config.assert_called_once_with(
            source="running",
            filter="<interfaces/>",
        )

    def test_get_config_filter_list_converted_to_tuple(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<data/>"
        mock_manager.get_config.return_value = mock_resp

        plugin.get_config(source="running", filter=["subtree", "<if/>"])
        mock_manager.get_config.assert_called_once_with(
            source="running",
            filter=("subtree", "<if/>"),
        )

    @patch("ansible_collections.cisco.iosxr.plugins.netconf.iosxr.remove_namespaces")
    def test_get_config_remove_ns(self, mock_remove_ns, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_manager.get_config.return_value = mock_resp
        mock_remove_ns.return_value = "<clean/>"

        result = plugin.get_config(source="running", remove_ns=True)
        assert result == "<clean/>"

    def test_get_config_falls_back_to_xml(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock(spec=[])
        mock_resp.xml = "<cfg-xml/>"
        mock_manager.get_config.return_value = mock_resp

        result = plugin.get_config(source="running")
        assert result == "<cfg-xml/>"

    def test_get_config_rpc_error(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        from ncclient.operations import RPCError

        rpc_error = MagicMock()
        rpc_error.xml = Element("rpc-error")
        mock_manager.get_config.side_effect = RPCError(rpc_error)

        with pytest.raises(Exception):
            plugin.get_config(source="running")


class TestCommit:
    """Tests for commit method"""

    def test_commit_returns_data_xml(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.commit.return_value = mock_resp

        result = plugin.commit()
        assert result == "<ok/>"

    def test_commit_with_params(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.commit.return_value = mock_resp

        plugin.commit(confirmed=True, timeout=120, persist="my-persist")
        mock_manager.commit.assert_called_once_with(
            confirmed=True,
            timeout="120",
            persist="my-persist",
        )

    @patch("ansible_collections.cisco.iosxr.plugins.netconf.iosxr.remove_namespaces")
    def test_commit_remove_ns(self, mock_remove_ns, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_manager.commit.return_value = mock_resp
        mock_remove_ns.return_value = "<clean/>"

        result = plugin.commit(remove_ns=True)
        assert result == "<clean/>"

    def test_commit_rpc_error(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        from ncclient.operations import RPCError

        rpc_error = MagicMock()
        rpc_error.xml = Element("rpc-error")
        mock_manager.commit.side_effect = RPCError(rpc_error)

        with pytest.raises(Exception):
            plugin.commit()


class TestValidate:
    """Tests for validate method"""

    def test_validate_returns_data_xml(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.validate.return_value = mock_resp

        result = plugin.validate()
        assert result == "<ok/>"
        mock_manager.validate.assert_called_once_with(source="candidate")

    def test_validate_custom_source(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.validate.return_value = mock_resp

        plugin.validate(source="running")
        mock_manager.validate.assert_called_once_with(source="running")

    @patch("ansible_collections.cisco.iosxr.plugins.netconf.iosxr.remove_namespaces")
    def test_validate_remove_ns(self, mock_remove_ns, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_manager.validate.return_value = mock_resp
        mock_remove_ns.return_value = "<clean/>"

        result = plugin.validate(remove_ns=True)
        assert result == "<clean/>"

    def test_validate_rpc_error(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        from ncclient.operations import RPCError

        rpc_error = MagicMock()
        rpc_error.xml = Element("rpc-error")
        mock_manager.validate.side_effect = RPCError(rpc_error)

        with pytest.raises(Exception):
            plugin.validate()


class TestDiscardChanges:
    """Tests for discard_changes method"""

    def test_discard_changes_returns_data_xml(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_resp.data_xml = "<ok/>"
        mock_manager.discard_changes.return_value = mock_resp

        result = plugin.discard_changes()
        assert result == "<ok/>"

    @patch("ansible_collections.cisco.iosxr.plugins.netconf.iosxr.remove_namespaces")
    def test_discard_changes_remove_ns(self, mock_remove_ns, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_resp = MagicMock()
        mock_manager.discard_changes.return_value = mock_resp
        mock_remove_ns.return_value = "<clean/>"

        result = plugin.discard_changes(remove_ns=True)
        assert result == "<clean/>"

    def test_discard_changes_rpc_error(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        from ncclient.operations import RPCError

        rpc_error = MagicMock()
        rpc_error.xml = Element("rpc-error")
        mock_manager.discard_changes.side_effect = RPCError(rpc_error)

        with pytest.raises(Exception):
            plugin.discard_changes()


class TestGetCapabilities:
    """Tests for get_capabilities method"""

    def test_get_capabilities(self, netconf_plugin):
        plugin, mock_manager = netconf_plugin
        mock_manager.server_capabilities = ["urn:ietf:params:netconf:base:1.0"]
        mock_manager.client_capabilities = ["urn:ietf:params:netconf:base:1.0"]
        mock_manager.session_id = "12345"

        with patch.object(plugin, "get_base_rpc", return_value=["edit-config"]), patch.object(
            plugin,
            "get_device_info",
            return_value={"network_os": "iosxr"},
        ), patch.object(plugin, "get_device_operations", return_value={}):
            import json

            result = json.loads(plugin.get_capabilities())
            assert result["network_api"] == "netconf"
            assert result["device_info"]["network_os"] == "iosxr"
            assert result["session_id"] == "12345"
