"""Webhook controller."""
from flask import jsonify, request
from app.models.configuration import Configuration
from config import session


class Webhook:
    """Webhook controller."""
    @staticmethod
    def set():
        """Set webhook."""
        if not request.json:
            return jsonify({"error": "No JSON data."}), 400
        if "url" not in request.json:
            return jsonify({"error": "No URL provided."}), 400
        webhook_url = request.json.get("url")
        configuration = Configuration()
        configuration.name = "webhook_url"
        configuration.value = {"url": webhook_url}
        configuration.description = "Telegram Webhook URL"
        configuration.set()
        # return 200
        return jsonify({"message": "Webhook URL set."}), 200

    @staticmethod
    def get():
        """Get webhook."""
        session = Session()
        # configuration = (
        # session.query(Configuration)
        # .filter(Configuration._name == "webhook_url")
        # .first()
        # )
        # session.close()
        # return jsonify(configuration.value)
        configuration = Configuration()
        recordset = configuration.get()
        for record in recordset:
            # print(record)
            print(record.id)
            print(record.value)
        session.close()
        return jsonify("test"), 200
