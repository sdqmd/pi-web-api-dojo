# Finding PI Points

PI Points are the core data containers in PI System. Learn to search for points.

## Objective
Search for PI Points with "Temperature" in the name using the search endpoint.

## Example
```bash
curl "http://challenge/piwebapi/search/query?q=name:Temperature*"
```

Find the point named "PLANT1.Temperature.Value" to get the flag.
