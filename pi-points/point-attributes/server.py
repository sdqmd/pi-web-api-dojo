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
        if self.path == "/piwebapi/points/P1DP100":
            self._json({"WebId": "P1DP100", "Name": "REACTOR.Level.PV", "Links": {"Attributes": "http://challenge:80/piwebapi/points/P1DP100/attributes"}})
        elif self.path == "/piwebapi/points/P1DP100/attributes":
            flag = open("/flag").read().strip()
            self._json({"Items": [{"Name": "PointType", "Value": "Float64"}, {"Name": "EngineeringUnits", "Value": "meters"}, {"Name": "flag", "Value": flag}]})
        else:
            self._json({"hint": "Get attributes from /piwebapi/points/P1DP100/attributes"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
