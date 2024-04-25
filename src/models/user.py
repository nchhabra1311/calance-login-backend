from mongoengine import Document, StringField, DateTimeField, ReferenceField, UUIDField
from datetime import datetime
import uuid

class User(Document):
      """
      TASK: Create a model for user with minimalistic
            information required for user authentication

      HINT: Do not store password as is.
      """
      id = UUIDField(primary_key=True, default=uuid.uuid4())
      username = StringField(required=True, unique=True)
      password_hash = StringField(required=True)
      email = StringField(required=True, unique=True)
      display_name = StringField(required=True)
      created_at = DateTimeField(default=datetime.now, required=True)

      meta = {
            'collection': 'users'
      }

class LoginEvent(Document):
      """
      Model to represent login events in the database.
      """
      id = UUIDField(primary_key=True, default=uuid.uuid4())
      user = ReferenceField(User, required=True)
      timestamp = DateTimeField(required=True)

      meta = {
            'collection': 'login_events'
      }
