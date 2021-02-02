import pyowm
from api_key import API_KEY

open_weather_map = pyowm.OWM(API_KEY)
open_weather_manager = open_weather_map.weather_manager()


def weather_status(place):
    weather_observation = open_weather_manager.weather_at_place(place)

    weather = weather_observation.weather

    status = weather.status
    detailed_status = weather.detailed_status

    return [status, detailed_status]

def weather_info(place):
    weather_observation = open_weather_manager.weather_at_place(place)

    weather = weather_observation.weather

    humidity = weather.humidity
    clouds = weather.clouds
    wind = weather.wind(unit='km_hour')['speed']

    return [humidity, clouds, wind]

