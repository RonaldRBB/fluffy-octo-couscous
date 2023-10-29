"""Abstract class controller"""
import io
from datetime import datetime

import pandas as pd
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from app.helpers.response import ApiResponse
from config import session
from app.models import User


class Controller:
    """Abstract class controller."""
    model = None
    model_params = []
    data_conversion = {}

    def create(self):
        """Create"""
        request_data = request.get_json()
        print(" * request_data:", request_data)
        if self.validate(request_data) is False:
            return self.handle_response("incomplete_data")
        try:
            data = self.load_data(request_data)
            session.add(data)
            session.commit()
            return self.handle_response("created", data.get_dict())
        except IntegrityError as error:
            session.rollback()
            print(f" * {error}")
            if "Duplicate entry" in str(error):
                return self.handle_response("exists")
            elif "Cannot add or update a child row" in str(error):
                return self.handle_response("foreign_key")
            return self.handle_response("error")
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(f" * {error}")
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
            print(f" * {error}")
            return self.handle_response("error")

    def get_all(self):
        """Get all"""
        try:
            data = session.query(self.model).all()
            array_data = []
            if not data:
                raise ValueError(f"No {self.__class__.__name__}s found")
            for item in data:
                array_data.append(item.get_dict(with_relation=False))
            return self.handle_response("found_all", array_data)
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(f" * {error}")
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
            print(f" * {error}")
            if "Duplicate entry" in str(error):
                return self.handle_response("exists")
            elif "Cannot add or update a child row" in str(error):
                return self.handle_response("foreign_key")
            return self.handle_response("error")
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(f" * {error}")
            return self.handle_response("error")

    def delete(self, oid):
        """Delete"""
        try:
            data = session.query(self.model).filter_by(id=oid).first()
            if not data:
                return self.handle_response("not_exist")
            json_data = data.get_dict()
            session.delete(data)
            session.commit()
            return self.handle_response("deleted", json_data)
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(f" * {error}")
            return self.handle_response("error")

    def store_file_data(self):
        """Store file data."""
        user_id = request.form.get("user_id")
        user = session.query(User).filter_by(id=user_id).first()
        if not user:
            return self.handle_response("not_exist", class_name="User")
        uploaded_file = request.files["file"]
        data = uploaded_file.read()
        data = pd.read_csv(io.BytesIO(data))
        try:
            for row in data.itertuples():
                model = self.model()
                model.user_id = user_id
                print(f" * {row}")
                for key, data_conversion_key in self.data_conversion.items():
                    setattr(model, data_conversion_key, getattr(row, key))
                session.add(model)
            session.commit()
        except IntegrityError as error:
            session.rollback()
            print(f" * {error}")
            if "Duplicate entry" in str(error):
                return self.handle_response("exists")
            elif "Cannot add or update a child row" in str(error):
                return self.handle_response("foreign_key")
            return self.handle_response("error")
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(f" * {error}")
            return self.handle_response("error")
        return self.handle_response("file received")

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
            if param in ["date", "start_time", "birth_date"] and data[param] is not None:
                setattr(model, param, datetime.strptime(
                    data[param], '%Y-%m-%d %H:%M:%S'))
            else:
                setattr(model, param, data[param])
        return model

    def handle_response(self, code, data=None, class_name=None):
        """Handle response."""
        response = ApiResponse()
        message = self.get_message_and_code(code, class_name)
        response.success = message["success"]
        response.message = message["message"]
        if data is not None:
            response.data = data
        return jsonify(response.serialize()), message["http_code"]

    def get_message_and_code(self, code, class_name=None):
        """Get message."""
        if class_name is None:
            class_name = self.__class__.__name__
        message = {
            "incomplete_data":
            {
                "success": False,
                "message": "Incomplete data",
                "http_code": 400
            },
            "created":
            {
                "success": True,
                "message": f"{class_name}(s) created",
                "http_code": 201
            },
            "found":
            {
                "success": True,
                "message": f"{class_name}(s) found",
                "http_code": 200
            },
            "exists":
            {
                "success": False,
                "message": f"{class_name}(s) already exists",
                "http_code": 400
            },
            "not_exist":
            {
                "success": False,
                "message": f"{class_name}(s) does not exist",
                "http_code": 404
            },
            "updated":
            {
                "success": True,
                "message": f"{class_name}(s) updated",
                "http_code": 200
            },
            "deleted":
            {
                "success": True,
                "message": f"{class_name}(s) deleted",
                "http_code": 200
            },
            "found_all":
            {
                "success": True,
                "message": f"{class_name}(s) found",
                "http_code": 200
            },
            "file received":
            {
                "success": True,
                "message": "File received",
                "http_code": 200
            },
            "error":
            {
                "success": False,
                "message": "Oops! Something happened",
                "http_code": 500
            },
            "foreign_key":
            {
                "success": False,
                "message": "Foreign key does not exist",
                "http_code": 400
            }
        }
        return message[code]
