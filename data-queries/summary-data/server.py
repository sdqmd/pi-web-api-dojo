#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/piwebapi/streams/P1DP600/summary", methods=["GET"])
def summary():
    types = request.args.getlist("summaryType")
    if "Average" in types and "Minimum" in types and "Maximum" in types:
        flag = open("/flag").read().strip()
        return jsonify({
            "Items": [
                {"Type": "Average", "Value": {"Timestamp": "2026-02-03T08:00:00Z", "Value": 45.6}},
                {"Type": "Minimum", "Value": {"Timestamp": "2026-02-02T14:32:00Z", "Value": 38.2}},
                {"Type": "Maximum", "Value": {"Timestamp": "2026-02-02T22:15:00Z", "Value": 52.8}}
            ],
            "flag": flag
        })
    return jsonify({"error": "Request Average, Minimum, and Maximum summary types"}), 400

@app.route("/")
def index():
    return jsonify({"hint": "Query /piwebapi/streams/P1DP600/summary with multiple summaryType params"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
