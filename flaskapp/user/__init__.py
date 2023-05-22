from flask import Blueprint
from flask_restful import Api

user_bp = Blueprint('user', __name__)
user_api = Api(user_bp)

from flaskapp.user.resources import Login, Register, Update, Information, Profile

user_api.add_resource(Login, '/login')
user_api.add_resource(Register, '/register')
user_api.add_resource(Update, '/update')
user_api.add_resource(Information, '/information')
user_api.add_resource(Profile, '/<string:user_id>')