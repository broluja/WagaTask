"""Weather Data Schemas module"""
from pydantic import BaseModel


class WeatherDataSchema(BaseModel):
    """Schema for Weather Data"""
    name: str

    class Config:
        """Configuration Class"""
        orm_mode = True
