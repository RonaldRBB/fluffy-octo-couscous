"""Activity controller."""
from app.controllers.controller import Controller
from app.models.activity import Activity as ActivityModel


class Activity(Controller):
    """Activity controller."""
    model = ActivityModel
    model_params = ["user_id", "date", "steps",
                    "distance", "run_distance", "calories"]
