"""User class."""
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.models.model import Model
from config.config import shared_sequence


class User(Model):
    """User class."""

    __tablename__ = f"{Model._prefix}users"
    id = Column(Integer, shared_sequence, primary_key=True)
    _username = Column("username", String(50), nullable=False, unique=True)
    _email = Column("email", String(50), nullable=False, unique=True)
    _gen_date = Column("gen_date", DateTime, default=datetime.now())

    @property
    def username(self) -> Column[str] | str:
        """Get username."""
        return self._username

    @username.setter
    def username(self, value: Column[str] | str) -> None:
        """Set username."""
        self._username = value

    @property
    def email(self) -> Column[str] | str:
        """Get email."""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        """Set email."""
        self._email = value
