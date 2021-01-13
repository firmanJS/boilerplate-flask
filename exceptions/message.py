from flask import jsonify

def successResponse(msg, data = None):
    response = {
        "code": 200,
        "message": msg,
        "status": 'success',
        "data": data
    }
    return jsonify(response)
