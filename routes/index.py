from flask import Blueprint, request
from exceptions.message import successResponse
from helpers.postgre_psycopg import connect

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
    a, b = connect()
    print(str(a))

    data = {
        'api': 'api running',
        'database': [dict(row) for row in b]
    }

    return successResponse('Connected', data)
