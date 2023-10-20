"""Main."""
# import requests
from flask import jsonify

from app.controllers.activity import Activity
from app.controllers.user import User


def setup_routes(app):
    """Set routes."""
    # Hello world
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])
    # User
    app.add_url_rule("/users", "get_users", User().get_all, methods=["GET"])
    app.add_url_rule("/user", "create_user", User().create, methods=["POST"])
    app.add_url_rule("/user/<int:oid>", "get_user", User().get, methods=["GET"])
    app.add_url_rule("/user/<int:oid>", "update_user", User().update, methods=["PUT"])
    app.add_url_rule("/user/<int:oid>", "delete_user", User().delete, methods=["DELETE"])
    # Activity
    app.add_url_rule("/activities", "get_activities", Activity().get_all, methods=["GET"])
    app.add_url_rule("/activity", "create_activity", Activity().create, methods=["POST"])
    app.add_url_rule("/activity/<int:oid>", "get_activity", Activity().get, methods=["GET"])
    app.add_url_rule("/activity/<int:oid>", "update_activity", Activity().update, methods=["PUT"])
    app.add_url_rule("/activity/<int:oid>", "delete_activity", Activity().delete, methods=["DELETE"])
    return app


def hello_world():
    """Hello world."""
    return jsonify({"Hello World!"}), 200
