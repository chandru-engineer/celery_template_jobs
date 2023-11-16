""" 
    Developer: Chandru
    Github profile: https://github.com/chandru-engineer
    github repo: https://github.com/chandru-engineer
"""


from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# loading all the variables
BROKER_URL = os.getenv('BROKER_URL')
RESULT_BACKEND = os.getenv('RESULT_BACKEND')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')