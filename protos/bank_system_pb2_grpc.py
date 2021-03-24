# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import bank_system_pb2 as protos_dot_bank__system__pb2


class BranchServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MsgDelivery = channel.unary_unary(
                '/BranchService/MsgDelivery',
                request_serializer=protos_dot_bank__system__pb2.Events.SerializeToString,
                response_deserializer=protos_dot_bank__system__pb2.Events.FromString,
                )
        self.SyncBranch = channel.unary_unary(
                '/BranchService/SyncBranch',
                request_serializer=protos_dot_bank__system__pb2.Events.SerializeToString,
                response_deserializer=protos_dot_bank__system__pb2.Events.FromString,
                )
        self.getFinalBalance = channel.unary_unary(
                '/BranchService/getFinalBalance',
                request_serializer=protos_dot_bank__system__pb2.Event.SerializeToString,
                response_deserializer=protos_dot_bank__system__pb2.Event.FromString,
                )


class BranchServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MsgDelivery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SyncBranch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getFinalBalance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BranchServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MsgDelivery': grpc.unary_unary_rpc_method_handler(
                    servicer.MsgDelivery,
                    request_deserializer=protos_dot_bank__system__pb2.Events.FromString,
                    response_serializer=protos_dot_bank__system__pb2.Events.SerializeToString,
            ),
            'SyncBranch': grpc.unary_unary_rpc_method_handler(
                    servicer.SyncBranch,
                    request_deserializer=protos_dot_bank__system__pb2.Events.FromString,
                    response_serializer=protos_dot_bank__system__pb2.Events.SerializeToString,
            ),
            'getFinalBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.getFinalBalance,
                    request_deserializer=protos_dot_bank__system__pb2.Event.FromString,
                    response_serializer=protos_dot_bank__system__pb2.Event.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'BranchService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BranchService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MsgDelivery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BranchService/MsgDelivery',
            protos_dot_bank__system__pb2.Events.SerializeToString,
            protos_dot_bank__system__pb2.Events.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SyncBranch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BranchService/SyncBranch',
            protos_dot_bank__system__pb2.Events.SerializeToString,
            protos_dot_bank__system__pb2.Events.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getFinalBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/BranchService/getFinalBalance',
            protos_dot_bank__system__pb2.Event.SerializeToString,
            protos_dot_bank__system__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
