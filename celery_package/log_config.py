""" 
    Developer: Chandru
    Github profile: https://github.com/chandru-engineer
    github repo: https://github.com/chandru-engineer/celery_template_jobs
"""


import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)


# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

