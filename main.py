import time
from services.openweather_api import get_weather
from services.data_files import append
from services.dashboard import create_app
from services.mysql_db import initialize_db, insert_record

initialize_db()

# create_app()

while True:
    # pobieranie danych
    weather = get_weather()

    # zapisywanie do excel
    append([weather])

    # zapisywanie do mysql
    insert_record(weather)

    print("Pobrałem dane pogodowe")
    time.sleep(10)