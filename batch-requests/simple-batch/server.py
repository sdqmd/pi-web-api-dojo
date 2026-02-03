#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/piwebapi/batch", methods=["POST"])
def batch():
    data = request.get_json() or {}
    if len(data) >= 2:
        flag = open("/flag").read().strip()
        return jsonify({
            "point1": {"Status": 200, "Content": {"WebId": "P1DP700", "Name": "TANK1.Level"}},
            "point2": {"Status": 200, "Content": {"WebId": "P1DP701", "Name": "TANK2.Level"}},
            "flag": flag
        })
    return jsonify({"error": "Batch must contain at least 2 requests"}), 400

@app.route("/")
def index():
    return jsonify({"hint": "POST batch request to /piwebapi/batch"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
