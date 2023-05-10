"""Place Model module"""
from sqlalchemy import Column, String, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db import Base


class Place(Base):
    """Base Model for Place"""
    __tablename__ = "places"
    __table_args__ = (UniqueConstraint("name", "country", "admin1", "admin2", name="place_constraint"),)

    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
    country = Column(String(100))
    admin1 = Column(String(100))
    admin2 = Column(String(100))

    data = relationship("WeatherData", lazy='subquery')

    def __init__(self, name: str, country: str, admin1: str, admin2: str):
        self.name = name
        self.country = country
        self.admin1 = admin1
        self.admin2 = admin2
