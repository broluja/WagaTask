import sys
import os

from user_input import get_city, get_start_date, get_end_date, get_days
from app.base import BaseAPPException
from weather_manager import weather_manager

sys.path.append(os.getcwd())


def main():
    try:
        city_object = get_city()
        if not city_object:
            return print("Exiting...")
        start_date = get_start_date()
        if not start_date:
            return print("Exiting...")
        else:
            end_date = get_end_date(start_date)
        if not end_date:
            return print("Exiting...")
        print("Data collected.")
    except BaseAPPException as exc:
        print(exc, "", sep="\n")
    else:
        days = get_days(start_date, end_date)
        weather_manager.record_data(city_object, days)


if __name__ == "__main__":
    main()
