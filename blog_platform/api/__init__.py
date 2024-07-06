# blog_platform/api/__init__.py
from flask import Blueprint
from flask_restx import Api
from blog_platform.api.v1.user import api as v1_user
from blog_platform.api.v1.blog_post import api as v1_post
from blog_platform.api.v1.auth import api as v1_auth
from blog_platform.utils.error_handlers import register_error_handlers

api_v1 = Blueprint("api_v1", __name__, url_prefix="/blog")
api = Api(api_v1,
          version="1.0",
          title="Blog APIs",
          description="Blog Platform",
          doc="/doc/")

api.add_namespace(v1_user)
api.add_namespace(v1_post)
api.add_namespace(v1_auth)

register_error_handlers(api)
