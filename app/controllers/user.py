"""Webhook controller."""
from flask import jsonify, request

from app.models.user import User as UserModel
from config import session


class User:
    """User controller."""
    @staticmethod
    def set():
        """Set User."""
        data = request.get_json()
        # id, username, first_name, last_name, email, gen_date
        user = UserModel(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"]
        )
        session.add(user)
        session.commit()
        session.close()
        return jsonify({"text": "User created!"}), 200
