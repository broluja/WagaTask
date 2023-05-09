import requests
from requests.exceptions import ConnectionError
import datetime

from app.base import BaseAPPException
from app.command.exceptions import UnsuccessfulConnectionError
from app.validators.validators import validate_start_date, validate_end_date
from app.config import settings as sttg

CITY_LAT_AND_LONG = sttg.CITY_LAT_AND_LONG


def print_available_cities(message, results: dict) -> None:
    """
    Prompt user for correct option.

    Return: None.
    """
    print(message, "-" * 50, sep="\n")
    for index, result in enumerate(results, start=1):
        print(f"Option {index}: {result.get('name', '')}, {result.get('country', '')}, {result.get('admin1', '')}, "
              f"{result.get('admin2', '')}")
    print("-" * 50)


def get_city() -> dict | bool:
    """
    Ask for places and get Latitude and Longitude for user's places.

    Return: a places object or False if User decides to quit.
    """
    cities = input("Enter places: ")
    endpoint = CITY_LAT_AND_LONG + "%20".join(cities.strip().split())
    try:
        response = requests.get(endpoint)
    except ConnectionError as exc:
        raise UnsuccessfulConnectionError from exc
    results = response.json().get("results", None)
    if results:
        print_available_cities("Select desired places from options below:", results)
        city = input("Enter option or b for choosing different places: ")
        if city.lower().strip() == "b":
            return get_city()
        while city.strip() not in (str(i) for i in range(1, len(results) + 1)):
            print_available_cities("Invalid option. Available options are:", results)
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
    date = input("Enter start date or 'q' for exit: ")
    if date.lower().strip() == 'q':
        return False
    try:
        validate_start_date(date)
    except BaseAPPException as exc:
        print(exc)
        return get_start_date()
    return date


def get_end_date(start_date: str) -> str | bool:
    """
    Get end date from User.

    Return: validated date string or False if User decides to quit.
        """
    date = input("Enter end date or 'q' for exit: ")
    if date.lower().strip() == 'q':
        return False
    try:
        validate_end_date(start_date, date)
    except BaseAPPException as exc:
        print(exc)
        return get_end_date(start_date)
    return date


def get_days(start, end):
    """
    Get all the days between start and end date.

    Return: list of date objects.
    """
    start_date = datetime.date.fromisoformat(start)
    end_date = datetime.date.fromisoformat(end)
    delta = end_date - start_date
    return [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
