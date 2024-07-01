# blog_platform/api/v1/schemas.py

from marshmallow import Schema, fields, validate, ValidationError

from blog_platform.core.database.db import db
from blog_platform.database_services.user_database_services import UserDatabaseServices

def create_schema():
    db.create_all()


def drop_schema():
    db.drop_all()


class UserSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)


