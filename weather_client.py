import requests
import datetime

# API key
API_KEY = "d4a9b89830bc690d692129a676546bcb"

    
def get_weather_data(response, city):
    
    """A function to fetch data from OpenWeatherMap API."""
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
        "appid": API_KEY
    }
    response = requests.get(base_url, params=params)
    data = get_weather_data(response, city)
    
    if response:
        try:
            print(f"\nCurrent Weather in {data['name']}:")
            kelvin_temp = data['main']['temp']
            celsius_temp = kelvin_temp - 273.15
            print(f"Temperature: {celsius_temp:.2f}°C")
            print(f"Condition: {data['weather'][0]['description'].capitalize()}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        except KeyError:
            print(f"Could not retrieve complete weather data for '{city}'.")

def get_weather_forecast(city):
    """Fetch and display 5-day weather forecast for a given city."""
    forecast_base_url = "https://api.openweathermap.org/data/2.5/forecast" # Base URL for forecast
    params = {
        "q": city,
        "units": "metric",
        "appid": API_KEY
    }
    response = requests.get(forecast_base_url, params=params)
    data = get_weather_data(response, city)


    if response:
        print(f"\n5-Day Weather Forecast for {data.get('city', {}).get('name', city)}:")
        for forecast in data.get("list", [])[::8]:  # fetch daily data at every 8th position since 24hrs =8*3
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

# Run the script
if __name__ == "__main__":
    main()
    
