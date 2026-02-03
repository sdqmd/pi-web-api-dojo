# PI Web API Authentication

PI Web API supports various authentication methods. This challenge uses Basic Auth.

## Objective
Authenticate to the API using:
- Username: `piuser`
- Password: `pipass123`

Then access the protected endpoint `/piwebapi/system/status`

## Example
```bash
curl -u piuser:pipass123 http://challenge/piwebapi/system/status
```
