# Blog_platform/conftest.py
import pytest
from blog_platform.config import config_by_name
from blog_platform.manage import make_app
from blog_platform.database.schemas import create_schema, drop_schema

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test."""
    app = make_app('testing')  # or 'testing' for test-specific config
    with app.app_context():
        create_schema()
    yield app
    with app.app_context():
        drop_schema()
    # Clean up after tests
    app.teardown_appcontext()

@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()

@pytest.fixture
def init_db(app):
    """Initialize the database."""
    with app.app_context():
        create_schema()
    yield
    with app.app_context():
        drop_schema()
