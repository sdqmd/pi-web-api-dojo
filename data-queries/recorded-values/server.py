#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/piwebapi/streams/P1DP400/recorded", methods=["GET"])
def recorded():
    start = request.args.get("startTime", "")
    end = request.args.get("endTime", "")
    if start and end:
        flag = open("/flag").read().strip()
        return jsonify({
            "Items": [
                {"Timestamp": "2026-02-03T07:00:00Z", "Value": 20.1},
                {"Timestamp": "2026-02-03T07:15:00Z", "Value": 21.5},
                {"Timestamp": "2026-02-03T07:30:00Z", "Value": 22.3},
                {"Timestamp": "2026-02-03T07:45:00Z", "Value": 23.8},
                {"Timestamp": "2026-02-03T08:00:00Z", "Value": 24.2}
            ],
            "flag": flag
        })
    return jsonify({"error": "Specify startTime and endTime parameters"}), 400

@app.route("/")
def index():
    return jsonify({"hint": "Query /piwebapi/streams/P1DP400/recorded with time range"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
