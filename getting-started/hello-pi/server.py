#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/piwebapi/", methods=["GET"])
def api_root():
    flag = open("/flag").read().strip()
    return jsonify({
        "Links": {
            "Self": "http://challenge/piwebapi/",
            "AssetServers": "http://challenge/piwebapi/assetservers",
            "DataServers": "http://challenge/piwebapi/dataservers",
            "Search": "http://challenge/piwebapi/search"
        },
        "WebId": "P1DS1234567890",
        "Version": "2019 SP1",
        "flag": flag
    })

@app.route("/")
def index():
    return jsonify({"hint": "Try GET /piwebapi/"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
