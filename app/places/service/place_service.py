"""Place Service module"""
from app.db import SessionLocal
from app.places.models import Place
from app.places.repositories import PlaceRepository


class PlaceServices:
    """Service for User routes."""
    @staticmethod
    def get_place_data_differences(name):
        try:
            with SessionLocal() as db:
                repository = PlaceRepository(db, Place)
                places = repository.read_place_by_name(name)
                return places
        except Exception as exc:
            raise exc
