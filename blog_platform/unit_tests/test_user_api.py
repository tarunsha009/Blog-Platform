# import pytest
#
#
# def test_create_user(client, init_db):
#     """Test the POST /blog/User/ endpoint."""
#     response = client.post('/blog/User/', json={
#         'username': 'tarun',
#         'email': 'tarun@gmail.com'
#     })
#
#     assert response.status_code == 201
#     response_json = response.get_json()
#     print(response_json)
#     assert response_json['username'] == 'tarun', f"Unexpected username: {response_json.get('username')}"
#     assert response_json['email'] == 'tarun@gmail.com', f"Unexpected email: {response_json.get('email')}"
#
#
# def test_create_user_invalid(client, init_db):
#     """Test invalid data for the POST /blog/User/ endpoint."""
#     response = client.post('/blog/User/', json={
#         'username': 'tarun'
#     })
#
#     assert response.status_code == 400
#     response_json = response.get_json()
#     print(response_json)
#     assert 'message' in response_json, f"Response JSON: {response_json}"
#     assert response_json[
#                'message'] == 'Input payload validation failed', f"Unexpected message: {response_json['message']}"
#     # assert response_json['message'] == {'email': ['Missing data for required field.']}, f"Unexpected message: {response_json['message']}"
#
#
# def test_get_all_users(client, init_db):
#     """Test the GET /blog/User/ endpoint."""
#     client.post('/blog/User/', json={
#         'username': 'tarun',
#         'email': 'tarun@gmail.com'
#     })
#
#     response = client.get('/blog/User/')
#     assert response.status_code == 200
#     response_json = response.get_json()
#     assert len(response_json) > 0, "No users found"
#     assert response_json[0]['username'] == 'tarun'
#     assert response_json[0]['email'] == 'tarun@gmail.com'
#
#
# def test_get_user_by_id_with_mock(client, mock_user_services):
#     """Test the GET /blog/User/<id> endpoint with a mock."""
#     # Mock the `get_user_by_id` method in the `UserServices` class
#     mock_user_services.get_user_by_id.return_value = {'id': 1, 'username': 'tarun', 'email': 'tarun@gmail.com'}
#
#     response = client.get('/blog/User/1')
#
#     assert response.status_code == 200
#     response_json = response.get_json()
#     assert response_json['id'] == 1
#     assert response_json['username'] == 'tarun'
#     assert response_json['email'] == 'tarun@gmail.com'
#
#
# def test_get_user_by_id_not_found_with_mock(client, mock_user_services):
#     """Test the GET /blog/User/<id> endpoint with a mock for not found."""
#     # Mock the `get_user_by_id` method in the `UserServices` class
#     mock_user_services.get_user_by_id.return_value = None
#
#     response = client.get('/blog/User/999')
#
#     assert response.status_code == 404
#     response_json = response.get_json()
#     assert response_json['message'] == 'User not found'
#
#
# def test_update_user_with_mock(client, mock_user_services):
#     """Test the PUT /blog/User/<id> endpoint with a mock."""
#     # Mock the `update_user` method in the `UserServices` class
#     mock_user_services.update_user.return_value = {'id': 1, 'username': 'tarun', 'email': 'tarun_updated@gmail.com'}
#
#     response = client.put('/blog/User/1', json={
#         'username': 'tarun',
#         'email': 'tarun_updated@gmail.com'
#     })
#
#     assert response.status_code == 200
#     response_json = response.get_json()
#     assert response_json['username'] == 'tarun'
#     assert response_json['email'] == 'tarun_updated@gmail.com'
#
#
# def test_delete_user_with_mock(client, mock_user_services):
#     """Test the DELETE /blog/User/<id> endpoint with a mock."""
#     # Mock the `delete_user` method in the `UserServices` class
#     mock_user_services.delete_user.return_value = None
#
#     response = client.delete('/blog/User/1')
#
#     assert response.status_code == 204
#     assert response.data == b''  # No content expected for a successful delete
