"""Food Macro model."""
from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from config import DB_PREFIX, Base


class FoodMacro(Base):
    """Food Macro model."""
    __tablename__ = f"{DB_PREFIX}_food_macros"
    id: Mapped[int] = mapped_column(primary_key=True)
    _name: Mapped[str] = mapped_column("name", String(30), nullable=False)
    _protein: Mapped[float] = mapped_column("protein", Float, nullable=False)
    _carbohydrate: Mapped[float] = mapped_column(
        "carbohydrate", Float, nullable=False
    )
    _fat: Mapped[float] = mapped_column("fat", Float, nullable=False)
    _calories: Mapped[float] = mapped_column("calories", Float, nullable=False)

    def __str__(self):
        return (f"<id = {self.id}, "
                f"name = {self.name}, "
                f"protein = {self.protein}, "
                f"carbohydrate = {self.carbohydrate}, "
                f"fat = {self.fat}, "
                f"calories = {self.calories}>")

    def get_dict(self):
        """JSON representation of the model."""
        return {
            "id": self.id,
            "name": self.name,
            "protein": self.protein,
            "carbohydrate": self.carbohydrate,
            "fat": self.fat,
            "calories": self.calories
        }

    @property
    def name(self) -> str:
        """Name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def protein(self) -> float:
        """Protein."""
        return self._protein

    @protein.setter
    def protein(self, value: float) -> None:
        self._protein = value

    @property
    def carbohydrate(self) -> float:
        """Carbohydrate."""
        return self._carbohydrate

    @carbohydrate.setter
    def carbohydrate(self, value: float) -> None:
        self._carbohydrate = value

    @property
    def fat(self) -> float:
        """Fat."""
        return self._fat

    @fat.setter
    def fat(self, value: float) -> None:
        self._fat = value

    @property
    def calories(self) -> float:
        """Calories."""
        return self._calories

    @calories.setter
    def calories(self, value: float) -> None:
        self._calories = value
