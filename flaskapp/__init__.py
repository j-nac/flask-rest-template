from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt import JWT

# Set up dependencies
db = SQLAlchemy()
api = Api()
bcrypt = Bcrypt()
jwt = JWT()

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    bcrypt.init_app(app)

    # Set up database
    db.init_app(app)
    from flaskapp import models
    with app.app_context():
        db.create_all()
    
    # Add jwt
    from flaskapp.auth import authenticate, identity
    jwt.authentication_handler(authenticate)
    jwt.identity_handler(identity)
    jwt.init_app(app)
    
    # Resources must be added before api.init_app
    from flaskapp import resources
    api.init_app(app)
    
    # Import blueprints like below
    # from flaskapp.app import app_blueprint
    # app.register_blueprint(app_blueprint, url_prefix='/app')

    return app