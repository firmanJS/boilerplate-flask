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

postgre_host = os.getenv("POSTGRE_HOST")
postgre_port = os.getenv("POSTGRE_PORT")
postgre_db = os.getenv("POSTGRE_DB")
postgre_user = os.getenv("POSTGRE_USER")
postgre_password = os.getenv("POSTGRE_PASSWORD")

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
    SQLALCHEMY_DATABASE_URI = "postgresql://"+postgre_user+":" + \
        postgre_password+"@"+postgre_host+":"+postgre_port+"/"+postgre_db
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("POSTGRE_TRACK_MODIFICATIONS")
