import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
BASE_URL = os.environ.get("BASE_URL") or 'https://api.weather.yandex.ru/v2'
DATA_URL = os.environ.get("DATA_URL") or '/forecast'
PARAMS = os.environ.get("PARAMS") or {'lat': '59.9386', 'lon': '30.3141', 'hours': 'false', 'extra': 'false', 'limit': 7}
