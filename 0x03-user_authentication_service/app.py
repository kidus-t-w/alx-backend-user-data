#!/usr/bin/env python3
"""API Routes for Authentication Service"""
from flask import (Flask,
                   jsonify,
                   request,
                   abort,
                   redirect)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world() -> str:
    """ Base route"""
    msg = {"message": "Bienvenue"}
    return jsonify(msg)

@app.route('/users', methods=['POST'])
def register_user() -> str:
    """Registers a new user if it doesn't exist"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg)
