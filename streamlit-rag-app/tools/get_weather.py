import requests
def get_weather(city: str) -> str:
    # Simulated API call (you can integrate real APIs)
    """ weather_data = {
        "Delhi": "32°C, Sunny",
        "Mumbai": "29°C, Humid",
        "London": "15°C, Rainy"
    }
    return f"The weather in {city} is {weather_data.get(city, 'unknown')}." """
    url = f"https://wttr.in/{city}?format=3"  # simple free API from wttr.in
    response = requests.get(url)
    return response.text  # e.g., Delhi: 🌤 +32°C
