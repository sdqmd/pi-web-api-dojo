#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/piwebapi/", methods=["GET"])
def api_root():
    return jsonify({
        "Links": {
            "Self": "http://challenge/piwebapi/",
            "DataServers": "http://challenge/piwebapi/dataservers"
        }
    })

@app.route("/piwebapi/dataservers", methods=["GET"])
def dataservers():
    return jsonify({
        "Items": [
            {
                "WebId": "F1DS1234",
                "Name": "PI-SERVER-01",
                "Links": {"Self": "http://challenge/piwebapi/dataservers/F1DS1234"}
            }
        ]
    })

@app.route("/piwebapi/dataservers/F1DS1234", methods=["GET"])
def dataserver_detail():
    flag = open("/flag").read().strip()
    return jsonify({
        "WebId": "F1DS1234",
        "Name": "PI-SERVER-01",
        "ServerVersion": "3.4.440.21",
        "IsConnected": True,
        "flag": flag
    })

@app.route("/")
def index():
    return jsonify({"hint": "Start at /piwebapi/ and explore"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
