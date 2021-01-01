import requests
import jwt
import json
import time
from flask import current_app, request
from functools import wraps
from helpers import Helper
from exceptions import BadRequest
from exceptions import ErrorMessage
from exceptions import SuccessMessage
from flask import Response
from helpers.jsonencoder import JSONEncoder
from config import configuration

helper = Helper()


def jwt_check():

    def wrapper(func):

        @wraps(func)
        def decorator(*args, **kwargs):

            token = request.headers.get('Authorization', None)
            app_code = configuration.app_code
            controller = request.path
            action = request.method

            if(controller[0] == '/'):
                controller = controller[(len(controller)-1)*-1:]

            res = ''
            fullurl = configuration.rolecheck_url + 'auth/check?app_code=' + str(app_code) + '&controller=' + str(controller) + '&action=' + str(action)

            res_data = {}
            res_data['token'] = token
            res_data['app_code'] = app_code
            res_data['controller'] = controller
            res_data['action'] = action
            res_data['fullurl'] = fullurl


            try:
                while res == '':
                    try:
                        req = requests.get(fullurl, headers={"Authorization":token})
                        break
                    except:
                        print("Connection refused by the server..")
                        print("Let me sleep for 5 seconds")
                        print("ZZzzzz...")
                        time.sleep(5)
                        print("Was a nice sleep, now let me continue...")
                        continue

            except Exception as e:
                res_data['req'] = req

                res_msg = {}
                res_msg['error'] = 1
                res_msg['message'] = "Internal Server Error, Failed while loop sleep . " + str(e)
                res_msg['data'] = res_data

                return Response(json.dumps(res_msg, cls=JSONEncoder), mimetype='application/json'), 403

            try:
                res = req.json()

            except Exception as e:
                res_data['res'] = res

                res_msg = {}
                res_msg['error'] = 1
                res_msg['message'] = "Internal Server Error, Failed while get json response from check permission . " + str(e)
                res_msg['data'] = res_data

                return Response(json.dumps(res_msg, cls=JSONEncoder), mimetype='application/json'), 403

            try:
                if(res['error'] > 0):
                    return Response(json.dumps(res, cls=JSONEncoder), mimetype='application/json'), 403
                else:
                    pass

                return func(*args, **kwargs)

            except Exception as e:
                print(e)
                res_msg = {}
                res_msg['error'] = 1
                res_msg['message'] = "Internal Server Error, Failed while check permission. " + str(e)
                res_msg['data'] = {}
                return Response(json.dumps(res_msg, cls=JSONEncoder), mimetype='application/json'), 403

        return decorator

    return wrapper
