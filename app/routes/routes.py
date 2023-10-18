"""Main."""
# import requests
from flask import jsonify

from app.controllers.user import User


def setup_routes(app):
    """Set routes."""
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])
    app.add_url_rule("/users", "get_users", User().get_all, methods=["GET"])
    app.add_url_rule("/user", "create_user", User().create, methods=["POST"])
    app.add_url_rule("/user/<int:uid>", "get_user", User().get, methods=["GET"])
    app.add_url_rule("/user/<int:uid>", "update_user", User().update, methods=["PUT"])
    app.add_url_rule("/user/<int:uid>", "delete_user", User().delete, methods=["DELETE"])
    return app


def hello_world():
    """Hello world."""
    return jsonify({"Hello World!"}), 200
