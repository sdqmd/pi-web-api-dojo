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
        if parsed.path == "/piwebapi/streams/P1DP600/summary":
            types = parse_qs(parsed.query).get("summaryType", [])
            if "Average" in types and "Minimum" in types and "Maximum" in types:
                flag = open("/flag").read().strip()
                self._json({"Items": [{"Type": "Average", "Value": {"Value": 45.6}}, {"Type": "Minimum", "Value": {"Value": 38.2}}, {"Type": "Maximum", "Value": {"Value": 52.8}}], "flag": flag})
            else:
                self._json({"error": "Request Average, Minimum, and Maximum summary types"}, 400)
        else:
            self._json({"hint": "Query with multiple summaryType params"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
