"""Place Repository module"""
from app.base import BaseCRUDRepository
from app.weather_data.models import WeatherData
from app.weather_data.exceptions import NoCityDataException


class WeatherDataRepository(BaseCRUDRepository):
    """Repository for User Model"""

    def read_data_by_place_id(self, place_id):
        try:
            data = self.db.query(WeatherData).filter(WeatherData.place_id == place_id).all()
            if not data:
                raise NoCityDataException
            return data
        except Exception as exc:
            self.db.rollback()
            raise exc
