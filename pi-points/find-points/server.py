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
        if parsed.path == "/piwebapi/search/query":
            q = parse_qs(parsed.query).get("q", [""])[0].lower()
            if "temperature" in q:
                self._json({"Items": [{"WebId": "P1DP001", "Name": "PLANT1.Temperature.Value", "PointType": "Float32"}], "TotalHits": 1})
            else:
                self._json({"Items": [], "TotalHits": 0})
        elif parsed.path == "/piwebapi/points/P1DP001":
            flag = open("/flag").read().strip()
            self._json({"WebId": "P1DP001", "Name": "PLANT1.Temperature.Value", "PointType": "Float32", "EngineeringUnits": "°C", "flag": flag})
        else:
            self._json({"hint": "Search for Temperature points at /piwebapi/search/query?q=name:Temperature*"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
