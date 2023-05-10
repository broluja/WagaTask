"""Weather Data Service module"""
from app.db import SessionLocal
from app.weather_data.models import WeatherData
from app.weather_data.repositories import WeatherDataRepository


class WeatherDataService:
    """Service for User routes."""
    @staticmethod
    def get_all_data():
        try:
            with SessionLocal() as db:
                repository = WeatherDataRepository(db, WeatherData)
                return repository.read_all()
        except Exception as exc:
            raise exc

    @staticmethod
    def get_by_place_id(place_id: int):
        try:
            with SessionLocal() as db:
                repository = WeatherDataRepository(db, WeatherData)
                return repository.read_data_by_place_id(place_id)
        except Exception as exc:
            raise exc
