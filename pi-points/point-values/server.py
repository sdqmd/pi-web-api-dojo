#!/usr/bin/python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def _json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == "/piwebapi/streams/P1DP200/value":
            flag = open("/flag").read().strip()
            self._json({"Timestamp": "2026-02-03T08:00:00Z", "Value": 42.5, "UnitsAbbreviation": "°C", "Good": True, "flag": flag})
        else:
            self._json({"hint": "Read value from /piwebapi/streams/P1DP200/value"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
