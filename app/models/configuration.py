"""Configuration model."""
from typing import Any
from datetime import datetime
from sqlalchemy import JSON, Column, DateTime, Integer, String, Text
from app.models.model import Model
from config.config import shared_sequence


class Configuration(Model):
    """Configuration class."""

    __tablename__ = Model._prefix + "configuration"
    id = Column(Integer, shared_sequence,
                primary_key=True, autoincrement=True)
    _name = Column("name", String(255), nullable=False, unique=True)
    _value = Column("value", JSON)
    _description = Column("description", Text)
    _gen_date = Column("gen_date", DateTime, default=datetime.now())

    @property
    def name(self) -> Column[str] | str:
        """Get name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set name."""
        self._name = value

    @property
    def value(self) -> Column[Any] | dict[str, Any]:
        """Get value."""
        return self._value

    @value.setter
    def value(self, value: dict[str, Any]) -> None:
        """Set value."""
        self._value = value

    @property
    def description(self) -> Column[str] | str:
        """Get description."""
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """Set description."""
        self._description = value
