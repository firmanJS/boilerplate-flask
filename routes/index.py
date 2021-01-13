from flask import Blueprint, request
from exceptions.message import successResponse

bp = Blueprint(__name__, 'index')

# DONE
@bp.route("/", methods=["GET"])
def index():
    msg = "Welcome to Boilerplate API."
    data = { "doc": "%sdocumentation" % (request.url) }
    return successResponse(msg, data)


@bp.route("/is_alive", methods=["GET"])
def isAlive():
    '''Do something.

    Parameters
    ----------
    Returns
    -------
    '''
    # success response format
    return successResponse("Connected")
