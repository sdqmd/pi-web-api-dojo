#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/piwebapi/points/P1DP100", methods=["GET"])
def point():
    return jsonify({
        "WebId": "P1DP100",
        "Name": "REACTOR.Level.PV",
        "Links": {"Attributes": "http://challenge/piwebapi/points/P1DP100/attributes"}
    })

@app.route("/piwebapi/points/P1DP100/attributes", methods=["GET"])
def attributes():
    flag = open("/flag").read().strip()
    return jsonify({
        "Items": [
            {"Name": "PointType", "Value": "Float64"},
            {"Name": "EngineeringUnits", "Value": "meters"},
            {"Name": "Zero", "Value": 0},
            {"Name": "Span", "Value": 100},
            {"Name": "Descriptor", "Value": "Reactor Tank Level"},
            {"Name": "flag", "Value": flag}
        ]
    })

@app.route("/")
def index():
    return jsonify({"hint": "Get attributes from /piwebapi/points/P1DP100/attributes"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
