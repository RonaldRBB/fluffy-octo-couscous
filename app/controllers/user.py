"""Webhook controller."""
from app.controllers.controller import Controller
from app.models.user import User as UserModel


class User(Controller):
    """User controller."""
    model = UserModel
    model_params = ["username", "first_name", "last_name", "email"]
