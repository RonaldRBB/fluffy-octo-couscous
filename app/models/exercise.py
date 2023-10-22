"""Exercises model."""
from typing import List

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from app.models.sport import Sport
from config import DB_PREFIX, Base


class Exercise(Base):
    """Exercises model."""
    __tablename__ = f"{DB_PREFIX}_exercises"
    id: Mapped[int] = mapped_column(primary_key=True)
    _name: Mapped[str] = mapped_column("name", String(30), nullable=False)
    _description: Mapped[str] = mapped_column("description", Text)
    sport: Mapped[List["Sport"]] = relationship(
        "Sport", back_populates="exercise")

    def __str__(self):
        return (f"<id = {self.id}, "
                f"name = {self.name}, "
                f"description = {self.description}, "
                f"sport = {self.sport}>")

    def get_dict(self, with_relation=False):
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
        if with_relation:
            data["sport"] = [sport.get_dict() for sport in self.sport]
        return data

    @property
    def name(self) -> str:
        """Name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def description(self) -> str:
        """Description."""
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        self._description = value
