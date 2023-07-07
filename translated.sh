ghz --insecure \
--proto=recommendation/proto/recommendation.proto \
--call=recommendation.Recommendation.GetRecommendations \
127.0.0.1:50051 \
-n 5000 \
-D recommendation/proto/test.json