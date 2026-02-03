#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/piwebapi/batch", methods=["POST"])
def batch():
    data = request.get_json() or {}
    has_parent = any("ParentIds" in v for v in data.values() if isinstance(v, dict))
    if has_parent and len(data) >= 2:
        flag = open("/flag").read().strip()
        return jsonify({
            "search": {"Status": 200, "Content": {"Items": [{"WebId": "P1DPFLOW", "Name": "FLOW.Rate"}]}},
            "getValue": {"Status": 200, "Content": {"Value": 250.5, "UnitsAbbreviation": "m³/h"}},
            "flag": flag
        })
    return jsonify({"error": "Create a batch with ParentIds dependency"}), 400

@app.route("/")
def index():
    return jsonify({"hint": "Use ParentIds to chain requests"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
