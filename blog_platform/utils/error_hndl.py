# from datetime import datetime
# from flask_restx import Namespace
#
# from blog_platform.utils.exceptions import CustomHTTPException
#
# api = Namespace('error_h')
#
# @api.errorhandler(CustomHTTPException)
# def custom_http_exception_handler(error):
#     response = {"custom_http_status_code": error.http_code, "message": error.response}
#     return response, error.http_code
#
#
# @api.errorhandler(CustomHTTPException)
# def default_error_handler(error: Exception):
#     resp = {
#         'code': 'error.code',
#         'timestamp': getTimestamp(),
#         'severity': "Error",
#         'message': str(error)
#     }
#     response = {"generic_http_status_code": 500, "message": resp}
#     return response, 500
#
#
# def getTimestamp(self):
#     current_timestamp = datetime.now().timestamp()
#     dt = datetime.fromtimestamp(current_timestamp)
#     return str(dt)
#
# api.default_error_handler = Exception
# api.errorhandler[Exception] = default_error_handler