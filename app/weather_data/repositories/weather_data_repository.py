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

    def read_data_by_place_id_and_date(self, place_id, date):
        try:
            data = self.db.query(WeatherData).filter(WeatherData.place_id == place_id).filter(
                WeatherData.date == date).all()
            return data
        except Exception as exc:
            self.db.rollback()
            raise exc

    def read_all_dates_for_place(self, place_id):
        try:
            dates = self.db.query(WeatherData.date).filter(WeatherData.place_id == place_id).all()
            return dates
        except Exception as exc:
            self.db.rollback()
            raise exc
