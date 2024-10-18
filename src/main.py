import time
from api import WeatherAPI
from processing import WeatherProcessor
from alerts import AlertSystem

def main():
    api = WeatherAPI(api_key='YOUR_API_KEY')
    processor = WeatherProcessor()
    alerts = AlertSystem()

    while True:
        weather_data = api.get_weather(['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad'])
        for city, data in weather_data.items():
            processed_data = processor.process(data)
            alerts.check_alerts(processed_data)
        
        time.sleep(300)  # Wait for 5 minutes

if __name__ == "__main__":
    main()
