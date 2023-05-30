from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Set up dependencies
db = SQLAlchemy()
api = Api()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    bcrypt.init_app(app)

    # Set up database
    db.init_app(app)
    from flaskapp import models
    with app.app_context():
        db.create_all()
    
    jwt.init_app(app)
    
    # Import blueprints
    from flaskapp.hello import hello_bp
    from flaskapp.user import user_bp

    app.register_blueprint(hello_bp, url_prefix='')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
