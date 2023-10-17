"""User health model."""
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import Base

# user_id, gender, height


class UserHealth(Base):
    """User health model."""
    __tablename__ = "foc_user_health"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", Integer, ForeignKey("foc_users.id"), nullable=False)
    _gender: Mapped[str] = mapped_column(
        "gender", String(30), nullable=False)
    _height: Mapped[float] = mapped_column(
        "height", Float, nullable=False)
    _gen_date: Mapped[datetime] = mapped_column(
        "gen_date", DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="user_health")

    def __str__(self):
        return (f"<id = {self.id}, "
                f"gender = {self.gender}, "
                f"height = {self.height}, "
                f"user_id = {self.user_id}, "
                f"user = {self.user}>")

    @property
    def user_id(self) -> int:
        """User id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        self._user_id = value

    @property
    def gender(self) -> str:
        """Gender."""
        return self._gender

    @gender.setter
    def gender(self, value: str) -> None:
        self._gender = value

    @property
    def height(self) -> float:
        """Height."""
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def gen_date(self) -> datetime:
        """Generation date."""
        return self._gen_date

    @gen_date.setter
    def gen_date(self, value: datetime) -> None:
        self._gen_date = value
