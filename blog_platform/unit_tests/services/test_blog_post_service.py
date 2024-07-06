# blog_platform/unit_tests/services/test_blog_post_service.py
import pytest
from blog_platform.services.blog_post_service import BlogPostService
from blog_platform.utils.errors import NotFoundError, ValidationError
from blog_platform.core.database.models import BlogPost

@pytest.fixture
def blog_post_data():
    return {'title': 'Test Post', 'content': 'This is a test post', 'author_id': 1}

def test_create_blog_post(blog_post_data):
    post = BlogPostService.create_blog_post(blog_post_data)
    assert post.title == 'Test Post'
    assert post.content == 'This is a test post'
    assert post.author_id == 1

def test_get_blog_post_by_id(blog_post_data):
    post = BlogPostService.create_blog_post(blog_post_data)
    fetched_post = BlogPostService.get_blog_post_by_id(post.id)
    assert fetched_post.id == post.id

def test_get_blog_post_by_id_not_found():
    with pytest.raises(NotFoundError):
        BlogPostService.get_blog_post_by_id(9999)  # Invalid ID

def test_update_blog_post(blog_post_data):
    post = BlogPostService.create_blog_post(blog_post_data)
    update_data = {'title': 'Updated Title'}
    updated_post = BlogPostService.update_blog_post(post.id, update_data)
    assert updated_post.title == 'Updated Title'

def test_delete_blog_post(blog_post_data):
    post = BlogPostService.create_blog_post(blog_post_data)
    BlogPostService.delete_blog_post(post.id)
    with pytest.raises(NotFoundError):
        BlogPostService.get_blog_post_by_id(post.id)
