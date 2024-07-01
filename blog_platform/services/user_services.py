from sqlalchemy.exc import NoResultFound

from blog_platform.database_services.user_database_services import UserDatabaseServices
from blog_platform.utils.errors import NotFoundError, InternalServerError


class UserServices:

    def get_all_users(self):
        try:
            user_database_service = UserDatabaseServices()
            return user_database_service.get_all_users()
        except Exception as err:
            raise err

    def add_user(self, data):
        try:
            user_database_service = UserDatabaseServices()
            return user_database_service.add_user(data)
        except Exception as err:
            raise err

    def get_user_by_id(self, user_id):
        user_database_service = UserDatabaseServices()
        try:
            user = user_database_service.get_user_by_id(user_id)
            if user is None:
                raise NotFoundError(message=f"User with ID {user_id} not found")
            return user
        except NotFoundError as e:
            raise e
        except Exception as err:
            raise InternalServerError(message=str(err))

    def update_user(self, user_id, data):
        try:
            user_database_service = UserDatabaseServices()
            return user_database_service.update_user(user_id, data)
        except Exception as err:
            raise err

    def delete_user(self, user_id):
        try:
            user_database_service = UserDatabaseServices()
            return user_database_service.delete_user(user_id)
        except Exception as err:
            raise err
