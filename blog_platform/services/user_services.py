from datetime import datetime, timezone
from blog_platform.database_services.user_database_services import UserDBService
from blog_platform.utils.errors import (
    BadRequestError,
    NotFoundError,
    InternalServerError,
    UnauthorizedError,
)
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, decode_token
from blog_platform.utils.redis_client import redis_client

# Define a global blacklist set
blacklist = set()


class UserService:

    @staticmethod
    def register_user(data):
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        if not username or not password or not email:
            raise BadRequestError("Username, password, and email are required")

        if UserDBService.get_user_by_username(username):
            raise BadRequestError("Username already exists")

        user = UserDBService.create_user(username, password, email)
        return {
            "message": "User registered successfully",
            "user_id": user.id
        }, 201

    @staticmethod
    def login_user(username, password):
        """Authenticate a user and generate a JWT token"""
        user = UserDBService.get_user_by_username(username)
        if user and check_password_hash(user.password, password):
            # Create JWT token
            access_token = create_access_token(identity={"username": username})
            return access_token
        else:
            raise UnauthorizedError("Invalid username or password")

    @staticmethod
    def generate_password_hash(password):
        return generate_password_hash(password, method="scrypt")

    @staticmethod
    def logout_user(token):
        """Invalidate the JWT token."""
        if not token:
            raise BadRequestError("Missing authorization token")
        # # Add the token to the blacklist in Redis
        # redis_client.set(token, "", ex=1)
        try:
            decoded_token = decode_token(token)
            jti = decoded_token["jti"]
            expires = decoded_token["exp"]
            now = datetime.now(timezone.utc)
            exp_time = datetime.fromtimestamp(expires, timezone.utc)
            delta = exp_time - now
            redis_client.set(jti, "", ex=int(delta.total_seconds()))
        except Exception as e:
            raise InternalServerError("Failed to invalidate token")

    @staticmethod
    def get_user_by_username(username):
        return UserDBService.get_user_by_username(username)