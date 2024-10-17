#!/usr/bin/env python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@ app.route('/')
def home():
    return jsonify ("Welcome to the Flask API!")


@ app.route('/data')
def data():
    return jsonify(list(users.keys()))


@ app.route('/status')
def status():
    return jsonify("OK"), 200


@ app.route('/users/<username>', methods=['GET'])
def get_user(username):

    user = users.get(username)
    
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@ app.route('/add_user', methods=['POST'])
def add_user():
    """function that add user"""
    new_user = request.get_json()
    username = new_user.get("username")
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == '__main__':
    app.run(debug=True, port=5000)
