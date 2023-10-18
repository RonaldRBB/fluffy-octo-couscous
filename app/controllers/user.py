"""Webhook controller."""
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from app.models.user import User as UserModel
from config import session


class User:
    """User controller."""
    @staticmethod
    def set():
        """Set User."""
        data = request.get_json()
        # call validate
        if User.validate(data) is False:
            return jsonify("¡Datos incompletos!"), 400
        try:
            user = UserModel(*data.values())
            session.add(user)
            session.commit()
            return jsonify("¡Usuario Creado!"), 200
        except IntegrityError:
            session.rollback()
            return jsonify("¡Usuario ya existe!"), 400
        except Exception:
            session.rollback()
            return jsonify("¡Oops! Algo paso!"), 500

    @staticmethod
    def validate(data):
        """Validate data."""
        array_data = ["username", "first_name", "last_name", "email"]
        for item in array_data:
            if item not in data:
                return False
        return True

    @staticmethod
    def get(uid):
        """Get User."""
        try:
            user = session.query(UserModel).filter_by(id=uid).first()
            if not user:
                return jsonify("¡Usuario no existe!"), 404
            return jsonify(user.get_dict()), 200
        except Exception:
            session.rollback()
            return jsonify("¡Oops! Algo paso!"), 500
