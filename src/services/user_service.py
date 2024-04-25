from models import User
from flask import jsonify
from tasks.user import update_last_login

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
        if user and user.password_hash == str(hash(password)):
            user_id = user.id
            user_obj = {
                "name": user.display_name,
                "email": user.email,
                "user_id": user_id,
            }

            # Call Celery task to update last login
            update_last_login.delay(user_id)

            return jsonify({"user": user_obj, "status": 'LOGGED_IN', "last_login_at": user.last_login_at})
        else:
            return jsonify({"error":"Incorrect username or password"}), 400
        

    def register_user(self, username, password, email, name):

        # Check if username or email already exists
        if User.objects(username=username).first():
            return jsonify({"error":"Username already taken"}), 400

        if User.objects(email=email).first():
            return jsonify({"error":"Email already taken"}), 400 


        # Hash the password
        password_hash = str(hash(password))
        # Create and save the new user
        user = User(username=username, email=email, password_hash=password_hash, display_name=name)
        user.save()
        user_obj = {
            "name": user.display_name,
            "email": user.email,
            "user_id": user.id,
        }

        return jsonify({"user": user_obj, "status": 'SIGNED_UP'})
        

