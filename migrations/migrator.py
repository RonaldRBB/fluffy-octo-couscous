"""Migration script for the database."""
import sqlalchemy
from sqlalchemy import text

from app.models import (
    Activity,
    Body,
    Configuration,
    Exercise,
    ExerciseInfo,
    HeartRate,
    Session,
    User,
    UserHealth,
    Workout,
)
from config import (
    Base,
    engine,
    session,
)


def test_connection():
    """Test the connection to the database."""
    with engine.connect() as conn:
        result = conn.execute(text("select 'connection successful'"))
        print(f" * {result.all()}")


def create_tables(drop_all=True):
    """Create tables."""
    if drop_all:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_last_user():
    """Practice using the connection."""
    user = session.query(User).order_by(sqlalchemy.asc(User.id)).first()
    print(f" * {user}")


def get_last_configuration():
    """Practice using the connection."""
    configuration = session.query(Configuration).order_by(
        sqlalchemy.desc(Configuration.id)).first()
    print(f" * {configuration}")


def get_last_activity():
    """Practice using the connection."""
    activity = session.query(Activity).order_by(
        sqlalchemy.desc(Activity.id)).first()
    print(f" * {activity}")


def get_last_body():
    """Practice using the connection."""
    body = session.query(Body).order_by(
        sqlalchemy.desc(Body.id)).first()
    print(f" * {body}")


def get_last_heartrate():
    """Practice using the connection."""
    heart_rate = session.query(HeartRate).order_by(
        sqlalchemy.desc(HeartRate.id)).first()
    print(f" * {heart_rate}")


def get_last_session():
    """Practice using the connection."""
    session = session.query(Session).order_by(
        sqlalchemy.desc(Session.id)).first()
    print(f" * {session}")


def get_last_user_health():
    """Practice using the connection."""
    user_health = session.query(UserHealth).order_by(
        sqlalchemy.desc(UserHealth.id)).first()
    print(f" * {user_health}")


def main():
    """Main entry point of the app."""
    test_connection()
    create_tables(drop_all=True)
    get_last_user()
    # get_last_configuration()
    # get_last_activity()
    # get_last_body()
    get_last_heartrate()
    # get_last_session()
    # get_last_user_health()
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
