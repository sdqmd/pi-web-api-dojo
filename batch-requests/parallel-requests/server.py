#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/piwebapi/batch", methods=["POST"])
def batch():
    data = request.get_json() or {}
    if len(data) >= 3:
        flag = open("/flag").read().strip()
        return jsonify({
            "v1": {"Status": 200, "Content": {"Value": 100.5}},
            "v2": {"Status": 200, "Content": {"Value": 98.2}},
            "v3": {"Status": 200, "Content": {"Value": 101.8}},
            "flag": flag
        })
    return jsonify({"error": "Need at least 3 parallel requests"}), 400

@app.route("/")
def index():
    return jsonify({"hint": "POST 3 value queries in batch"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
