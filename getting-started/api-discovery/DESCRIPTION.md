# API Discovery

PI Web API uses a self-documenting structure. Navigate through the API to find the Data Server.

## Objective
1. Start at `/piwebapi/`
2. Follow the `DataServers` link
3. Find the data server named "PI-SERVER-01"

## Hints
- Each response contains links to related resources
- Data servers host the PI Points

```bash
curl http://challenge/piwebapi/dataservers
```
