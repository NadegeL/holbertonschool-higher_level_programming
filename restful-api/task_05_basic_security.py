#!/usr/bin/env python3

import os
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv('.variables')

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

"""list of users with hashed passwords"""
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("adminpass"), "role": "admin"}
}


"""verify password"""
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(
        users[username]['password'], password):
        return username


"""route protected with basic auth"""
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return("Basic Auth: Access Granted")


"""route connected and generate token"""
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if not password:
        return jsonify({"error": "Password is required"}), 400
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={
            'username': username,
            'role': user['role']})
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid username or password"}), 401


"""route protected with jwt"""
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify({"JWT Auth: Access Granted"})


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
