import os
import sqlite3

HOME_LOCATION = os.getcwd()

class DatabaseManager(object):
    """
    Class for interaction with database table 'weather_data'.
    """
    INSTRUCTION = "CREATE TABLE IF NOT EXISTS weather_data(place_name TEXT UNIQUE, date TEXT, min_temp REAL, " \
                  "max_temp REAL, max_wind_speed REAL, precipitation_sum REAL, is_measured INTEGER)"

    def __init__(self):
        self.conn = sqlite3.connect(f'{HOME_LOCATION}/weather_data.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.INSTRUCTION)
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

    def __str__(self):
        return f'Weather Manager for {self.conn}'

    def __repr__(self):
        return f'{type(self).__name__}()'

    @staticmethod
    def get_model(player):
        pass

    def commit(self):
        """
        Saving and committing into a database.
        Return: None.
        """
        self.conn.commit()
        self.conn.close()

    def connect(self):
        """
        Connecting to database.
        Return: None.
        """
        self.conn = sqlite3.connect('minesweeper.db')
        self.cursor = self.conn.cursor()

    def write_from_input(self, weather_data):
        print("Database updated...")


database_manager = DatabaseManager()
