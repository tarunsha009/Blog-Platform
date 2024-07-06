from functools import wraps
import logging
import logging.config

from blog_platform.api import api_v1
from flask import Flask, jsonify, request
from sqlalchemy_utils import create_database, database_exists
from blog_platform.config import config_by_name
from blog_platform.core.database.db import db
from flask_jwt_extended import JWTManager, decode_token

from blog_platform.utils.errors import UnauthorizedError
from blog_platform.services.user_services import blacklist
from blog_platform.utils.jwt_utils import setup_jwt
from blog_platform.utils.redis_client import redis_client  # Import the Redis client

def make_app(config_name=None):
    config = config_by_name[config_name]
    app = Flask(config.APP_NAME)
    setup_jwt(app)

    db_connection_uri = f"{config.DB_DIALECT}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_connection_uri
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        "pool_size": 30,
        "max_overflow": 15,
        "pool_recycle": 60,
        "pool_pre_ping": True
    }

    if not database_exists(db_connection_uri):
        create_database(db_connection_uri)

    db.init_app(app)
    app.config.from_object(config)
    app.register_blueprint(api_v1)

    with app.app_context():
        db.create_all()

    # @app.before_request
    # def handle_request():
    #     """Ensure the JWT token is valid for protected routes."""
    #     if request.endpoint and not is_public_endpoint():
    #         if not request.headers.get('Authorization'):
    #             raise UnauthorizedError("Missing authorization token")

    #         token = request.headers.get('Authorization').split(' ')[1]
    #         try:
    #             decode_token(token)
    #         except Exception as e:
    #             raise UnauthorizedError('Invalid token')
            
    #         # Check if the token is blacklisted
    #         if redis_client.get(token):
    #             raise UnauthorizedError("Token is blacklisted")

    # Define a protected route for testing
    @app.route('/protected', methods=['GET'])
    @token_required
    def protected():
        return {'message': 'This is a protected route'}

    return app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            raise UnauthorizedError("Missing authorization token")
        token = token.replace("Bearer ", "")
        if redis_client.get(token):
            raise UnauthorizedError("Token is blacklisted")
        # Add your JWT verification logic here
        return f(*args, **kwargs)
    return decorated

def is_public_endpoint():
    """Check if the current endpoint is public (no authentication required)."""
    public_endpoints = ['login', 'logout', 'register']
    return any(endpoint in request.endpoint for endpoint in public_endpoints)

def main():
    app = make_app('dev')
    host = "0.0.0.0"
    port = "5000"
    app.run(host=host, port=port, debug=False)

if __name__ == "__main__":
    main()
