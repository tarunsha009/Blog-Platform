# blog_platform/services/blog_post_service.py

from blog_platform.database_services.blog_post_db_service import BlogPostDBService
from blog_platform.utils.errors import NotFoundError

class BlogPostService:

    @staticmethod
    def create_blog_post(data):
        # Assuming `data` is already validated by the API layer
        new_post = BlogPostDBService.create_blog_post(
            title=data['title'],
            content=data['content'],
            author_id=data['author_id']
        )
        return new_post

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
        # Assuming `data` is already validated by the API layer
        updated_post = BlogPostDBService.update_blog_post(
            post_id,
            title=data.get('title'),
            content=data.get('content')
        )
        if not updated_post:
            raise NotFoundError("Blog post not found")
        return updated_post

    @staticmethod
    def delete_blog_post(post_id):
        deleted_post = BlogPostDBService.delete_blog_post(post_id)
        if not deleted_post:
            raise NotFoundError("Blog post not found")
        return deleted_post
