"""Configuration."""
from decouple import config
from sqlalchemy import create_engine, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
APP_PORT: int = config("APP_PORT")
DB_CONNECTION: str = config("DB_CONNECTION")
DB_HOST: str = config("DB_HOST")
DB_PORT: int = config("DB_PORT")
DB_DATABASE: str = config("DB_DATABASE")
DB_USERNAME: str = config("DB_USERNAME")
DB_PASSWORD: str = config("DB_PASSWORD")
engine = create_engine(
    f"{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
)
Base = declarative_base()
Session = sessionmaker(engine)
shared_sequence = Sequence("shared_sequence")
