

# Celery Template Project

This is a template project to help new learners get started with Celery. It includes configurations for logging, environment variables using `.env`, PostgreSQL as the message broker, and scheduled jobs with different timings.

## Prerequisites

Before running the application, ensure you have the following installed:

- [RabbitMQ](https://www.rabbitmq.com/download.html)
- Python 3.6 or later

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/celery-template.git
    cd celery-template
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**

    Create a `.env` file in the project root and add the following:

    ```dotenv
    BROKER_URL=pyamqp://guest:guest@localhost//
    RESULT_BACKEND=db+postgresql://your_username:your_password@localhost/your_database
    ```

    Adjust the values according to your RabbitMQ and PostgreSQL configurations.

5. **Run RabbitMQ:**

    Ensure RabbitMQ is running on your machine.

## Running Celery

### Start Celery Beat:

```bash
celery -A run beat --loglevel=info
```

### Start Celery Worker:

```bash
celery -A run worker --loglevel=info -P eventlet
```


### Increase Celery Worker Concurrency

When starting the Celery worker, you can specify the concurrency level using the `-c` flag. For example:

```bash
celery -A run worker --loglevel=info -P eventlet -c 10
```

This command starts the Celery worker with a concurrency of 10. Adjust the number according to your requirements and system resources.


Adjust the `-P eventlet` based on your concurrency needs.

## Schedule Jobs

The project includes the following scheduled tasks:

- `execute_task_1_job`: The first scheduled task is simple schedule job will run every 1 min.
- `execute_task_2_job`: The second scheduled task to demonstrate celery retry functionalty.
- ...

## Retrying Mechanism

Tasks in this project are configured with a retrying mechanism. For example:

```python
@app.task(bind=True, max_retries=3, retry_backoff=60)
def execute_task_2_job(self):
    try:
        # Your task logic here
    except Exception as exc:
        # Log the exception
        print(f"Task failed: {exc}")
        # Retry the task
        raise self.retry(exc=exc)
```

Adjust the `max_retries` and `retry_backoff` values according to your requirements.

## Send Mail Functionality

The project includes functionality to send emails asynchronously. For example:

```python
@app.task
def send_mail_task(email_address, subject, message):
    # Your email sending logic here
```

To trigger the email sending task, create a Flask route or use Celery's `send_task` method.

## Additional Notes

- Make sure your PostgreSQL server is running, and update the `RESULT_BACKEND` URL in the `.env` file accordingly.
- Refer to Celery documentation for advanced configurations and customization options.



### Create a Celery Task for Sending Emails

In your `tasks.py` file, define a Celery task for sending emails. This task will contain the logic for sending emails asynchronously.

```python
# celery_package/tasks.py
@app.task
def send_mail_task(user_name, email_id):
    try:
        # Your SMTP email sending logic here
        return f"Mail sent successfully to {email_id}"
    except Exception as error:
        # Log the exception or handle it as needed
        print(f"Error sending mail: {error}")
        raise

```


### Trigger the Email Sending Task in Your Flask Route

Create a Flask route that triggers the Celery task to send emails. Make sure to import and use `send_mail_task` from the Celery tasks.

Create a New task in the Celery application for the send_mail 
Configure the Celery in you Flask application and send the requeried args to the particular task. Example

```python
# app.py or your main Flask application file

from flask import Flask
from celery import Celery

app = Flask(__name__)

# Configure Celery
celery = Celery(
    app.import_name,
    broker=app.config['CELERY_BROKER_URL'],
    backend=app.config['CELERY_RESULT_BACKEND']
)

@app.route('/send_mail')
def send_mail():
    # Run a Celery task
    result = celery.send_task('send_mail_task', args=["user_name", "email_id"])
    return {'successfull': 'Mail Sent Successfully'}, 200
```

Now, when you hit the `/send_mail` route in your Flask application, it will trigger the Celery task to send emails asynchronously. The increased concurrency level will allow multiple tasks to be processed concurrently by the Celery worker.

