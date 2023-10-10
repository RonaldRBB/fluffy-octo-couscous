"""App module"""
from flask import Flask
from app.routes.routes import setup_routes


def create_app() -> Flask:
    """Create and configure an instance of the Flask application."""
    app: Flask = Flask(__name__)
    setup_routes(app)
    return app
