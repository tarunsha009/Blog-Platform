from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Resource, Namespace, fields
from flask import request
from blog_platform.database.schemas import BlogPostSchema
from blog_platform.services.blog_post_service import BlogPostService
from marshmallow import ValidationError
from blog_platform.services.user_services import UserService
from blog_platform.utils.errors import BadRequestError, InternalServerError, NotFoundError

api = Namespace("BlogPost", description="Blog Post operations")

blog_post_model = api.model(
    "BlogPost",
    {
        "title":
        fields.String(required=True, description="The title of the blog post"),
        "content":
        fields.String(required=True,
                      description="The content of the blog post"),
        "author_id":
        fields.Integer(required=True, description="The ID of the author"),
    },
)


@api.route("/posts")
class BlogPostCreate(Resource):

    @api.expect(blog_post_model, validate=True)
    def post(self):
        data = request.get_json()
        try:
            blog_post_schema = BlogPostSchema()
            validated_data = blog_post_schema.load(data)

            new_post = BlogPostService.create_blog_post(validated_data)
            response = {
                "id":
                new_post.id,
                "title":
                new_post.title,
                "content":
                new_post.content,
                "author_id":
                new_post.author_id,
                "created_at": (new_post.created_at.isoformat()
                               if new_post.created_at else None),
                "updated_at": (new_post.updated_at.isoformat()
                               if new_post.updated_at else None),
            }
            return response, 201
        except ValidationError as err:
            return {"message": err.messages}, 422
        except Exception as e:
            raise InternalServerError(
                "An unexpected error occurred while creating the blog post.")

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        username = current_user.get("username")
        try:
            user = UserService.get_user_by_username(username)
            if not username:
                raise NotFoundError("user not found")
            
            posts = BlogPostService.get_blog_posts_by_user_id(user.id)
            response = [
                    {
                        'id': post.id,
                        'title': post.title,
                        'content': post.content,
                        'author_id': post.author_id,
                        'created_at': post.created_at.isoformat(),
                        'updated_at': post.updated_at.isoformat()
                    } for post in posts
                ]
            return response, 200
        except Exception as e:
            raise InternalServerError("An unexpected error occurred while retrieving the blog posts.")
    