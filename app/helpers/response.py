"""Class to handle API response"""
from typing import Any


class ApiResponse:
    """Class to handle API response"""
    _success = False
    message: str | None = None
    data: Any | None = None

    @property
    def success(self):
        """success"""
        return self._success

    @success.setter
    def success(self, value):
        if not isinstance(value, bool):
            raise TypeError("success must be boolean")
        self._success = value

    def serialize(self):
        """Serialize object"""
        return {
            "success": self._success,
            "message": self.message,
            "data": self.data
        }
