from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_CONNECTION = config("DB_CONNECTION")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
DB_DATABASE = config("DB_DATABASE")
DB_USERNAME = config("DB_USERNAME")
DB_PASSWORD = config("DB_PASSWORD")
engine = create_engine(
    f"{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
)
Base = declarative_base()
Session = sessionmaker(engine)
