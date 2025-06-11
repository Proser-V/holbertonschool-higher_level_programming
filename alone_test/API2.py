#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/users", methods=["GET"])
def get_user():
    users = User.query.all()
    result = [{"id": user.id, "name": user.name} for user in users]
    return jsonify(result)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = User(name=data["name"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "name": new_user.name}), 201

if __name__ == "__main__":
    app.run(debug=True)