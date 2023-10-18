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
        user = UserModel(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"]
        )
        try:
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
