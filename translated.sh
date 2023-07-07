#!/bin/bash

# Set variables for convenience
protoFile="/recommendation/proto/recommendation.proto"
callPath="/recommendation/proto/recommendation_pb2_grpc.RecommendationStub.GetRecommendations"
targetAddress="127.0.0.1:50051"
dataPayload='{"require": "dist","lat":37.7867, "lon": -122.4112}'

# Execute the ghz command
ghz --insecure \
    --proto $protoFile \
    --call $callPath \
    -d $dataPayload \
    $targetAddress
