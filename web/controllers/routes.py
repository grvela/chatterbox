from flask import render_template, request, make_response, jsonify, json
from flask import redirect, flash, url_for
import requests
from web import app


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        data = json.dumps({"sender": "Rasa", "message": "Queria pedir uma pizza"})
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        reponse = requests.post("http://localhost:5005/webhooks/rest/webhook", data= data, headers= headers)
        reponse = reponse.json()
        return make_response(jsonify(reponse), 200)