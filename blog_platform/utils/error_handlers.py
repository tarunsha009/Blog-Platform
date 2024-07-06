# blog_platform/api/v1/error_handlers.py
from flask import jsonify
from blog_platform.utils.errors import (
    BadRequestError,
    NotFoundError,
    InternalServerError,
    UnauthorizedError,
)

# from marshmallow import ValidationError


def register_error_handlers(api):

    @api.errorhandler(BadRequestError)
    def handle_bad_request_error(error):
        response = {"message": error.description}
        return response, error.code

    @api.errorhandler(NotFoundError)
    def handle_not_found_error(error):
        response = {"message": error.description}
        return response, error.code

    @api.errorhandler(UnauthorizedError)
    def handle_unauthorized_error(error):
        response = {"message": error.description}
        return response, error.code

    @api.errorhandler(InternalServerError)
    def handle_internal_server_error(error):
        response = {"message": error.description}
        return response, error.code

    @api.errorhandler(Exception)
    def handle_general_exception(error):
        response = {"message": "Internal Server Error"}
        return response, 500

    # @api.errorhandler(ValidationError)
    # def handle_validation_error(error):
    #     response = {'message': error.messages}
    #     return response, 400
