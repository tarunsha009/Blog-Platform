from flask import Response, request
from flask_restx import Namespace, Resource, fields
from marshmallow import ValidationError

from blog_platform.database.schemas import UserSchema
from blog_platform.services.user_services import UserServices

api = Namespace("User", description="User operations")

user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user username'),
    'email': fields.String(required=True, description='The user email')
})

@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        user_service = UserServices()
        return user_service.get_all_users()

    @api.doc('create_user')
    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        '''Create a new user'''
        json_data = request.get_json()
        user_schema = UserSchema()
        try:
            data = user_schema.load(json_data)
        except ValidationError as err:
            return {'message': err.messages}, 400

        user_service = UserServices()
        result = user_service.add_user(data)
        return result, 201
        # return {
        #     'user': result.username,
        #     'email': result.email
        #     }, 201