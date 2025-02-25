# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/e2t/admin/admin.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterable, AsyncIterator, Dict, Iterable, List, Optional, Union

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


class E2NodeConnectionType(betterproto.Enum):
    """E2NodeConnectionType specifies the type of an E2 connection"""

    UNKNOWN = 0
    G_NB = 1
    E_NB = 2
    ENG_MB = 3
    NGE_NB = 4


@dataclass(eq=False, repr=False)
class UploadRegisterServiceModelRequest(betterproto.Message):
    """
    UploadRegisterServiceModelRequest is for streaming a model plugin file to
    the server. There is a built in limit in gRPC of 4MB - plugin is usually
    around 20MB so break in to chunks of approx 1-2MB.
    """

    # so_file is the name being streamed.
    so_file: str = betterproto.string_field(1)
    # content is the bytes content.
    content: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class UploadRegisterServiceModelResponse(betterproto.Message):
    """
    UploadRegisterServiceModelResponse carries status of model plugin
    registration.
    """

    # name is name of the model plugin.
    name: str = betterproto.string_field(1)
    # version is the semantic version of the model plugin.
    version: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ListRegisteredServiceModelsResponse(betterproto.Message):
    """
    ListRegisteredServiceModelsResponse is general information about a service
    model plugin.
    """

    # name is the name given to the service model plugin - no spaces and title
    # case.
    name: str = betterproto.string_field(1)
    # version is the semantic version of the Plugin e.g. 1.0.0.
    version: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ListRegisteredServiceModelsRequest(betterproto.Message):
    """
    ListRegisteredServiceModelsRequest carries data for querying registered
    service model plugins.
    """

    # An optional filter on the name of the model plugins to list.
    model_name: str = betterproto.string_field(1)
    # An optional filter on the version of the model plugins to list
    model_version: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ListE2NodeConnectionsRequest(betterproto.Message):
    """
    ListE2NodeConnectionsRequest carries request for a list of E2 node SCTP
    connections.
    """

    pass


@dataclass(eq=False, repr=False)
class RanFunction(betterproto.Message):
    oid: str = betterproto.string_field(1)
    ran_function_id: str = betterproto.string_field(2)
    description: bytes = betterproto.bytes_field(3)


@dataclass(eq=False, repr=False)
class ListE2NodeConnectionsResponse(betterproto.Message):
    """
    ListE2NodeConnectionsResponse carries information about the SCTP connection
    to the remote E2 node.
    """

    id: str = betterproto.string_field(3)
    remote_ip: List[str] = betterproto.string_field(1)
    remote_port: int = betterproto.uint32_field(2)
    node_id: str = betterproto.string_field(7)
    plmn_id: str = betterproto.string_field(4)
    connection_type: "E2NodeConnectionType" = betterproto.enum_field(5)
    ran_functions: List["RanFunction"] = betterproto.message_field(6)
    age_ms: int = betterproto.int32_field(8)


