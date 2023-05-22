"""Place Controller module"""
from fastapi import HTTPException

from app.base import BaseAPPException
from app.places.service import PlaceServices


class PlaceController:
    """Controller for Place routes"""
    @staticmethod
    def get_place_data_differences(place: str):
        try:
            return PlaceServices.get_place_data_differences(place)
        except BaseAPPException as exc:
            raise HTTPException(status_code=exc.status_code, detail=exc.message_to_user) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc
