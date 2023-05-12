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
    weather_data = None

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

    def create_weather_data_example(self, date: str):
        with TestingSessionLocal() as db:
            repository = WeatherDataRepository(db, WeatherData)
            obj = repository.create(
                {
                    "place_id": self.city.id,
                    "date": date,
                    "min_temp": 11.1,
                    "max_temp": 22.2,
                    "max_wind_speed": 10.8,
                    "precipitation_sum": 12.2,
                    "is_measured": 1
                }
            )
            self.weather_data = obj

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

    def test_read_weather_data_by_place_id(self):
        self.create_city_example()
        self.create_weather_data_example("2023-05-05")
        with TestingSessionLocal() as db:
            repository = WeatherDataRepository(db, WeatherData)
            objects = repository.read_data_by_place_id(self.city.id)
        assert objects[0].place_id == self.city.id
        assert objects[0].date == self.weather_data.date
        assert objects[0].min_temp == self.weather_data.min_temp
        assert objects[0].max_temp == self.weather_data.max_temp
        assert objects[0].max_wind_speed == self.weather_data.max_wind_speed
        assert objects[0].precipitation_sum == self.weather_data.precipitation_sum
        assert objects[0].is_measured == self.weather_data.is_measured

    def test_read_weather_data_by_place_id_fail(self):
        self.create_city_example()
        self.create_weather_data_example("2023-05-05")
        with pytest.raises(BaseAPPException):
            with TestingSessionLocal() as db:
                repository = WeatherDataRepository(db, WeatherData)
                repository.read_data_by_place_id(2)

    def test_read_data_by_place_id_and_date(self):
        self.create_city_example()
        self.create_weather_data_example("2023-05-05")
        with TestingSessionLocal() as db:
            repository = WeatherDataRepository(db, WeatherData)
            objects = repository.read_data_by_place_id_and_date(self.city.id, self.weather_data.date)
        assert objects[0].place_id == self.city.id
        assert objects[0].date == self.weather_data.date
        assert objects[0].min_temp == self.weather_data.min_temp
        assert objects[0].max_temp == self.weather_data.max_temp
        assert objects[0].max_wind_speed == self.weather_data.max_wind_speed
        assert objects[0].precipitation_sum == self.weather_data.precipitation_sum
        assert objects[0].is_measured == self.weather_data.is_measured

    def test_read_data_by_place_id_and_date_fail(self):
        self.create_city_example()
        self.create_weather_data_example("2023-05-05")
        with TestingSessionLocal() as db:
            repository = WeatherDataRepository(db, WeatherData)
            objects = repository.read_data_by_place_id_and_date(2, self.weather_data.date)
        assert len(objects) == 0

    def test_read_all_dates_for_place(self):
        self.create_city_example()
        self.create_weather_data_example("2023-05-05")
        self.create_weather_data_example("2023-05-06")
        self.create_weather_data_example("2023-05-07")
        with TestingSessionLocal() as db:
            repository = WeatherDataRepository(db, WeatherData)
            objects = repository.read_all_dates_for_place(self.city.id)
        assert len(objects) == 3
