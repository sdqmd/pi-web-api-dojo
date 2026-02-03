#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json, base64

class Handler(BaseHTTPRequestHandler):
    def _json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == "/piwebapi/system/status":
            auth = self.headers.get("Authorization", "")
            if auth.startswith("Basic "):
                try:
                    creds = base64.b64decode(auth[6:]).decode()
                    if creds == "piuser:pipass123":
                        flag = open("/flag").read().strip()
                        self._json({"State": "Running", "ServerTime": "2026-02-03T08:00:00Z", "flag": flag})
                        return
                except: pass
            self._json({"error": "Authentication required"}, 401)
        else:
            self._json({"hint": "Authenticate to /piwebapi/system/status"})

    def log_message(self, *args): pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 80), Handler).serve_forever()
