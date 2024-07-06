from blog_platform.core.database.models import User
from blog_platform.core.database.db import db
from werkzeug.security import generate_password_hash

from blog_platform.utils.errors import NotFoundError, InternalServerError


class UserDBService:

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username, password, email):
        hashed_password = generate_password_hash(password, method="scrypt")
        new_user = User(username=username,
                        password=hashed_password,
                        email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user
