"""Main."""
# import requests
from flask import jsonify

from app.controllers.webhook import Webhook


def setup_routes(app):
    """Set routes."""
    app.add_url_rule("/webhook", "set_webhook", Webhook.set, methods=["POST"])
    app.add_url_rule("/webhook", "get_webhook", Webhook.get, methods=["GET"])
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])
    return app


def hello_world():
    """Hello world."""
    return jsonify({"text": "Hello World!"}), 200
