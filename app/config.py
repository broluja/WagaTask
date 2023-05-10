"""Configuration module"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class for storing settings data."""
    CITY_LAT_AND_LONG: str
    ARCHIVE_DAY_WIND_SPEED: str
    ARCHIVE_DAY_PRECIPITATION: str
    ARCHIVE_DAY_MIN_TEMP: str
    ARCHIVE_DAY_MAX_TEMP: str
    FORECASTED_WIND_SPEED: str
    FORECASTED_PRECIPITATION: str
    FORECASTED_MIN_TEMP: str
    FORECASTED_MAX_TEMP: str

    class Config:
        """Configuration Class"""
        env_file = './.env'


settings = Settings()
