import sqlite3
from sqlite3 import IntegrityError
from config import settings as sttg
from user_input import mprint

DB_LOCATION = sttg.DB_LOCATION


class DatabaseManager(object):
    """
    Class for interaction with a database 'weather_data.db'.
    """
    INSTRUCTION_ONE = "CREATE TABLE IF NOT EXISTS places(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, " \
                      "country TEXT, admin1 TEXT, admin2 TEXT, UNIQUE(name, country, admin1, admin2)) "

    INSTRUCTION_TWO = "CREATE TABLE IF NOT EXISTS weather_data(id INTEGER PRIMARY KEY AUTOINCREMENT, place_id " \
                      "INTEGER NOT NULL, date TEXT, min_temp REAL, max_temp REAL, max_wind_speed REAL, " \
                      "precipitation_sum REAL, is_measured INTEGER, " \
                      "FOREIGN KEY (place_id) REFERENCES places (id)," \
                      "UNIQUE(place_id, date, is_measured))"

    def __init__(self):
        self.conn = sqlite3.connect(DB_LOCATION)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.INSTRUCTION_ONE)
        self.cursor.execute(self.INSTRUCTION_TWO)
        self.commit()

    def __enter__(self):  # Implementing context manager
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.commit()
        else:
            self.commit()
            mprint(f'File closed but an exception appeared: {str(exc_type)}')
            return False

    def __repr__(self):
        return f'{type(self).__name__}()'

    def commit(self):
        """
        Saving and committing into a db.
        Return: None.
        """
        self.conn.commit()
        self.conn.close()

    def connect(self):
        """
        Connecting to db.
        Return: None.
        """
        self.conn = sqlite3.connect(DB_LOCATION)
        self.cursor = self.conn.cursor()

    def get_or_create_place(self, city: dict) -> int:
        """
        Get or create places if not exists.

        Param places: Dictionary containing citi data.
        Return: ID of created or existing places object.
        """
        name, country = city.get("name"), city.get("country")
        admin1, admin2 = city.get("admin1", "N/A"), city.get("admin2", "N/A")
        city = self.get_place(name, country, admin1, admin2)
        if not city:
            self.cursor.execute('INSERT INTO places (name, country, admin1, admin2) VALUES(?, ?, ?, ?);',
                                (name, country, admin1, admin2))
            return self.cursor.lastrowid
        return city[0]

    def get_place(self, name: str, country: str, admin1: str, admin2: str) -> dict:
        """
        Function retrieves place from database by name, country, admin1 and admin2.

        Param name: name of the place.
        Param country: country of place.
        Param admin1: municipality.
        Param admin2: municipality.
        Return: Place object.
        """
        city = self.cursor.execute(
            "SELECT id, name, country, admin1, admin2 FROM places WHERE name=? AND country=? AND admin1=? AND admin2=?",
            (name, country, admin1, admin2)).fetchone()
        return city

    def write_to_weather_data(
            self,
            city_id: int,
            day: str,
            min_t: float,
            max_t: float,
            wind_speed: float,
            precipitation: float,
            is_measured: int = 0
    ) -> None:
        """
        Record weather data.

        Param city_id: ID of place
        Param day: date.
        Param min_t: minimum temperature for the date.
        Param max_t: maximum temperature for the date.
        Param wind_speed: wind speed.
        Param precipitation: precipitation sum.
        Param is_measured: bool, True if data is measured, and False if it is forecasted.
        Return: None.
        """
        try:
            self.cursor.execute(
                """INSERT INTO weather_data (place_id, date, min_temp, max_temp, max_wind_speed, 
                precipitation_sum, is_measured) VALUES(?, ?, ?, ?, ?, ?, ?);""",
                (city_id, day, min_t, max_t, wind_speed, precipitation, is_measured)
            )
        except IntegrityError as exc:
            mprint(f"Data for {day} already exists.")
