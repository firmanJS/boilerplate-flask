import time
import json
import datetime, pytz
import jwt, csv
from passlib.hash import pbkdf2_sha256
from config import configuration
from flask import Response
from helpers.jsonencoder import JSONEncoder
from flask import request
from helpers.postgre_alchemy import postgre_alchemy as db
import pandas as pd
from pandas import ExcelWriter, ExcelFile

class Helper(object):

    def date_to_timestamp(self, date: str):

        timestamp = time.mktime(datetime.datetime.strptime(
            date, "%Y-%m-%dT%H:%M:%S%z").timetuple())

        return int(timestamp)

    @staticmethod
    def generate_hash(password):
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return pbkdf2_sha256.verify(password, hash)

    @staticmethod
    def jwt_encode(payload: dict):
        payload["iat"] = datetime.datetime.utcnow()
        payload["exp"] = datetime.datetime.utcnow() + \
            datetime.timedelta(days=1)
        return jwt.encode(payload, configuration.jwt_secret_key, algorithm=configuration.jwt_algorithm).decode("utf-8")

    @staticmethod
    def read_jwt():
        try:
            token = request.headers.get('Authorization', None)
            tokens = token.split(" ")
            payload = jwt.decode(tokens[1], configuration.jwt_secret_key, algorithm=[configuration.jwt_algorithm])
            return payload
        except Exception as e:
            return {}

    @staticmethod
    def LocalDate():
        try:
            ServerTime = (datetime.datetime.utcnow() + datetime.timedelta(minutes=18, seconds=34)).replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Jakarta")).strftime('%Y-%m-%d %H:%M:%S')
            return ServerTime

        except Exception as e:
            print(e)

    @staticmethod
    def SortList(lst):
        try:
            lst = [str(i) for i in lst]
            lst.sort()
            lst = [int(i) if i.isdigit() else i for i in lst ]
            return lst
        except Exception as e:
            print(e)
