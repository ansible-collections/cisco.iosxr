from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest


pytest.importorskip("grpc")
pytest.importorskip("google.protobuf")

from grpc import experimental as grpc_experimental

from ansible_collections.cisco.iosxr.plugins.sub_plugins.grpc import iosxr
from ansible_collections.cisco.iosxr.plugins.sub_plugins.grpc.pb import ems_grpc_pb2_grpc


@pytest.fixture
def grpc_plugin(monkeypatch):
    connection = MagicMock()
    connection._channel = MagicMock()
    connection._timeout = 30
    connection._login_credentials = (("username", "admin"),)
    connection._connected = True
    plugin = iosxr.Grpc(connection)

    config_stub = MagicMock()
    exec_stub = MagicMock()
    monkeypatch.setattr(
        ems_grpc_pb2_grpc,
        "GrpcConfigOperStub",
        MagicMock(return_value=config_stub),
    )
    monkeypatch.setattr(
        ems_grpc_pb2_grpc,
        "GrpcExecStub",
        MagicMock(return_value=exec_stub),
    )
    return plugin, config_stub, exec_stub


def test_generated_stubs_expose_snake_case_python_methods():
    channel = MagicMock()
    config_stub = ems_grpc_pb2_grpc.GrpcConfigOperStub(channel)
    exec_stub = ems_grpc_pb2_grpc.GrpcExecStub(channel)

    assert hasattr(config_stub, "get_config")
    assert hasattr(config_stub, "get_oper")
    assert hasattr(config_stub, "config_discard_changes")
    assert not hasattr(config_stub, "GetOper")
    assert hasattr(exec_stub, "show_cmd_text_output")
    assert hasattr(exec_stub, "show_cmd_json_output")


def test_get_config_and_get_use_snake_case_stub_methods(grpc_plugin):
    plugin = grpc_plugin[0]
    config_stub = grpc_plugin[1]
    config_stub.get_config.return_value = [
        SimpleNamespace(yangjson="config", errors=""),
    ]
    config_stub.get_oper.return_value = [
        SimpleNamespace(yangjson="oper", errors="warning"),
    ]

    assert plugin.get_config("/interfaces") == {"response": "config", "error": ""}
    assert plugin.get("/interfaces-state") == {"response": "oper", "error": "warning"}
    assert config_stub.get_config.call_args.args[0].yangpathjson == "/interfaces"
    assert config_stub.get_oper.call_args.args[0].yangpathjson == "/interfaces-state"


@pytest.mark.parametrize(
    ("method_name", "plugin_method"),
    [
        ("merge_config", "merge_config"),
        ("replace_config", "replace_config"),
        ("delete_config", "delete_config"),
    ],
)
def test_config_updates_use_snake_case_stub_methods(
    grpc_plugin,
    method_name,
    plugin_method,
):
    plugin = grpc_plugin[0]
    config_stub = grpc_plugin[1]
    getattr(config_stub, method_name).return_value = SimpleNamespace(errors="")

    assert getattr(plugin, plugin_method)({"interface": "Loopback0"}) == ""
    getattr(config_stub, method_name).assert_called_once()


def test_run_cli_uses_snake_case_exec_methods(grpc_plugin):
    plugin = grpc_plugin[0]
    exec_stub = grpc_plugin[2]
    exec_stub.show_cmd_text_output.return_value = [
        SimpleNamespace(output="IOS XR", errors=""),
    ]
    exec_stub.show_cmd_json_output.return_value = [
        SimpleNamespace(jsonoutput='{"hostname": "xr"}', errors=""),
    ]

    assert plugin.run_cli("show version", "text") == {"response": "IOS XR", "error": ""}
    assert plugin.run_cli("show version", "json") == {
        "response": '{"hostname": "xr"}',
        "error": "",
    }


def test_run_cli_requires_a_command(grpc_plugin):
    plugin = grpc_plugin[0]

    with pytest.raises(ValueError, match="command value must be provided"):
        plugin.run_cli()


