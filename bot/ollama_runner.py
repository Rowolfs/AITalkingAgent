import requests
import json

system="""Ты — быстрый голосовой ассистент.
    Отвечай максимально кратко и по делу.
    1–2 предложения.
    Без лишнего контекста.
    Без повторения вопроса.
    Без объяснений если их не просили.

    Ответ должен звучать естественно для озвучки."""


def ask_ollama(prompt: str):
    payload = {
        "model": "mistral:7b",
        "prompt": prompt,
        "system": system,
        "stream": False,
        "options": {
            "num_predict": 60
        }
    }

    try:
        response = requests.post(
            "http://192.168.1.95:11434/api/generate",
            json=payload,
            timeout=60,
            
        )
        response.raise_for_status()

        try:
            # обычный случай
            data = response.json()
            return data.get("response", "")
        except json.JSONDecodeError:
            # если пришёл stream JSON
            text = ""
            for line in response.text.splitlines():
                if not line.strip():
                    continue
                obj = json.loads(line)
                text += obj.get("response", "")
            return text

    except Exception as e:
        print("Ошибка при обращении к Ollama:", e)
        return ""