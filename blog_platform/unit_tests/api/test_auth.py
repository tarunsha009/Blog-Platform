# blog_platform/unit_tests/api/test_user_login.py
import pytest

def test_user_login_success(client, new_user):
    """Test successful user login."""
    login_data = {
        'username': 'testuser',
        'password': 'password'
    }
    response = client.post('/blog/User/login', json=login_data)
    assert response.status_code == 200
    assert 'token' in response.json

def test_user_login_failure_invalid_credentials(client):
    """Test user login with invalid credentials."""
    login_data = {
        'username': 'wronguser',
        'password': 'wrongpassword'
    }
    response = client.post('/blog/User/login', json=login_data)
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid username or password'

def test_user_login_failure_missing_fields(client):
    """Test user login with missing fields."""
    response = client.post('/blog/User/login', json={})
    assert response.status_code == 500
    assert 'password' in response.json['errors']
    assert response.json['errors']['password'] == "'password' is a required property"
    assert 'username' in response.json['errors']
    assert response.json['errors']['username'] == "'username' is a required property"

    response = client.post('/blog/User/login', json={'username': 'testuser'})
    assert response.status_code == 500
    assert response.json['errors']['password'] == "'password' is a required property"

    response = client.post('/blog/User/login', json={'password': 'password'})
    assert response.status_code == 500
    assert response.json['errors']['username'] == "'username' is a required property"
