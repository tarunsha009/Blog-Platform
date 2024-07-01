from flask_restx import Resource, Namespace, fields
from flask import request
from blog_platform.services.user_services import UserServices
from blog_platform.database.schemas import UserSchema
from marshmallow.exceptions import ValidationError

from blog_platform.utils.errors import NotFoundError, InternalServerError

user_schema = UserSchema()
api = Namespace("User", description="User operations")

user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of the user'),
    'username': fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user')
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
        try:
            data = user_schema.load(json_data)
        except ValidationError as err:
            return {'message': err.messages}, 400

        user_service = UserServices()
        result = user_service.add_user(data)
        return result, 201

@api.route('/<int:user_id>')
class UserDetail(Resource):
    @api.doc('get_user')
    # @api.marshal_with(user_model)
    def get(self, user_id):
        """Fetch a user by ID"""
        user_service = UserServices()
        try:
            user = user_service.get_user_by_id(user_id)
            if user is None:
                raise NotFoundError(message=f"User with ID {user_id} not found")
            return user
        except NotFoundError as e:
            raise e
        except Exception as e:
            raise InternalServerError(message=str(e))

    @api.doc('update_user')
    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update a user by ID"""
        json_data = request.get_json()
        try:
            data = user_schema.load(json_data)
        except ValidationError as err:
            return {'message': err.messages}, 400

        user_service = UserServices()
        try:
            user = user_service.update_user(user_id, data)
            return user
        except ValueError:
            return {'message': 'User not found'}, 404

    @api.doc('delete_user')
    def delete(self, user_id):
        """Delete a user by ID"""
        user_service = UserServices()
        try:
            user_service.delete_user(user_id)
            return '', 204
        except ValueError:
            return {'message': 'User not found'}, 404
