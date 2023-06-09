from app.weather_data.schemas import WeatherDataSchemaOut


def get_data_differences(data_object_one: WeatherDataSchemaOut, data_object_two: WeatherDataSchemaOut):
    try:
        min_temp_diff = round(abs(data_object_one.min_temp - data_object_two.min_temp), 2)
    except TypeError:
        min_temp_diff = None
    try:
        max_temp_diff = round(abs(data_object_one.max_temp - data_object_two.max_temp), 2)
    except TypeError:
        max_temp_diff = None
    try:
        max_wind_speed_diff = round(abs(data_object_one.max_wind_speed - data_object_two.max_wind_speed), 2)
    except TypeError:
        max_wind_speed_diff = None
    try:
        precipitation_sum_diff = round(abs(data_object_one.precipitation_sum - data_object_two.precipitation_sum), 2)
    except TypeError:
        precipitation_sum_diff = None
    return min_temp_diff, max_temp_diff, max_wind_speed_diff, precipitation_sum_diff
