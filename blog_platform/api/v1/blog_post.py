from flask_restx import Resource, Namespace, fields
from flask import request
from blog_platform.database.schemas import BlogPostSchema
from blog_platform.services.blog_post_service import BlogPostService
from marshmallow.exceptions import ValidationError

from blog_platform.utils.errors import InternalServerError

api = Namespace("BlogPost", description="Blog Post operations")

blog_post_model = api.model('BlogPost', {
    'title': fields.String(required=True, description='The title of the blog post'),
    'content': fields.String(required=True, description='The content of the blog post'),
    'author_id': fields.Integer(required=True, description='The ID of the author')
})

@api.route('/posts')
class BlogPostCreate(Resource):
    @api.expect(blog_post_model, validate=True)  # API model for documentation and basic validation
    def post(self):
        data = request.get_json()  # Get the request data
        try:
            # Validate and transform data using Marshmallow schema
            blog_post_schema = BlogPostSchema()
            validated_data = blog_post_schema.load(data)

            # Call the service layer to handle business logic
            new_post = BlogPostService.create_blog_post(validated_data)
            return blog_post_schema.dump(new_post), 201  # Return the newly created post
            
        except ValidationError as err:
            return ValidationError(err.messages)  # Return validation errors if any
        except Exception as e:
            # Handle unexpected errors
            raise InternalServerError("An unexpected error occurred while creating the blog post.")
