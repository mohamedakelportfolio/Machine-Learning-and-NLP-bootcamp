curl -X POST http://localhost:80/predict \
    -d @./with_batch/census-examples/batch1.json \
    -H "Content-Type: application/json"
