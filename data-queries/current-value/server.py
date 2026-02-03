#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/piwebapi/streamsets/value", methods=["GET"])
def multi_value():
    web_ids = request.args.getlist("webId")
    if set(web_ids) == {"P1DP300", "P1DP301", "P1DP302"}:
        flag = open("/flag").read().strip()
        return jsonify({
            "Items": [
                {"WebId": "P1DP300", "Value": {"Timestamp": "2026-02-03T08:00:00Z", "Value": 25.3}},
                {"WebId": "P1DP301", "Value": {"Timestamp": "2026-02-03T08:00:00Z", "Value": 101.2}},
                {"WebId": "P1DP302", "Value": {"Timestamp": "2026-02-03T08:00:00Z", "Value": 50.0}}
            ],
            "flag": flag
        })
    return jsonify({"error": "Query all three points: P1DP300, P1DP301, P1DP302"}), 400

@app.route("/")
def index():
    return jsonify({"hint": "Query /piwebapi/streamsets/value with multiple webId params"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
