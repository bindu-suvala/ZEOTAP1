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
