"""Configuration model."""
from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.user import User
from config import Base


class Configuration(Base):
    """Configuration model."""
    __tablename__ = "foc_configuration"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('foc_user.id'))
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    value: Mapped[str] = mapped_column(JSON, nullable=False)
    gen_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    username: Mapped[User] = relationship(back_populates="configurations")

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"name = {self.name}, "
                f"value = {self.value}, "
                f"user_id = {self.user_id}, "
                f"user = {self.username}>")
