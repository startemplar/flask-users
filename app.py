import os
from flask import Flask, session, jsonify, url_for, redirect, render_template, request, abort, flash
import requests
import random

app = Flask(__name__)

users_api_base = os.getenv('users_api', "http://127.0.0.1:3000")

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/user')
def GetUsers():
    resp = requests.get(users_api_base + "/api/users/")
    return jsonify(results=resp.content.decode("utf-8"))

@app.route('/user/create')
def CreateUser():
    id = random.randrange(1000)
    user = {"id": id, "name": "user"+str(id)}
    resp = requests.post(users_api_base + "/api/users/", json=user)
    return jsonify(results=resp.content.decode("utf-8"))

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))