import os
import sys
import requests
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY not found in .env")
        sys.exit(1)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"The weather in {city.title()} is {desc} with a temperature of {temp}°F.")
    else:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    get_weather(city)

