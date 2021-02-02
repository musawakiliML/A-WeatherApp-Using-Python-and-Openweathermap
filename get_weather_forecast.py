import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime
from api_key import API_KEY

degree_sign = u'\N{DEGREE SIGN}'

open_weather_map = pyowm.OWM(API_KEY)

def three_hour_forecast(place, interval):
    open_weather_manager = open_weather_map.weather_manager()
    forecaster = open_weather_manager.forecast_at_place(place,interval)

    forecast = forecaster.forecast

    weather_list = forecast.weathers
    
    print('Three hours forecast (Times are in GMT):')

    for weather in weather_list:
        temp = weather.temperature(unit='fahrenheit')['temp']
        print(weather.reference_time('iso'),f"Temperature:{temp} {degree_sign}F")

three_hour_forecast("bauchi",'3h')

def weather_at_time(user_time, place, interval):
    open_weather_manager = open_weather_map.weather_manager()
    forecaster = open_weather_manager.forecast_at_place(place, interval)

    time = datetime.now() + timedelta(days = 0, hours=12)
    weather = forecaster.get_weather_at(time)
    temperature = weather.temperature(unit="fahrenheit")['temp']

    print(f'The temperature at {time.strftime("%Y-%m-%d %H:%M:%S")} is {temperature}{degree_sign}F')

    time = timestamps.tomorrow(user_time,0)
    weather = forecaster.get_weather_at(time)
    temperature = weather.temperature(unit='fahrenheit')['temp']
    print(f"The temperature at {time} is {temperature}{degree_sign}F")


weather_at_time(12, 'Los Angeles','3h')
