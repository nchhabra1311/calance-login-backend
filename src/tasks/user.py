from celery_config import celery
from models.user import LoginEvent
from models.user import User
from datetime import datetime

@celery.task
def update_last_login(user_id):
    # Fetch user from the database
    user = User.objects.get(id=user_id)

    # Update last_login field
    user.last_login_at = datetime.now()
    user.save()

    # Store last login information in LoginEvent collection
    login_event = LoginEvent(user=user, timestamp=user.last_login_at)
    login_event.save()