@pytest.mark.parametrize("method_name", ["merge_config", "replace_config", "delete_config"])
def test_config_updates_return_none_without_a_grpc_response(grpc_plugin, method_name):
    plugin = grpc_plugin[0]
    config_stub = grpc_plugin[1]
    getattr(config_stub, method_name).return_value = None

    assert getattr(plugin, method_name)({"interface": "Loopback0"}) is None


def test_get_capabilities_reports_grpc_features(grpc_plugin):
    plugin = grpc_plugin[0]

    result = plugin.get_capabilities()

    assert result["network_api"] == "ansible.netcommon.grpc"
    assert result["server_capabilities"]["supports_cli_command"] is True


def test_servicer_request_parameters_remain_compatible_with_grpc_handlers():
    context = MagicMock()
    servicer = ems_grpc_pb2_grpc.GrpcConfigOperServicer()

    with pytest.raises(NotImplementedError):
        servicer.get_oper(MagicMock(), context)

    context.set_code.assert_called_once()
    context.set_details.assert_called_once_with("Method not implemented!")


@pytest.mark.parametrize(
    "method_name",
    [
        "get_config",
        "merge_config",
        "delete_config",
        "replace_config",
        "cli_config",
        "commit_replace",
        "commit_config",
        "config_discard_changes",
        "get_oper",
        "create_subs",
    ],
)
def test_config_servicer_methods_keep_the_grpc_handler_signature(method_name):
    servicer = ems_grpc_pb2_grpc.GrpcConfigOperServicer()

    with pytest.raises(NotImplementedError):
        getattr(servicer, method_name)(MagicMock(), MagicMock())


@pytest.mark.parametrize(
    "method_name",
    ["show_cmd_text_output", "show_cmd_json_output"],
)
def test_exec_servicer_methods_keep_the_grpc_handler_signature(method_name):
    servicer = ems_grpc_pb2_grpc.GrpcExecServicer()

    with pytest.raises(NotImplementedError):
        getattr(servicer, method_name)(MagicMock(), MagicMock())


def test_generated_registration_helpers_keep_wire_rpc_names():
    server = MagicMock()

    ems_grpc_pb2_grpc.add_grpc_config_oper_servicer_to_server(
        ems_grpc_pb2_grpc.GrpcConfigOperServicer(),
        server,
    )
    ems_grpc_pb2_grpc.add_grpc_exec_servicer_to_server(
        ems_grpc_pb2_grpc.GrpcExecServicer(),
        server,
    )

    assert server.add_generic_rpc_handlers.call_count == 2


@pytest.mark.parametrize(
    ("method_name", "rpc_type"),
    [
        ("get_config", "unary_stream"),
        ("merge_config", "unary_unary"),
        ("delete_config", "unary_unary"),
        ("replace_config", "unary_unary"),
        ("cli_config", "unary_unary"),
        ("commit_replace", "unary_unary"),
        ("commit_config", "unary_unary"),
        ("config_discard_changes", "unary_unary"),
        ("get_oper", "unary_stream"),
        ("create_subs", "unary_stream"),
        ("show_cmd_text_output", "unary_stream"),
        ("show_cmd_json_output", "unary_stream"),
    ],
)
def test_experimental_clients_use_snake_case_methods(monkeypatch, method_name, rpc_type):
    unary_stream = MagicMock(return_value="stream")
    unary_unary = MagicMock(return_value="unary")
    monkeypatch.setattr(grpc_experimental, "unary_stream", unary_stream)
    monkeypatch.setattr(grpc_experimental, "unary_unary", unary_unary)

    client_class = (
        ems_grpc_pb2_grpc.GrpcConfigOper
        if hasattr(ems_grpc_pb2_grpc.GrpcConfigOper, method_name)
        else ems_grpc_pb2_grpc.GrpcExec
    )

    assert getattr(client_class, method_name)(MagicMock(), "localhost:57400") in {
        "stream",
        "unary",
    }
    assert (unary_stream if rpc_type == "unary_stream" else unary_unary).called
