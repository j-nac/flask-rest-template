from flask_restful import Resource, reqparse
from flaskapp import api, db
from flaskapp.models import User
import re

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('profile_picture', type=str)
        parser.add_argument('description', type=str)
        args = parser.parse_args()

        if not re.match(r'[^@]+@[^@]+\.[^@]+', args['email']):
            return {'message': 'Invalid email format.'}, 400

        user = User(username=args['username'], email=args['email'], profile_picture=args['profile_picture'], description=args['description'])
        user.set_password(args['password'])
        db.session.add(user)
        db.session.commit()

        return {'message': f'User {user.username} has been successfully created'}

api.add_resource(HelloWorld, '/')
api.add_resource(Register, '/register')