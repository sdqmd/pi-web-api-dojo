# Recorded Values

Retrieve historical recorded values for a PI Point within a time range.

## Objective
Get recorded values for the last hour from point P1DP400.

## Parameters
- startTime: *-1h (one hour ago)
- endTime: * (now)

## Example
```bash
curl "http://challenge/piwebapi/streams/P1DP400/recorded?startTime=*-1h&endTime=*"
```
