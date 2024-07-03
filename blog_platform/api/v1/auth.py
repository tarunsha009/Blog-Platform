# blog_platform/api/v1/auth.py
from flask_restx import Namespace, Resource, fields
from flask import request
from marshmallow import ValidationError
from blog_platform.services.user_services import UserService
from blog_platform.utils.errors import BadRequestError, UnauthorizedError
from blog_platform.database.schemas import LoginSchema

api = Namespace('User', description='User Authentication operations')

login_schema = LoginSchema()

login_model = api.model('Login', {
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password')
})

@api.route('/login')
class UserLogin(Resource):
    @api.expect(login_model)
    def post(self):
        """User Login"""
        json_data = request.get_json()
        try:
            # Validate and deserialize input data
            data = login_schema.load(json_data)
        except ValidationError as err:
            raise BadRequestError(err.messages)

        username = data.get('username')
        password = data.get('password')
        
        try:
            token = UserService.login_user(username, password)
            return {'token': token}, 200
        except UnauthorizedError as e:
            raise UnauthorizedError(e.description)
