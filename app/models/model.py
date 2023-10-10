"""model class."""
from typing import Any
from sqlalchemy import exc as sqlalchemy_exc
from config.config import Base, Session


class Model(Base):
    """User class."""

    __abstract__ = True
    _prefix = "ofc_"

    def __str__(self) -> str:
        """Return string representation."""
        return str(self.__dict__)

    def set(self) -> None:
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

    def get(self, **kwargs: Any) -> list[Any]:
        """Get user from database."""
        session = Session()
        try:
            query = session.query(self.__class__).filter_by(**kwargs).all()
            print(query)
            return query
        except Exception as error:
            session.rollback()
            raise error
        finally:
            session.close()
