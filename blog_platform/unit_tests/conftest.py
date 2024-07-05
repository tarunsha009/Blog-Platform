# import pytest
# from blog_platform.config import config_by_name
# from blog_platform.manage import make_app
# from blog_platform.database.schemas import create_schema, drop_schema
# from blog_platform.core.database.db import db
# from blog_platform.core.database.models import User
# from blog_platform.services.user_services import UserService

# @pytest.fixture(scope='session')
# def app():
#     """Create and configure a new app instance for each test session."""
#     app = make_app('testing')
#     with app.app_context():
#         create_schema()
#         yield app
#         drop_schema()

# @pytest.fixture(scope='session')
# def client(app):
#     """Create a test client for the Flask app."""
#     return app.test_client()

# @pytest.fixture(scope='session')
# def init_db(app):
#     """Initialize the database for the test session."""
#     with app.app_context():
#         create_schema()
#         yield
#         drop_schema()

# @pytest.fixture(scope='session')
# def new_user(app, init_db):
#     """Create a new user for testing."""
#     user = User(username='testuser', password=UserService.generate_password_hash('password'), email='testuser@example.com')
#     with app.app_context():
#         db.session.add(user)
#         db.session.commit()
#     return user
