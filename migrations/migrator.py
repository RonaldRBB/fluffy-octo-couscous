"""Migrator for the database."""
import time

from app.models.configuration import Configuration
from app.models.user import User
from config.config import Base, engine


def test_user(value="test"):
    """Test user."""
    user = User()
    user.username = value
    user.email = f"{value}@test.com"
    user.set()


def test_configuration(value="test"):
    """Test configuration."""
    configuration = Configuration()
    configuration.name = value
    configuration.value = {"value": value}
    configuration.description = value
    configuration.set()


def main():
    """Main function."""
    Base.metadata.create_all(engine)
    test_value = str(time.time())
    test_user(test_value)
    test_configuration(test_value)


if __name__ == "__main__":
    main()
