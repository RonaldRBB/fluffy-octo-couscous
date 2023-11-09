"""Hart Rate Controller"""
from datetime import datetime

import pandas as pd
from flask import request

from app.controllers.controller import Controller
from app.models import HeartRate as HeartRateModel
from config import session


class HeartRate(Controller):
    """Hart Rate Controller"""
    model = HeartRateModel
    model_params = ["user_id", "date", "heart_rate"]
    data_conversion = {
        "datetime": ["date", "time"],
        "heart_rate": "heartRate"
    }

    def get_average(self):
        """Get average"""
        request_data = request.get_json()
        start_date = datetime.strptime(request_data["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(request_data["end_date"], "%Y-%m-%d")
        try:
            data = session.query(HeartRateModel).filter(
                HeartRateModel._datetime.between(start_date, end_date)).all()
            if not data:
                return self.handle_response("not_found")
            df = pd.DataFrame([item.get_dict(with_relation=False)
                              for item in data])
            average = round(df["heart_rate"].mean(), 2)
            return self.handle_response("found_all", average)
        except Exception as error:  # pylint: disable=W0703
            session.rollback()
            print(f" * {error}")
            return self.handle_response("error")
