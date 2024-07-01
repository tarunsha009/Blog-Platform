from blog_platform.core.database.db import db

from blog_platform.core.database.models import User


class UserDatabaseServices:

    def get_all_users(self):
        return User.query.all()

    def add_user(self, data):
        # try:
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user
