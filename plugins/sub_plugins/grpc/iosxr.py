# (c) 2019 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
---
author: Ansible Networking Team
name: grpc
short_description: gRPC plugin for IOS-XR devices
description:
  - This gRPC plugin provides methods to connect and talk to Cisco IOS XR
    devices over gRPC protocol.
version_added: "3.3.0"
"""

import json

from ansible.errors import AnsibleError
from ansible_collections.ansible.netcommon.plugins.sub_plugins.grpc.base import (
    GrpcBase,
    ensure_connect,
)

from .pb import ems_grpc_pb2, ems_grpc_pb2_grpc


class Grpc(GrpcBase):
    def __init__(self, connection):
        super(Grpc, self).__init__(connection)
        self._ems_grpc_pb2 = ems_grpc_pb2
        self._ems_grpc_pb2_grpc = ems_grpc_pb2_grpc
        if not hasattr(self._ems_grpc_pb2, "DESCRIPTOR"):
            raise AnsibleError(
                "protobuf>=3.20.0 is required to use the IOS XR gRPC connection",
            )
        if not hasattr(self._ems_grpc_pb2_grpc, "GrpcConfigOperStub"):
            raise AnsibleError(
                "grpcio>=1.48.4 is required to use the IOS XR gRPC connection",
            )

    def get_config(self, section=None):
        stub = self._ems_grpc_pb2_grpc.GrpcConfigOperStub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.ConfigGetArgs(yangpathjson=section)
        responses = stub.get_config(
            message,
            self._connection._timeout,
            metadata=self._connection._login_credentials,
        )
        output = {"response": "", "error": ""}
        for response in responses:
            output["response"] += response.yangjson
            output["error"] += response.errors
        return output

    def get(self, section=None):
        stub = self._ems_grpc_pb2_grpc.GrpcConfigOperStub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.GetOperArgs(yangpathjson=section)
        responses = stub.get_oper(
            message,
            self._connection._timeout,
            metadata=self._connection._login_credentials,
        )
        output = {"response": "", "error": ""}
        for response in responses:
            output["response"] += response.yangjson
            output["error"] += response.errors
        return output

    @ensure_connect
    def merge_config(self, path):
        """Merge grpc call equivalent  of PATCH RESTconf call
        :param data: JSON
        :type data: str
        :return: Return the response object
        :rtype: Response object
        """
        path = json.dumps(path)
        stub = self._ems_grpc_pb2_grpc.GrpcConfigOperStub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.ConfigArgs(yangjson=path)
        response = stub.merge_config(
            message,
            self._connection._timeout,
            metadata=self._connection._login_credentials,
        )
        if response:
            return response.errors
        else:
            return None

    @ensure_connect
    def replace_config(self, path):
        """Replace grpc call equivalent  of PATCH RESTconf call
        :param data: JSON
        :type data: str
        :return: Return the response object
        :rtype: Response object
        """
        path = json.dumps(path)
        stub = self._ems_grpc_pb2_grpc.GrpcConfigOperStub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.ConfigArgs(yangjson=path)
        response = stub.replace_config(
            message,
            self._connection._timeout,
            metadata=self._connection._login_credentials,
        )
        if response:
            return response.errors
        else:
            return None

    @ensure_connect
    def delete_config(self, path):
        """Delete grpc call equivalent  of PATCH RESTconf call
        :param data: JSON
        :type data: str
        :return: Return the response object
        :rtype: Response object
        """
        path = json.dumps(path)
        stub = self._ems_grpc_pb2_grpc.GrpcConfigOperStub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.ConfigArgs(yangjson=path)
        response = stub.delete_config(
            message,
            self._connection._timeout,
            metadata=self._connection._login_credentials,
        )
        if response:
            return response.errors
        else:
            return None

    @ensure_connect
    def run_cli(self, command=None, display=None):
        if command is None:
            raise ValueError("command value must be provided")

        output = {"response": "", "error": ""}
        stub = self._ems_grpc_pb2_grpc.GrpcExecStub(
            self._connection._channel,
        )

        message = self._ems_grpc_pb2.ShowCmdArgs(cli=command)
        if display == "text":
            responses = stub.show_cmd_text_output(
                message,
                self._connection._timeout,
                metadata=self._connection._login_credentials,
            )
            for response in responses:
                output["response"] += response.output
                output["error"] += response.errors
        else:
            responses = stub.show_cmd_json_output(
                message,
                self._connection._timeout,
                metadata=self._connection._login_credentials,
            )
            for response in responses:
                output["response"] += response.jsonoutput
                output["error"] += response.errors
        return output

    @property
    def server_capabilities(self):
        capability = dict()
        capability["display"] = ["json", "text"]
        capability["data_type"] = ["config", "oper"]
        capability["supports_commit"] = True
        capability["supports_cli_command"] = True
        return capability

    @ensure_connect
    def get_capabilities(self):
        result = dict()
        result["rpc"] = self.__rpc__ + ["commit", "discard_changes"]
        result["network_api"] = "ansible.netcommon.grpc"
        result["server_capabilities"] = self.server_capabilities
        return result
