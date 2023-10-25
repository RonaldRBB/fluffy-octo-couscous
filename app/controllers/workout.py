"""Workouts controller."""
from app.controllers.controller import Controller
from app.models import Workout as WorkoutModel


class Workout(Controller):
    """Workouts controller."""
    model = WorkoutModel
    model_params = ["name", "description"]
