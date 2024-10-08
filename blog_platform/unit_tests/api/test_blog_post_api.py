# blog_platform/unit_tests/api/v1/test_blog_post_api.py
from datetime import datetime, timezone
import pytest
from flask import Flask
from flask_restx import Api
from blog_platform.api.v1.blog_post import api as blog_post_api
from unittest.mock import MagicMock, patch
from blog_platform.services.blog_post_service import BlogPostService


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    api = Api(app)
    api.add_namespace(blog_post_api, path="/blog")
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def blog_post_data():
    return {
        "title": "Test Post",
        "content": "This is a test post",
        "author_id": 1
    }


@pytest.fixture
def blog_post_return_data():
    return {
        "id": 1,
        "title": "Test Post",
        "content": "This is a test post",
        "author_id": 1,
        "created_at": "2024-07-06T17:16:29.788725",
        "updated_at": "2024-07-06T17:16:29.788725",
    }


def test_create_blog_post_success(mocker, client):
    # Define the input data and expected response data
    blog_post_data = {
        "title": "Test Post",
        "content": "This is a test post",
        "author_id": 1,
    }
    now = datetime.now(timezone.utc)

    blog_post_return_data = {
        "id": 1,
        "title": "Test Post",
        "content": "This is a test post",
        "author_id": 1,
        "created_at": now,
        "updated_at": now,
    }

    # Mock the BlogPostService.create_blog_post method
    mock_create_blog_post = mocker.patch(
        "blog_platform.services.blog_post_service.BlogPostService.create_blog_post",
        return_value=MagicMock(**blog_post_return_data),
    )

    # Send a POST request to the endpoint
    response = client.post("/blog/posts", json=blog_post_data)

    # Check the response status and data
    assert response.status_code == 201
    assert response.json["title"] == blog_post_return_data["title"]
    assert response.json["content"] == blog_post_return_data["content"]
    assert response.json["author_id"] == blog_post_return_data["author_id"]
    assert response.json["id"] == blog_post_return_data["id"]
    assert (response.json["created_at"] ==
            blog_post_return_data["created_at"].isoformat())
    assert (response.json["updated_at"] ==
            blog_post_return_data["updated_at"].isoformat())
    mock_create_blog_post.assert_called_once_with(blog_post_data)


@patch("blog_platform.api.v1.blog_post.BlogPostService.create_blog_post")
def test_create_blog_post_validation_error(mock_create_blog_post, client):
    invalid_data = {
        "title": "",
        "content": "This is a test post",
        "author_id": 1
    }
    response = client.post("/blog/posts", json=invalid_data)

    assert response.status_code == 422
    assert "message" in response.json
    validation_errors = response.json["message"]
    assert "title" in validation_errors
    assert "Shorter than minimum length 1." in validation_errors["title"]


