""" 
    Developer: Chandru
    Github profile: https://github.com/chandru-engineer
    github repo: https://github.com/chandru-engineer
"""


from celery_package.main import app
from celery_package.log_config import logger
# from celery_package.modules.task1 import task_1_function
# from celery_package.modules.task2 import task_2_function
# from celery_package.modules.task3 import task_3_function
# from celery_package.modules.send_mail import send_opt_mail


@app.task
def execute_task_1_job():
    try:
        # write a functionality here which you want to execute
        return "Task 1 Executed"
    except Exception as error: 
        pass


@app.task
def execute_task_2_job():
    try:
        # write a functionality here which you want to execute
        return "Task 2 Executed"
    except Exception as error: 
        pass


@app.task
def execute_task_3_job():
    try:
       # write a functionality here which you want to execute
       return "Task 3 Executed"
    except Exception as error: 
        pass


@app.task
def execute_send_mail_job():
    try:
       # write a functionality here which you want to execute
       return "Mail Sented successfully"
    except Exception as error: 
        pass

