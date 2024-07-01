from flask import Blueprint
from flask_restx import Api
from blog_platform.api.v1.user import api as v1_user
from blog_platform.api.v1.post import post_ns as v1_post



api_v1 = Blueprint("api_v1", __name__, url_prefix="/blog")
api = Api(api_v1, version="1.0", title="Blog APIs", description="Blog Platform")

api.add_namespace(v1_user)
api.add_namespace(v1_post)