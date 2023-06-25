import sys, os, random

sys.path.insert(1, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from recommendation.proto.recommendation_pb2 import Request


def generate_requests():
    request_list=[]
    for _ in range(198):
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        request_list.append(Request(require="dis", lat=lat, lon=lon))
    request_list.append(Request(require="rate", lat=0, lon=0))
    request_list.append(Request(require="price", lat=0, lon=0))
    return request_list

