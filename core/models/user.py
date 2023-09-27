"""User class."""
from core.models.model import Model
from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String


class User(Model):
    """User class."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    _username = Column("username", String(50), nullable=False, unique=True)
    _email = Column("email", String(50), nullable=False, unique=True)
    _created_at = Column("created_at", DateTime, default=datetime.now())

    @property
    def username(self):
        """Get username."""
        return self._username

    @username.setter
    def username(self, value):
        """Set username."""
        if not isinstance(value, str):
            raise ValueError("Username must be a string")
        self._username = value

    @property
    def email(self):
        """Get email."""
        return self._email

    @email.setter
    def email(self, value):
        """Set email."""
        if not isinstance(value, str):
            raise ValueError("Email must be a string")
        self._email = value
