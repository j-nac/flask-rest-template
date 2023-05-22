from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource
from flask_jwt_extended import jwt_required

hello_bp = Blueprint('hello', __name__)
hello_api = Api(hello_bp)

class HelloWorld(Resource):
    def get(self):
        return {'message': 'hello world'}

class Protected(Resource):
    @jwt_required()
    def get(self):
        return {'message': 'jwt token is working'}

hello_api.add_resource(HelloWorld, '/')
hello_api.add_resource(Protected, '/protected')