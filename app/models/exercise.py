"""Exercise model."""
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.exercise_info import ExerciseInfo
from config import DB_PREFIX, Base


class Exercise(Base):
    """Exercise model."""
    __tablename__ = f"{DB_PREFIX}_exercises"
    id: Mapped[int] = mapped_column(primary_key=True)
    _user_id: Mapped[int] = mapped_column(
        "user_id", ForeignKey(f"{DB_PREFIX}_users.id"))
    _exercise_info_id: Mapped[int] = mapped_column(
        "exercise_info_id", ForeignKey(f"{DB_PREFIX}_exercises_info.id"))
    _datetime: Mapped[datetime] = mapped_column(
        "date", DateTime, default=datetime.utcnow)
    _set: Mapped[int] = mapped_column("set", Integer, nullable=False)
    _reps: Mapped[int] = mapped_column("reps", Integer, nullable=False)
    _weight: Mapped[int] = mapped_column("weight", Integer, nullable=False)
    info: Mapped[ExerciseInfo] = relationship(
        "ExerciseInfo", back_populates="exercise"
    )
    user: Mapped["User"] = relationship("User", back_populates="exercises")

    def __str__(self):
        """String representation of the model."""
        return (f"<id = {self.id}, "
                f"datetime = {self.datetime}, "
                f"set = {self.set}, "
                f"reps = {self.reps}, "
                f"weight = {self.weight}, "
                f"user_id = {self.user_id}, "
                f"user = {self.user}>")

    def get_dict(self, with_relation=True):
        """Get dictionary representation of the model."""
        data = {
            "id": self.id,
            "datetime": self.datetime,
            "set": self.set,
            "reps": self.reps,
            "weight": self.weight,
            "user_id": self.user_id,
        }
        if with_relation:
            data["user"] = self.user.get_dict()
        return data

    @property
    def user_id(self) -> int:
        """User id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        self._user_id = value

    @property
    def exercise_info_id(self) -> int:
        """Exercise info id."""
        return self._exercise_info_id

    @exercise_info_id.setter
    def exercise_info_id(self, value: int) -> None:
        self._exercise_info_id = value

    @property
    def datetime(self) -> datetime:
        """Date."""
        return self._datetime

    @datetime.setter
    def datetime(self, value: datetime) -> None:
        self._datetime = value

    @property
    def set(self) -> int:
        """Set."""
        return self._set

    @set.setter
    def set(self, value: int) -> None:
        self._set = value

    @property
    def reps(self) -> int:
        """Reps."""
        return self._reps

    @reps.setter
    def reps(self, value: int) -> None:
        self._reps = value

    @property
    def weight(self) -> int:
        """Weight."""
        return self._weight

    @weight.setter
    def weight(self, value: int) -> None:
        self._weight = value
