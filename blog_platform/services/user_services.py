from blog_platform.database_services.user_database_services import UserDatabaseServices


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
