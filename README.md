# Weather Monitoring System

## Overview
This project implements a real-time weather monitoring system using Java. It leverages Kafka for message streaming, Spring Boot for building the REST API, and OpenWeatherMap API for weather data retrieval.

## Project Structure
Refer to the [Project Structure](#project-structure) section for a detailed view of the project layout.

## Setup Instructions
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/weather-monitoring-system.git
    cd weather-monitoring-system
    ```

2. **Build the Project**:
    ```bash
    ./mvnw clean install
    ```

3. **Run the Application**:
    ```bash
    ./mvnw spring-boot:run
    ```

4. **Access the Weather API**:
    Open your browser and go to:
    ```
    http://localhost:8080/weather?city=Delhi
    ```

## Configuration
- Replace `YOUR_API_KEY` in `WeatherAPI.java` with your actual OpenWeatherMap API key.

## Testing
- Unit tests are located in the `src/test/java/com/tati/backend` directory. Run tests using:
    ```bash
    ./mvnw test
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## How to Upload to GitHub
1. Create a new repository on GitHub.
2. Initialize a local Git repository in your project folder:
    ```bash
    git init
    ```
3. Add all files to the staging area:
    ```bash
    git add .
    ```
4. Commit your changes:
    ```bash
    git commit -m "Initial commit of weather monitoring system"
    ```
5. Add the remote repository:
    ```bash
    git remote add origin https://github.com/yourusername/weather-monitoring-system.git
    ```
6. Push your code to GitHub:
    ```bash
    git push -u origin master
    ```

Now your project should be live on GitHub! If you have any questions or need further assistance, feel free to ask.
