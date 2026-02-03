# Interpolated Values

Get evenly-spaced interpolated values at a specific interval.

## Objective
Get interpolated values every 10 minutes for the last hour.

## Parameters
- startTime: *-1h
- endTime: *
- interval: 10m

## Example
```bash
curl "http://challenge/piwebapi/streams/P1DP500/interpolated?startTime=*-1h&endTime=*&interval=10m"
```
