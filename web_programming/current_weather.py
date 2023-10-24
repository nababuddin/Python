import requests

API_KEY = ""  # <-- Put your free Weatherstack API key here!
URL_BASE = "http://api.weatherstack.com/current"

def current_weather(location: str, api_key: str = API_KEY) -> dict:
    params = {
        "access_key": api_key,
        "query": location
    }
    return requests.get(URL_BASE, params=params).json()

if __name__ == "__main__":
    from pprint import pprint

    while True:
        location = input("Enter a location (city name): ").strip()
        if location:
            pprint(current_weather(location, API_KEY))
        else:
            break
