"""Module containing all necessary endpoints."""
from typing import List

import requests
import datetime

from database_manager import DatabaseManager
from app.config import settings as sttg


class WeatherManager:

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

    def process_days(self, days: List[datetime.date]):
        """
        Given a list of days, function returns one list of past days and list of future days (including today)

        Param days: List of date objects
        Return: tuple
        """
        past_days = [date for date in days if date < self.current_day]
        future_days = [date for date in days if date >= self.current_day]
        return past_days, future_days

    def write_data(self, city_id, days, latitude, longitude, timezone):
        past_days, future_days = self.process_days(days)
        for day in past_days:
            min_t, max_t, wind_speed, precipitation = self.get_data_from_archive(latitude, longitude, day, timezone)
            with self.data_agent as manager:
                manager.write_to_weather_data(city_id, day, min_t[0], max_t[0], wind_speed[0], precipitation[0], is_measured=1)
        for day in future_days:
            min_t, max_t, wind_speed, precipitation = self.get_forecasted_data(latitude, longitude, day, timezone)
            with self.data_agent as manager:
                manager.write_to_weather_data(city_id, day, min_t[0], max_t[0], wind_speed[0], precipitation[0])

    def get_data_from_archive(self, latitude, longitude, day, timezone):
        wind_speed = requests.get(
            self.ARCHIVE_DAY_WIND_SPEED.format(latitude, longitude, day, day, timezone)
        )
        wind_speed = wind_speed.json()["daily"].get("windspeed_10m_max")
        precipitation = requests.get(
            self.ARCHIVE_DAY_PRECIPITATION.format(latitude, longitude, day, day, timezone)
        )
        precipitation_data = precipitation.json()["daily"].get("precipitation_sum")
        min_temp = requests.get(
            self.ARCHIVE_DAY_MIN_TEMP.format(latitude, longitude, day, day, timezone)
        )
        min_t = min_temp.json()["daily"].get("temperature_2m_min")
        max_temp = requests.get(
            self.ARCHIVE_DAY_MAX_TEMP.format(latitude, longitude, day, day, timezone)
        )
        max_t = max_temp.json()["daily"].get("temperature_2m_max")
        return min_t, max_t, wind_speed, precipitation_data

    def get_forecasted_data(self, latitude, longitude, day, timezone):
        wind_speed = requests.get(
            self.FORECASTED_WIND_SPEED.format(latitude, longitude, day, day, timezone)
        )
        wind_speed = wind_speed.json()["daily"].get("windspeed_10m_max")
        precipitation = requests.get(
            self.FORECASTED_PRECIPITATION.format(latitude, longitude, day, day, timezone)
        )
        precipitation_data = precipitation.json()["daily"].get("precipitation_sum")
        min_temp = requests.get(
            self.FORECASTED_MIN_TEMP.format(latitude, longitude, day, day, timezone)
        )
        min_t = min_temp.json()["daily"].get("temperature_2m_min")
        max_temp = requests.get(
            self.FORECASTED_MAX_TEMP.format(latitude, longitude, day, day, timezone)
        )
        max_t = max_temp.json()["daily"].get("temperature_2m_max")
        return min_t, max_t, wind_speed, precipitation_data

    def record_data(self, city_object, days):
        lat, long, timezone = city_object.get("latitude"), city_object.get("longitude"), city_object.get("timezone")
        with self.data_agent as manager:
            city_id = manager.get_or_create_place(city_object)
        self.write_data(city_id, days, lat, long, timezone)
        print("Data recorded.")


weather_manager = WeatherManager()
