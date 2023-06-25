import grpc

from recommendation.proto.recommendation_pb2_grpc import RecommendationStub
from recommendation.proto.recommendation_pb2 import Request


channel = grpc.insecure_channel("localhost:50051")
client = RecommendationStub(channel)

request = Request(require="dist", lat=371, lon=-122.24199999999999)
print(client.GetRecommendations(request))

