# tests/test_auth.py

import json
import pytest
from flask import Flask
from flask_restx import Api
from blog_platform.api.v1.auth import api as auth_api
from blog_platform.api.v1.user import api as user_api
from blog_platform.services.user_services import UserService
from blog_platform.utils.errors import BadRequestError, UnauthorizedError

@pytest.fixture
def app():
    app = Flask(__name__)
    api = Api(app)
    api.add_namespace(auth_api, path='/blog/User')
    api.add_namespace(user_api, path='/blog/User')
    app.config['TESTING'] = True
    app.config['JWT_SECRET_KEY'] = 'testsecretkey'  # Set up a secret key for JWT
    return app

@pytest.fixture
def client(app):
    return app.test_client()


def test_login_success(client, mocker):
    # Mock the UserService login_user method
    mocker.patch('blog_platform.services.user_services.UserService.login_user', return_value='fake_token')

    response = client.post('/blog/User/login', data=json.dumps({
        'username': 'testuser',
        'password': 'correctpassword'
    }), content_type='application/json')

    assert response.status_code == 200
    assert response.get_json() == {'token': 'fake_token'}

def test_login_failure_invalid_credentials(client, mocker):
    # Mock the UserService login_user method to raise UnauthorizedError
    mocker.patch('blog_platform.services.user_services.UserService.login_user', side_effect=UnauthorizedError("Invalid username or password"))

    response = client.post('/blog/User/login', data=json.dumps({
        'username': 'testuser',
        'password': 'wrongpassword'
    }), content_type='application/json')

    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid username or password'}

def test_login_failure_validation_error(client, mocker):
    # Mock the UserService login_user method to do nothing
    mocker.patch('blog_platform.services.user_services.UserService.login_user')

    response = client.post('/blog/User/login', data=json.dumps({
        'username': 'testuser'
        # Missing password field
    }), content_type='application/json')

    assert response.status_code == 400
    assert 'password' in response.get_json()['message']

def test_logout_success(client, mocker):
    # Mock the UserService logout_user method
    mocker.patch('blog_platform.services.user_services.UserService.logout_user')

    response = client.post('/blog/User/logout', headers={
        'Authorization': 'Bearer fake_token'
    })

    assert response.status_code == 200
    assert response.get_json() == {'message': 'User logged out successfully'}

def test_logout_failure_missing_token(client, mocker):
    # Mock the UserService logout_user method
    mocker.patch('blog_platform.services.user_services.UserService.logout_user')

    response = client.post('/blog/User/logout')

    assert response.status_code == 400
    assert response.get_json() == {'message': 'Missing authorization token'}
