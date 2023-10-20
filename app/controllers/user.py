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
        data = request.get_json()
        if self.validate(data) is False:
            return self.handle_response("incomplete_data")
        try:
            user = self.load_user(data)
            session.add(user)
            session.commit()
            return self.handle_response("created", user.get_dict())
        except IntegrityError as error:
            session.rollback()
            print(f"ERROR: {error}!")
            return self.handle_response("exists")
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(f"ERROR: {error}!")
            return self.handle_response("error")

    def get(self, oid):
        """Show User."""
        try:
            user = session.query(UserModel).filter_by(id=oid).first()
            if not user:
                return self.handle_response("not_exist")
            return self.handle_response("found", user.get_dict())
        except Exception:  # pylint: disable=W0703
            session.rollback()
            return self.handle_response("error")

    def get_all(self):
        """Get User."""
        try:
            users = session.query(UserModel).all()
            array_users = []
            if not users:
                raise ValueError("No users found")
            for user in users:
                array_users.append(user.get_dict())
            return self.handle_response("found_all", None, array_users)
        except Exception:  # pylint: disable=W0703
            session.rollback()
            return self.handle_response("error")

    def update(self, oid):
        """Update User."""
        data = request.get_json()
        # call validate
        if self.validate(data) is False:
            return self.handle_response("incomplete_data")
        try:
            user = session.query(UserModel).filter_by(id=oid).first()
            if not user:
                return self.handle_response("not_exist")
            self.load_user(data, user)
            session.commit()
            return self.handle_response("updated", user.get_dict())
        except IntegrityError:
            session.rollback()
            return self.handle_response("exists")
        except Exception:  # pylint: disable=W0703
            session.rollback()
            return self.handle_response("error")

    def delete(self, oid):
        """Delete User."""
        try:
            user = session.query(UserModel).filter_by(id=oid).first()
            if not user:
                return self.handle_response("not_exist")
            session.delete(user)
            session.commit()
            return self.handle_response("deleted")
        except Exception:  # pylint: disable=W0703
            session.rollback()
            return self.handle_response("error")

    def validate(self, data):
        """Validate data."""
        array_data = ["username", "first_name", "last_name", "email"]
        for item in array_data:
            if item not in data:
                return False
        return True

    def load_user(self, data, user=None):
        """Load user."""
        if not user:
            user = UserModel()
        user.username = data["username"]
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        return user

    def handle_response(self, code, user=None, array_users=None):
        """Handle response."""
        response = ApiResponse()
        message = self.get_message_and_code(code)
        response.success = message["succes"]
        response.message = message["message"]
        if user is not None:
            response.data = user
        elif array_users is not None:
            response.data = array_users
        return jsonify(response.serialize()), message["http_code"]

    def get_message_and_code(self, code):
        """Get message."""
        message = {
            "incomplete_data":
            {
                "succes": False,
                "message": "Incomplete data",
                "http_code": 400
            },
            "created":
            {
                "succes": True,
                "message": "User created",
                "http_code": 201
            },
            "found":
            {
                "succes": True,
                "message": "User found",
                "http_code": 200
            },
            "exists":
            {
                "succes": False,
                "message": "User already exists",
                "http_code": 400
            },
            "not_exist":
            {
                "succes": False,
                "message": "User does not exist",
                "http_code": 404
            },
            "updated":
            {
                "succes": True,
                "message": "User updated",
                "http_code": 200
            },
            "deleted":
            {
                "succes": True,
                "message": "User deleted",
                "http_code": 200
            },
            "found_all":
            {
                "succes": True,
                "message": "Users found",
                "http_code": 200
            },
            "error":
            {
                "succes": False,
                "message": "Oops! Something happened",
                "http_code": 500
            }
        }
        return message[code]
