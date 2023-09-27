import requests
from flask import Flask, jsonify, request

webhook_url = None
token = None

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def set_webhook():
    webhook_url = request.json.get("url")
    print(f"URL: {webhook_url}")
    # telegram_api = "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook"
    # response = requests.post(telegram_api, data={"url": url})
    return jsonify("eres un puto crack")


@app.route("/webhook", methods=["GET"])
def get_webhook():
    return jsonify({"url": webhook_url})


@app.route("/")
def hello_world():
    return jsonify({"text": "Hello, World!"})


if __name__ == "__main__":
    app.run(port=3000)
