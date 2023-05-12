"""Test Class module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.db import Base

SQLITE_TEST_URL = 'sqlite:///weather_data_test.db'

engine = create_engine(SQLITE_TEST_URL, echo=True)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)


class TestClass:
    """Class for running tests."""

    @staticmethod
    def setup_method():
        """
        Setup any state tied to the execution of the given method in a class.
        This method is invoked for every test method of a class.
        """
        Base.metadata.create_all(bind=engine)

    @staticmethod
    def teardown_method():
        """Teardown any state that was previously setup with a setup method call."""
        Base.metadata.drop_all(bind=engine)
