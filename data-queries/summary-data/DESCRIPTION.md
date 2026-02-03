# Summary Data

Calculate summary statistics over a time range.

## Objective
Get the average, minimum, and maximum values for the last day.

## Parameters
- startTime: *-1d
- endTime: *
- summaryType: Average,Minimum,Maximum

## Example
```bash
curl "http://challenge/piwebapi/streams/P1DP600/summary?startTime=*-1d&endTime=*&summaryType=Average&summaryType=Minimum&summaryType=Maximum"
```
