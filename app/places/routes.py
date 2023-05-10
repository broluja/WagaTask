"""Place routes module"""
from typing import List
from fastapi import APIRouter

from app.places.schemas import PlaceSchemaOut
from app.places.controller import PlaceController

weather_router = APIRouter(prefix="/api/places", tags=["Places"])


@weather_router.get("/", summary="City input", response_model=List[PlaceSchemaOut])
def get_city_data_differences(place: str):
    return PlaceController.get_place_data_differences(place.title())
