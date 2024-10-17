#!/usr/bin/env python3
""" Develop a Simple API using Python with Flask
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify([user for user in users.values()])

@app.route('/users/<username>', methods=['GET'])
def get_user(username):

    user = users.get(username)

    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """function that add user"""
    new_user = request.get_json()
    username = new_user.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = new_user
    return jsonify({"message": "User added successfully",
                    "user": new_user}), 201


@app.route('/status')
def status():
    return "OK"


if __name__ == '__main__':
    app.run()
