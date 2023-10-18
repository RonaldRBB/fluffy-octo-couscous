"""Webhook controller."""
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from app.controllers.controller import Controller
from app.helpers.response import ApiResponse
from app.models.user import User as UserModel
from config import session


class User(Controller):
    """User controller."""

    def create(self):
        """Create User."""
        response = ApiResponse()
        data = request.get_json()
        if self.validate(data) is False:
            response.message = "Incomplete data"
            return jsonify(response.serialize()), 400
        try:
            user = self.load_user(data)
            session.add(user)
            session.commit()
            response.success = True
            response.message = "User created"
            response.data = user.get_dict()
            return jsonify(response.serialize()), 201
        except IntegrityError:
            session.rollback()
            response.message = "User already exists"
            return jsonify(response.serialize()), 400
        except Exception:
            session.rollback()
            response.message = "Oops! Something happened"
            return jsonify(response.serialize()), 500

    def get(self, oid):
        """Show User."""
        response = ApiResponse()
        try:
            user = session.query(UserModel).filter_by(id=oid).first()
            if not user:
                response.message = "User does not exist"
                return jsonify(response.serialize()), 404
            response.success = True
            response.message = "User found"
            response.data = user.get_dict()
            return jsonify(response.serialize()), 200
        except Exception:
            session.rollback()
            response.message = "Oops! Something happened"
            return jsonify(response.serialize()), 500

    def get_all(self):
        """Get User."""
        response = ApiResponse()
        try:
            users = session.query(UserModel).all()
            array_users = []
            for user in users:
                array_users.append(user.get_dict())
            response.success = True
            response.message = "Users found"
            response.data = array_users
            return jsonify(response.serialize()), 200
        except Exception:
            session.rollback()
            response.message = "Oops! Something happened"
            return jsonify(response.serialize()), 500

    def update(self, oid):
        """Update User."""
        response = ApiResponse()
        data = request.get_json()
        # call validate
        if self.validate(data) is False:
            response.message = "Incomplete data"
            return jsonify(response.serialize()), 400
        try:
            user = session.query(UserModel).filter_by(id=oid).first()
            if not user:
                response.message = "User does not exist"
                return jsonify(response.serialize()), 404
            self.load_user(data, user)
            session.commit()
            response.success = True
            response.message = "User updated"
            response.data = user.get_dict()
            return jsonify(response.serialize()), 200
        except IntegrityError:
            session.rollback()
            response.message = "User already exists"
            return jsonify(response.serialize()), 400
        except Exception:
            session.rollback()
            response.message = "Oops! Something happened"
            return jsonify(response.serialize()), 500

    def delete(self, oid):
        """Delete User."""
        response = ApiResponse()
        try:
            user = session.query(UserModel).filter_by(id=oid).first()
            if not user:
                response.message = "User does not exist"
                return jsonify(response.serialize()), 404
            session.delete(user)
            session.commit()
            response.success = True
            response.message = "User deleted"
            return jsonify(response.serialize()), 200
        except Exception:
            session.rollback()
            response.message = "Oops! Something happened"
            return jsonify(response.serialize()), 500

    def validate(self, data):
        """Validate data."""
        array_data = ["username", "first_name", "last_name", "email"]
        for item in array_data:
            if item not in data:
                return False
        return True

    def load_user(self, data, user=None):
        """Load user."""
        if user is not None:
            user.username = data["username"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
        else:
            user = UserModel(
                username=data["username"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"]
            )
            return user
