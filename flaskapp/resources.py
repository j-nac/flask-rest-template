from flask_restful import Resource, reqparse
from flaskapp import api, db, bcrypt
from flaskapp.models import User

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Need to add more input validation for security
class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True)
        parser.add_argument('password', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('profile_picture')
        parser.add_argument('description')
        args = parser.parse_args()

        user = User(username=args['username'], email=args['email'], profile_picture=args['profile_picture'], description=args['description'])
        user.set_password(args['password'])
        db.session.add(user)
        db.session.commit()

        return {'message': f'User {user.username} has been successfully created'}

api.add_resource(HelloWorld, '/')
api.add_resource(Register, '/register')