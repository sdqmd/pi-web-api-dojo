# Current Value Query

The snapshot value is the most recent value stored for a PI Point.

## Objective
Get the snapshot (current) value for multiple points at once using the batch endpoint.

Query current values for points: P1DP300, P1DP301, P1DP302

## Example
```bash
curl "http://challenge/piwebapi/streamsets/value?webId=P1DP300&webId=P1DP301&webId=P1DP302"
```
