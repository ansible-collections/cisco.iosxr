# (c) 2019 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
---
author: Ansible Networking Team
grpc : iosxr
short_description: gRPC Plugin for IOS XR devices
description:
  - This gRPC plugin provides methods to connect and talk to Cisco IOS XR
    devices over gRPC protocol.
version_added: ""
"""
import os

from imp import load_source

from ansible_collections.ansible.netcommon.plugins.sub_plugins.grpc.base import (
    GrpcBase, ensure_connect
)
import json
import os

from imp import load_source

from ansible_collections.ansible.netcommon.plugins.sub_plugins.grpc.base import (
    GrpcBase,
    ensure_connect,
)


class Grpc(GrpcBase):
    def __init__(self, connection):
        super(Grpc, self).__init__(connection)
        self._ems_grpc_pb2 = load_source(
            "ems_grpc_pb2",
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "pb/ems_grpc_pb2.py",
            ),
        )

    def get_config(self, section=None):
        stub = self._ems_grpc_pb2.beta_create_gRPCConfigOper_stub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.ConfigGetArgs(yangpathjson=section)
        responses = stub.GetConfig(
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
        stub = self._ems_grpc_pb2.beta_create_gRPCConfigOper_stub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.GetOperArgs(yangpathjson=section)
        responses = stub.GetOper(
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
        stub = self._ems_grpc_pb2.beta_create_gRPCConfigOper_stub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.ConfigArgs(yangjson=path)
        response = stub.MergeConfig(
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
        stub = self._ems_grpc_pb2.beta_create_gRPCConfigOper_stub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.ConfigArgs(yangjson=path)
        response = stub.ReplaceConfig(
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
        stub = self._ems_grpc_pb2.beta_create_gRPCConfigOper_stub(
            self._connection._channel,
        )
        message = self._ems_grpc_pb2.ConfigArgs(yangjson=path)
        response = stub.DeleteConfig(
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
        stub = self._ems_grpc_pb2.beta_create_gRPCExec_stub(
            self._connection._channel,
        )

        message = self._ems_grpc_pb2.ShowCmdArgs(cli=command)
        if display == "text":
            responses = stub.ShowCmdTextOutput(
                message,
                self._connection._timeout,
                metadata=self._connection._login_credentials,
            )
            for response in responses:
                output["response"] += response.output
                output["error"] += response.errors
        else:
            responses = stub.ShowCmdJSONOutput(
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
