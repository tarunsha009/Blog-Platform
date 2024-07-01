import pytest


def test_create_user(client, init_db):
    """Test the POST /blog/User/ endpoint."""
    response = client.post('/blog/User/', json={
        'username': 'tarun',
        'email': 'tarun@gmail.com'
    })

    assert response.status_code == 201
    response_json = response.get_json()
    assert response_json['username'] == 'tarun'
    assert response_json['email'] == 'tarun@gmail.com'


def test_create_user_invalid(client, init_db):
    """Test invalid data for the POST /blog/User/ endpoint."""
    response = client.post('/blog/User/', json={
        'username': 'tarun'
    })

    assert response.status_code == 400
    response_json = response.get_json()
    assert 'message' in response_json, f"Response JSON: {response_json}"
    assert response_json['message'] == 'Input payload validation failed', f"Unexpected message: {response_json['message']}"


def test_get_all_users(client, init_db):
    """Test the GET /blog/User/ endpoint."""
    client.post('/blog/User/', json={
        'username': 'tarun',
        'email': 'tarun@gmail.com'
    })

    response = client.get('/blog/User/')
    assert response.status_code == 200
    response_json = response.get_json()
    assert len(response_json) > 0, "No users found"
    assert response_json[0]['username'] == 'tarun'
    assert response_json[0]['email'] == 'tarun@gmail.com'


def test_get_user_by_id(client, init_db):
    """Test the GET /blog/User/<id> endpoint."""
    client.post('/blog/User/', json={
        'username': 'tarun',
        'email': 'tarun@gmail.com'
    })
    response = client.get('/blog/User/1')
    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['username'] == 'tarun'
    assert response_json['email'] == 'tarun@gmail.com'


def test_get_user_by_id_not_found(client, init_db):
    """Test the GET /blog/User/<id> endpoint for a non-existent user."""
    response = client.get('/blog/User/999')
    assert response.status_code == 404
    response_json = response.get_json()
    assert response_json['message'] == 'User not found'


def test_update_user(client, init_db):
    """Test the PUT /blog/User/<id> endpoint."""
    client.post('/blog/User/', json={
        'username': 'tarun',
        'email': 'tarun@gmail.com'
    })

    response = client.put('/blog/User/1', json={
        'username': 'tarun',
        'email': 'tarun_updated@gmail.com'
    })

    assert response.status_code == 200
    response_json = response.get_json()
    assert response_json['username'] == 'tarun'
    assert response_json['email'] == 'tarun_updated@gmail.com'


def test_delete_user(client, init_db):
    """Test the DELETE /blog/User/<id> endpoint."""
    client.post('/blog/User/', json={
        'username': 'tarun',
        'email': 'tarun@gmail.com'
    })

    response = client.delete('/blog/User/1')

    assert response.status_code == 204
    assert response.data == b''  # No content expected for a successful delete
