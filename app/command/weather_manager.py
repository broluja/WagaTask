"""Module containing all necessary endpoints."""
from typing import List
import requests
import datetime

from user_input import mprint
from database_manager import DatabaseManager
from config import settings as sttg


class WeatherManager:
    """Class for accessing Weather Forecast API."""

    ARCHIVE_DAY_WIND_SPEED = sttg.ARCHIVE_DAY_WIND_SPEED
    ARCHIVE_DAY_PRECIPITATION = sttg.ARCHIVE_DAY_PRECIPITATION
    ARCHIVE_DAY_MIN_TEMP = sttg.ARCHIVE_DAY_MIN_TEMP
    ARCHIVE_DAY_MAX_TEMP = sttg.ARCHIVE_DAY_MAX_TEMP
    FORECASTED_WIND_SPEED = sttg.FORECASTED_WIND_SPEED
    FORECASTED_PRECIPITATION = sttg.FORECASTED_PRECIPITATION
    FORECASTED_MIN_TEMP = sttg.FORECASTED_MIN_TEMP
    FORECASTED_MAX_TEMP = sttg.FORECASTED_MAX_TEMP

    def __init__(self):
        self.data_agent = DatabaseManager()
        self.current_day = datetime.date.today()

    def process_days(self, days: List[datetime.date]) -> tuple:
        """
        Given a list of days, function returns one list of past days and list of future days (including today)

        Param days: List of date objects
        Return: tuple
        """
        past_days = [date for date in days if date < self.current_day]
        future_days = [date for date in days if date >= self.current_day]
        return past_days, future_days

    def write_data(self, city_id: int, days: list, latitude: float, longitude: float, tz: str) -> None:
        """
        Function splits an array of dates to past and future days for reaching different endpoints.

        Param city_id: ID of place.
        Param days: list of dates.
        Param latitude: latitude of place.
        Param longitude: longitude of place.
        Param tz: timezone.
        Return: None.
        """
        past_days, future_days = self.process_days(days)
        if past_days:
            min_t, max_t, wind_speed, precipitation = self.get_data_from_archive(latitude, longitude, past_days, tz)
            for index, day in enumerate(past_days):
                with self.data_agent as manager:
                    manager.write_to_weather_data(city_id, day, min_t[index], max_t[index], wind_speed[index],
                                                  precipitation[index], is_measured=1)
        if future_days:
            min_t, max_t, wind_speed, precipitation = self.get_forecasted_data(latitude, longitude, future_days, tz)
            for index, day in enumerate(future_days):
                with self.data_agent as manager:
                    manager.write_to_weather_data(city_id, day, min_t[index], max_t[index], wind_speed[index],
                                                  precipitation[index])

    def get_data_from_archive(self, latitude: float, longitude: float, days: list, timezone: str) -> tuple:
        """
        Function takes necessary parameters to get weather data from archive.

        Param latitude: latitude of place.
        Param longitude: longitude of place.
        Param days: list of dates.
        Param timezone: place's timezone.
        Return: tuple.
        """
        wind_speed = requests.get(
            self.ARCHIVE_DAY_WIND_SPEED.format(latitude, longitude, days[0], days[-1], timezone)
        )
        wind_speed = wind_speed.json()["daily"].get("windspeed_10m_max")
        precipitation = requests.get(
            self.ARCHIVE_DAY_PRECIPITATION.format(latitude, longitude, days[0], days[-1], timezone)
        )
        precipitation_data = precipitation.json()["daily"].get("precipitation_sum")
        min_temp = requests.get(
            self.ARCHIVE_DAY_MIN_TEMP.format(latitude, longitude, days[0], days[-1], timezone)
        )
        min_t = min_temp.json()["daily"].get("temperature_2m_min")
        max_temp = requests.get(
            self.ARCHIVE_DAY_MAX_TEMP.format(latitude, longitude, days[0], days[-1], timezone)
        )
        max_t = max_temp.json()["daily"].get("temperature_2m_max")
        return min_t, max_t, wind_speed, precipitation_data

    def get_forecasted_data(self, latitude: float, longitude: float, days: list, timezone: str) -> tuple:
        """
        Function takes necessary parameters to get weather data forecast.

        Param latitude: latitude of place.
        Param longitude: longitude of place.
        Param days: list of dates.
        Param timezone: place's timezone.
        Return: tuple.
        """
        wind_speed = requests.get(
            self.FORECASTED_WIND_SPEED.format(latitude, longitude, days[0], days[-1], timezone)
        )
        wind_speed = wind_speed.json()["daily"].get("windspeed_10m_max")
        precipitation = requests.get(
            self.FORECASTED_PRECIPITATION.format(latitude, longitude, days[0], days[-1], timezone)
        )
        precipitation_data = precipitation.json()["daily"].get("precipitation_sum")
        min_temp = requests.get(
            self.FORECASTED_MIN_TEMP.format(latitude, longitude, days[0], days[-1], timezone)
        )
        min_t = min_temp.json()["daily"].get("temperature_2m_min")
        max_temp = requests.get(
            self.FORECASTED_MAX_TEMP.format(latitude, longitude, days[0], days[-1], timezone)
        )
        max_t = max_temp.json()["daily"].get("temperature_2m_max")
        return min_t, max_t, wind_speed, precipitation_data

    def record_data(self, city_object: dict, days: list) -> None:
        """
        Function records data to DB.

        Param city_object: a city object.
        Param days: list of dates.
        Return: None.
        """
        lat, long, timezone = city_object.get("latitude"), city_object.get("longitude"), city_object.get("timezone")
        with self.data_agent as manager:
            city_id = manager.get_or_create_place(city_object)
        self.write_data(city_id, days, lat, long, timezone)
        mprint("Finished.")


weather_manager = WeatherManager()
