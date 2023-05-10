"""Weather Data Controller module"""
from fastapi import HTTPException

from app.base import BaseAPPException
from app.weather_data.service import WeatherDataService


class WeatherDataController:
    """Controller for Place routes"""
    @staticmethod
    def get_all_data():
        try:
            return WeatherDataService.get_all_data()
        except BaseAPPException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message_to_user) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_by_place_id(place_id: int):
        try:
            return WeatherDataService.get_by_place_id(place_id)
        except BaseAPPException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message_to_user) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
