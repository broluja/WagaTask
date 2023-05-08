"""Module containing all necessary endpoints."""
import requests

CITY_LAT_AND_LONG = "https://geocoding-api.open-meteo.com/v1/search?name="
DAY_FROM_ARCHIVE_WITH_WIND_SPEED = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date={}&end_date={}&hourly=temperature_2m&daily=windspeed_10m_max&timezone={}"
DAY_FROM_ARCHIVE_WITH_PRECIPITATION_SUM = "https://archive-api.open-meteo.com/v1/archive?latitude=52.52&longitude=13.41&start_date={}&end_date={}&hourly=temperature_2m&daily=precipitation_sum&timezone={}"

FORECASTED_MAX_WIND_SPEED = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&start_date={}&end_date={}&daily=windspeed_10m_max&timezone={}}"
FORECASTED_PERCIPITATION = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&start_date={}&end_date={}&daily=precipitation_sum&timezone={}}"


def get_city() -> dict:
    cities = input("Enter city: ")
    endpoint = CITY_LAT_AND_LONG + "%20".join(cities.split())
    response = requests.get(endpoint)
    results = response.json().get("results", None)
    if results:
        print("Select desired city from options below:")
        for index, result in enumerate(results, start=1):
            print(f"Option {index}: {result.get('name', '')}, {result.get('country', '')}, {result.get('admin1','')}, {result.get('admin2', '')}")
        city = input("Enter option or b for choosing different city: ")
        if city.lower().strip() == "b":
            return get_city()
        while city.strip() not in (str(i) for i in range(1, len(results) + 1)):
            print("Invalid option. Available options are:")
            for index, result in enumerate(results, start=1):
                print(f"Option {index}: {result.get('name', '')}, {result.get('country', '')}, {result.get('admin1', '')}, {result.get('admin2', '')}")
            city = input("Enter option or b for choosing different city: ")
            if city.lower().strip() == "b":
                return get_city()
        return results[int(city) - 1]
    else:
        option = input("Unknown city. Press any key for choosing another city or 'Q' for exit: ")
        if option.upper() == "Q":
            return {"latitude": None, "longitude": None}
        return get_city()


selected = get_city()
print(f"Selected latitude and longitude: {selected['latitude']} / {selected['longitude']}")
