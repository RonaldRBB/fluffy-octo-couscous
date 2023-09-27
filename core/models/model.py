"""model class."""
from sqlalchemy import exc as sqlalchemy_exc
from core.config import Base, Session


class Model(Base):
    """User class."""

    __abstract__ = True

    def set(self):
        """Save user in database."""
        session = Session()
        try:
            session.add(self)
            session.commit()
        except sqlalchemy_exc.IntegrityError as error:
            session.rollback()
            raise error
        except Exception as error:
            session.rollback()
            raise error
        finally:
            session.close()
