# blog_platform/services/blog_post_service.py
from blog_platform.database.schemas import BlogPostSchema
from blog_platform.utils.errors import ValidationError, NotFoundError
from blog_platform.database_services.blog_post_db_service import BlogPostDBService

class BlogPostService:

    @staticmethod
    def create_blog_post(data):
        blog_post_schema = BlogPostSchema()
        try:
            validated_data = blog_post_schema.load(data)
            new_post = BlogPostDBService.create_blog_post(
                title=validated_data['title'],
                content=validated_data['content'],
                author_id=validated_data['author_id']
            )
            return new_post
        except ValidationError as err:
            raise ValidationError("Validation error", description=err.messages)

    @staticmethod
    def get_blog_post_by_id(post_id):
        post = BlogPostDBService.get_blog_post_by_id(post_id)
        if not post:
            raise NotFoundError("Blog post not found")
        return post

    @staticmethod
    def get_all_blog_posts():
        return BlogPostDBService.get_all_blog_posts()

    @staticmethod
    def update_blog_post(post_id, data):
        blog_post_schema = BlogPostSchema(partial=True)  # Partial update
        try:
            validated_data = blog_post_schema.load(data, partial=True)
            updated_post = BlogPostDBService.update_blog_post(
                post_id,
                title=validated_data.get('title'),
                content=validated_data.get('content')
            )
            if not updated_post:
                raise NotFoundError("Blog post not found")
            return updated_post
        except ValidationError as err:
            raise ValidationError("Validation error", description=err.messages)

    @staticmethod
    def delete_blog_post(post_id):
        deleted_post = BlogPostDBService.delete_blog_post(post_id)
        if not deleted_post:
            raise NotFoundError("Blog post not found")
        return deleted_post
