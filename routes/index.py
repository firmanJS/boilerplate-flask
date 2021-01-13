from flask import Blueprint, request
from exceptions.message import successResponse
from helpers.postgre_alchemy import postgre_alchemy as db

bp = Blueprint(__name__, 'index')

# DONE
@bp.route("/", methods=["GET"])
def index():
    msg = "Welcome to Boilerplate API."
    data = {}
    return successResponse(msg, data)

@bp.route("/api/", methods=["GET"])
def api():
    msg = "Welcome to Boilerplate API."
    data = { "doc": "%sdocumentation" % (request.url) }
    return successResponse(msg, data)


@bp.route("/api/ping", methods=["GET"])
def isAlive():
    '''Do something.

    Parameters
    ----------
    Returns
    -------
    '''

    try:
        connection = db.session.execute("SELECT 1")
        user = []
        for res in connection:
            user.append(res[0])


        return str(user)
    except Exception as err :
        return str(err)

    # success response format
    data = {
        'api': 'api running',
        'database': err
    }

    return successResponse('Connected', data)
