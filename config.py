from dotenv import load_dotenv
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") # Токен бота Telegram

YANDEX_OAUTH_TOKEN = os.getenv("YANDEX_OAUTH_TOKEN") # Токен OAuth для Yandex
YANDEX_FOLDER_ID = os.getenv("YANDEX_FOLDER_ID") # ID папки YandexGPT
YANDEX_GPT_API_ENDPOINT = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion" # URL API YandexGPT