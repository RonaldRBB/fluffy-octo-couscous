"""Abstract class controller"""
from datetime import datetime

from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from app.helpers.response import ApiResponse
from config import session


class Controller:
    """Abstract class controller."""
    model = None
    model_params = None

    def create(self):
        """Create"""
        request_data = request.get_json()
        if self.validate(request_data) is False:
            return self.handle_response("incomplete_data")
        try:
            data = self.load_data(request_data)
            session.add(data)
            session.commit()
            return self.handle_response("created", data.get_dict())
        except IntegrityError as error:
            session.rollback()
            if "Duplicate entry" in str(error):
                return self.handle_response("exists")
            elif "Cannot add or update a child row" in str(error):
                return self.handle_response("foreign_key")
            return self.handle_response("error")
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(error)
            return self.handle_response("error")

    def get(self, oid):
        """Get"""
        try:
            data = session.query(self.model).filter_by(id=oid).first()
            if not data:
                return self.handle_response("not_exist")
            return self.handle_response("found", data.get_dict())
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(error)
            return self.handle_response("error")

    def get_all(self):
        """Get all"""
        try:
            data = session.query(self.model).all()
            array_data = []
            if not data:
                raise ValueError(f"No {self.__class__.__name__}s found")
            for item in data:
                array_data.append(item.get_dict(with_user=False))
            return self.handle_response("found_all", array_data)
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(error)
            return self.handle_response("error")

    def update(self, oid):
        """Update"""
        request_data = request.get_json()
        if self.validate(request_data) is False:
            return self.handle_response("incomplete_data")
        try:
            data = session.query(self.model).filter_by(id=oid).first()
            if not data:
                return self.handle_response("not_exist")
            self.load_data(request_data, data)
            session.commit()
            return self.handle_response("updated", data.get_dict())
        except IntegrityError as error:
            session.rollback()
            if "Duplicate entry" in str(error):
                return self.handle_response("exists")
            elif "Cannot add or update a child row" in str(error):
                return self.handle_response("foreign_key")
            return self.handle_response("error")
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(error)
            return self.handle_response("error")

    def delete(self, oid):
        """Delete"""
        try:
            data = session.query(self.model).filter_by(id=oid).first()
            json_data = data.get_dict()
            if not data:
                return self.handle_response("not_exist")
            session.delete(data)
            session.commit()
            return self.handle_response("deleted", json_data)
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(error)
            return self.handle_response("error")

    def validate(self, data):
        """Validate data."""
        if data is None:
            return False
        for param in self.model_params:
            if param not in data:
                return False
        return True

    def load_data(self, data, model=None):
        """Load data."""
        if model is None:
            model = self.model()
        for param in self.model_params:
            if param == "date" and data[param] is not None:
                setattr(model, param, datetime.strptime(
                    data[param], '%Y-%m-%d %H:%M:%S'))
            else:
                setattr(model, param, data[param])
        return model

    def handle_response(self, code, data=None):
        """Handle response."""
        response = ApiResponse()
        message = self.get_message_and_code(code)
        response.success = message["succes"]
        response.message = message["message"]
        if data is not None:
            response.data = data
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
                "message": f"{self.__class__.__name__}(s) created",
                "http_code": 201
            },
            "found":
            {
                "succes": True,
                "message": f"{self.__class__.__name__}(s) found",
                "http_code": 200
            },
            "exists":
            {
                "succes": False,
                "message": f"{self.__class__.__name__}(s) already exists",
                "http_code": 400
            },
            "not_exist":
            {
                "succes": False,
                "message": f"{self.__class__.__name__}(s) does not exist",
                "http_code": 404
            },
            "updated":
            {
                "succes": True,
                "message": f"{self.__class__.__name__}(s) updated",
                "http_code": 200
            },
            "deleted":
            {
                "succes": True,
                "message": f"{self.__class__.__name__}(s) deleted",
                "http_code": 200
            },
            "found_all":
            {
                "succes": True,
                "message": f"{self.__class__.__name__}(s) found",
                "http_code": 200
            },
            "error":
            {
                "succes": False,
                "message": "Oops! Something happened",
                "http_code": 500
            },
            "foreign_key":
            {
                "succes": False,
                "message": "Foreign key does not exist",
                "http_code": 400
            }
        }
        return message[code]
