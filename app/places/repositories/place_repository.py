"""Place Repository module"""
from app.base import BaseCRUDRepository
from app.places.models import Place


class PlaceRepository(BaseCRUDRepository):
    """Repository for User Model"""
    def read_place_by_name(self, name: str):
        try:
            return self.db.query(Place).filter(Place.name == name).all()
        except Exception as exc:
            self.db.rollback()
            raise exc
