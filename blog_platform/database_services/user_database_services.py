from blog_platform.core.database.models import User
from blog_platform.core.database.db import db
from blog_platform.utils.errors import NotFoundError, InternalServerError


class UserDatabaseServices:
    def get_all_users(self):
        """Retrieve all users from the database."""
        try:
            return User.query.all()
        except Exception as err:
            raise err

    def add_user(self, user_data):
        """Add a new user to the database."""
        try:
            new_user = User(username=user_data['username'], email=user_data['email'])
            db.session.add(new_user)
            db.session.commit()
            return new_user
        except Exception as err:
            db.session.rollback()
            raise err

    def get_user_by_id(self, user_id):
        """Retrieve a user by ID from the database."""
        try:
            return User.query.get(user_id)
        except Exception as err:
            raise InternalServerError(message=str(err))

    def update_user(self, user_id, user_data):
        """Update a user's information."""
        try:
            user = User.query.get(user_id)
            if user:
                user.username = user_data['username']
                user.email = user_data['email']
                db.session.commit()
                return user
            else:
                return None
        except Exception as err:
            db.session.rollback()
            raise err

    def delete_user(self, user_id):
        """Delete a user from the database."""
        try:
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
        except Exception as err:
            db.session.rollback()
            raise err
