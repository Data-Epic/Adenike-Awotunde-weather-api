import requests
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file one level up
load_dotenv()

# Get API key
api_key = os.getenv("API_KEY")
if api_key is None:
    print("API_KEY not found")
else:
    print(f"API Key: {api_key}")

def get_weather_data(response, city):
    """Fetch data from OpenWeatherMap API and return JSON."""
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for '{city}': {e}")
        if hasattr(response, 'status_code'):
            print(f"Status Code: {response.status_code}")
        return None

def get_current_weather(city):
    """Fetch and display current weather details for a given city."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric",
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    data = get_weather_data(response, city)

    if data:
        try:
            print(f"\nCurrent Weather in {data['name']}:")
            print(f"Temperature: {data['main']['temp']:.2f}°C")
            print(f"Condition: {data['weather'][0]['description'].capitalize()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        except KeyError:
            print(f"Could not retrieve complete weather data for '{city}'.")

def get_weather_forecast(city):
    """Fetch and display 5-day weather forecast for a given city."""
    forecast_base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "units": "metric",
        "appid": api_key
    }
    response = requests.get(forecast_base_url, params=params)
    data = get_weather_data(response, city)

    if data:
        print(f"\n5-Day Weather Forecast for {data.get('city', {}).get('name', city)}:")
        for forecast in data.get("list", [])[::8]:  # every 8th 3-hour step ≈ daily
            try:
                date = forecast["dt_txt"].split()[0]
                condition = forecast["weather"][0]["description"].capitalize()
                temp = forecast["main"]["temp"]
                print(f"{date}: {condition}, {temp}°C")
            except KeyError:
                continue 

def main():
    """Prompt the user to enter multiple city names and fetch weather details."""
    cities = [c.strip() for c in input("Enter city names (comma-separated): ").split(",") if c.strip()]
    for city in cities:
        get_current_weather(city)
        get_weather_forecast(city)

if __name__ == "__main__":
    main()
