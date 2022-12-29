from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt

# Set up dependencies
db = SQLAlchemy()
api = Api()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('flaskapp.config.DevelopmentConfig')

    # Resources must be added before api.init_app
    from flaskapp import resources

    db.init_app(app)
    api.init_app(app)
    bcrypt.init_app(app)

    # Set up database
    from flaskapp import models
    with app.app_context():
        db.create_all()
    
    # Import blueprints like below
    # from flaskapp.app import app_blueprint
    # app.register_blueprint(app_blueprint, url_prefix='/app')

    return app