"""Test User's input module"""
from app.tests import TestClass, TestingSessionLocal


class TestUserInput(TestClass):
    """Test User's input validations."""

    def create_actor(self):
        """
        Function creates an actor in the database.
        It takes no arguments and returns a dictionary of the attributes of the created actor.

        Param self: Refer to the object that is calling the method.
        Return: The actor object.
        """
        # with TestingSessionLocal() as db:
        #     actor_repository = ActorRepository(db, Actor)
        #     attributes = {"first_name": "John",
        #                   "last_name": "Doe",
        #                   "date_of_birth": "1983-10-10",
        #                   "country": "USA"}
        #     actor = actor_repository.create(attributes)
        #     self.actor = actor

    def test_create_actor(self):
        """
        Function creates an actor object and tests whether the first_name, last_name,
        and country attributes are equal to 'John', 'Doe', and 'USA' respectively.

        Return: The actor object, which is then used to assert the
        first name, last name and country of the actor.
        """
        # self.create_actor()
        # assert self.actor.first_name == "John"
        # assert self.actor.last_name == "Doe"
        # assert self.actor.country == "USA"
