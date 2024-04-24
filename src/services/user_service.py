from src.models import User
import bcrypt
from flask import jsonify, abort

class UserService(object):
    """
    service function for user related business logic
    """

    def login_user(self, username, password):
        """
        TASKS: write the logic here for user login
               authenticate user credentials as per your
               schema and return the identifier user.

               raise appropriate errors wherever necessary
        """
        user = User.objects(username=username).first()

        # Check if user exists and validate password
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            return jsonify({"user": user, "status": 'LOGGED_IN'})
        else:
            raise abort(400, "Incorrect username or password")
        

    def register_user(self, username, password, email, name):

        # Check if username or email already exists
        if User.objects(username=username).first():
            raise abort(400, "Username already taken")
        if User.objects(email=email).first():
            raise abort(400, "Email already taken")

        # Hash the password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create and save the new user
        user = User(username=username, email=email, password_hash=password_hash, display_name=name)
        user.save()

        return jsonify({"user": user, "status": 'SIGNED_UP'})
        

