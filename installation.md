# Real-Time Weather Monitoring System

## Overview
This project is a real-time weather monitoring system that retrieves weather data from the OpenWeatherMap API for various cities in India. It processes this data to provide summarized insights using rollups and aggregates, triggers alerts based on user-defined thresholds, and visualizes the results.

## Features
- Continuous retrieval of weather data every 5 minutes.
- Calculation of daily weather summaries, including:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- Alerting system for temperature thresholds.
- Visualization of temperature data over time.

## Installation

### Prerequisites
- Python 3.x
- An OpenWeatherMap API key (sign up at [OpenWeatherMap](https://openweathermap.org/))

### Dependencies
To install the required Python packages, run:
```bash
pip install -r requirements.txt

```
### configuration

1.Replace YOUR_API_KEY in weather_monitor.py with your actual OpenWeatherMap API key.

2.Update email settings in the send_email_alert method to use your email provider's SMTP settings.

### Usage

Run the application using:
```bash
python weather_monitor.py

```
The application will start fetching weather data for the specified cities and processing it in real-time.

### Testing

1.System Setup: Ensure the application connects to the OpenWeatherMap API using a valid API key.

2.Data Retrieval: Verify that weather data is retrieved correctly for specified locations.

3.Temperature Conversion: Check the conversion of temperature values from Kelvin to Celsius.

4.Daily Weather Summary: Simulate weather updates and verify daily summaries are calculated correctly.

5.Alerting Thresholds: Test alert functionality by defining temperature thresholds and simulating weather data.

### Bonus Features

Support for additional weather parameters (e.g., humidity, wind speed).

Retrieval of weather forecasts and summary generation based on predicted conditions.
