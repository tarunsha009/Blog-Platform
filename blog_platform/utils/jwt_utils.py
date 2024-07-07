from flask_jwt_extended import JWTManager
from blog_platform.utils.redis_client import redis_client


def setup_jwt(app):
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return redis_client.get(jti) is not None
