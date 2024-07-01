import pytest
from blog_platform.config import config_by_name
from blog_platform.manage import make_app

@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test."""
    app = make_app('testing')  # or 'testing' for test-specific config
    yield app
    # Clean up after tests
    app.teardown_appcontext()

@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()
