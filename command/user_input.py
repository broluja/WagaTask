import requests

from validators import *

CITY_LAT_AND_LONG = "https://geocoding-api.open-meteo.com/v1/search?name="


def print_available_cities(message, results: dict) -> None:
    print(message)
    for index, result in enumerate(results, start=1):
        print(f"Option {index}: {result.get('name', '')}, {result.get('country', '')}, {result.get('admin1', '')}, {result.get('admin2', '')}")


def get_city() -> dict | bool:
    cities = input("Enter city: ")
    endpoint = CITY_LAT_AND_LONG + "%20".join(cities.split())
    response = requests.get(endpoint)
    results = response.json().get("results", None)
    if results:
        print_available_cities("Select desired city from options below:", results)
        city = input("Enter option or b for choosing different city: ")
        if city.lower().strip() == "b":
            return get_city()
        while city.strip() not in (str(i) for i in range(1, len(results) + 1)):
            print_available_cities("Invalid option. Available options are:", results)
            city = input("Enter option or b for choosing different city: ")
            if city.lower().strip() == "b":
                return get_city()
        return results[int(city) - 1]
    else:
        option = input("Unknown city. Press any key for choosing another city or 'Q' for exit: ")
        return False if option.upper() == "Q" else get_city()


def get_start_date() -> str | bool:
    date = input("Enter start date or 'q' for exit: ")
    if date.lower().strip() == 'q':
        return False
    try:
        validate_start_date(date)
    except UserInputException as exc:
        print(exc)
        return get_start_date()
    return date


def get_end_date(start_date: str) -> str | bool:
    date = input("Enter end date or 'q' for exit: ")
    if date.lower().strip() == 'q':
        return False
    try:
        validate_end_date(start_date, date)
    except UserInputException as exc:
        print(exc)
        return get_end_date(start_date)
    return date


def get_days(start, end):
    start_date = datetime.date.fromisoformat(start)
    end_date = datetime.date.fromisoformat(end)
    delta = end_date - start_date
    return [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]
