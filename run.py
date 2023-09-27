"""Main."""
# import requests
from flask import Flask, jsonify, request
from core.models.configuration import Configuration

webhook_url = None
token = None

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def set_webhook():
    webhook_url = request.json.get("url")
    configuration = Configuration()
    configuration.name = "webhook_url"
    configuration.value = {"url": webhook_url}
    configuration.description = "Webhook URL"
    configuration.set()


@app.route("/webhook", methods=["GET"])
def get_webhook():
    return jsonify({"url": webhook_url})


@app.route("/")
def hello_world():
    return jsonify({"text": "Hello, World!"})


if __name__ == "__main__":
    app.run(port=3000)
