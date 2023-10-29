"""heart rate model."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class HeartRate(Base):
    """heart rate model."""
    __tablename__ = f"{DB_PREFIX}_heart_rates"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", ForeignKey(f"{DB_PREFIX}_users.id"))
    _datetime: Mapped[datetime] = mapped_column(
        "datetime", DateTime, default=datetime.utcnow)
    _heart_rate: Mapped[int] = mapped_column(
        "heart_rate", Integer, nullable=False)
    user: Mapped["User"] = relationship(
        "User", back_populates="heart_rate")

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"date = {self.datetime}, "
                f"heart_rate = {self.heart_rate}, "
                f"user_id = {self.user_id}, "
                f"user = {self.user}>")

    def get_dict(self, with_relation=True):
        """Get dictionary representation of the model."""
        data = {
            "id": self.id,
            "datetime": self.datetime,
            "heart_rate": self.heart_rate,
            "user_id": self.user_id,
        }
        if with_relation:
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
    def datetime(self) -> datetime:
        """Date."""
        return self._datetime

    @datetime.setter
    def datetime(self, value: datetime) -> None:
        self._datetime = value

    @property
    def heart_rate(self) -> int:
        """heart_rate."""
        return self._heart_rate

    @heart_rate.setter
    def heart_rate(self, value: int) -> None:
        self._heart_rate = value
