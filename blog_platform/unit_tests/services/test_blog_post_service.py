# blog_platform/unit_tests/services/test_blog_post_service.py

import pytest
from unittest.mock import patch
from blog_platform.services.blog_post_service import BlogPostService
from blog_platform.utils.errors import NotFoundError
from blog_platform.core.database.models import BlogPost

# Test for `create_blog_post` method


@patch(
    "blog_platform.services.blog_post_service.BlogPostDBService.create_blog_post"
)
def test_create_blog_post_success(mock_create_blog_post):
    # Mock DB service
    mock_create_blog_post.return_value = BlogPost(
        id=1, title="Test Post", content="This is a test post", author_id=1)

    data = {
        "title": "Test Post",
        "content": "This is a test post",
        "author_id": 1
    }
    result = BlogPostService.create_blog_post(data)

    assert result.title == "Test Post"
    assert result.content == "This is a test post"
    assert result.author_id == 1
    mock_create_blog_post.assert_called_once_with(
        title="Test Post", content="This is a test post", author_id=1)


# Test for `get_blog_post_by_id` method


@patch(
    "blog_platform.services.blog_post_service.BlogPostDBService.get_blog_post_by_id"
)
def test_get_blog_post_by_id_success(mock_get_blog_post_by_id):
    mock_get_blog_post_by_id.return_value = BlogPost(
        id=1, title="Test Post", content="This is a test post", author_id=1)

    result = BlogPostService.get_blog_post_by_id(1)

    assert result.title == "Test Post"
    assert result.content == "This is a test post"
    assert result.author_id == 1
    mock_get_blog_post_by_id.assert_called_once_with(1)


@patch(
    "blog_platform.services.blog_post_service.BlogPostDBService.get_blog_post_by_id"
)
def test_get_blog_post_by_id_not_found(mock_get_blog_post_by_id):
    mock_get_blog_post_by_id.return_value = None

    with pytest.raises(NotFoundError) as exc_info:
        BlogPostService.get_blog_post_by_id(999)

    assert str(exc_info.value) == "404 Not Found: Blog post not found"
    mock_get_blog_post_by_id.assert_called_once_with(999)


# Test for `get_all_blog_posts` method


@patch(
    "blog_platform.services.blog_post_service.BlogPostDBService.get_all_blog_posts"
)
def test_get_all_blog_posts_success(mock_get_all_blog_posts):
    mock_get_all_blog_posts.return_value = [
        BlogPost(id=1,
                 title="Test Post",
                 content="This is a test post",
                 author_id=1)
    ]

    result = BlogPostService.get_all_blog_posts()

    assert len(result) == 1
    assert result[0].title == "Test Post"
    assert result[0].content == "This is a test post"
    assert result[0].author_id == 1
    mock_get_all_blog_posts.assert_called_once()


# Test for `update_blog_post` method


@patch(
    "blog_platform.services.blog_post_service.BlogPostDBService.update_blog_post"
)
def test_update_blog_post_success(mock_update_blog_post):
    mock_update_blog_post.return_value = BlogPost(id=1,
                                                  title="Updated Title",
                                                  content="Updated content",
                                                  author_id=1)

    data = {"title": "Updated Title", "content": "Updated content"}
    result = BlogPostService.update_blog_post(1, data)

    assert result.title == "Updated Title"
    assert result.content == "Updated content"
    mock_update_blog_post.assert_called_once_with(1,
                                                  title="Updated Title",
                                                  content="Updated content")


@patch(
    "blog_platform.services.blog_post_service.BlogPostDBService.update_blog_post"
)
def test_update_blog_post_not_found(mock_update_blog_post):
    mock_update_blog_post.return_value = None

    data = {"title": "Updated Title", "content": "Updated content"}
    with pytest.raises(NotFoundError) as exc_info:
        BlogPostService.update_blog_post(999, data)

    assert str(exc_info.value) == "404 Not Found: Blog post not found"
    mock_update_blog_post.assert_called_once_with(999,
                                                  title="Updated Title",
                                                  content="Updated content")


# Test for `delete_blog_post` method


@patch(
    "blog_platform.services.blog_post_service.BlogPostDBService.delete_blog_post"
)
def test_delete_blog_post_success(mock_delete_blog_post):
    mock_delete_blog_post.return_value = BlogPost(
        id=1, title="Test Post", content="This is a test post", author_id=1)

    result = BlogPostService.delete_blog_post(1)

    assert result.title == "Test Post"
    assert result.content == "This is a test post"
    assert result.author_id == 1
    mock_delete_blog_post.assert_called_once_with(1)


@patch(
    "blog_platform.services.blog_post_service.BlogPostDBService.delete_blog_post"
)
def test_delete_blog_post_not_found(mock_delete_blog_post):
    mock_delete_blog_post.return_value = None

    with pytest.raises(NotFoundError) as exc_info:
        BlogPostService.delete_blog_post(999)

    assert str(exc_info.value) == "404 Not Found: Blog post not found"
    mock_delete_blog_post.assert_called_once_with(999)
