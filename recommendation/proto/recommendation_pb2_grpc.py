# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import recommendation.proto.recommendation_pb2 as recommendation__pb2


class RecommendationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetRecommendations = channel.unary_unary(
                '/recommendation.Recommendation/GetRecommendations',
                request_serializer=recommendation__pb2.Request.SerializeToString,
                response_deserializer=recommendation__pb2.Result.FromString,
                )


class RecommendationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetRecommendations(self, request, context):
        """GetRecommendations returns recommended hotels for a given requirement
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetRecommendations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecommendations,
                    request_deserializer=recommendation__pb2.Request.FromString,
                    response_serializer=recommendation__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'recommendation.Recommendation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recommendation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetRecommendations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recommendation.Recommendation/GetRecommendations',
            recommendation__pb2.Request.SerializeToString,
            recommendation__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
