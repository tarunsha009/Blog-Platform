# import pytest
# from blog_platform.services.user_services import UserServices
#
#
# @pytest.fixture
# def user_services():
#     return UserServices()
#
#
# def test_get_all_users(user_services, mocker):
#     """Test get_all_users method."""
#     mock_user_db_services = mocker.patch('blog_platform.database_services.user_database_services.UserDatabaseServices')
#     mock_user_db_services.get_all_users.return_value = [{'id': 1, 'username': 'tarun', 'email': 'tarun@gmail.com'}]
#
#     result = user_services.get_all_users()
#     assert len(result) == 1
#     assert result[0]['username'] == 'tarun'
#
#
# def test_add_user(user_services, mocker):
#     """Test add_user method."""
#     mock_user_db_services = mocker.patch('blog_platform.database_services.user_database_services.UserDatabaseServices')
#     mock_user_db_services.add_user.return_value = {'username': 'tarun', 'email': 'tarun@gmail.com'}
#
#     data = {'username': 'tarun', 'email': 'tarun@gmail.com'}
#     result = user_services.add_user(data)
#     assert result['username'] == 'tarun'
#     assert result['email'] == 'tarun@gmail.com'
#
#
# def test_get_user_by_id(user_services, mocker):
#     """Test get_user_by_id method."""
#     mock_user_db_services = mocker.patch('blog_platform.database_services.user_database_services.UserDatabaseServices')
#     mock_user_db_services.get_user_by_id.return_value = {'id': 1, 'username': 'tarun', 'email': 'tarun@gmail.com'}
#
#     result = user_services.get_user_by_id(1)
#     assert result['username'] == 'tarun'
#     assert result['email'] == 'tarun@gmail.com'
#
#
# def test_update_user(user_services, mocker):
#     """Test update_user method."""
#     mock_user_db_services = mocker.patch('blog_platform.database_services.user_database_services.UserDatabaseServices')
#     mock_user_db_services.update_user.return_value = {'id': 1, 'username': 'tarun', 'email': 'tarun_updated@gmail.com'}
#
#     data = {'username': 'tarun', 'email': 'tarun_updated@gmail.com'}
#     result = user_services.update_user(1, data)
#     assert result['email'] == 'tarun_updated@gmail.com'
#
#
# def test_delete_user(user_services, mocker):
#     """Test delete_user method."""
#     mock_user_db_services = mocker.patch('blog_platform.database_services.user_database_services.UserDatabaseServices')
#     mock_user_db_services.delete_user.return_value = None
#
#     result = user_services.delete_user(1)
#     assert result is None
