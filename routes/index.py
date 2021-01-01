from flask import Blueprint
from flask import jsonify

bp = Blueprint(__name__, 'index')


# DONE
@bp.route("/", methods=["GET"])
def index():
    response = {
        "error": 0,
        "message": "Welcome to Boilerplate API.",
        "data": {
            "doc":  "/documentation"
        }
    }
    return jsonify(response)


@bp.route("/is_alive", methods=["GET"])
def is_alive():
    # success response format
    response = {
        "error": 0,
        "message": "Connected",
        "data": []
    }

    return jsonify(response)
