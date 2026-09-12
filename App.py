import requests
import pycountry
import difflib

API_KEY = 'a6db76b5bcf7e7afbc1e6bb7ca8e35d9'
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
GEO_URL = "https://api.openweathermap.org/geo/1.0/direct"

CONTINENTS = {
    "asia", "europe", "africa", "antarctica",
    "australia", "north america", "south america"
}


def is_country_or_continent(name):
    """Reject if input is a country or continent."""
    name_title = name.title()
    if pycountry.countries.get(name=name_title):
        return True
    if name.lower() in CONTINENTS:
        return True
    return False


def is_state(name):
    """Reject if input matches or closely resembles any known state/province."""
    name_lower = name.lower().strip()
    all_states = [subdiv.name.lower() for subdiv in pycountry.subdivisions]

    # Exact or fuzzy match
    if name_lower in all_states:
        return True
    close_matches = difflib.get_close_matches(name_lower, all_states, n=1, cutoff=0.8)
    if close_matches:
        return True

    # Reject if name contains typical state keywords
    bad_keywords = ["state", "province", "region", "territory"]
    if any(word in name_lower for word in bad_keywords):
        return True

    return False


def is_valid_city(city_name):
    """Verify if input is a valid city using OpenWeatherMap Geocoding API."""
    if is_country_or_continent(city_name) or is_state(city_name):
        return False

    params = {"q": city_name, "limit": 1, "appid": API_KEY}
    response = requests.get(GEO_URL, params=params)
    data = response.json()

    if not data:
        return False

    location = data[0]

    # Reject if name looks like a state
    if is_state(location.get("name", "")):
        return False

    # Must have 'state' and 'country' to be a real city
    if "country" not in location:
        return False

    # 🔥 Major fix: reject if OWM does NOT provide a 'state' field
    # Because most states only have country-level data
    if "state" not in location:
        return False

    # Reject if input name matches the returned state (example: Rajasthan → Rajasthan)
    if location.get("name", "").lower() == location.get("state", "").lower():
        return False

    return True


def get_weather(city_name):
    """Fetch weather data from OpenWeatherMap API."""
    if is_country_or_continent(city_name):
        print(f"❌ '{city_name}' is a country or continent. Please enter a city name.")
        return

    if is_state(city_name):
        print(f"❌ '{city_name}' is a state or province. Please enter a city name.")
        return

    if not is_valid_city(city_name):
        print(f"❌ '{city_name}' does not seem to be a valid city.")
        return

    params = {"q": city_name, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()
        data = response.json()

        print(f"\n📍 Weather Details for {city_name.title()}")
        print("-" * 40)
        print(f"🌡️ Temperature : {data['main']['temp']} °C")
        print(f"💧 Humidity    : {data['main']['humidity']} %")
        print(f"🌤️ Condition   : {data['weather'][0]['description'].title()}")
        print(f"🌬️ Wind Speed  : {data['wind']['speed']} m/s")
        print("-" * 40)

    except requests.exceptions.HTTPError as err:
        print(f"❌ API Error: {err}")
    except requests.exceptions.RequestException:
        print("⚠️ Network error. Please check your connection.")
    except KeyError:
        print("⚠️ Unexpected data format received from API.")


def main():
    print("===== 🌦️ Weather App =====")
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("❗ Please enter a valid city name.")


if __name__ == "__main__":
    main()
