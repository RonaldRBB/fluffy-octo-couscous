"""User model."""""
from datetime import datetime
from typing import List

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Activity, Body, Configuration, HeartRate, Sport, UserHealth
from config import DB_PREFIX, Base


class User(Base):
    """User model."""
    __tablename__ = f"{DB_PREFIX}_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    _username: Mapped[str] = mapped_column(
        "username", String(30), nullable=False, unique=True)
    _first_name: Mapped[str] = mapped_column(
        "first_name", String(30), nullable=False)
    _last_name: Mapped[str] = mapped_column(
        "last_name", String(30), nullable=False)
    _email: Mapped[str] = mapped_column(
        "email", String(50), nullable=False, unique=True)
    _gen_date: Mapped[datetime] = mapped_column(
        "gen_date", DateTime, default=datetime.utcnow)
    configurations: Mapped[List[Configuration]] = relationship(
        "Configuration", back_populates="username")
    user_health: Mapped[List[UserHealth]] = relationship(
        "UserHealth", back_populates="user")
    activities: Mapped[List[Activity]] = relationship(
        "Activity", back_populates="username")
    body: Mapped[List[Body]] = relationship(
        "Body", back_populates="username")
    heart_rate: Mapped[List[HeartRate]] = relationship(
        "HeartRate", back_populates="username")
    sport: Mapped[List[Sport]] = relationship(
        "Sport", back_populates="username")

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"username = {self.username}, "
                f"first_name = {self.first_name}, "
                f"last_name = {self.last_name}, "
                f"email = {self.email}, "
                f"user_health = {len(self.user_health)}, "
                f"configurations = {len(self.configurations)}, "
                f"activities = {len(self.activities)}, "
                f"body = {len(self.body)}, "
                f"heart_rate = {len(self.heart_rate)}, "
                f"sport = {len(self.sport)}, "
                f"gen_date = {self.gen_date}>")

    def get_dict(self, with_relation=False):
        """JSON representation of the model."""
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "gen_date": self.gen_date
        }

    @property
    def username(self) -> str:
        """Username."""
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value.lower()

    @property
    def first_name(self) -> str:
        """First name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._first_name = value.lower()

    @property
    def last_name(self) -> str:
        """Last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._last_name = value.lower()

    @property
    def email(self) -> str:
        """Email."""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value.lower()

    @property
    def gen_date(self) -> datetime:
        """Generation date."""
        return self._gen_date

    @gen_date.setter
    def gen_date(self, value: datetime) -> None:
        self._gen_date = value

    @property
    def full_name(self) -> str:
        """Full name."""
        return f"{self._first_name} {self._last_name}"
