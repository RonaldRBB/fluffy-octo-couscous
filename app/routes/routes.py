"""Main."""
# import requests
from flask import request

from app.controllers import (
    Activity,
    Body,
    Exercise,
    ExerciseInfo,
    HeartRate,
    Session,
    User,
    UserHealth,
    Workout,
)
from config import DOWNLOAD_PATH


def setup_routes(app):
    """Set routes."""
    # Hello world
    app.add_url_rule("/", "hello_world", hello_world, methods=["GET"])
    # User
    app.add_url_rule("/users", "get_users", User().get_all, methods=["GET"])
    app.add_url_rule("/user", "create_user", User().create, methods=["POST"])
    app.add_url_rule("/user/<int:id>", "get_user", User().get, methods=["GET"])
    app.add_url_rule("/user/<int:id>", "update_user", User().update, methods=["PUT"])
    app.add_url_rule("/user/<int:id>", "delete_user", User().delete, methods=["DELETE"])
    # Activity
    app.add_url_rule("/activities", "get_activities", Activity().get_all, methods=["GET"])
    app.add_url_rule("/activities", "create_activities", Activity().store_file_data, methods=["POST"])
    app.add_url_rule("/activity", "create_activity", Activity().create, methods=["POST"])
    app.add_url_rule("/activity/<int:id>", "get_activity", Activity().get, methods=["GET"])
    app.add_url_rule("/activity/<int:id>", "update_activity", Activity().update, methods=["PUT"])
    app.add_url_rule("/activity/<int:id>", "delete_activity", Activity().delete, methods=["DELETE"])
    # Body
    app.add_url_rule("/bodies", "get_bodys", Body().get_all, methods=["GET"])
    app.add_url_rule("/bodies", "create_bodys", Body().store_file_data, methods=["POST"])
    app.add_url_rule("/body", "create_body", Body().create, methods=["POST"])
    app.add_url_rule("/body/<int:id>", "get_body", Body().get, methods=["GET"])
    app.add_url_rule("/body/<int:id>", "update_body", Body().update, methods=["PUT"])
    app.add_url_rule("/body/<int:id>", "delete_body", Body().delete, methods=["DELETE"])
    # Workout
    app.add_url_rule("/workouts", "get_workouts", Workout().get_all, methods=["GET"])
    app.add_url_rule("/workout", "create_workout", Workout().create, methods=["POST"])
    app.add_url_rule("/workout/<int:id>", "get_workout", Workout().get, methods=["GET"])
    app.add_url_rule("/workout/<int:id>", "update_workout", Workout().update, methods=["PUT"])
    app.add_url_rule("/workout/<int:id>", "delete_workout", Workout().delete, methods=["DELETE"])
    # Hear Rate
    app.add_url_rule("/heart_rates", "get_heart_rates", HeartRate().get_all, methods=["GET"])
    app.add_url_rule("/heart_rates", "create_heart_rates", HeartRate().store_file_data, methods=["POST"])
    app.add_url_rule("/heart_rate", "create_heart_rate", HeartRate().create, methods=["POST"])
    app.add_url_rule("/heart_rate/<int:id>", "get_heart_rate", HeartRate().get, methods=["GET"])
    app.add_url_rule("/heart_rate/<int:id>", "update_heart_rate", HeartRate().update, methods=["PUT"])
    app.add_url_rule("/heart_rate/<int:id>", "delete_heart_rate", HeartRate().delete, methods=["DELETE"])
    app.add_url_rule("/heart_rate/average", "get_average", HeartRate().get_average, methods=["GET"])
    #Session
    app.add_url_rule("/sessions", "get_sessions", Session().get_all, methods=["GET"])
    app.add_url_rule("/sessions", "create_sessions", Session().store_file_data, methods=["POST"])
    app.add_url_rule("/session", "create_session", Session().create, methods=["POST"])
    app.add_url_rule("/session/<int:id>", "get_session", Session().get, methods=["GET"])
    app.add_url_rule("/session/<int:id>", "update_session", Session().update, methods=["PUT"])
    app.add_url_rule("/session/<int:id>", "delete_session", Session().delete, methods=["DELETE"])
    #User Health
    app.add_url_rule("/user_healths", "get_user_healths", UserHealth().get_all, methods=["GET"])
    app.add_url_rule("/user_health", "create_user_health", UserHealth().create, methods=["POST"])
    app.add_url_rule("/user_health/<int:id>", "get_user_health", UserHealth().get, methods=["GET"])
    app.add_url_rule("/user_health/<int:id>", "update_user_health", UserHealth().update, methods=["PUT"])
    app.add_url_rule("/user_health/<int:id>", "delete_user_health", UserHealth().delete, methods=["DELETE"])
    #Exercise
    app.add_url_rule("/exercises", "get_exercises", Exercise().get_all, methods=["GET"])
    app.add_url_rule("/exercise", "create_exercise", Exercise().create, methods=["POST"])
    app.add_url_rule("/exercise/<int:id>", "get_exercise", Exercise().get, methods=["GET"])
    app.add_url_rule("/exercise/<int:id>", "update_exercise", Exercise().update, methods=["PUT"])
    app.add_url_rule("/exercise/<int:id>", "delete_exercise", Exercise().delete, methods=["DELETE"])
    #Exercise Info
    app.add_url_rule("/exercise_infos", "get_exercise_infos", ExerciseInfo().get_all, methods=["GET"])
    app.add_url_rule("/exercise_info", "create_exercise_info", ExerciseInfo().create, methods=["POST"])
    app.add_url_rule("/exercise_info/<int:id>", "get_exercise_info", ExerciseInfo().get, methods=["GET"])
    app.add_url_rule("/exercise_info/<int:id>", "update_exercise_info", ExerciseInfo().update, methods=["PUT"])
    app.add_url_rule("/exercise_info/<int:id>", "delete_exercise_info", ExerciseInfo().delete, methods=["DELETE"])
    # receive file post
    app.add_url_rule("/receive_file", "receive_file", receive_file, methods=["POST"])
    return app


def hello_world():
    """Hello world."""
    return "Hello World!", 200


def receive_file():
    """Receive file."""
    uploaded_file=request.files['file']
    download_path=f"{DOWNLOAD_PATH}{uploaded_file.filename}"
    uploaded_file.save(download_path)
    return "File received", 200