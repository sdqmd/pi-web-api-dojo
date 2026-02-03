#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request
import base64

app = Flask(__name__)

def check_auth():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Basic "):
        return False
    try:
        creds = base64.b64decode(auth[6:]).decode()
        return creds == "piuser:pipass123"
    except:
        return False

@app.route("/piwebapi/system/status", methods=["GET"])
def system_status():
    if not check_auth():
        return jsonify({"error": "Authentication required"}), 401
    flag = open("/flag").read().strip()
    return jsonify({
        "State": "Running",
        "ServerTime": "2026-02-03T08:00:00Z",
        "flag": flag
    })

@app.route("/")
def index():
    return jsonify({"hint": "Authenticate to /piwebapi/system/status"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
