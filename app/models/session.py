"""Session model."""
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Workout
from config import DB_PREFIX, Base


class Session(Base):
    """Session model."""
    __tablename__ = f"{DB_PREFIX}_sessions"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", ForeignKey(f"{DB_PREFIX}_users.id"))
    _type_id: Mapped[int] = mapped_column("type_id", ForeignKey(
        f"{DB_PREFIX}_workouts.id"))
    _start_time: Mapped[datetime] = mapped_column(
        "start_time", DateTime, default=datetime.utcnow)
    _session_time: Mapped[int] = mapped_column(
        "session_time", Integer, nullable=False)
    _max_pace: Mapped[float] = mapped_column("max_pace", Float)
    _min_pace: Mapped[float] = mapped_column("min_pace", Float)
    _avg_pace: Mapped[float] = mapped_column("avg_pace", Float)
    _distance: Mapped[float] = mapped_column("distance", Float)
    _calories: Mapped[int] = mapped_column("calories", Integer, nullable=False)
    workout: Mapped[Workout] = relationship(
        "Workout", back_populates="session")
    user: Mapped["User"] = relationship("User", back_populates="session")

    def __str__(self):
        return (
            f"<id = {self.id}, "
            f"type = {self.type_id}, "
            f"start_time = {self.start_time}, "
            f"session_time = {self.session_time}, "
            f"max_pace = {self.max_pace}, "
            f"min_pace = {self.min_pace}, "
            f"avg_pace = {self.avg_pace}, "
            f"distance = {self.distance}, "
            f"calories = {self.calories}, "
            f"workout = {self.workout}, "
            f"user_id = {self.user_id}, "
            f"user = {self.user}>"
        )

    def get_dict(self, with_relation=True):
        """Get dictionary representation of the model."""
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "type_id": self.type_id,
            "start_time": self.start_time,
            "session_time": self.session_time,
            "max_pace": self.max_pace,
            "min_pace": self.min_pace,
            "avg_pace": self.avg_pace,
            "distance": self.distance,
            "calories": self.calories,
        }
        if with_relation:
            data["workout"]: self.workout.get_dict(
                with_relation=with_relation)
            data["user"] = self.user.get_dict()
        return data

    @property
    def user_id(self) -> int:
        """User id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        self._user_id = value

    @property
    def type_id(self) -> int:
        """Type id."""
        return self._type_id

    @type_id.setter
    def type_id(self, value: int) -> None:
        self._type_id = value

    @property
    def start_time(self) -> datetime:
        """Start time."""
        return self._start_time

    @start_time.setter
    def start_time(self, value: datetime | str) -> None:
        if isinstance(value, str):
            value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S%z")
        self._start_time = value

    @property
    def session_time(self) -> int:
        """Session time."""
        return self._session_time

    @session_time.setter
    def session_time(self, value: int) -> None:
        self._session_time = value

    @property
    def max_pace(self) -> float:
        """Max pace."""
        return self._max_pace

    @max_pace.setter
    def max_pace(self, value: float) -> None:
        self._max_pace = value

    @property
    def min_pace(self) -> float:
        """Min pace."""
        return self._min_pace

    @min_pace.setter
    def min_pace(self, value: float) -> None:
        self._min_pace = value

    @property
    def avg_pace(self) -> float:
        """Avg pace."""
        return self._avg_pace

    @avg_pace.setter
    def avg_pace(self, value: float) -> None:
        self._avg_pace = value

    @property
    def distance(self) -> float:
        """Distance."""
        return self._distance

    @distance.setter
    def distance(self, value: float) -> None:
        self._distance = value

    @property
    def calories(self) -> int:
        """Calories."""
        return self._calories

    @calories.setter
    def calories(self, value: int) -> None:
        self._calories = value
