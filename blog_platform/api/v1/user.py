from flask_restx import Resource, Namespace, fields
from flask import request
from blog_platform.services.user_services import UserService
from blog_platform.database.schemas import UserSchema
from marshmallow.exceptions import ValidationError

from blog_platform.utils.errors import NotFoundError, InternalServerError

user_schema = UserSchema()
api = Namespace("User", description="User operations")

user_registration_model = api.model('UserRegistration', {
    'username': fields.String(required=True, description='The username'),
    'password': fields.String(required=True, description='The password'),
    'email': fields.String(required=True, description='The email address')
})

@api.route('/register')
class UserRegister(Resource):
    @api.expect(user_registration_model, validate=True)
    def post(self):
        data = request.get_json()
        return UserService.register_user(data)
