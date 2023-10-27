"""Exercise Controller"""
from app.controllers.controller import Controller
from app.models import Exercise as ExerciseModel


class Exercise(Controller):
    """Exercise Controller"""
    model = ExerciseModel
    model_params = ["user_id", "session_id", "date", "set", "reps", "weight"]
