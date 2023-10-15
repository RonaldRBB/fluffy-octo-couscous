"""App module"""
from flask import Flask
from app.routes.routes import setup_routes


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    setup_routes(app)
    return app
