from user_input import get_city, get_start_date, get_end_date, get_days
from app.base import BaseAPPException
from weather_manager import WeatherManager


def main():
    try:
        city_object = get_city()
        if not city_object:
            return print("Exiting...")
        latitude, longitude, timezone = city_object.get("latitude"), city_object.get("longitude"), city_object.get("timezone")
        start_date = get_start_date()
        if not start_date:
            return print("Exiting")
        else:
            end_date = get_end_date(start_date)
        if not end_date:
            return print("Exiting")
        print("Data collected.")
    except BaseAPPException as exc:
        print(exc)
    else:
        days = get_days(start_date, end_date)
        WeatherManager().get_data(days, latitude, longitude, timezone)


if __name__ == "__main__":
    main()
