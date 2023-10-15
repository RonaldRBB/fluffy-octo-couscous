"""User model."""""
from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.config import Base


class User(Base):
    """User model."""
    __tablename__ = "ofc_user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    configurations: Mapped[str] = relationship("Configuration", back_populates="username")
    gen_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __str__(self):
        """String representation of the model."""
        return f"<id={self.id}, username={self.username}, email={self.email}>"
