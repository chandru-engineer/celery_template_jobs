""" 
    Developer: Chandru
    Github profile: https://github.com/chandru-engineer
    github repo: https://github.com/chandru-engineer
"""

# celeryconfig.py
from celery.schedules import crontab
from dotenv import load_dotenv
import os

load_dotenv()

BROKER_URL = os.getenv('BROKER_URL')
RESULT_BACKEND = os.getenv('RESULT_BACKEND')

imports = ('celery_package.tasks',)

# Additional Celery configuration settings
beat_schedule = {
    'schedule_jobs_task1': {
        'task': 'celery_package.tasks.execute_task_1_job',  
        'schedule': crontab(minute='*/1'),
    },
    'schedule_jobs_task2': {
        'task': 'celery_package.tasks.execute_task_2_job',  
        'schedule': crontab(minute='*/2'),
    },
    'schedule_jobs_task3': {
        'task': 'celery_package.tasks.execute_task_3_job',  
        'schedule': crontab(minute='*/3'),
    },
    'schedule_jobs_task4': {
        'task': 'celery_package.tasks.execute_task_4_job',  
        'schedule': crontab(minute='*/4'),
    },
}
