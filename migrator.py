"""Migrator for the database."""
from core.models.user import User
from core.config import Base, engine


def main():
    Base.metadata.create_all(engine)
    user = User()
    user.username = "test"
    user.email = "test@test.com"
    user.set()


if __name__ == "__main__":
    main()
