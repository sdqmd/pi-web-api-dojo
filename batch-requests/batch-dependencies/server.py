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
        self._json({"hint": "Use ParentIds to chain requests"})

    def do_POST(self):
        if self.path == "/piwebapi/batch":
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length)) if length else {}
            has_parent = any("ParentIds" in v for v in data.values() if isinstance(v, dict))
            if has_parent and len(data) >= 2:
                flag = open("/flag").read().strip()
                self._json({"search": {"Status": 200, "Content": {"Items": [{"WebId": "P1DPFLOW"}]}}, "getValue": {"Status": 200, "Content": {"Value": 250.5}}, "flag": flag})
            else:
                self._json({"error": "Create a batch with ParentIds dependency"}, 400)
        else:
            self._json({"error": "Not found"}, 404)

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
