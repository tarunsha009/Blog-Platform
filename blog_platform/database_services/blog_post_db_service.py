# blog_platform/services/blog_post_db_service.py
from blog_platform.core.database.db import db
from blog_platform.core.database.models import BlogPost

class BlogPostDBService:

    @staticmethod
    def create_blog_post(title, content, author_id):
        new_post = BlogPost(
            title=title,
            content=content,
            author_id=author_id
        )
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def get_blog_post_by_id(post_id):
        return BlogPost.query.get(post_id)

    @staticmethod
    def get_all_blog_posts():
        return BlogPost.query.all()

    @staticmethod
    def update_blog_post(post_id, title=None, content=None):
        post = BlogPost.query.get(post_id)
        if post:
            if title:
                post.title = title
            if content:
                post.content = content
            db.session.commit()
        return post

    @staticmethod
    def delete_blog_post(post_id):
        post = BlogPost.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
        return post
