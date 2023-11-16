""" 
    Developer: Chandru
    Github profile: https://github.com/chandru-engineer
    github repo: https://github.com/chandru-engineer
"""



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from celery_package.load_env import DB_USERNAME, DB_HOST, DB_NAME, \
    DB_PASSWORD, DB_PORT


# Create the database URL
db_uri = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}' 

try:
    engine = create_engine(db_uri)  # Create the SQLAlchemy engine 
    Session = sessionmaker(bind=engine) # Create a session factory
except Exception as error:
    # logger.error(str(error))
    engine = None
    Session = None
