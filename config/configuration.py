import os
from datetime import timedelta

from dotenv import load_dotenv, find_dotenv

# Load environment
load_dotenv(find_dotenv())

# get absolute path static directory in root project
log_folder = os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 'log'))
jwt_algorithm = os.getenv("JWT_ALGORITHM")
jwt_secret_key = os.getenv("JWT_SECRET_KEY")

POSTGRE_HOST = os.getenv("POSTGRE_HOST")
POSTGRE_PORT = os.getenv("POSTGRE_PORT")
POSTGRE_DB = os.getenv("POSTGRE_DB")
POSTGRE_USER = os.getenv("POSTGRE_USER")
POSTGRE_PASSWORD = os.getenv("POSTGRE_PASSWORD")

class Configuration(object):
    # Basic
    DEBUG = os.getenv("DEBUG") == "True"
    PORT = int(os.getenv("PORT", 5000))

    # JWT
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_AUTH_URL_RULE = None
    JWT_EXPIRATION_DELTA = timedelta(days=7)  # token expired in 1 weeks

    # POSTGRESQL
    SQLALCHEMY_DATABASE_URI = "postgresql://"+POSTGRE_USER+":" + \
        POSTGRE_PASSWORD+"@"+POSTGRE_HOST+":"+POSTGRE_PORT+"/"+POSTGRE_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("POSTGRE_TRACK_MODIFICATIONS")
