# blog_platform/utils/errors.py
from werkzeug.exceptions import HTTPException


class CustomError(HTTPException):

    def __init__(self, message):
        self.description = message
        super().__init__(description=message)


class BadRequestError(CustomError):
    code = 400


class NotFoundError(CustomError):
    code = 404


class InternalServerError(CustomError):
    code = 500


class UnauthorizedError(CustomError):
    code = 401


class ValidationError(CustomError):
    code = 422
