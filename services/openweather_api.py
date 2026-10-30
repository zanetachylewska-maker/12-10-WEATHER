import requests
from config import AppConfig
from common.functions import temp_c, timestamp, time_dt

def get_weather(API_CITY = AppConfig.API_CITY):
    API_KEY = AppConfig.API_KEY


    url = f"https://api.openweathermap.org/data/2.5/weather?q={API_CITY}&appid={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        weather = {
            "place": data.get("name"),
            "temp": temp_c(data.get("main").get("temp")),
            "feels_like": temp_c(data.get("main").get("feels_like")),
            "wind": data.get("wind").get("speed"),
            "timestamp": timestamp(),
            "sunrise": time_dt(data.get("sys").get("sunrise")),
            "sunset": time_dt(data.get("sys").get("sunset")),
        }

        return weather

    except Exception as e:
        print(e)