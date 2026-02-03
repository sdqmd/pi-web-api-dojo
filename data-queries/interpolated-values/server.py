#!/usr/bin/env python3
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
        if parsed.path == "/piwebapi/streams/P1DP500/interpolated":
            if parse_qs(parsed.query).get("interval"):
                flag = open("/flag").read().strip()
                self._json({"Items": [{"Timestamp": "2026-02-03T07:00:00Z", "Value": 50.0}, {"Timestamp": "2026-02-03T08:00:00Z", "Value": 50.3}], "flag": flag})
            else:
                self._json({"error": "Specify interval parameter"}, 400)
        else:
            self._json({"hint": "Query with interval parameter for interpolated values"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
