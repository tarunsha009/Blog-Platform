from flask import jsonify
from flask_babel import gettext

from blog_platform.utils.errors import BadRequestError, NotFoundError, InternalServerError

def register_error_handlers(app):
    @app.errorhandler(BadRequestError)
    def handle_bad_request_error(error):
        response = jsonify({'message': gettext(error.message)})
        response.status_code = error.status_code
        return response

    @app.errorhandler(NotFoundError)
    def handle_not_found_error(error):
        response = jsonify({'message': gettext(error.message)})
        response.status_code = error.status_code
        return response

    @app.errorhandler(InternalServerError)
    def handle_internal_server_error(error):
        response = jsonify({'message': gettext(error.message)})
        response.status_code = error.status_code
        return response

    @app.errorhandler(Exception)
    def handle_general_exception(error):
        response = jsonify({'message': gettext('Internal Server Error')})
        response.status_code = 500
        return response
