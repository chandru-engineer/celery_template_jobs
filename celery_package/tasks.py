""" 
    Developer: Chandru
    Github profile: https://github.com/chandru-engineer
    github repo: https://github.com/chandru-engineer/celery_template_jobs
"""


from celery_package.main import app
from celery_package.log_config import logger
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



@app.task
def execute_task_1_job():
    try:
        # write a functionality here which you want to execute
        return "Task 1 Executed"
    except Exception as error: 
        pass


@app.task(bind=True, max_retries=3, retry_backoff=60)
def execute_task_2_job(self):
    """
    Celery Task: execute_task_3_job

    This Celery task demonstrates the use of retries and exponential backoff.
    
    Parameters:
        - self (Task): The task instance (automatically passed by Celery).
        
    Raises:
        - Exception: Simulates a potential exception during task execution.

    Returns:
        - float: The result of the task's logic (unreachable in this example).
        
    Task Logic:
        The task attempts to perform a calculation that might raise an exception
        (division by zero in this example). If an exception occurs, the task
        logs the exception and requests Celery to retry the task with
        exponential backoff up to a maximum of three retries.
    """
    try:
        # Your task logic here
        result = 1 / 0  # An example that might cause an exception
        return result
    except Exception as exc:
        # Log the exception
        print(f"Task failed: {exc}")
        # Retry the task
        raise self.retry(exc=exc)


# celery_package/tasks.py
@app.task
def send_mail_task(user_name, email_id):
    try:
        # Your SMTP email sending logic here
        smtp_server = "your_smtp_server"
        smtp_port = 587  # or your SMTP server's port
        smtp_username = "your_smtp_username"
        smtp_password = "your_smtp_password"

        subject = "Welcome to Your App"
        body = f"Hello {user_name},\n\nThank you for signing up at Your App! We're excited to have you on board."

        # Create the MIMEText object
        msg = MIMEMultipart()
        msg['From'] = "your_email@example.com"
        msg['To'] = email_id
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail("your_email@example.com", email_id, msg.as_string())

        return f"Mail sent successfully to {email_id}"
    except Exception as error:
        # Log the exception or handle it as needed
        print(f"Error sending mail: {error}")
        raise


