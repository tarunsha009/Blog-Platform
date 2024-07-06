# blog_platform/unit_tests/api/v1/test_blog_post_api.py
import pytest
from flask import Flask
from flask_restx import Api
from blog_platform.api.v1.blog_post import api as blog_post_api
from unittest.mock import patch
from blog_platform.services.blog_post_service import BlogPostService

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    api = Api(app)
    api.add_namespace(blog_post_api, path='/blog')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def blog_post_data():
    return {'title': 'Test Post', 'content': 'This is a test post', 'author_id': 1}

@patch('blog_platform.api.v1.blog_post.BlogPostService.create_blog_post')
def test_create_blog_post_success(mock_create_blog_post, client, blog_post_data):
    mock_create_blog_post.return_value = blog_post_data

    response = client.post('/blog/posts', json=blog_post_data)
    
    assert response.status_code == 201
    assert response.json['title'] == 'Test Post'
    assert response.json['content'] == 'This is a test post'
    assert response.json['author_id'] == 1

@patch('blog_platform.api.v1.blog_post.BlogPostService.create_blog_post')
def test_create_blog_post_validation_error(mock_create_blog_post, client):
    invalid_data = {'title': '', 'content': 'This is a test post', 'author_id': 1}
    response = client.post('/blog/posts', json=invalid_data)
    
    assert response.status_code == 400
    assert 'Title is required' in response.json['message']

@patch('blog_platform.api.v1.blog_post.BlogPostService.create_blog_post')
def test_create_blog_post_service_error(mock_create_blog_post, client, blog_post_data):
    mock_create_blog_post.side_effect = Exception("Service error")

    response = client.post('/blog/posts', json=blog_post_data)
    
    assert response.status_code == 500
    assert response.json['message'] == 'Internal Server Error'
