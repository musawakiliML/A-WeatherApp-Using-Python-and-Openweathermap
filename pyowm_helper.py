import pyowm
from datetime import datetime
from timezone_conversion import gmt_to_eastern
from api_key import API_KEY

open_weather_map = pyowm.OWM(API_KEY)
open_weather_manager = open_weather_map.weather_manager()


def get_temperature(place, interval):
    days = []
    dates = []
    temp_min = []
    temp_max = []

    forecaster = open_weather_manager.forecast_at_place(place, interval)
    forecast = forecaster.forecast

    for weather in forecast:
        day = gmt_to_eastern(weather.reference_time())
        date = day.date()
        if date not in dates:
            dates.append(date)
            temp_min.append(None)
            temp_max.append(None)
            days.append(date)
        temperature = weather.temperature(unit='fahrenheit')['temp']
        if not temp_min[-1] or temperature < temp_min[-1]:
            temp_min[-1] = temperature
        if not temp_max[-1] or temperature > temp_max[-1]:
            temp_max[-1] = temperature
    
    return [days, temp_min, temp_max]

if __name__ == '__main__':
    get_temperature('los angeles','3h')