"""Exercise Info model."""
from typing import List

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base


class ExerciseInfo(Base):
    """Exercise Info model."""
    __tablename__ = f"{DB_PREFIX}_exercises_info"
    id: Mapped[int] = mapped_column(primary_key=True)
    _name: Mapped[str] = mapped_column("name", String(30), nullable=False)
    _description: Mapped[str] = mapped_column("description", Text)
    exercise: Mapped[List["Exercise"]] = relationship(
        "Exercise", back_populates="info"
    )

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"name = {self.name}, "
                f"description = {self.description}>")

    def get_dict(self, with_relation=True):
        """Get dictionary representation of the model."""
        data = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
        if with_relation:
            data["exercise"] = [exercise.get_dict(with_relation=False)
                                for exercise in self.exercise]
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
