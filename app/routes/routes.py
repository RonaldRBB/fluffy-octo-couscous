"""Main."""
# import requests
from flask import jsonify

from app.controllers import Activity, Body, Workout, User, HeartRate, Sport, UserHealth

def setup_routes(app):
    """Set routes."""
    # Hello world
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])
    # User
    app.add_url_rule("/users", "get_users", User().get_all, methods=["GET"])
    app.add_url_rule("/user", "create_user", User().create, methods=["POST"])
    app.add_url_rule("/user/<int:oid>", "get_user", User().get, methods=["GET"])
    app.add_url_rule("/user/<int:oid>", "update_user", User().update, methods=["PUT"])
    app.add_url_rule("/user/<int:oid>", "delete_user", User().delete, methods=["DELETE"])
    # Activity
    app.add_url_rule("/activities", "get_activities", Activity().get_all, methods=["GET"])
    app.add_url_rule("/activity", "create_activity", Activity().create, methods=["POST"])
    app.add_url_rule("/activity/<int:oid>", "get_activity", Activity().get, methods=["GET"])
    app.add_url_rule("/activity/<int:oid>", "update_activity", Activity().update, methods=["PUT"])
    app.add_url_rule("/activity/<int:oid>", "delete_activity", Activity().delete, methods=["DELETE"])
    # Body
    app.add_url_rule("/bodies", "get_bodys", Body().get_all, methods=["GET"])
    app.add_url_rule("/body", "create_body", Body().create, methods=["POST"])
    app.add_url_rule("/body/<int:oid>", "get_body", Body().get, methods=["GET"])
    app.add_url_rule("/body/<int:oid>", "update_body", Body().update, methods=["PUT"])
    app.add_url_rule("/body/<int:oid>", "delete_body", Body().delete, methods=["DELETE"])
    # Workout
    app.add_url_rule("/workouts", "get_workouts", Workout().get_all, methods=["GET"])
    app.add_url_rule("/workout", "create_workout", Workout().create, methods=["POST"])
    app.add_url_rule("/workout/<int:oid>", "get_workout", Workout().get, methods=["GET"])
    app.add_url_rule("/workout/<int:oid>", "update_workout", Workout().update, methods=["PUT"])
    app.add_url_rule("/workout/<int:oid>", "delete_workout", Workout().delete, methods=["DELETE"])
    # Hear Rate
    app.add_url_rule("/heart_rates", "get_heart_rates", HeartRate().get_all, methods=["GET"])
    app.add_url_rule("/heart_rate", "create_heart_rate", HeartRate().create, methods=["POST"])
    app.add_url_rule("/heart_rate/<int:oid>", "get_heart_rate", HeartRate().get, methods=["GET"])
    app.add_url_rule("/heart_rate/<int:oid>", "update_heart_rate", HeartRate().update, methods=["PUT"])
    app.add_url_rule("/heart_rate/<int:oid>", "delete_heart_rate", HeartRate().delete, methods=["DELETE"])
    #Sport
    app.add_url_rule("/sports", "get_sports", Sport().get_all, methods=["GET"])
    app.add_url_rule("/sport", "create_sport", Sport().create, methods=["POST"])
    app.add_url_rule("/sport/<int:oid>", "get_sport", Sport().get, methods=["GET"])
    app.add_url_rule("/sport/<int:oid>", "update_sport", Sport().update, methods=["PUT"])
    app.add_url_rule("/sport/<int:oid>", "delete_sport", Sport().delete, methods=["DELETE"])
    #User Health
    app.add_url_rule("/user_healths", "get_user_healths", UserHealth().get_all, methods=["GET"])
    app.add_url_rule("/user_health", "create_user_health", UserHealth().create, methods=["POST"])
    app.add_url_rule("/user_health/<int:oid>", "get_user_health", UserHealth().get, methods=["GET"])
    app.add_url_rule("/user_health/<int:oid>", "update_user_health", UserHealth().update, methods=["PUT"])
    app.add_url_rule("/user_health/<int:oid>", "delete_user_health", UserHealth().delete, methods=["DELETE"])
    return app


def hello_world():
    """Hello world."""
    return jsonify({"Hello World!"}), 200
