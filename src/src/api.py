import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, cities):
        weather_data = {}
        for city in cities:
            response = requests.get(self.base_url, params={'q': city, 'appid': self.api_key, 'units': 'metric'})
            if response.status_code == 200:
                weather_data[city] = response.json()
        return weather_data
