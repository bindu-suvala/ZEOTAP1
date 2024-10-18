package com.tati.controller;

import com.tati.api.WeatherAPI;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class WeatherController {
    @Autowired
    private WeatherAPI weatherAPI;

    @GetMapping("/weather")
    public String getWeather(@RequestParam String city) {
        return weatherAPI.getWeather(city);
    }
}
