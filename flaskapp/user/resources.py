from datetime import datetime
from flask_restful import Resource, reqparse
from flaskapp import db
from flaskapp.models import User
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
import re

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        user = db.session.execute(db.select(User).filter_by(email=args['email'])).scalar()
        if not user or not user.check_password(args['password'].encode('utf-8')):
            return {'message': 'Bad email or password'}, 401

        user.last_login_timestamp = datetime.now()
        db.session.commit()
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}

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

class Update(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('newPassword', type=str)
        parser.add_argument('newEmail', type=str)
        parser.add_argument('newUsername', type=str)
        parser.add_argument('newDescription', type=str)
        args = parser.parse_args()

        user = db.session.get(User, get_jwt_identity())

        if args['newPassword']:
            user.set_password(args['newPassword'])
        if args['newEmail'] and re.match(r'[^@]+@[^@]+\.[^@]+', args['newEmail']):
            user.email = args['newEmail']
        if args['newUsername']:
            user.username = args['newUsername']
        if args['newDescription']:
            user.description = args['newDescription']
        db.session.commit()

        return {'message': 'User information updated successfully'}

class Information(Resource):
    @jwt_required()
    def get(self):
        user = db.session.get(User, get_jwt_identity())
        return {
            'username': user.username,
            'email': user.email,
            'email_is_verified': user.email_is_verified,
            'account_created_timestamp': str(user.account_created_timestamp),
            'email_confirmed_timestamp': str(user.email_confirmed_timestamp),
            'last_login_timestamp': str(user.last_login_timestamp),
            'profile_picture': user.profile_picture,
            'description': user.description,
            'role': user.role,
        }

class Profile(Resource):
    def get(self, user_id):
        user = db.session.get(User, user_id)
        return {
            'username': user.username,
            'profile_picture': user.profile_picture,
            'description': user.description,
            'role': user.role,
        }