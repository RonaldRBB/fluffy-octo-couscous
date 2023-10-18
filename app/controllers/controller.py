"""Abstract class controller"""
from abc import abstractmethod


class Controller:
    """Abstract class controller."""
    @abstractmethod
    def create(self):
        """Create"""
    @abstractmethod
    def get(self, oid):
        """Get"""
    @abstractmethod
    def get_all(self):
        """Get all"""
    @abstractmethod
    def update(self, oid):
        """Update"""
    @abstractmethod
    def delete(self, oid):
        """Delete"""
