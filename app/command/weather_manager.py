"""Module containing all necessary endpoints."""
from typing import List

import requests
import datetime

from model import DatabaseManager


class WeatherManager:

    ARCHIVE_DAY_WIND_SPEED = "https://archive-api.open-meteo.com/v1/archive?latitude={}&longitude={}&start_date={}" \
                             "&end_date={}&hourly=temperature_2m&daily=windspeed_10m_max&timezone={}"

    ARCHIVE_DAY_PRECIPITATION = "https://archive-api.open-meteo.com/v1/archive?latitude={}&longitude={}&" \
                                "start_date={}&end_date={}&hourly=temperature_2m&daily=precipitation_sum&timezone={}"

    ARCHIVE_DAY_MIN_TEMP = "https://archive-api.open-meteo.com/v1/archive?latitude={}&longitude={}&" \
                           "start_date={}&end_date={}&hourly=temperature_2m&daily=temperature_2m_min&timezone={}"

    ARCHIVE_DAY_MAX_TEMP = "https://archive-api.open-meteo.com/v1/archive?latitude={}&longitude={}&" \
                           "start_date={}&end_date={}&hourly=temperature_2m&daily=temperature_2m_max&timezone={}"

    FORECASTED_WIND_SPEED = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&start_date={}" \
                            "&end_date={}&daily=windspeed_10m_max&timezone={}"

    FORECASTED_PRECIPITATION = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&start_date={}" \
                               "&end_date={}&daily=precipitation_sum&timezone={}"

    FORECASTED_MIN_TEMP = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&start_date={}" \
                          "&end_date={}&daily=temperature_2m_min&timezone={}"

    FORECASTED_MAX_TEMP = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&start_date={}" \
                          "&end_date={}&daily=temperature_2m_max&timezone={}"

    def __init__(self):
        self.manager = DatabaseManager()
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

    def get_data(self, days, latitude, longitude, timezone):
        past_days, future_days = self.process_days(days)
        for day in past_days:
            print(f"For day {day} collected following data: ")
            print(self.get_data_from_archive(latitude, longitude, day, timezone))
        for day in future_days:
            print(f"For day {day} collected following data: ")
            print(self.get_forecasted_data(latitude, longitude, day, timezone))

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
