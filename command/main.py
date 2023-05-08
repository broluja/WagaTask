from user_input import get_city, get_start_date, get_end_date
from exceptions import UserInputException
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
    except UserInputException as exc:
        print(exc)
    else:
        WeatherManager().get_day_from_archive(latitude, longitude, [start_date, end_date], timezone)


if __name__ == "__main__":
    main()
