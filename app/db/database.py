"""Database settings module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQLITE_URL = 'sqlite:///weather_data.db'

engine = create_engine(SQLITE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
