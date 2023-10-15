"""Configuration."""
from decouple import config
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm.session import sessionmaker

# APP
# -----------------------------------------------------------------------------
APP_PORT = config("APP_PORT", cast=int)
DB_CONNECTION = config("DB_CONNECTION")
# DB
# -----------------------------------------------------------------------------
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_DATABASE = config("DB_DATABASE")
DB_USERNAME = config("DB_USERNAME")
DB_PASSWORD = config("DB_PASSWORD")
# ORM
Base = declarative_base()
engine: Engine = create_engine(
    f"{DB_CONNECTION}://"
    f"{DB_USERNAME}:"
    f"{DB_PASSWORD}@"
    f"{DB_HOST}/"
    f"{DB_DATABASE}", echo=False)
print("-" * 80)
session = sessionmaker(engine)()
