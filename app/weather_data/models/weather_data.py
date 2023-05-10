"""Weather Data Model module"""
from sqlalchemy import Column, String, Integer, UniqueConstraint, Float, ForeignKey

from app.db import Base


class WeatherData(Base):
    """Base Model for Weather Data"""
    __tablename__ = "weather_data"
    __table_args__ = (UniqueConstraint("place_id", "date", "is_measured", name="weather_data_constraint"),)

    id = Column(Integer(), primary_key=True)
    place_id = Column(Integer(), ForeignKey('places.id'))
    date = Column(String(15))
    min_temp = Column(Float())
    max_temp = Column(Float())
    max_wind_speed = Column(Float())
    precipitation_sum = Column(Float())
    is_measured = Column(Integer())

    def __init__(
            self,
            place_id: int,
            date: str,
            min_temp: float,
            max_temp: float,
            max_wind_speed: float,
            precipitation_sum: float,
            is_measured: int
    ):
        self.place_id = place_id
        self.date = date
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.max_wind_speed = max_wind_speed
        self.precipitation_sum = precipitation_sum
        self.is_measured = is_measured
