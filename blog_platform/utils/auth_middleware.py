# auth_middleware.py

from flask_jwt_extended import jwt_required


def protected():
    """Protect routes with JWT authentication."""
    return jwt_required()
