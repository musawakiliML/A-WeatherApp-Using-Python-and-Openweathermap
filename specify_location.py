import pyowm
from api_key import API_KEY

open_weather_map = pyowm.OWM(API_KEY)
open_weather_manager = open_weather_map.weather_manager()

def city_name(place):

    weather_observation = open_weather_manager.weather_at_place(place)

    weather = weather_observation.weather

    temperature = weather.temperature(unit='kelvin')['temp']

    return temperature


def city_id(place_id):
    
    weather_observation = open_weather_manager.weather_at_id(place_id)

    weather = weather_observation.weather

    temperature = weather.temperature(unit='fahrenheit')['temp']

    return temperature

def lat_lon_coordinates(lat, lon):
    weather_observation = open_weather_manager.weather_at_coords(lat, lon)

    weather = weather_observation.weather

    temperature = weather.temperature(unit='fehrenhiet')['temp']

    return temperature

def zip_codes(zip_code,country):
    weather_observation = open_weather_manager.weather_at_zip_code(zip_code, country)

    weather = weather_observation.weather

    temperature = weather.temperature(unit='fahrenheit')['temp']

    return temperature



