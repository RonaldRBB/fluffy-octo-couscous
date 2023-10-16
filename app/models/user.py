"""User model."""""
from datetime import datetime

# from app.models.configuration import Configuration
from typing import List

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import Base

# from app.models.configuration import Configuration


class User(Base):
    """User model."""
    __tablename__ = "foc_user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(30), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    configurations: Mapped[List["Configuration"]] = relationship(
        "Configuration", back_populates="username")
    gen_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"username = {self.username}, "
                f"email = {self.email}, "
                f"configurations = {len(self.configurations)}, "
                f"gen_date = {self.gen_date}>")
