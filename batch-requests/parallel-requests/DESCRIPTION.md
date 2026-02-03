# Parallel Batch Requests

Execute multiple independent requests in parallel for better performance.

## Objective
Create a batch with 3 parallel value queries using the ParentIds field.

Requests without ParentIds run in parallel.

## Example
```bash
curl -X POST http://challenge/piwebapi/batch \
  -H "Content-Type: application/json" \
  -d '{
    "v1": {"Method": "GET", "Resource": "/piwebapi/streams/P1DP800/value"},
    "v2": {"Method": "GET", "Resource": "/piwebapi/streams/P1DP801/value"},
    "v3": {"Method": "GET", "Resource": "/piwebapi/streams/P1DP802/value"}
  }'
```
