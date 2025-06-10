#!/usr/bin/python3
"""
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@app.route("/basic-protected")
@auth.login_required
def verify_password(username, pwd):
	if username in users and check_password_hash(users.get(username), pwd):
		return "Basic Auth: Access Granted"
	else:
		return jsonify({"error":"Unauthorized"}), 401


@app.route("/login", methods=["POST"])
@auth.login_required
def login():
	data = request.get_json()
	username = data.get["username"]
	pwd = data.get["password"]
	if username in users and check_password_hash(users.get(username), pwd):
		return jsonify(access_token="access_token")