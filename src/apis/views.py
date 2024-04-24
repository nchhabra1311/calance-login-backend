import logging
from flask import request, abort
from src.services import UserService

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
        username = data.get('username')
        password = data.get('password')
    except KeyError as e:
        abort(400, e.args)

    return UserService.login_user(username, password)

def register_user():
    """
        API to sign up a user to test it's login
    """
    data = request.json
    try:
        username = data.get('username')
        password = data.get('password')
        display_name = data.get('display_name')
        email = data.get('email')

    except KeyError as e:
        abort(400, e.args)

    return UserService.register_user(username, password, email, display_name)