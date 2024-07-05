# tests/test_user_registration.py

import json
import pytest
from flask import Flask
from flask_restx import Api
from blog_platform.api.v1.user import api as user_api
from blog_platform.services.user_services import UserService
from blog_platform.utils.errors import BadRequestError

@pytest.fixture
def app():
    app = Flask(__name__)
    api = Api(app)
    api.add_namespace(user_api, path='/blog/User')
    app.config['TESTING'] = True
    app.config['JWT_SECRET_KEY'] = 'testsecretkey'  # Set up a secret key for JWT
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_register_success(client, mocker):
    # Mock the UserService register_user method
    mocker.patch('blog_platform.services.user_services.UserService.register_user', return_value={'message': 'User registered successfully', 'user_id': 1})

    response = client.post('/blog/User/register', data=json.dumps({
        'username': 'testuser',
        'password': 'testpassword',
        'email': 'testuser@example.com'
    }), content_type='application/json')

    assert response.status_code == 201
    assert response.get_json() == {'message': 'User registered successfully', 'user_id': 1}

def test_register_failure_existing_user(client, mocker):
    # Mock the UserService register_user method to raise BadRequestError
    mocker.patch('blog_platform.services.user_services.UserService.register_user', side_effect=BadRequestError("Username already exists"))

    response = client.post('/blog/User/register', data=json.dumps({
        'username': 'testuser',
        'password': 'testpassword',
        'email': 'testuser@example.com'
    }), content_type='application/json')

    assert response.status_code == 400
    assert response.get_json() == {'message': 'Username already exists'}

def test_register_failure_validation_error(client, mocker):
    # Mock the UserService register_user method to do nothing
    mocker.patch('blog_platform.services.user_services.UserService.register_user')

    response = client.post('/blog/User/register', data=json.dumps({
        'username': 'testuser'
        # Missing password and email fields
    }), content_type='application/json')

    assert response.status_code == 400
    print(response)
    assert 'Input payload validation failed' in response.get_json()['message']
