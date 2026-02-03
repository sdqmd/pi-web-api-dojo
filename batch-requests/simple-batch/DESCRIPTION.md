# Simple Batch Request

Batch requests allow multiple API calls in a single HTTP request.

## Objective
Create a batch request that queries two points simultaneously.

## Request Format
POST a JSON object with named requests to `/piwebapi/batch`

## Example
```bash
curl -X POST http://challenge/piwebapi/batch \
  -H "Content-Type: application/json" \
  -d '{"point1": {"Method": "GET", "Resource": "/piwebapi/points/P1DP700"}, "point2": {"Method": "GET", "Resource": "/piwebapi/points/P1DP701"}}'
```
