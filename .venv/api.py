# This file contains the code for the API request from OpenWeather
# Import statements for modules required for API call
import os
import requests
from dotenv import load_dotenv

# Creating a dictionary of destinations with their name, latitude and longitude
destinations = [
    {"name" : "lake_district_national_park", "lat" : "54.4609", "lon" : "-3.0886"},
    {"name" : "corfe_castle", "lat" : "50.6395", "lon" : "-2.0566"},
    {"name" : "the_cotswolds", "lat" : "51.8330", "lon" : "-1.8433"},
    {"name" : "cambridge", "lat" : "52.2053", "lon" : "0.1218"},
    {"name" : "bristol", "lat" : "51.4545", "lon" : "-2.5879"},
    {"name" : "oxford", "lat" : "51.7520", "lon" : "-1.2577"},
    {"name" : "norwich", "lat" : "52.6309", "lon" : "-1.2974"},
    {"name" : "stonehenge", "lat" : "51.1789", "lon" : "-1.8262"},
    {"name" : "watergate_bay", "lat" : "50.4429", "lon" : "-5.0553"},
    {"name" : "birmingham", "lat" : "52.4862", "lon" : "-1.8904"}
]

# Creating a list to store JSON weather data
weather_data = []

# Creating variable for exclusions in API call per OpenWeather URL format
part = 'minutely,hourly,daily,alert'

# Function to access API key stored separately for security
load_dotenv(dotenv_path="/Users/reneemundie/PythonProjects/api-weather-map/.venv/key.env")
api_key = os.getenv('API_KEY')

# Function to update API URL & make API request
def get_weather_data():
    for i in range(len(destinations)):
        lat = (destinations[i]["lat"])
        lon = (destinations[i]["lon"])
        api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"
        response = requests.get(f"{api_url}")             
        if response.status_code == 200:
            data = response.json()
            weather_data.append(data)
        else:
            print(f"Failed to fetch weather data, {response.status_code} error with your request")
    return weather_data