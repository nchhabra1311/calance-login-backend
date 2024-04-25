import logging
from flask import request, abort, jsonify
from services import UserService

logger = logging.getLogger("default")
user_service = UserService()

def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"


def login():
    """
    TASKS: write the logic here to parse a json request
           and send the parsed parameters to the appropriate service.

           return a json response and an appropriate status code.
    """

    # Extract username and password from request
    data = request.json
    try:
        username = data['username']
        password = data['password']
    except KeyError as e:
        return jsonify({"error": f"{e.args[0]} is mandatory"}), 400

    return user_service.login_user(username, password)

def register_user():
    """
        API to sign up a user to test it's login
    """
    data = request.json
    try:
        username = data['username']
        password = data['password']
        display_name = data['display_name']
        email = data['email']

    except KeyError as e:
        return jsonify({"error": f"{e.args[0]} is mandatory"}), 400


    return user_service.register_user(username, password, email, display_name)