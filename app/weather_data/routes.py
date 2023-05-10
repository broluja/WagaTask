"""Weather Data routes module"""
from typing import List
from fastapi import APIRouter

from app.weather_data.schemas import WeatherDataSchemaOut
from app.weather_data.controller import WeatherDataController

weather_data_router = APIRouter(prefix="/api/weather_data", tags=["WeatherData"])


@weather_data_router.get("/", summary="Get all data", response_model=List[WeatherDataSchemaOut])
def get_all_data():
    return WeatherDataController.get_all_data()


@weather_data_router.get("/place", summary="Get weather data by place name", response_model=List[WeatherDataSchemaOut])
def get_by_place_id(place_id: int):
    return WeatherDataController.get_by_place_id(place_id)