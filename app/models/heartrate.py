"""Heartrate model."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class Heartrate(Base):
    """Heartrate model."""
    # date,user_id,heartRate
    __tablename__ = f"{DB_PREFIX}_heartrates"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", ForeignKey(f"{DB_PREFIX}_users.id"))
    _date: Mapped[datetime] = mapped_column(
        "date", DateTime, default=datetime.utcnow)
    _heart_rate: Mapped[int] = mapped_column(
        "heart_rate", Integer, nullable=False)
    username: Mapped["User"] = relationship(back_populates="heartrate")

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"date = {self.date}, "
                f"heartRate = {self.heart_rate}, "
                f"user_id = {self.user_id}, "
                f"user = {self.username}>")

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
    def heart_rate(self) -> int:
        """HeartRate."""
        return self._heart_rate

    @heart_rate.setter
    def heart_rate(self, value: int) -> None:
        self._heart_rate = value
