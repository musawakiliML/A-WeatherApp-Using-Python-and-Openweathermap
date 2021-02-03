#This program collect weather status and info from openweather map api

# Getting libraries and API Key
import pyowm
from api_key import API_KEY

# creating the openweather map instance
# you must pass the API key as an argument to the method OWM
open_weather_map = pyowm.OWM(API_KEY)
open_weather_manager = open_weather_map.weather_manager() # weather manager instance, it contains the methods for getting weather value. 


# declaring function to accept (place) as an argument and return its weather status
# eg. place = 'bauchi', return[cold, clear]
def weather_status(place):
    # creating an observation instance of the weather manager, and calls the weather at place method to get the weather value
    weather_observation = open_weather_manager.weather_at_place(place)
    
    # creating an object of the weather obeservation 
    weather = weather_observation.weather

    status = weather.status
    detailed_status = weather.detailed_status

    return [status, detailed_status]

# declaring function to accept (place) as an argument and return its weather info
# like humidity, clouds.

def weather_info(place):
    weather_observation = open_weather_manager.weather_at_place(place)

    weather = weather_observation.weather

    # the variables declared will have boolean variables(True or False) based on the method call
    humidity = weather.humidity 
    clouds = weather.clouds
    
    # gets wind speed in kilometer per hour form
    wind = weather.wind(unit='km_hour')['speed']

    return [humidity, clouds, wind]