@dataclass(eq=False, repr=False)
class DropE2NodeConnectionsRequest(betterproto.Message):
    """DropE2NodeConnectionsRequest carries drop connection request"""

    connections: List["ListE2NodeConnectionsResponse"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class DropE2NodeConnectionsResponse(betterproto.Message):
    """DropE2NodeConnectionsResponse carries drop connection response"""

    success: List[bool] = betterproto.bool_field(1)


class E2TAdminServiceStub(betterproto.ServiceStub):
    async def upload_register_service_model(
        self,
        request_iterator: Union[
            AsyncIterable["UploadRegisterServiceModelRequest"],
            Iterable["UploadRegisterServiceModelRequest"],
        ],
    ) -> "UploadRegisterServiceModelResponse":

        return await self._stream_unary(
            "/onos.e2t.admin.E2TAdminService/UploadRegisterServiceModel",
            request_iterator,
            UploadRegisterServiceModelRequest,
            UploadRegisterServiceModelResponse,
        )

    async def list_registered_service_models(
        self, *, model_name: str = "", model_version: str = ""
    ) -> AsyncIterator["ListRegisteredServiceModelsResponse"]:

        request = ListRegisteredServiceModelsRequest()
        request.model_name = model_name
        request.model_version = model_version

        async for response in self._unary_stream(
            "/onos.e2t.admin.E2TAdminService/ListRegisteredServiceModels",
            request,
            ListRegisteredServiceModelsResponse,
        ):
            yield response

    async def list_e2_node_connections(
        self,
    ) -> AsyncIterator["ListE2NodeConnectionsResponse"]:

        request = ListE2NodeConnectionsRequest()

        async for response in self._unary_stream(
            "/onos.e2t.admin.E2TAdminService/ListE2NodeConnections",
            request,
            ListE2NodeConnectionsResponse,
        ):
            yield response

    async def drop_e2_node_connections(
        self, *, connections: Optional[List["ListE2NodeConnectionsResponse"]] = None
    ) -> "DropE2NodeConnectionsResponse":
        connections = connections or []

        request = DropE2NodeConnectionsRequest()
        if connections is not None:
            request.connections = connections

        return await self._unary_unary(
            "/onos.e2t.admin.E2TAdminService/DropE2NodeConnections",
            request,
            DropE2NodeConnectionsResponse,
        )


class E2TAdminServiceBase(ServiceBase):
    async def upload_register_service_model(
        self, request_iterator: AsyncIterator["UploadRegisterServiceModelRequest"]
    ) -> "UploadRegisterServiceModelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_registered_service_models(
        self, model_name: str, model_version: str
    ) -> AsyncIterator["ListRegisteredServiceModelsResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_e2_node_connections(
        self,
    ) -> AsyncIterator["ListE2NodeConnectionsResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def drop_e2_node_connections(
        self, connections: Optional[List["ListE2NodeConnectionsResponse"]]
    ) -> "DropE2NodeConnectionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_upload_register_service_model(
        self, stream: grpclib.server.Stream
    ) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        response = await self.upload_register_service_model(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_list_registered_service_models(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "model_name": request.model_name,
            "model_version": request.model_version,
        }

        await self._call_rpc_handler_server_stream(
            self.list_registered_service_models,
            stream,
            request_kwargs,
        )

    async def __rpc_list_e2_node_connections(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        await self._call_rpc_handler_server_stream(
            self.list_e2_node_connections,
            stream,
            request_kwargs,
        )

    async def __rpc_drop_e2_node_connections(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "connections": request.connections,
        }

        response = await self.drop_e2_node_connections(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/onos.e2t.admin.E2TAdminService/UploadRegisterServiceModel": grpclib.const.Handler(
                self.__rpc_upload_register_service_model,
                grpclib.const.Cardinality.STREAM_UNARY,
                UploadRegisterServiceModelRequest,
                UploadRegisterServiceModelResponse,
            ),
            "/onos.e2t.admin.E2TAdminService/ListRegisteredServiceModels": grpclib.const.Handler(
                self.__rpc_list_registered_service_models,
                grpclib.const.Cardinality.UNARY_STREAM,
                ListRegisteredServiceModelsRequest,
                ListRegisteredServiceModelsResponse,
            ),
            "/onos.e2t.admin.E2TAdminService/ListE2NodeConnections": grpclib.const.Handler(
                self.__rpc_list_e2_node_connections,
                grpclib.const.Cardinality.UNARY_STREAM,
                ListE2NodeConnectionsRequest,
                ListE2NodeConnectionsResponse,
            ),
            "/onos.e2t.admin.E2TAdminService/DropE2NodeConnections": grpclib.const.Handler(
                self.__rpc_drop_e2_node_connections,
                grpclib.const.Cardinality.UNARY_UNARY,
                DropE2NodeConnectionsRequest,
                DropE2NodeConnectionsResponse,
            ),
        }
