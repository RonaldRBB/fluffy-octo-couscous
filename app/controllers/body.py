"""Body controller."""
from app.controllers.controller import Controller
from app.models import Body as BodyModel


class Body(Controller):
    """Body controller."""
    model = BodyModel
    model_params = ["user_id", "date", "weight"]
