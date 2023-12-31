""" 
    Developer: Chandru
    Github profile: https://github.com/chandru-engineer
    github repo: https://github.com/chandru-engineer/celery_template_jobs
"""

from celery import Celery
from celery_package.load_env import BROKER_URL, RESULT_BACKEND
from celery_package.celeryconfig import beat_schedule
from celery_package.log_config import logger

# create celery app instance
app = Celery(
    'tasks',
    broker=BROKER_URL,
    backend=RESULT_BACKEND
)


from celery_package.tasks import app

# registering the schedules jobs. 
app.conf.beat_schedule = beat_schedule








