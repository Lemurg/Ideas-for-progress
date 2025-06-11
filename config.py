import os
from dotenv import load_dotenv
import requests

load_dotenv()  # Считываем переменные из .env

# Токен телеграм-бота (из .env)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Настройки для YandexGPT
YANDEX_GPT_API_ENDPOINT = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
YANDEX_OAUTH_TOKEN = os.getenv("YANDEX_OAUTH_TOKEN")
YANDEX_FOLDER_ID   = os.getenv("YANDEX_FOLDER_ID")

# Путь к базе данных SQLite
DB_PATH = "sqlite:///dbmodel.db"

# Дополнительные параметры для запроса к Yandex GPT (если хотите вынести и их)
YANDEX_GPT_TEMPERATURE = 0.8
YANDEX_GPT_MAX_TOKENS  = 1000

# Функция для получения IAM токена Yandex Cloud
def get_iam_token():
    response = requests.post(
        'https://iam.api.cloud.yandex.net/iam/v1/tokens',
        json={'yandexPassportOauthToken': YANDEX_OAUTH_TOKEN}
    )
    response.raise_for_status()
    return response.json()['iamToken']