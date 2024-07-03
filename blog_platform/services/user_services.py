from blog_platform.database_services.user_database_services import UserDBService
from blog_platform.utils.errors import BadRequestError, NotFoundError, InternalServerError


class UserServices:

    @staticmethod
    def register_user(data):
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if not username or not password or not email:
            raise BadRequestError("Username, password, and email are required")

        if UserDBService.get_user_by_username(username):
            raise BadRequestError("Username already exists")

        user = UserDBService.create_user(username, password, email)
        return {"message": "User registered successfully", "user_id": user.id}, 201
