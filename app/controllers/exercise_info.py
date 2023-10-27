"""Exercise Info Controller"""
from app.controllers.controller import Controller
from app.models import ExerciseInfo as ExerciseInfoModel


class ExerciseInfo(Controller):
    """Exercise Info Controller"""
    model = ExerciseInfoModel
    model_params = ["name", "description"]
