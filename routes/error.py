import logging
import json
from flask import Blueprint
from flask import jsonify
from flask import Response
from helpers.jsonencoder import JSONEncoder

from exceptions import RestException

bp = Blueprint(__name__, "error")
log = logging.getLogger(__name__)


@bp.app_errorhandler(RestException)
def handle_rest_exception(e):
    """This error will show if RestException raised"""
    log.warning(e)
    return Response(json.dumps(e.to_dict(), cls=JSONEncoder),
                    mimetype='application/json')


@bp.app_errorhandler(404)
def page_not_found(e):
    """Not found handle"""
    log.warning(e)
    response = {"error": 1, "message": "Resource Not exists", "data": {}}
    return jsonify(response), 404


@bp.app_errorhandler(405)
def method_not_allowed(e):
    """Method not allowed handle"""
    log.warning(e)
    response = {"error": 1, "message": "Method not allowed", "data": {}}
    return jsonify(response), 405


@bp.app_errorhandler(500)
def server_error(e):
    """This error will show if error un handle"""
    log.error(e)
    response = {"error": 1, "message": "Internal server error", "data": {}}
    return jsonify(response), 500
