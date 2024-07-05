# blog_platform/unit_tests/test_user.py
import json

def test_user_registration(client):
    """Test user registration with valid data."""
    response = client.post(
        '/blog/User/register',
        data=json.dumps(dict(
            username='testuser1',
            password='testpassword1',
            email='test1@example.com'
        )),
        content_type='application/json'
    )
    data = json.loads(response.data)
    assert response.status_code == 201
    assert 'User registered successfully' in data['message']

def test_user_registration_existing_username(client, new_user):
    """Test user registration with an existing username."""
    response = client.post(
        '/blog/User/register',
        data=json.dumps(dict(
            username='testuser',
            password='newpassword',
            email='new@example.com'
        )),
        content_type='application/json'
    )
    data = json.loads(response.data)
    assert response.status_code == 400
    assert 'Username already exists' in data['message']

def test_user_registration_missing_field(client):
    """Test user registration with missing fields."""
    response = client.post(
        '/blog/User/register',
        data=json.dumps(dict(
            username='',
            password='testpassword',
            email='test@example.com'
        )),
        content_type='application/json'
    )
    data = json.loads(response.data)
    assert response.status_code == 400
    assert 'Username, password, and email are required' in data['message']
