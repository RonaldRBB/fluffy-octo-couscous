"""Sport model."""
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class Sport(Base):
    """Sport model."""
    __tablename__ = f"{DB_PREFIX}_sport"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", ForeignKey(f"{DB_PREFIX}_users.id"))
    _type_id: Mapped[int] = mapped_column("type_id", ForeignKey(
        f"{DB_PREFIX}_sport_type.id"))
    _start_time: Mapped[datetime] = mapped_column(
        "start_time", DateTime, default=datetime.utcnow)
    _sport_time: Mapped[int] = mapped_column(
        "sport_time", Integer, nullable=False)
    _max_pace: Mapped[float] = mapped_column("max_pace", Float)
    _min_pace: Mapped[float] = mapped_column("min_pace", Float)
    _avg_pace: Mapped[float] = mapped_column("avg_pace", Float)
    _distance: Mapped[float] = mapped_column("distance", Float)
    _calories: Mapped[int] = mapped_column("calories", Integer, nullable=False)
    excersice: Mapped["Excersice"] = relationship(
        "Excersice", back_populates="sport")
    username: Mapped["User"] = relationship(back_populates="sport")

    def __str__(self):
        return (
            f"<id = {self.id}, "
            f"type = {self.type}, "
            f"start_time = {self.start_time}, "
            f"sport_time = {self.sport_time}, "
            f"max_pace = {self.max_pace}, "
            f"min_pace = {self.min_pace}, "
            f"avg_pace = {self.avg_pace}, "
            f"distance = {self.distance}, "
            f"calories = {self.calories}, "
            f"excersice = {self.excersice}, "
            f"user_id = {self.user_id}, "
            f"user = {self.username}>"
        )

    @property
    def user_id(self) -> int:
        """User id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        self._user_id = value

    @property
    def type(self) -> int:
        """Type."""
        return self._type

    @type.setter
    def type(self, value: int) -> None:
        self._type = value

    @property
    def start_time(self) -> datetime:
        """Start time."""
        return self._start_time

    @start_time.setter
    def start_time(self, value: datetime) -> None:
        self._start_time = value

    @property
    def sport_time(self) -> int:
        """Sport time."""
        return self._sport_time

    @sport_time.setter
    def sport_time(self, value: int) -> None:
        self._sport_time = value

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
