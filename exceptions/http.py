
import json
from typing import Dict
from flask import jsonify
from flask import Response
from helpers.jsonencoder import JSONEncoder


class RestException(Exception):
    """Indicates that the request could not be processed
    because of request in client is invalid"""

    message = __doc__.strip()
    status_code = 400
    payload = None

    def __init__(self,
                 message=None,
                 status_code=None,
                 error_code=None,
                 payload=None):

        if message is not None:
            self.message = message

        if status_code is not None:
            self.status_code = status_code

        if error_code is not None:
            self.error_code = error_code

        if payload is not None:
            self.payload = payload

        super(RestException, self).__init__(self.message)

    def to_dict(self):
        res = dict()  # type: Dict
        if self.payload:
            res = dict(payload=self.payload)
        res['message'] = self.message
        res['error'] = self.error_code
        res['data'] = []
        return json.dumps(res, cls=JSONEncoder)


class BadRequest(RestException):
    """Indicates that the query was invalid.
    E.g. some parameter missing."""

    message = __doc__.strip()
    status_code = 400


class ErrorMessage(RestException):
    """Indicates that the query was invalid.
    E.g. some parameter missing."""

    message = __doc__.strip()
    status_code = 400


class SuccessMessage(RestException):
    """Response success message."""

    message = __doc__.strip()
    status_code = 200
