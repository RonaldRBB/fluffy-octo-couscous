"""User health model."""
from datetime import datetime

from sqlalchemy import Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class UserHealth(Base):
    """User health model."""
    __tablename__ = f"{DB_PREFIX}_users_health"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column("user_id", Integer, ForeignKey(
        f"{DB_PREFIX}_users.id"), unique=True, nullable=False)
    _gender: Mapped[str] = mapped_column(
        "gender", String(30), nullable=False)
    _birth_date: Mapped[Date] = mapped_column(
        "birth_date", Date, nullable=False)
    _height: Mapped[float] = mapped_column(
        "height", Float, nullable=False)
    _gen_date: Mapped[datetime] = mapped_column(
        "gen_date", DateTime, default=datetime.utcnow)
    user: Mapped["User"] = relationship(back_populates="user_health")

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
        if value.lower() not in ["male", "female"]:
            raise ValueError("Gender must be either 'male' or 'female'")
        self._gender = value.lower()

    @property
    def birth_date(self) -> datetime:
        """Birth date."""
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: datetime) -> None:
        self._birth_date = value

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
