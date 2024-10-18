class WeatherProcessor:
    def process(self, data):
        return {
            'city': data['name'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'condition': data['weather'][0]['main'],
            'timestamp': data['dt']
        }

    def daily_summary(self, daily_data):
        # Placeholder for daily summary logic
        pass
