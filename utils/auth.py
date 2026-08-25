
from flask_httpauth import HTTPBasicAuth
from flask import jsonify

auth = HTTPBasicAuth()

USERS = {                       # hardcoded credentials
    "admin": "secret"
}

@auth.verify_password
def verify_password(username, password):      # verification

    if username in USERS and USERS[username] == password:
        return username

    return None

@auth.error_handler
def unauthorized():       # aunauthorized error handler

    return jsonify({
        "error": "Unauthorized. Please provide valid details"
    }), 401

