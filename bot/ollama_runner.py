import requests
import json
from config import config




def ask_ollama(prompt: str):
    payload = {
        "model": config['ollama']['model'],
        "prompt": prompt,
        "system": config['ollama']['system'],
        "stream": config['ollama']['stream'],
        "options": {
            "num_predict": 60
        }
    }

    try:
        response = requests.post(
            config['ollama']['address'],
            json=payload,
            timeout=config['ollama']['timeout'],
            
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