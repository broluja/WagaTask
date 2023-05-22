"""Place Service module"""
from itertools import chain
from collections import Counter

from app.db import SessionLocal
from app.places.exceptions import NoCityDifferencesException
from app.places.models import Place
from app.places.repositories import PlaceRepository
from app.weather_data.repositories import WeatherDataRepository
from app.weather_data.models import WeatherData
from app.weather_data.utils import get_data_differences
from app.weather_data.schemas import WeatherDataDifferencesSchema


class PlaceServices:
    """Service for User routes."""
    @staticmethod
    def get_place_data_differences(name: str):
        try:
            with SessionLocal() as db:
                place_repository = PlaceRepository(db, Place)
                places = place_repository.read_place_by_name(name)  # Get all places for given name.
                weather_data_repository = WeatherDataRepository(db, WeatherData)
                schemas_to_return = []
                for place in places:
                    dates = weather_data_repository.read_all_dates_for_place(place_id=place.id)  # Get data for place.
                    print(dates)
                    flatten_list = list(chain(*dates))  # Flatten the list
                    date_count = Counter(flatten_list)  # Count the number of single date appearance.
                    for date in date_count:
                        if date_count[date] == 2:  # If there is two dates, then date has measured and forecasted data.
                            objects = weather_data_repository.read_data_by_place_id_and_date(place.id, date)
                            min_temp, max_temp, wind_speed, precipitation = get_data_differences(objects[0], objects[1])
                            schema = WeatherDataDifferencesSchema(
                                place=place,
                                date=date,
                                min_temp_differences=min_temp,
                                max_temp_differences=max_temp,
                                max_wind_speed_differences=wind_speed,
                                precipitation_sum_differences=precipitation)
                            schemas_to_return.append(schema)
                if not schemas_to_return:
                    raise NoCityDifferencesException
                return schemas_to_return
        except Exception as exc:
            raise exc
