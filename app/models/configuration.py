"""Configuration model."""
from sqlalchemy import JSON, Column, Integer, String, Text

from core.config import shared_sequence
from core.models.model import Model


class Configuration(Model):
    """Configuration class."""

    __tablename__ = "configuration"
    id = Column(Integer, shared_sequence, primary_key=True, autoincrement=True)
    _name = Column("name", String(255), nullable=False, unique=True)
    _value = Column("value", JSON)
    _description = Column("description", Text)

    @property
    def name(self):
        """Get name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set name."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def value(self):
        """Get value."""
        return self._value

    @value.setter
    def value(self, value):
        """Set value."""
        if not isinstance(value, dict):
            raise ValueError("Value must be a dictionary")
        self._value = value

    @property
    def description(self):
        """Get description."""
        return self._description

    @description.setter
    def description(self, value):
        """Set description."""
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        self._description = value
