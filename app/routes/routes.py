"""Main."""
# import requests
from flask import jsonify

from app.controllers.user import User


def setup_routes(app):
    """Set routes."""
    app.add_url_rule("/user", "set_user", User.set, methods=["POST"])
    app.add_url_rule("/user", "get_user", User.get, methods=["GET"])
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])
    return app


def hello_world():
    """Hello world."""
    return jsonify({"text": "Hello World!"}), 200
