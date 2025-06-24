from db.database import SessionLocal
from db.model import Ideas
from config import YANDEX_OAUTH_TOKEN, YANDEX_FOLDER_ID, YANDEX_GPT_API_ENDPOINT
import requests

def get_iam_token():
    response = requests.post(
        'https://iam.api.cloud.yandex.net/iam/v1/tokens',
        json={'yandexPassportOauthToken': YANDEX_OAUTH_TOKEN}
    )
    response.raise_for_status()
    return response.json()['iamToken']


def request_yandex_gpt(user_text: str) -> dict:
    # Получение iamToken
    iam_token = get_iam_token()

    headers = {
        "Authorization": f"Bearer {iam_token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    data = {
        "modelUri": f"gpt://{YANDEX_FOLDER_ID}/yandexgpt",
        "completionOptions": {
            "temperature": 0.8,
            "maxTokens": 1000
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты помощник, который анализирует отзывы сотрудников."
            },
            {
                "role": "user",
                "text": user_text
            }
        ]
    }

    try:
        response = requests.post(
            YANDEX_GPT_API_ENDPOINT,
            headers=headers,
            json=data
        )
        response.raise_for_status()
        result = response.json()
        # Текст ответа ищем в result["result"]["alternatives"][0]["message"]["text"]
        # или возвращаем весь словарь
        return result
    except requests.RequestException as e:
        print(f"[ERROR] request_yandex_gpt: {e}")
        return {}
    

def analyze_all_ideas_with_yandex_gpt() -> dict:
    session = SessionLocal()
    ideas = session.query(Ideas).all()
    session.close()

    if not ideas:
        return {"error": "Нет инициатив для анализа."}

    idea_payload = [
        {"text": idea.text_idea, "chat_id": int(idea.chat_id)}
        for idea in ideas
    ]

    prompt = (
        "Ты получаешь список инициатив от сотрудников компании"
        "Каждая инициатива содержит текст предложения и chat_id отправителя. Твоя задача:\n\n"
        "1. Проанализируй все инициативы.\n"
        "2. Объедини похожие по смыслу инициативы в группы (кластеры).\n"
        "3. Для каждой группы:\n"
        "◦ Сформулируй объединённую идею, которая обобщает все инициативы внутри группы.\n"
        "◦ Примерная структура:\n"
        " идея 1: ...\n"
        " идея 2: ...\n"
        "и т.д."
        f"А вот данные: ```{idea_payload}```"
    )

    return request_yandex_gpt(prompt)