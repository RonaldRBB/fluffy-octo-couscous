"""Hart Rate Controller"""
from app.controllers.controller import Controller
from app.models import HeartRate as HeartRateModel


class HeartRate(Controller):
    """Hart Rate Controller"""
    model = HeartRateModel
    model_params = ["user_id", "date", "heart_rate"]
