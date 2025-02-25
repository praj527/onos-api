# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/perf/perf.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterable, AsyncIterator, Dict, Iterable, Union

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class Data(betterproto.Message):
    length: int = betterproto.uint32_field(1)
    data: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class PingRequest(betterproto.Message):
    payload: "Data" = betterproto.message_field(1)
    timestamp: int = betterproto.uint64_field(2)
    repeat_count: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class PingResponse(betterproto.Message):
    payload: "Data" = betterproto.message_field(1)
    timestamp: int = betterproto.uint64_field(2)


class PerfServiceStub(betterproto.ServiceStub):
    async def ping(
        self, *, payload: "Data" = None, timestamp: int = 0, repeat_count: int = 0
    ) -> "PingResponse":

        request = PingRequest()
        if payload is not None:
            request.payload = payload
        request.timestamp = timestamp
        request.repeat_count = repeat_count

        return await self._unary_unary(
            "/onos.perf.PerfService/Ping", request, PingResponse
        )

    async def ping_stream(
        self,
        request_iterator: Union[AsyncIterable["PingRequest"], Iterable["PingRequest"]],
    ) -> AsyncIterator["PingResponse"]:

        async for response in self._stream_stream(
            "/onos.perf.PerfService/PingStream",
            request_iterator,
            PingRequest,
            PingResponse,
        ):
            yield response


class PerfServiceBase(ServiceBase):
    async def ping(
        self, payload: "Data", timestamp: int, repeat_count: int
    ) -> "PingResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def ping_stream(
        self, request_iterator: AsyncIterator["PingRequest"]
    ) -> AsyncIterator["PingResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_ping(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "payload": request.payload,
            "timestamp": request.timestamp,
            "repeat_count": request.repeat_count,
        }

        response = await self.ping(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_ping_stream(self, stream: grpclib.server.Stream) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        await self._call_rpc_handler_server_stream(
            self.ping_stream,
            stream,
            request_kwargs,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/onos.perf.PerfService/Ping": grpclib.const.Handler(
                self.__rpc_ping,
                grpclib.const.Cardinality.UNARY_UNARY,
                PingRequest,
                PingResponse,
            ),
            "/onos.perf.PerfService/PingStream": grpclib.const.Handler(
                self.__rpc_ping_stream,
                grpclib.const.Cardinality.STREAM_STREAM,
                PingRequest,
                PingResponse,
            ),
        }
