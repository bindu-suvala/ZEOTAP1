class AlertSystem:
    def __init__(self):
        self.thresholds = {
            'temp': 35  # degrees Celsius
        }

    def check_alerts(self, data):
        if data['temp'] > self.thresholds['temp']:
            print(f"Alert: {data['city']} has exceeded temperature threshold with {data['temp']}°C")
