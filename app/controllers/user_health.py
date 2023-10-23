"""User HealthController"""
from app.controllers.controller import Controller
from app.models import UserHealth as userHealthModel


class UserHealth(Controller):
    """User Health Controller"""
    model = userHealthModel
    model_params = ["user_id", "gender", "birth_date", "height"]
