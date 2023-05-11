"""Place routes module"""
from typing import List
from fastapi import APIRouter

from app.weather_data.schemas import WeatherDataDifferencesSchema
from app.places.controller import PlaceController

weather_router = APIRouter(prefix="/api/places", tags=["Places"])


@weather_router.get(
    "/",
    summary="City input",
    description="On given city, return differences between measured and forecasted data if available.",
    response_model=List[WeatherDataDifferencesSchema]
)
def get_city_data_differences(place: str):
    return PlaceController.get_place_data_differences(place.title())
