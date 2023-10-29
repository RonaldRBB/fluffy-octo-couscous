"""Activity controller."""
from app.controllers.controller import Controller
from app.models import Activity as ActivityModel


class Activity(Controller):
    """Activity controller."""
    model = ActivityModel
    # type:ignore
    model_params = ["user_id", "date", "steps",
                    "distance", "run_distance", "calories"]
    data_conversion = {
        "date": "date",
        "steps": "steps",
        "distance": "distance",
        "run_distance": "runDistance",
        "calories": "calories"
    }
