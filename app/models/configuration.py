"""Configuration model."""
from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import Base


class Configuration(Base):
    """Configuration model."""
    __tablename__ = "foc_configurations"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", ForeignKey('foc_users.id'))
    _name: Mapped[str] = mapped_column("name", String(30), nullable=False)
    _value: Mapped[str] = mapped_column("value", JSON, nullable=False)
    _gen_date: Mapped[datetime] = mapped_column(
        "gen_date", DateTime, default=datetime.utcnow)
    username: Mapped["User"] = relationship(back_populates="configurations")

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"name = {self.name}, "
                f"value = {self.value}, "
                f"user_id = {self.user_id}, "
                f"user = {self.username}>")

    @property
    def user_id(self) -> int:
        """User id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        self._user_id = value

    @property
    def name(self) -> str:
        """Name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value.lower()

    @property
    def value(self) -> str:
        """Value."""
        return self._value

    @value.setter
    def value(self, value: str) -> None:
        self._value = value

    @property
    def gen_date(self) -> datetime:
        """Generation date."""
        return self._gen_date

    @gen_date.setter
    def gen_date(self, value: datetime) -> None:
        self._gen_date = value
