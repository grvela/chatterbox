from flask import render_template, request, jsonify, json
from flask import redirect, flash, url_for
import requests
from web import app


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/requestBot', methods = ['POST'])
def requestBot():
    data = request.get_json()
    data = json.dumps(data)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post("http://localhost:5005/webhooks/rest/webhook", data= data, headers= headers)
    response = response.json()
    return jsonify(response)