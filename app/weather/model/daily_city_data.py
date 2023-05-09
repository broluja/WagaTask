from uuid import uuid4
from sqlalchemy import Column, String, Boolean, Float

from app.db import Base


class DailyCityData(Base):
    """Base Model for User"""
    __tablename__ = "cities"
    id = Column(String(50), primary_key=True, default=uuid4)
    place_name = Column(String(100))
    date = Column(String(15))
    min_temp = Column(Float)
    max_temp = Column(Float)
    max_wind_speed = Column(Float)
    precipitation_sum = Column(Float)
    is_measured = Column(Boolean)

    def __init__(self, place_name: str, date: str, min_temp: float, max_temp: float, max_wind_speed: float,
                 precipitation_sum: float, is_measured: bool):
        self.place_name = place_name
        self.date = date
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.max_wind_speed = max_wind_speed
        self.precipitation_sum = precipitation_sum
        self.is_measured = is_measured
