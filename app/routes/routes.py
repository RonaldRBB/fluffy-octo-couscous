"""Main."""
# import requests
from flask import Flask, jsonify

from app.controllers.webhook import Webhook


def setup_routes(app: Flask) -> Flask:
    """Set routes."""
    app.add_url_rule("/webhook", "set_webhook", Webhook.set, methods=["POST"])
    app.add_url_rule("/webhook", "get_webhook", Webhook.get, methods=["GET"])
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])
    return app


def hello_world() -> tuple[Flask.response_class, int]:
    """Hello world."""
    return jsonify({"text": "Marico el que lo lea!"}), 200
