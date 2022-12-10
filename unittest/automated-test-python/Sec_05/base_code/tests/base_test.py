"""
Base Test


This class should be the parent class to each non-unit test.
It allows for instantiation of the databases dynamically
and makes sure that it is a new blank database each time.

You have to make sure that each test is not using a db with data on it.
"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):

    def setUp(self) -> None:
        # Make sure database exists
        # Get a test client
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        # If, for example 'sqlite:///testdb.db' is used, a db file will be created.
        # This will create a blank SQLite file on the current dir.
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self) -> None:
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
