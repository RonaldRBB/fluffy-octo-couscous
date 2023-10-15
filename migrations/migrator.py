"""Migration script for the database."""
import random

import sqlalchemy
from sqlalchemy import text

from app.helpers.random_person import Person
from app.models.configuration import Configuration
from app.models.user import User
from config.config import Base, engine, session


def test_connection():
    """Test the connection to the database."""
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())


def create_tables():
    """Create tables."""
    Base.metadata.create_all(engine)


def create_user():
    """Practice using the connection."""
    person = Person()
    user = User(username=person.username, email=person.email)
    session.add(user)


def create_configuration(value="testt"):
    """Practice using the connection."""
    configuration = Configuration(
        name=value, value={"test": value}, user_id=random.randint(1, 10))
    session.add(configuration)


def get_last_configuration():
    """Practice using the connection."""
    configuration = session.query(Configuration).order_by(
        sqlalchemy.desc(Configuration.id)).first()
    print(configuration)


def main():
    """Main entry point of the app."""
    # test_connection()
    # create_tables()
    # create_user()
    # create_configuration()
    get_last_configuration()
    session.commit()


if __name__ == "__main__":
    main()
