#!/usr/bin/python3
"""
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from flask_jwt_extended import get_jwt


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "une_clef_secrete_des_enfers"
auth = HTTPBasicAuth()
jwt = JWTManager(app)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, pwd):
    if username in users and check_password_hash(users.get(username), pwd):
        return username


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    pwd = data.get("password")
    user = users.get(username)

    if username in users and check_password_hash(user["password"], pwd):
        access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Unauthorized"}), 401


@app.route("/jwt-protected", endpoint="jwt_protected_endpoint")
@jwt_required
def jwt_protected():
    return "JWT Auth: Access Granted"


@jwt.unauthorized_loader
def unauthorized_callback(msg):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.expired_token_loader
def expired_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.invalid_token_loader
def invalid_callback(msg):
    return jsonify({"error": "Invalid token"}), 401


@app.route("/admin_only", endpoint="admin_only_endpoint")
@jwt_required
def isadmin():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)