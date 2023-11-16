""" 
    Developer: Chandru
    Github profile: https://github.com/chandru-engineer
    github repo: https://github.com/chandru-engineer
"""

"""
commend for the running the worker and beat
beat: 
celery -A run beat --loglevel=info

worker: 
celery -A run worker --loglevel=info -P eventlet
"""

from celery_package.main import app

if __name__ == '__main__':
    app.start()

