import grpc
import sys, os

sys.path.insert(1, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from recommendation.proto.recommendation_pb2_grpc import RecommendationStub
from recommendation.proto.recommendation_pb2 import Request
from index import *


channel_1 = grpc.insecure_channel("localhost:50051")
client_1 = RecommendationStub(channel_1)

channel_2 = grpc.insecure_channel("localhost:8090")
client_2 = RecommendationStub(channel_2)

request_list  = generate_requests()

for request in request_list:
    t1 = sorted(client_1.GetRecommendations(request).HotelIds)
    t2 = sorted(client_2.GetRecommendations(request).HotelIds)
    if (t1!=t2):
        print("Failure")
        break
else:
    print("All tests Passed")


