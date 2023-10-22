"""Body model."""
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class Body(Base):
    """Body model."""
    __tablename__ = f"{DB_PREFIX}_bodies"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", ForeignKey(f"{DB_PREFIX}_users.id"))
    _date: Mapped[datetime] = mapped_column(
        "date", DateTime, default=datetime.utcnow)
    _weight: Mapped[float] = mapped_column("weight", Float, nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="body")

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"date = {self.date}, "
                f"weight = {self.weight}, "
                f"user_id = {self.user_id}, "
                f"user = {self.user}>")

    def get_dict(self, with_relation=True):
        """Get dictionary representation of the model."""
        data = {
            "id": self.id,
            "date": self.date,
            "weight": self.weight,
            "user_id": self.user_id
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
    def date(self) -> datetime:
        """Date."""
        return self._date

    @date.setter
    def date(self, value: datetime) -> None:
        self._date = value

    @property
    def weight(self) -> float:
        """Weight."""
        return self._weight

    @weight.setter
    def weight(self, value: int) -> None:
        self._weight = value
