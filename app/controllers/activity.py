
from datetime import datetime
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

from app.controllers.controller import Controller
from app.helpers.response import ApiResponse
from app.models.activity import Activity as ActivityModel
from config import session


class Activity(Controller):
    """Activity controller."""

    def create(self):
        """Create Activity."""
        data = request.get_json()
        if self.validate(data) is False:
            return self.handle_response("incomplete_data")
        try:
            activity = self.load_activity(data)
            session.add(activity)
            session.commit()
            return self.handle_response("created", activity.get_dict())
        except IntegrityError as error:
            session.rollback()
            print(f"ERROR: {error}!")
            return self.handle_response("exists")
        except Exception as error:
            session.rollback()
            print(f"ERROR: {error}!")
            return self.handle_response("error")

    def get(self, oid):
        """Show Activity."""
        try:
            activity = session.query(ActivityModel).filter_by(id=oid).first()
            if not activity:
                return self.handle_response("not_exist")
            return self.handle_response("found", activity.get_dict())
        except Exception:
            session.rollback()
            return self.handle_response("error")

    def get_all(self):
        """Get Activity."""
        try:
            activities = session.query(ActivityModel).all()
            array_activities = []
            if not activities:
                raise ValueError("No activities found")
            for activity in activities:
                array_activities.append(activity.get_dict())
            return self.handle_response("found_all", None, array_activities)
        except Exception:
            session.rollback()
            return self.handle_response("error")

    def update(self, oid):
        """Update Activity."""
        data = request.get_json()
        print(data)
        # call validate
        if self.validate(data) is False:
            return self.handle_response("incomplete_data")
        try:
            activity = session.query(ActivityModel).filter_by(id=oid).first()
            if not activity:
                return self.handle_response("not_exist")
            self.load_activity(data, activity)
            session.commit()
            return self.handle_response("updated", activity.get_dict())
        except IntegrityError as error:
            session.rollback()
            print(f"ERROR: {error}!")
            return self.handle_response("exists")
        except Exception as error:
            session.rollback()
            print(f"ERROR: {error}!")
            return self.handle_response("error")

    def delete(self, oid):
        """Delete Activity."""
        try:
            activity = session.query(ActivityModel).filter_by(id=oid).first()
            if not activity:
                return self.handle_response("not_exist")
            session.delete(activity)
            session.commit()
            return self.handle_response("deleted")
        except Exception:
            session.rollback()
            return self.handle_response("error")

    def validate(self, data):
        """Validate Activity.u"""
        array_data = ["user_id", "date", "steps", "distance",
                      "run_distance", "calories"]
        for item in array_data:
            if item not in data:
                return False
        return True

    def load_activity(self, data, activity=None):
        """Load Activity."""
        if not activity:
            activity = ActivityModel()
        activity.user_id = data["user_id"]
        if data["date"] is not None:
            activity.date = datetime.strptime(data["date"], '%Y-%m-%d %H:%M:%S')
        activity.steps = data["steps"]
        activity.distance = data["distance"]
        activity.run_distance = data["run_distance"]
        activity.calories = data["calories"]
        return activity

    def handle_response(self, code, activity=None, array_activitys=None):
        """Handle response."""
        response = ApiResponse()
        message = self.get_message_and_code(code)
        response.success = message["succes"]
        response.message = message["message"]
        if activity:
            response.data = activity
        elif array_activitys:
            response.data = array_activitys
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
                "message": "Activity created",
                "http_code": 201
            },
            "exists":
            {
                "succes": False,
                "message": "Activity exists",
                "http_code": 400
            },
            "found":
            {
                "succes": True,
                "message": "Activity found",
                "http_code": 200
            },
            "found_all":
            {
                "succes": True,
                "message": "Activities found",
                "http_code": 200
            },
            "not_exist":
            {
                "succes": False,
                "message": "Activity does not exist",
                "http_code": 400
            },
            "updated":
            {
                "succes": True,
                "message": "Activity updated",
                "http_code": 200
            },
            "deleted":
            {
                "succes": True,
                "message": "Activity deleted",
                "http_code": 200
            },
            "error":
            {
                "succes": False,
                "message": "Error",
                "http_code": 500
            }
        }
        return message[code]
