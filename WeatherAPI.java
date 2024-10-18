package com.tati.api;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class WeatherAPI {
    private final String apiKey = "YOUR_API_KEY";
    private final String apiUrl = "https://api.openweathermap.org/data/2.5/weather";

    public String getWeather(String city) {
        RestTemplate restTemplate = new RestTemplate();
        String url = apiUrl + "?q=" + city + "&appid=" + apiKey;
        return restTemplate.getForObject(url, String.class);
    }
}
