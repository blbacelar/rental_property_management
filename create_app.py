import os

from dotenv import load_dotenv
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt = JWTManager(app)

    from routes.property_routes import property_bp
    app.register_blueprint(property_bp, url_prefix='/api')

    from routes.import_routes import import_bp
    app.register_blueprint(import_bp, url_prefix='/api')

    from routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    from routes.tenant_routes import tenant_bp
    app.register_blueprint(tenant_bp, url_prefix='/api')

    return app
