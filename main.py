import requests
import datetime as dt
from mesures_converter import kelvin_to_celcius, miles_to_km

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('api_key','r').read()
CITY = input("Browse for your weather city: ")

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url)
j = response.json()
main = j['main']
weather = j['weather']
wind = j['wind']
sys = j['sys']

temp = main['temp']
feels_like = main['feels_like']
tmax = main['temp_max']
tmin = main['temp_min']
humidity = main["humidity"]

desc = weather[0]['description']

wind_speed = wind['speed']

sunrise = dt.datetime.utcfromtimestamp(j['sys']['sunrise'] + j['timezone'])
sunset = dt.datetime.utcfromtimestamp(j['sys']['sunset'] + j['timezone'])

print(f"""\nWeather Service\n
City: {CITY.title()}, Country:{j['sys']['country']}
Temperature: {kelvin_to_celcius(temp):.2f} C° -- Feels like: {kelvin_to_celcius(feels_like):.2f} C°
Temp max: {kelvin_to_celcius(tmax):.2f} C° -- Temp min: {kelvin_to_celcius(tmin):.2f} C°
humidity: {humidity}%
Description: {desc}
Wind Speed: {miles_to_km(wind_speed):.2f} km/h
Sunrise: {sunrise} -- Sunset: {sunset}""")