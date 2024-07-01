import pytest
from blog_platform.services.user_services import UserServices


def test_create_user_with_mock(client, mocker):
    """Test the POST /blog/User/ endpoint using mock."""
    # Mock the `add_user` method in the `UserServices` class
    mock_add_user = mocker.patch.object(UserServices, 'add_user',
                                        return_value={'username': 'tarun', 'email': 'tarun@gmail.com'})

    response = client.post('/blog/User/', json={
        'username': 'tarun',
        'email': 'tarun@gmail.com'
    })

    assert response.status_code == 201
    assert response.json['username'] == 'tarun'
    assert response.json['email'] == 'tarun@gmail.com'
    mock_add_user.assert_called_once_with({'username': 'tarun', 'email': 'tarun@gmail.com'})


def test_create_user_invalid(client):
    """Test the POST /blog/User/ endpoint with invalid data."""
    response = client.post('/blog/User/', json={
        'username': 'tarun'
    })
    assert response.status_code == 400
    assert 'email' in response.json['message']


def test_get_all_users_with_mock(client, mocker):
    """Test the GET /blog/User/ endpoint using mock."""
    # Mock the `get_all_users` method in the `UserServices` class
    mock_get_all_users = mocker.patch.object(UserServices, 'get_all_users', return_value=[
        {'id': 1, 'username': 'existing_user', 'email': 'existing_user@example.com'}
    ])

    response = client.get('/blog/User/')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['username'] == 'existing_user'
    mock_get_all_users.assert_called_once()


def test_get_user_by_id_with_mock(client, mocker):
    """Test the GET /blog/User/<id> endpoint using mock."""
    # Mock the `get_user_by_id` method in the `UserServices` class
    mock_get_user_by_id = mocker.patch.object(UserServices, 'get_user_by_id',
                                              return_value={'id': 1, 'username': 'existing_user',
                                                            'email': 'existing_user@example.com'})

    response = client.get('/blog/User/1')

    assert response.status_code == 200
    assert response.json['username'] == 'existing_user'
    assert response.json['email'] == 'existing_user@example.com'
    mock_get_user_by_id.assert_called_once_with(1)


def test_get_user_by_id_not_found_with_mock(client, mocker):
    """Test the GET /blog/User/<id> endpoint with a non-existent user using mock."""
    # Mock the `get_user_by_id` method in the `UserServices` class to raise a `ValueError`
    mock_get_user_by_id = mocker.patch.object(UserServices, 'get_user_by_id', side_effect=ValueError('User not found'))

    response = client.get('/blog/User/999')

    assert response.status_code == 404
    assert response.json['message'] == 'User not found'
    mock_get_user_by_id.assert_called_once_with(999)


def test_update_user_with_mock(client, mocker):
    """Test the PUT /blog/User/<id> endpoint using mock."""
    # Mock the `update_user` method in the `UserServices` class
    mock_update_user = mocker.patch.object(UserServices, 'update_user', return_value={'username': 'updated_user',
                                                                                      'email': 'updated_user@example.com'})

    response = client.put('/blog/User/1', json={
        'username': 'updated_user',
        'email': 'updated_user@example.com'
    })

    assert response.status_code == 200
    assert response.json['username'] == 'updated_user'
    assert response.json['email'] == 'updated_user@example.com'
    mock_update_user.assert_called_once_with(1, {'username': 'updated_user', 'email': 'updated_user@example.com'})


def test_delete_user_with_mock(client, mocker):
    """Test the DELETE /blog/User/<id> endpoint using mock."""
    # Mock the `delete_user` method in the `UserServices` class
    mock_delete_user = mocker.patch.object(UserServices, 'delete_user', return_value=None)

    response = client.delete('/blog/User/1')

    assert response.status_code == 204
    mock_delete_user.assert_called_once_with(1)
