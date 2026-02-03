#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/piwebapi/streams/P1DP200/value", methods=["GET"])
def current_value():
    flag = open("/flag").read().strip()
    return jsonify({
        "Timestamp": "2026-02-03T08:00:00Z",
        "Value": 42.5,
        "UnitsAbbreviation": "°C",
        "Good": True,
        "flag": flag
    })

@app.route("/")
def index():
    return jsonify({"hint": "Read value from /piwebapi/streams/P1DP200/value"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
