from flask import Response, request
from flask_restx import Namespace, Resource, fields

post_ns = Namespace('posts', description='Post operations')

post_model = post_ns.model('Post', {
    'id': fields.Integer(readOnly=True, description='The post unique identifier'),
    'title': fields.String(required=True, description='The post title'),
    'content': fields.String(required=True, description='The post content'),
    'user_id': fields.Integer(required=True, description='The user identifier')
})

@post_ns.route('/')
class PostList(Resource):
    @post_ns.doc('list_posts')
    @post_ns.marshal_list_with(post_model)
    def get(self):
        '''List all posts'''
        # return Post.query.all()
        return True

    @post_ns.doc('create_post')
    @post_ns.expect(post_model)
    @post_ns.marshal_with(post_model, code=201)
    def post(self):
        '''Create a new post'''
        # data = request.json
        # new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
        # db.session.add(new_post)
        # db.session.commit()
        # return new_post, 201
        return "Success", 201