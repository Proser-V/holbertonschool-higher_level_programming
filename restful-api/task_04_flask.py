#!/usr/bin/python3

from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def json_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users.keys():
        return jsonify(users.get(username))
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data

    return jsonify({"message": "User added successfully", "user": data}), 201


if __name__ == "__main__":
    app.run()
