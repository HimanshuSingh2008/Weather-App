<div align="center">

# 🌦️ Python Weather App

### Real-Time Weather Information Using OpenWeatherMap API

A Python-based weather application that retrieves real-time weather information for valid cities using the OpenWeatherMap API. It also validates user input to help prevent country, continent, and state names from being accepted as cities.

<br>

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python\&logoColor=white)
![API](https://img.shields.io/badge/API-OpenWeatherMap-orange)
![HTTP](https://img.shields.io/badge/HTTP-Requests-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

</div>

---

## 📌 About the Project

The **Python Weather App** is a command-line application designed to provide weather information for a user-specified city.

It uses the OpenWeatherMap API to retrieve current weather conditions and displays temperature, humidity, weather description, and wind speed.

The application also uses Python libraries to validate location names and reject inputs that match known countries, continents, or administrative subdivisions.

## ✨ Features

* 🌡️ **Live Temperature:** Displays the current temperature in Celsius.
* 💧 **Humidity Information:** Shows the current humidity percentage.
* 🌤️ **Weather Conditions:** Displays a description of the current weather.
* 🌬️ **Wind Speed:** Provides wind speed in meters per second.
* 🌍 **City Validation:** Checks whether the entered location can be identified through the geocoding API.
* 🚫 **Invalid Location Handling:** Attempts to reject countries, continents, and states or provinces.
* 🔎 **Fuzzy Matching:** Uses `difflib` to identify names similar to known administrative subdivisions.
* ⚠️ **Error Handling:** Handles HTTP errors, network problems, and unexpected API responses.
* 💻 **Simple CLI Interface:** Easy to run from a terminal.

## 🛠️ Technologies Used

| Technology         | Purpose                                              |
| ------------------ | ---------------------------------------------------- |
| Python             | Core programming language                            |
| Requests           | Sends HTTP requests to the weather API               |
| PyCountry          | Provides country and administrative subdivision data |
| Difflib            | Performs approximate string matching                 |
| OpenWeatherMap API | Retrieves weather and geocoding information          |

## 📂 Project Structure

```text
Weather-App/
│
├── weather.py       # Main Python application
├── README.md        # Project documentation
└── requirements.txt # Python dependencies
```

*Replace `weather.py` with your actual Python filename if it is different.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Navigate to the project directory:

```bash
cd YOUR-REPOSITORY
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

### 2. Install Python

Install Python 3.9 or a compatible newer version.

Check your Python installation:

```bash
python --version
```

### 3. Install Dependencies

Create a file named `requirements.txt` containing:

```text
requests
pycountry
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure Your API Key

Obtain an API key from the official OpenWeatherMap website:

<a href="https://openweathermap.org/api" target="_blank">OpenWeatherMap API</a>

Store your API key in an environment variable instead of writing it directly into your Python source code.

**Windows PowerShell:**

```powershell
$env:OPENWEATHER_API_KEY="YOUR_API_KEY"
```

Then update your Python code to read the key:

```python
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "Please configure the OPENWEATHER_API_KEY environment variable."
    )
```

Keep your actual API key private. Never upload it to a public GitHub repository.

> Note: The environment variable configured using the PowerShell command above applies to the current terminal session.

## ▶️ How to Run

Open the terminal in your project directory and execute:

```bash
python weather.py
```

Enter the name of a city when prompted.

### Example Input

```text
===== 🌦️ Weather App =====
Enter city name: Dehradun
```

### Example Output

The values below are illustrative and will vary according to live weather conditions.

```text
📍 Weather Details for Dehradun
----------------------------------------
🌡️ Temperature : 27.5 °C
💧 Humidity    : 65 %
🌤️ Condition   : Scattered Clouds
🌬️ Wind Speed  : 2.8 m/s
----------------------------------------
```

### Example: Invalid Input

```text
===== 🌦️ Weather App =====
Enter city name: Asia

❌ 'Asia' is a country or continent.
Please enter a city name.
```

The exact message depends on the validation performed by the application.

## 🔄 How It Works

1. The user enters a location through the command-line interface.
2. The application checks whether the input matches a country, continent, or known administrative subdivision.
3. The OpenWeatherMap Geocoding API is used to look up the location.
4. The application validates the returned location information.
5. A weather request retrieves current weather data for the entered city.
6. The application displays temperature, humidity, weather conditions, and wind speed.
7. Errors are handled to provide useful feedback when requests fail or responses are unexpected.

## 🌐 APIs Used

### Current Weather API

Retrieves current weather information for the requested location.

<a href="https://openweathermap.org/current" target="_blank">OpenWeatherMap Current Weather Documentation</a>

### Geocoding API

Converts location names into geographic information that can be used to identify a location.

<a href="https://openweathermap.org/api/geocoding-api" target="_blank">OpenWeatherMap Geocoding Documentation</a>

## ⚠️ Limitations

* An active internet connection is required.
* A valid OpenWeatherMap API key is required.
* API access and request limits depend on your account and subscription.
* Location validation is heuristic rather than definitive.
* Some legitimate cities may be rejected if the geocoding API does not return the expected fields.
* Some cities share names, so using a city and country combination can improve location accuracy.
* A matching administrative subdivision does not always mean that an input is not also the name of a city.

## 🚀 Future Improvements

* Develop a graphical user interface using Tkinter or PyQt.
* Build a web interface using Flask or React.
* Add a five-day weather forecast.
* Display sunrise and sunset times.
* Support country-specific city searches.
* Add weather icons and improved formatting.
* Cache recent results to reduce repeated API requests.
* Improve city validation using geographic coordinates and administrative metadata.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Python functions and modular programming.
* Working with third-party REST APIs.
* HTTP requests and JSON response processing.
* Input validation and string matching.
* Exception handling.
* Environment variables and API key management.
* Dependency management and GitHub documentation.

## 👨‍💻 Author

**Himanshu Singh**

B.Tech — Artificial Intelligence and Machine Learning

### ⭐ Support

If you find this project useful, consider giving the repository a star on GitHub!

---

<div align="center">

**Built with Python 🐍 and OpenWeatherMap 🌦️**

</div>
