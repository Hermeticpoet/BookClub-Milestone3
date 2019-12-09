import os


# Imported OS and changed our postgreSQL database address to an environment variable for pushing out to production
DEBUG = False
SECRET_KEY = "topsecret"
SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
SQLALCHEMY_TRACK_MODIFICATIONS = False



