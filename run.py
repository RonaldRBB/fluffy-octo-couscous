"""Main."""
# import requests
from flask import Flask, jsonify, request
from app.models.configuration import Configuration

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def set_webhook():
    """Set webhook."""
    webhook_url = request.json.get("url")
    configuration = Configuration()
    configuration.name = "webhook_url"
    configuration.value = {"url": webhook_url}
    configuration.description = "Webhook URL"
    configuration.set()


@app.route("/webhook", methods=["GET"])
def get_webhook():
    """Get webhook."""
    return jsonify({"url": "test"})


@app.route("/")
def hello_world():
    """Hello world."""
    return jsonify({"text": "Hello, World!"})


if __name__ == "__main__":
    app.run(port=3000)
