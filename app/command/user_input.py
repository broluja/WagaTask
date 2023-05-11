import requests
from requests.exceptions import ConnectionError
import datetime

from exceptions import UserInputException, UnsuccessfulConnectionError, InvalidEndDateException
from validators import validate_start_date, validate_end_date
from config import settings as sttg

CITY_LAT_AND_LONG = sttg.CITY_LAT_AND_LONG


def mprint(*args, delimiter="-", end="\n", sep="\n") -> None:
    """
    Custom print function with two limit lines

    Param args: Message(s) for printing.
    Param delimiter: delimiter used for limit lines
    Param end: string appended after the last value, default a newline.
    Param sep: string inserted between values, default a new line.
    Return: None.
    """
    if len(args) == 1 and "\n" not in repr(args[0]):
        print(delimiter * 80, f"{args[0]:^80}", delimiter * 80, sep=sep, end=end)
    else:
        print(delimiter * 80, *args, delimiter * 80, sep=sep, end=end)


def print_available_cities(message: str, results: dict) -> None:
    """
    Prompt user for correct option.

    Return: None.
    """
    mprint(message)
    for index, result in enumerate(results, start=1):
        print(f"Option {index}: {result.get('name', '')}, {result.get('country', '')}, {result.get('admin1', '')}, "
              f"{result.get('admin2', '')}")


def get_city() -> dict | bool:
    """
    Ask for places and get Latitude and Longitude for user's places.

    Return: a places object or False if User decides to quit.
    """
    mprint("Weather Forecast API")
    cities = input("Enter place: ")
    endpoint = CITY_LAT_AND_LONG + "%20".join(cities.strip().split())
    try:
        response = requests.get(endpoint)
    except ConnectionError as exc:
        raise UnsuccessfulConnectionError from exc
    results = response.json().get("results", None)
    if results:
        print_available_cities("Select place from options below:", results)
        mprint()
        city = input("Enter option or b for choosing different places: ")
        if city.lower().strip() == "b":
            return get_city()
        while city.strip() not in (str(i) for i in range(1, len(results) + 1)):
            print_available_cities("Invalid option. Available options are:", results)
            mprint()
            city = input("Enter option or b for choosing different places: ")
            if city.lower().strip() == "b":
                return get_city()
        return results[int(city) - 1]
    else:
        option = input("Unknown places. Press any key for choosing another places or 'Q' for exit: ")
        return False if option.upper() == "Q" else get_city()


def get_start_date() -> str | bool:
    """
    Get start date from User.

    Return: validated date string or False if User decides to quit.
    """
    user_date = input("Enter START date (YYYY-MM-DD) or 'q' for exit: ")
    if user_date.lower().strip() == 'q':
        return False
    try:
        validate_start_date(user_date)
    except UserInputException as exc:
        mprint(str(exc))
        return get_start_date()
    return user_date


def get_end_date(start_date: str) -> str | bool:
    """
    Get end date from User.

    Return: validated date string or False if User decides to quit.
        """
    user_date = input("Enter END date (YYYY-MM-DD) or 'q' for exit: ")
    if user_date.lower().strip() == 'q':
        return False
    try:
        validate_end_date(start_date, user_date)
    except UserInputException as exc:
        mprint(str(exc))
        return get_end_date(start_date)
    return user_date


def get_days(start: str, end: str) -> list:
    """
    Get all the days between start and end date.

    Return: list of date objects.
    """
    try:
        start_date = datetime.date.fromisoformat(start)
        end_date = datetime.date.fromisoformat(end)
        delta = end_date - start_date
        return [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
    except ValueError as exc:
        raise InvalidEndDateException from exc
