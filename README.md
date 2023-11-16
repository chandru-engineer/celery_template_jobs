
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

Adjust the `-P eventlet` based on your concurrency needs.

## Additional Notes

- Make sure your PostgreSQL server is running, and update the `RESULT_BACKEND` URL in the `.env` file accordingly.
- Refer to Celery documentation for advanced configurations and customization options.

---