#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def _json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        self._json({"hint": "POST 3 value queries in batch"})

    def do_POST(self):
        if self.path == "/piwebapi/batch":
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length)) if length else {}
            if len(data) >= 3:
                flag = open("/flag").read().strip()
                self._json({"v1": {"Status": 200, "Content": {"Value": 100.5}}, "v2": {"Status": 200, "Content": {"Value": 98.2}}, "v3": {"Status": 200, "Content": {"Value": 101.8}}, "flag": flag})
            else:
                self._json({"error": "Need at least 3 parallel requests"}, 400)
        else:
            self._json({"error": "Not found"}, 404)

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
