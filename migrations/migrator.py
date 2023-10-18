"""Migration script for the database."""
import sqlalchemy
from sqlalchemy import text

from app.models.activity import Activity
from app.models.body import Body
from app.models.configuration import Configuration
from app.models.heartrate import Heartrate
from app.models.sport import Sport
from app.models.user import User
from app.models.user_health import UserHealth
from config import (
    Base,
    engine,
    session,
)


def test_connection():
    """Test the connection to the database."""
    with engine.connect() as conn:
        result = conn.execute(text("select 'connection successful'"))
        print(result.all())


def create_tables(drop_all=True):
    """Create tables."""
    if drop_all:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_last_user():
    """Practice using the connection."""
    user = session.query(User).order_by(sqlalchemy.asc(User.id)).first()
    print(user.get_dict())


def get_last_configuration():
    """Practice using the connection."""
    configuration = session.query(Configuration).order_by(
        sqlalchemy.desc(Configuration.id)).first()
    print(configuration)


def get_last_activity():
    """Practice using the connection."""
    activity = session.query(Activity).order_by(
        sqlalchemy.desc(Activity.id)).first()
    print(activity)


def get_last_body():
    """Practice using the connection."""
    body = session.query(Body).order_by(
        sqlalchemy.desc(Body.id)).first()
    print(body)


def get_last_heartrate():
    """Practice using the connection."""
    heartrate = session.query(Heartrate).order_by(
        sqlalchemy.desc(Heartrate.id)).first()
    print(heartrate)


def get_last_sport():
    """Practice using the connection."""
    sport = session.query(Sport).order_by(
        sqlalchemy.desc(Sport.id)).first()
    print(sport)


def get_last_user_health():
    """Practice using the connection."""
    user_health = session.query(UserHealth).order_by(
        sqlalchemy.desc(UserHealth.id)).first()
    print(user_health)


def main():
    """Main entry point of the app."""
    test_connection()
    # create_tables(drop_all=True)
    get_last_user()
    print("-"*100)
    # get_last_configuration()
    # get_last_activity()
    # get_last_body()
    # get_last_heartrate()
    # get_last_sport()
    # get_last_user_health()
    print("-"*100)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
