"""Webhook controller."""
import json

from flask import jsonify, request

from app.models.user import User as UserModel
from config import session


class User:
    """User controller."""
    @staticmethod
    def set():
        """Set User."""
        data = request.get_json()
        user = UserModel(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"]
        )
        session.add(user)
        session.commit()
        return jsonify({"text": "User created!"}), 200

    @staticmethod
    def get():
        """Get User."""
        data = request.get_json()
        user = session.query(UserModel).filter_by(id=data["id"]).first()
        return jsonify(user.get_dict()), 200


session.close()
