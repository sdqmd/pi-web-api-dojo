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
        self._json({"hint": "POST batch request to /piwebapi/batch"})

    def do_POST(self):
        if self.path == "/piwebapi/batch":
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length)) if length else {}
            if len(data) >= 2:
                flag = open("/flag").read().strip()
                self._json({"point1": {"Status": 200, "Content": {"WebId": "P1DP700"}}, "point2": {"Status": 200, "Content": {"WebId": "P1DP701"}}, "flag": flag})
            else:
                self._json({"error": "Batch must contain at least 2 requests"}, 400)
        else:
            self._json({"error": "Not found"}, 404)

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
