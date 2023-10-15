"""Configuration model."""
from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.user import User
from config.config import Base


class Configuration(Base):
    """Configuration model."""
    __tablename__ = "ofc_configuration"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    value: Mapped[str] = mapped_column(JSON, nullable=False)
    gen_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey('ofc_user.id'))
    username: Mapped[User] = relationship(back_populates="configurations")

    def __str__(self):
        """String representation of the model."""
        return f"<id={self.id}, name={self.name}, value={self.value}, user_id={self.user_id}, username={self.username}>"
