"""Sport Controller"""
from app.controllers.controller import Controller
from app.models import Sport as SportModel


class Sport(Controller):
    """Sport Controller"""
    model = SportModel
    model_params = ["user_id", "type_id", "start_time", "sport_time",
                    "max_pace", "min_pace", "avg_pace", "distance", "calories"]
