"""Exercises controller."""
from app.controllers.controller import Controller
from app.models import Exercise as ExerciseModel


class Exercise(Controller):
    """Exercises controller."""
    model = ExerciseModel
    model_params = ["name", "description"]
