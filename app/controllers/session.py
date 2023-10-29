"""Session Controller"""
from app.controllers.controller import Controller
from app.models import Session as SessionModel


class Session(Controller):
    """Session Controller"""
    model = SessionModel
    model_params = ["user_id", "type_id", "start_time", "session_time",
                    "max_pace", "min_pace", "avg_pace", "distance", "calories"]
    data_conversion = {
        "type_id": "type",
        "start_time": "startTime",
        "session_time": "sportTime",
        "max_pace": "maxPace",
        "min_pace": "minPace",
        "avg_pace": "avgPace",
        "distance": "distance",
        "calories": "calories"
    }
