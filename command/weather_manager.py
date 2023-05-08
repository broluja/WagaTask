"""Module containing all necessary endpoints."""
import requests


class WeatherManager:

    ARCHIVE_DAY_WIND_SPEED = "https://archive-api.open-meteo.com/v1/archive?latitude={}&longitude={}&start_date={}" \
                             "&end_date={}&hourly=temperature_2m&daily=windspeed_10m_max&timezone={}"
    ARCHIVE_DAY_PRECIPITATION = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&" \
                                "start_date={}&end_date={}&hourly=temperature_2m&daily=precipitation_sum&timezone={}"
    FORECASTED_WIND_SPEED = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&start_date={}" \
                            "&end_date={}&daily=windspeed_10m_max&timezone={}"
    FORECASTED_PRECIPITATION = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&start_date={}" \
                               "&end_date={}&daily=precipitation_sum&timezone={}}"

    def get_day_from_archive(self, latitude, longitude, days, timezone):
        wind_speed = requests.get(
            self.ARCHIVE_DAY_WIND_SPEED.format(latitude, longitude, days[0], days[1], timezone)
        )
        print(wind_speed.json())
