#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request

app = Flask(__name__)

POINTS = [
    {"WebId": "P1DP001", "Name": "PLANT1.Temperature.Value", "PointType": "Float32"},
    {"WebId": "P1DP002", "Name": "PLANT1.Pressure.Value", "PointType": "Float32"},
    {"WebId": "P1DP003", "Name": "PLANT2.Temperature.Value", "PointType": "Float32"},
]

@app.route("/piwebapi/search/query", methods=["GET"])
def search():
    q = request.args.get("q", "").lower()
    if "temperature" in q:
        results = [p for p in POINTS if "temperature" in p["Name"].lower()]
        return jsonify({"Items": results, "TotalHits": len(results)})
    return jsonify({"Items": [], "TotalHits": 0})

@app.route("/piwebapi/points/P1DP001", methods=["GET"])
def point_detail():
    flag = open("/flag").read().strip()
    return jsonify({
        "WebId": "P1DP001",
        "Name": "PLANT1.Temperature.Value",
        "PointType": "Float32",
        "EngineeringUnits": "°C",
        "flag": flag
    })

@app.route("/")
def index():
    return jsonify({"hint": "Search for Temperature points at /piwebapi/search/query?q=name:Temperature*"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
