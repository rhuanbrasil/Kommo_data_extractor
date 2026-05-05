import requests
import json
class Generator:

    @staticmethod
    def generate_first_token(payload, url, headers):
        response = requests.post(url = url, headers = headers, json=payload)
        tokens = response.json()
        with open('tokens.json', 'w', encoding='utf-8') as f:
            json.dump(tokens, f, indent= 4, ensure_ascii=False)     
        