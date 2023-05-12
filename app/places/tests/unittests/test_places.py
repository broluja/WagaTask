"""Test places module"""
import pytest

from app.base import BaseAPPException
from app.places.models import Place
from app.tests import TestClass, TestingSessionLocal
from app.places.repositories import PlaceRepository


class TestPlaceRepo(TestClass):
    """Test Places functionalities."""

    def test_create_place(self):
        """
        Test creates a place in the database.

        Return: None.
        """
        with TestingSessionLocal() as db:
            repository = PlaceRepository(db, Place)
            obj = repository.create({
                "name": "Belgrade",
                "country": "Serbia",
                "admin1": "Belgrade",
                "admin2": "Belgrade"}
            )
        assert obj.name == "Belgrade"
        assert obj.country == "Serbia"
        assert obj.admin1 == "Belgrade"
        assert obj.admin2 == "Belgrade"

    def test_create_place_fail(self):
        """
        Test tries to create a place with invalid field types.

        Return: None.
        """
        with pytest.raises(Exception):
            with TestingSessionLocal() as db:
                repository = PlaceRepository(db, Place)
                repository.create({
                    "name": None,
                    "country": None,
                    "admin1": "Belgrade",
                    "admin2": "Belgrade"}
                )

    def test_read_place_by_id(self):
        with TestingSessionLocal() as db:
            repository = PlaceRepository(db, Place)
            obj = repository.create({
                "name": "Belgrade",
                "country": "Serbia",
                "admin1": "Belgrade",
                "admin2": "Belgrade"}
            )
            place = repository.read_by_id(obj.id)
        assert place.name == "Belgrade"
        assert place.country == "Serbia"
        assert place.admin1 == "Belgrade"
        assert place.admin2 == "Belgrade"

    def test_read_place_by_id_fail(self):
        with TestingSessionLocal() as db:
            with pytest.raises(BaseAPPException):
                repository = PlaceRepository(db, Place)
                repository.create({
                    "name": "Belgrade",
                    "country": "Serbia",
                    "admin1": "Belgrade",
                    "admin2": "Belgrade"}
                )
                repository.read_by_id(3)
