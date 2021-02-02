import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime
from api_key import API_KEY

open_weather_map = pyowm.OWM(API_KEY)
open_weather_manager = open_weather_map.weather_manager()

def weather_condition(place, interval):
    forecaster = open_weather_manager.forecast_at_place(place, interval)
    print(forecaster.will_have_fog())
    print(forecaster.will_have_clouds())
    print(forecaster.will_have_rain())
    print(forecaster.will_be_rainy_at(timestamps.tomorrow(12)))
    print(forecaster.will_be_stormy_at(timestamps.tomorrow(12)))
    print(forecaster.will_be_earth)

weather_condition('Bauchi','3h')

