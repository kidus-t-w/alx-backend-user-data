#!/usr/bin/env python3
"""
Flask App
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def home():
    """
    Home route
    """
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = AUTH.register_user(email, password)
    if user:
        return jsonify({"email": email, "message":"user created"})
    return jsonify({"message": "email already registered"}), 400
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
