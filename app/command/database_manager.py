import sqlite3
from sqlite3 import IntegrityError

HOME_LOCATION = "./weather_data.db"


class DatabaseManager(object):
    """
    Class for interaction with db table 'weather_data'.
    """
    INSTRUCTION_ONE = "CREATE TABLE IF NOT EXISTS places(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, " \
                      "country TEXT, admin1 TEXT, admin2 TEXT, UNIQUE(name, country, admin1, admin2)) "

    INSTRUCTION_TWO = "CREATE TABLE IF NOT EXISTS weather_data(id INTEGER PRIMARY KEY AUTOINCREMENT, place_id " \
                      "INTEGER NOT NULL, date TEXT, min_temp REAL, max_temp REAL, max_wind_speed REAL, " \
                      "precipitation_sum REAL, is_measured INTEGER, " \
                      "FOREIGN KEY (place_id) REFERENCES places (id)," \
                      "UNIQUE(place_id, date, is_measured))"

    def __init__(self):
        self.conn = sqlite3.connect(HOME_LOCATION)
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
            print(f'File closed but an exception appeared: {str(exc_type)}')
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
        self.conn = sqlite3.connect(HOME_LOCATION)
        self.cursor = self.conn.cursor()

    def get_or_create_place(self, city: dict) -> int:
        name, country = city.get("name"), city.get("country")
        admin1, admin2 = city.get("admin1", "N/A"), city.get("admin2", "N/A")
        city = self.get_place(name, country, admin1, admin2)
        if not city:
            self.cursor.execute('INSERT INTO places (name, country, admin1, admin2) VALUES(?, ?, ?, ?);',
                                (name, country, admin1, admin2))
            return self.cursor.lastrowid
        return city[0]

    def get_place(self, name, country, admin1, admin2):
        city = self.cursor.execute(
            "SELECT id, name, country, admin1, admin2 FROM places WHERE name=? AND country=? AND admin1=? AND admin2=?;",
            (name, country, admin1, admin2)).fetchone()
        return city

    def write_to_weather_data(self, city_id, day, min_t, max_t, wind_speed, precipitation, is_measured=0) -> None:
        try:
            self.cursor.execute(
                """INSERT INTO weather_data (place_id, date, min_temp, max_temp, max_wind_speed, 
                precipitation_sum, is_measured) VALUES(?, ?, ?, ?, ?, ?, ?);""",
                (city_id, day, min_t, max_t, wind_speed, precipitation, is_measured)
            )
        except IntegrityError as exc:
            print(f"Data for {day} already exists.")
