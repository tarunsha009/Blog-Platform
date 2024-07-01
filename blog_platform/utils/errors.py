class APIError(Exception):
    def __init__(self, status_code, message):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class BadRequestError(APIError):
    def __init__(self, message="Bad Request"):
        super().__init__(400, message)


class NotFoundError(APIError):
    def __init__(self, message="Not Found"):
        super().__init__(404, message)


class InternalServerError(APIError):
    def __init__(self, message="Internal Server Error"):
        super().__init__(500, message)
