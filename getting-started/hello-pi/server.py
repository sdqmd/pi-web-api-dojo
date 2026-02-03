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
        if self.path == "/piwebapi/":
            flag = open("/flag").read().strip()
            self._json({
                "Links": {"Self": "http://challenge:80/piwebapi/", "DataServers": "http://challenge:80/piwebapi/dataservers"},
                "WebId": "P1DS1234567890", "Version": "2019 SP1", "flag": flag
            })
        else:
            self._json({"hint": "Try GET /piwebapi/"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
