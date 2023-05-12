"""Test weather data module"""
import pytest

from app.base import BaseAPPException
from app.places.models import Place
from app.tests import TestClass, TestingSessionLocal
from app.places.repositories import PlaceRepository
from app.weather_data.models import WeatherData
from app.weather_data.repositories import WeatherDataRepository


class TestWeatherDataRepo(TestClass):
    """Test Places functionalities."""
    city = None

    def create_city_example(self):
        with TestingSessionLocal() as db:
            repository = PlaceRepository(db, Place)
            obj = repository.create(
                {
                    "name": "Belgrade",
                    "country": "Serbia",
                    "admin1": "Belgrade",
                    "admin2": "Belgrade"
                }
            )
        self.city = obj

    def test_create_weather_data(self):
        self.create_city_example()
        with TestingSessionLocal() as db:
            repository = WeatherDataRepository(db, WeatherData)
            obj = repository.create(
                {
                    "place_id": self.city.id,
                    "date": "2023-05-05",
                    "min_temp": 11.1,
                    "max_temp": 22.2,
                    "max_wind_speed": 10.8,
                    "precipitation_sum": 12.2,
                    "is_measured": 1
                }
            )
        assert obj.place_id == self.city.id
        assert obj.date == "2023-05-05"
        assert obj.min_temp == 11.1
        assert obj.max_temp == 22.2
        assert obj.max_wind_speed == 10.8
        assert obj.precipitation_sum == 12.2
        assert obj.is_measured == 1
