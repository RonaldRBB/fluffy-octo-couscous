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
        start_date = request_data["start_date"]
        end_date = request_data["end_date"]
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        print(start_date, end_date)
        data = session.query(HeartRateModel).filter(
            HeartRateModel._datetime.between(start_date, end_date)).all()
        print(data)
        array_data = []
        # convert to pandas an get average of heart rate
        df = pd.DataFrame(
            [item.get_dict(with_relation=False) for item in data]
        )
        print(df)
        # get average of heart rage
        average = df["heart_rate"].mean()
        print(average)
        # round to two decimals
        average = round(average, 2)
        print(average)
        for item in data:
            # print(item.get_dict(with_relation=False))
            array_data.append(item.get_dict(with_relation=False))
        if not data:
            return self.handle_response("not_found")
        return self.handle_response("found_all", array_data)
