import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    # force instance folder to be 'backend/instance'
    instance_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'instance'))

    app = Flask(__name__, instance_path=instance_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['JWT_SECRET_KEY'] = 'supersecret'
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from .routes import api
    app.register_blueprint(api)

    return app



