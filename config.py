import os
import dotenv
dotenv.load_dotenv()

class AppConfig:
    API_KEY = os.getenv("API_KEY")
    API_CITY = "Cairo"
    WEATHER_FILE = os.getenv("WEATHER_FILE")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")