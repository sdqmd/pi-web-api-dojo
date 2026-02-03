#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/piwebapi/streams/P1DP500/interpolated", methods=["GET"])
def interpolated():
    interval = request.args.get("interval", "")
    if interval:
        flag = open("/flag").read().strip()
        return jsonify({
            "Items": [
                {"Timestamp": "2026-02-03T07:00:00Z", "Value": 50.0},
                {"Timestamp": "2026-02-03T07:10:00Z", "Value": 51.2},
                {"Timestamp": "2026-02-03T07:20:00Z", "Value": 52.1},
                {"Timestamp": "2026-02-03T07:30:00Z", "Value": 51.8},
                {"Timestamp": "2026-02-03T07:40:00Z", "Value": 50.5},
                {"Timestamp": "2026-02-03T07:50:00Z", "Value": 49.9},
                {"Timestamp": "2026-02-03T08:00:00Z", "Value": 50.3}
            ],
            "flag": flag
        })
    return jsonify({"error": "Specify interval parameter"}), 400

@app.route("/")
def index():
    return jsonify({"hint": "Query with interval parameter for interpolated values"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
