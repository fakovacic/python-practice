from flask import Flask, request, jsonify, Response, json
from math import ceil

app = Flask(__name__)
app.config["DEBUG"] = True


endpoints = {
    "up": "/up"
    }
 
@app.route('/', methods=["GET", "PUT", "POST", "DELETE"])
def home():

    if request.method == "GET":
        return  Response(json.dumps(endpoints), status=200, mimetype="application/json")
    else:
        return Response(json.dumps({"error": "HTTP request not allowed"}), status=405, mimetype='application/json')

@app.route('/up', methods=["GET", "PUT", "POST", "DELETE"])
def up():
    if request.method == "GET":
        if "number" in request.args:
            try:
                number = float(request.args["number"])
            except ValueError:
                return Response(json.dumps({"error": "you have not entered a number"}), status=400, mimetype="application/json") 
        else:
            return Response(json.dumps({"error": "no argument given"}), status=404, mimetype="application/json")

        up = ceil(number)

        result = {
            "number": request.args["number"],
            "up": up
        }
        return Response(json.dumps(result), status=200, mimetype="application/json")
    else:
        return Response(json.dumps({"error": "HTTP request not allowed"}), status=405, mimetype='application/json')

app.run(host="localhost", port=8080)