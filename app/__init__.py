# app/__init__.py

from flask import Flask
from .routes import app as flask_app  # Correct relative import for the Blueprint

def create_app():
    # Create the Flask application instance inside a function
    app = Flask(__name__)
    # Set a secret key for session management
    app.secret_key = 'blackrock-secret'

    # Register the Blueprint from app/routes.py
    app.register_blueprint(flask_app)
    
    return app
