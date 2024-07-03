# blog_platform/unit_tests/test_user.py
import json

def test_user_registration(client, init_db):
    response = client.post(
        '/blog/User/register',
        data=json.dumps(dict(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )),
        content_type='application/json'
    )
    data = json.loads(response.data)
    assert response.status_code == 201
    assert 'User registered successfully' in data['message']

def test_user_registration_existing_username(client, init_db):
    # First registration
    client.post(
        '/blog/User/register',
        data=json.dumps(dict(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )),
        content_type='application/json'
    )
    
    # Second registration with the same username
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

def test_user_registration_missing_field(client, init_db):
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
