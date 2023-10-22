"""Activity model."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class Activity(Base):
    """Activity model."""
    __tablename__ = f"{DB_PREFIX}_activities"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", ForeignKey(f"{DB_PREFIX}_users.id"))
    _date: Mapped[datetime] = mapped_column(
        "date", DateTime, default=datetime.utcnow)
    _steps: Mapped[int] = mapped_column("steps", Integer, nullable=False)
    _distance: Mapped[int] = mapped_column("distance", Integer, nullable=False)
    _run_distance: Mapped[int] = mapped_column(
        "run_distance", Integer, nullable=False)
    _calories: Mapped[int] = mapped_column("calories", Integer, nullable=False)
    username: Mapped["User"] = relationship(
        "User", back_populates="activities")

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"date = {self.date}, "
                f"steps = {self.steps}, "
                f"distance = {self.distance}, "
                f"runDistance = {self.run_distance}, "
                f"calories = {self.calories}, "
                f"user_id = {self.user_id}, "
                f"user = {self.username}>")

    def get_dict(self, with_relation=True):
        """Get JSON representation of the model."""
        data = {
            "id": self.id,
            "date": self.date,
            "steps": self.steps,
            "distance": self.distance,
            "run_distance": self.run_distance,
            "calories": self.calories,
            "user_id": self.user_id
        }
        if with_relation:
            data["user"] = self.username.get_dict()
        return data

    @property
    def user_id(self) -> int:
        """User id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        self._user_id = value

    @property
    def date(self) -> datetime:
        """Date."""
        return self._date

    @date.setter
    def date(self, value: datetime) -> None:
        self._date = value

    @property
    def steps(self) -> int:
        """Steps."""
        return self._steps

    @steps.setter
    def steps(self, value: int) -> None:
        self._steps = value

    @property
    def distance(self) -> int:
        """Distance."""
        return self._distance

    @distance.setter
    def distance(self, value: int) -> None:
        self._distance = value

    @property
    def run_distance(self) -> int:
        """Run Distance."""
        return self._run_distance

    @run_distance.setter
    def run_distance(self, value: int) -> None:
        self._run_distance = value

    @property
    def calories(self) -> int:
        """Calories."""
        return self._calories

    @calories.setter
    def calories(self, value: int) -> None:
        self._calories = value
