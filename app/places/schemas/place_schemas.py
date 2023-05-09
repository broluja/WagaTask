"""Place Schemas module"""
from pydantic import BaseModel


class PlaceSchemaOut(BaseModel):
    name: str
    country: str
    admin1: str | None
    admin2: str | None

    class Config:
        """Configuration Class"""
        orm_mode = True
