import os
import subprocess
import sys

try:
    import requests
except ImportError:
    print("Installing requests module...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests
import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    full_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(full_url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        feels_like = main["feels_like"]
        description = weather["description"]
        city = data["name"]

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print("\nCity not found. Please try again.")

def main():
    api_key = "d0c7e0f31c5d64da7bbaedf5c9d2cfd1"  # Replace with your OpenWeatherMap API key
    print("🌤️  Simple Weather App")

    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ")
        if city.lower() == "exit":
            break
        get_weather(city, api_key)

if __name__ == "__main__":
    main()