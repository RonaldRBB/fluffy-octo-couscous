"""Excersices model."""
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import DB_PREFIX, Base

from app.models.sport import Sport


class Excersice(Base):
    """Excersices model."""
    __tablename__ = f"{DB_PREFIX}_excersices"
    id: Mapped[int] = mapped_column(primary_key=True)
    _name: Mapped[str] = mapped_column("name", String(30), nullable=False)
    _description: Mapped[str] = mapped_column("description", Text)
    sport: Mapped[Sport] = relationship("Sport", back_populates="excersice")

    def __str__(self):
        return (f"<id = {self.id}, "
                f"name = {self.name}, "
                f"description = {self.description}, "
                f"sport = {self.sport}>")

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
