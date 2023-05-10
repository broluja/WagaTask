"""Weather Data Schemas module"""
from pydantic import BaseModel
from app.places.schemas import PlaceSchemaOut


class WeatherDataSchema(BaseModel):
    """Schema for Weather Data"""
    name: str

    class Config:
        """Configuration Class"""
        orm_mode = True


class WeatherDataSchemaOut(BaseModel):
    """Schema Out for Weather data."""
    date: str
    min_temp: float | None
    max_temp: float | None
    max_wind_speed: float | None
    precipitation_sum: float | None
    is_measured: int

    class Config:
        """Configuration Class"""
        orm_mode = True


class WeatherDataDifferencesSchema(BaseModel):
    """Weather differences schema."""

    place: PlaceSchemaOut

    date: str
    min_temp_differences: float | None
    max_temp_differences: float | None
    max_wind_speed_differences: float | None
    precipitation_sum_differences: float | None

    class Config:
        """Configuration Class"""
        orm_mode = True

