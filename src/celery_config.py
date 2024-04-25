from celery import Celery
import app

celery = Celery(app.application, backend='mongodb://localhost:27017')
