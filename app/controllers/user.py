"""Webhook controller."""
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from app.models.user import User as UserModel
from config import session


class User:
    """User controller."""

    def create(self):
        """Create User."""
        data = request.get_json()
        # call validate
        if self.validate(data) is False:
            return jsonify("¡Datos incompletos!"), 400
        try:
            user = self.load_user(data)
            session.add(user)
            session.commit()
            return jsonify("¡Usuario Creado!"), 200
        except IntegrityError:
            session.rollback()
            return jsonify("¡Usuario ya existe!"), 400
        except Exception:
            session.rollback()
            return jsonify("¡Oops! Algo paso!"), 500

    def get(self, uid):
        """Show User."""
        try:
            user = session.query(UserModel).filter_by(id=uid).first()
            if not user:
                return jsonify("¡Usuario no existe!"), 404
            return jsonify(user.get_dict()), 200
        except Exception:
            session.rollback()
            return jsonify("¡Oops! Algo paso!"), 500

    def get_all(self):
        """Get User."""
        try:
            users = session.query(UserModel).all()
            array_users = []
            for user in users:
                array_users.append(user.get_dict())
            return jsonify(array_users), 200
        except Exception:
            session.rollback()
            return jsonify("¡Oops! Algo paso!"), 500

    def update(self, uid):
        """Update User."""
        data = request.get_json()
        # call validate
        if self.validate(data) is False:
            return jsonify("¡Datos incompletos!"), 400
        try:
            user = session.query(UserModel).filter_by(id=uid).first()
            if not user:
                return jsonify("¡Usuario no existe!"), 404
            user.username = data["username"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            session.commit()
            return jsonify("¡Usuario Actualizado!"), 200
        except IntegrityError:
            session.rollback()
            return jsonify("¡Usuario ya existe!"), 400
        except Exception:
            session.rollback()
            return jsonify("¡Oops! Algo paso!"), 500

    def delete(self, uid):
        """Delete User."""
        try:
            user = session.query(UserModel).filter_by(id=uid).first()
            if not user:
                return jsonify("¡Usuario no existe!"), 404
            session.delete(user)
            session.commit()
            return jsonify("¡Usuario Eliminado!"), 200
        except Exception:
            session.rollback()
            return jsonify("¡Oops! Algo paso!"), 500

    def validate(self, data):
        """Validate data."""
        array_data = ["username", "first_name", "last_name", "email"]
        for item in array_data:
            if item not in data:
                return False
        return True

    def load_user(self, data):
        """Load user."""
        user = UserModel(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"]
        )
        return user
