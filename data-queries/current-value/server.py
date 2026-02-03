#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class Handler(BaseHTTPRequestHandler):
    def _json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/piwebapi/streamsets/value":
            ids = parse_qs(parsed.query).get("webId", [])
            if set(ids) == {"P1DP300", "P1DP301", "P1DP302"}:
                flag = open("/flag").read().strip()
                self._json({"Items": [{"WebId": "P1DP300", "Value": {"Value": 25.3}}, {"WebId": "P1DP301", "Value": {"Value": 101.2}}, {"WebId": "P1DP302", "Value": {"Value": 50.0}}], "flag": flag})
            else:
                self._json({"error": "Query all three points: P1DP300, P1DP301, P1DP302"}, 400)
        else:
            self._json({"hint": "Query /piwebapi/streamsets/value with multiple webId params"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
