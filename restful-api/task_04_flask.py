#!/usr/bin/python3
"""
Ceci est une API simple construite avec http.server et socketserver.
"""


from flask import Flask, jsonify, request
"""
Ceci est une API simple construite avec http.server et socketserver.
"""


app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def list_users():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json() or {}
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201

if __name__ == "__main__":
    app.run()
