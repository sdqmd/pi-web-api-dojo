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
        if parsed.path == "/piwebapi/streams/P1DP400/recorded":
            qs = parse_qs(parsed.query)
            if qs.get("startTime") and qs.get("endTime"):
                flag = open("/flag").read().strip()
                self._json({"Items": [{"Timestamp": "2026-02-03T07:00:00Z", "Value": 20.1}, {"Timestamp": "2026-02-03T08:00:00Z", "Value": 24.2}], "flag": flag})
            else:
                self._json({"error": "Specify startTime and endTime parameters"}, 400)
        else:
            self._json({"hint": "Query /piwebapi/streams/P1DP400/recorded with time range"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
