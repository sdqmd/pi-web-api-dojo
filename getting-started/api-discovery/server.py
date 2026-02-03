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
            self._json({"Links": {"Self": "http://challenge:80/piwebapi/", "DataServers": "http://challenge:80/piwebapi/dataservers"}})
        elif self.path == "/piwebapi/dataservers":
            self._json({"Items": [{"WebId": "F1DS1234", "Name": "PI-SERVER-01", "Links": {"Self": "http://challenge:80/piwebapi/dataservers/F1DS1234"}}]})
        elif self.path == "/piwebapi/dataservers/F1DS1234":
            flag = open("/flag").read().strip()
            self._json({"WebId": "F1DS1234", "Name": "PI-SERVER-01", "ServerVersion": "3.4.440.21", "IsConnected": True, "flag": flag})
        else:
            self._json({"hint": "Start at /piwebapi/ and explore"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
