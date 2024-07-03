# from datetime import datetime
#
# class CustomHTTPException(Exception):
#     def __init__(self, error_code: str, params: list = None, error_type="Error"):
#         self.response = {
#             'code': error_code,
#             'timestamp': self.getTimestamp(),
#             'severity': error_type
#         }
#         self.http_code = 500
#
#     def getTimestamp(self):
#         current_timestamp = datetime.now().timestamp()
#         dt = datetime.fromtimestamp(current_timestamp)
#         return str(dt)