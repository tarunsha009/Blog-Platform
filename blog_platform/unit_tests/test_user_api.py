import pytest


def test_create_user(client, init_db):
    """Test the POST /blog/User/ endpoint."""
    response = client.post('/blog/User/', json={
        'username': 'tarun',
        'email': 'tarun@gmail.com'
    })

    assert response.status_code == 201
    response_json = response.get_json()
    print(response_json)
    assert response_json['username'] == 'tarun', f"Unexpected username: {response_json.get('username')}"
    assert response_json['email'] == 'tarun@gmail.com', f"Unexpected email: {response_json.get('email')}"


def test_create_user_invalid(client, init_db):
    """Test invalid data for the POST /blog/User/ endpoint."""
    response = client.post('/blog/User/', json={
        'username': 'tarun'
    })

    assert response.status_code == 400
    response_json = response.get_json()
    print(response_json)
    assert 'message' in response_json, f"Response JSON: {response_json}"
    assert response_json[
               'message'] == 'Input payload validation failed', f"Unexpected message: {response_json['message']}"
    # assert response_json['message'] == {'email': ['Missing data for required field.']}, f"Unexpected message: {response_json['message']}"
