# tests/test_user_service.py

from flask import Flask
from flask_jwt_extended import JWTManager, decode_token
import pytest
from unittest.mock import patch, MagicMock
from werkzeug.security import check_password_hash
from blog_platform.services.user_services import UserService
from blog_platform.utils.errors import BadRequestError, UnauthorizedError
from blog_platform.database_services.user_database_services import UserDBService
from werkzeug.security import generate_password_hash


@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "testpassword",
        "email": "testuser@example.com",
    }


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "testsecretkey"
    JWTManager(app)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@patch(
    "blog_platform.services.user_services.UserDBService.get_user_by_username")
@patch("blog_platform.services.user_services.UserDBService.create_user")
def test_register_user_success(mock_create_user, mock_get_user_by_username,
                               user_data):
    # Mock get_user_by_username to return None, indicating no existing user
    mock_get_user_by_username.return_value = None
    mock_create_user.return_value = MagicMock(id=1)

    response, status_code = UserService.register_user(user_data)

    assert status_code == 201
    assert response == {
        "message": "User registered successfully",
        "user_id": 1
    }


@patch(
    "blog_platform.services.user_services.UserDBService.get_user_by_username")
def test_register_user_existing_username(mock_get_user_by_username, user_data):
    # Mock get_user_by_username to return a user, indicating existing user
    mock_get_user_by_username.return_value = MagicMock()

    with pytest.raises(BadRequestError) as excinfo:
        UserService.register_user(user_data)

    assert "Username already exists" in str(excinfo.value)
    # assert str(excinfo.value) == "Username already exists"


@patch(
    "blog_platform.services.user_services.UserDBService.get_user_by_username")
def test_login_user_success(mock_get_user_by_username, user_data, mocker, app):
    with app.app_context():
        # Mock user data and password check
        hashed_password = generate_password_hash(user_data["password"],
                                                 method="scrypt")
        user = MagicMock(password=hashed_password)
        mock_get_user_by_username.return_value = user
        mocker.patch("werkzeug.security.check_password_hash",
                     return_value=True)
        mocker.patch("flask_jwt_extended.create_access_token",
                     return_value="testtoken")

        token = UserService.login_user(user_data["username"],
                                       user_data["password"])

        # Decode the token and verify its contents
        decoded_token = decode_token(token)
        assert decoded_token["sub"]["username"] == user_data["username"]


@patch(
    "blog_platform.services.user_services.UserDBService.get_user_by_username")
def test_login_user_invalid_password(mock_get_user_by_username, user_data,
                                     mocker):
    # Mock user data and password check
    user = MagicMock(password=user_data["password"])
    mock_get_user_by_username.return_value = user
    mocker.patch("werkzeug.security.check_password_hash", return_value=False)

    with pytest.raises(UnauthorizedError) as excinfo:
        UserService.login_user(user_data["username"], user_data["password"])

    assert "Invalid username or password" in str(excinfo.value)


@patch(
    "blog_platform.services.user_services.UserDBService.get_user_by_username")
def test_login_user_not_found(mock_get_user_by_username, user_data):
    # Mock get_user_by_username to return None, indicating user not found
    mock_get_user_by_username.return_value = None

    with pytest.raises(UnauthorizedError) as excinfo:
        UserService.login_user(user_data["username"], user_data["password"])

    assert "Invalid username or password" in str(excinfo.value)


@patch("blog_platform.services.user_services.redis_client.set")
def test_logout_user_success(mock_redis_set):
    token = "testtoken"

    UserService.logout_user(token)

    mock_redis_set.assert_called_once_with(token, "", ex=1)


def test_logout_user_missing_token():
    with pytest.raises(BadRequestError) as excinfo:
        UserService.logout_user(None)

    assert "Missing authorization token" in str(excinfo.value)
