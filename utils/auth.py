
from flask_httpauth import HTTPBasicAuth
from flask import jsonify
import os

auth = HTTPBasicAuth()

# reading env credentials, just for better security practices
USERNAME = os.getenv('BASIC_AUTH_USERNAME', 'admin')
PASSWORD = os.getenv('BASIC_AUTH_PASSWORD', 'secret')

USERS = {                       # hardcoded credentials
    # "admin": "secret"
    USERNAME: PASSWORD
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

