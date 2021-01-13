from settings.configuration import Configuration
from helpers import Helper
from datetime import datetime
from dateutil import parser
from exceptions import BadRequest
from exceptions import ErrorMessage
from exceptions import SuccessMessage
from models import UserModel
from helpers.postgre_alchemy import postgre_alchemy as db
from sqlalchemy import text
from sqlalchemy.orm import defer
from sqlalchemy import or_
from sqlalchemy import join
from sqlalchemy import func
from sqlalchemy import cast
from sqlalchemy import String

configuration = Configuration()
helper = Helper()

# referensi query model sql alchemy
# https://docs.sqlalchemy.org/en/latest/orm/query.html

class UserServices(object):

    def __init__(self, **kwargs):
        pass

    def get(self, where: dict, search, sort, limit, skip):

        try:
            # query postgresql
            result = db.session.query(UserModel)
            for attr, value in where.items():
                result = result.filter(getattr(UserModel, attr) == value)
            result = result.filter(or_(cast(getattr(UserModel, col.name), String).ilike('%'+search+'%') for col in UserModel.__table__.columns ))
            result = result.order_by(text(sort[0]+" "+sort[1]))
            result = result.offset(skip).limit(limit)
            result = result.options(
                defer("password"))
            result = result.all()

            # change into dict
            user = []
            for res in result:
                res = res.__dict__
                res.pop('_sa_instance_state', None)

                user.append(res)

            # check if empty
            user = list(user)

            if (len(user) > 0):
                return True, user
            else:
                return False, []

        except Exception as err:
            # fail response
            raise ErrorMessage(str(err), 500, 1, {})
