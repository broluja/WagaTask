"""Weather Data Schemas module"""
from pydantic import BaseModel


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
        