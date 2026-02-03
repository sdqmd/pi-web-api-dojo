# Batch Dependencies

Chain requests using ParentIds to use results from previous requests.

## Objective
Create a batch where:
1. First request searches for a point
2. Second request uses the WebId from the first result

Use `ParentIds` to create the dependency.

## Example
```bash
curl -X POST http://challenge/piwebapi/batch \
  -H "Content-Type: application/json" \
  -d '{
    "search": {"Method": "GET", "Resource": "/piwebapi/search/query?q=name:FLOW*"},
    "getValue": {"Method": "GET", "Resource": "/piwebapi/streams/{0}/value", "ParentIds": ["search"], "Parameters": ["$.Items[0].WebId"]}
  }'
```
