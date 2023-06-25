import json
import sys
from db import *
from mongoengine import *
import os

sys.path.insert(1, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from recommendation.server import RecommendationService

def main():
    f = open("config.json")
    config = json.load(f)

    session_ = initializeDatabase(config["RecommendMongoAddress"])
    port = config["RecommendPort"]
    ip = config["RecommendIP"]
    srv = RecommendationService(session_, port, ip, [])
    srv.serve()
    session_.close()

main()