"""Migration script for the database."""
import sqlalchemy
from sqlalchemy import text

from app.helpers.random_person import Person
from app.models.configuration import Configuration
from app.models.user import User
from config import (
    USER_1_EMAIL,
    USER_1_FIRST_NAME,
    USER_1_LAST_NAME,
    USER_1_USERNAME,
    Base,
    engine,
    session,
)


def test_connection():
    """Test the connection to the database."""
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())


def create_tables(drop_all=True):
    """Create tables."""
    if drop_all:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def create_user():
    """Practice using the connection."""
    user = session.query(User).filter_by(id=1).first()
    if user:
        person = Person()
        user = User(username=person.username, first_name=person.first_name,
                    last_name=person.last_name, email=person.email)
    else:
        user = User(username=USER_1_USERNAME, first_name=USER_1_FIRST_NAME,
                    last_name=USER_1_LAST_NAME, email=USER_1_EMAIL)
    session.add(user)


def get_last_user():
    """Practice using the connection."""
    user = session.query(User).order_by(sqlalchemy.desc(User.id)).first()
    print(user)


def create_configuration(value="test"):
    """Practice using the connection."""
    configuration = Configuration(
        name=value, value={"test": value}, user_id=1)
    session.add(configuration)


def get_last_configuration():
    """Practice using the connection."""
    configuration = session.query(Configuration).order_by(
        sqlalchemy.desc(Configuration.id)).first()
    print(configuration)


def main():
    """Main entry point of the app."""
    test_connection()
    create_tables(drop_all=False)
    create_user()
    create_configuration()
    get_last_user()
    get_last_configuration()
    session.commit()


if __name__ == "__main__":
    main()
