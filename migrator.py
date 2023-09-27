"""Migrator for the database."""
import time

from core.config import Base, engine
from core.models.user import User
from core.models.configuration import Configuration


def main():
    Base.metadata.create_all(engine)
    user = User()
    name = str(time.time())
    user.username = name
    user.email = f"{name}@test.com"
    user.set()
    configuration = Configuration()
    configuration.name = name
    configuration.value = {name: name}
    configuration.description = name
    configuration.set()


if __name__ == "__main__":
    main()
