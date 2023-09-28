"""Main."""
# import requests
from flask import Flask, jsonify, request
from app.models.configuration import Configuration


def setup_routes(app: Flask):
    """Set routes."""
    app.add_url_rule("/webhook", "set_webhook", set_webhook, methods=["POST"])
    app.add_url_rule("/webhook", "get_webhook", get_webhook, methods=["GET"])
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])
    return app


def set_webhook():
    """Set webhook."""
    webhook_url = request.json.get("url")
    configuration = Configuration()
    configuration.name = "webhook_url"
    configuration.value = {"url": webhook_url}
    configuration.description = "Webhook URL"
    configuration.set()


def get_webhook():
    """Get webhook."""
    return jsonify({"url": "test"})


def hello_world():
    """Hello world."""
    return jsonify({"text": "Hello, World!"})
