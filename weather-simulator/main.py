import random
import time
import json

def generate_weather_data(
        min_temperature=8, 
        mode_temperature=12,
        max_temperature=20, 
        min_humidity=40, 
        max_humidity=90, 
        min_wind_speed=0.5,
        max_wind_speed=10
    ):
    # for a better simulation of temp, I'm using triangular distribution which is a better representation of the temperature data then uniform distribution / random.randint().
    # for even more realistic data, could use the normal distribution ie. numpy's  - np.random.normal(loc=12, scale=4)  
    temperature = random.triangular(min_temperature, max_temperature, mode_temperature)  
    humidity = random.randint(min_humidity, max_humidity)
    wind_speed = random.uniform(min_wind_speed, max_wind_speed)

    return {
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed
    }


if __name__ == "__main__":
    import os

    while True:
        weather_data = generate_weather_data()
        with open("weather_data.json", "w") as f:
            json.dump(weather_data, f)

        time.sleep(3)
