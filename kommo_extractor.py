import requests
import os
from dotenv import load_dotenv

load_dotenv()

#TODO tentar fazer refresh token
client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
code = os.environ.get('code')
subdomain = os.environ.get('subdomain')
url = f"https://{subdomain}.kommo.com/oauth2/access_token"


print(f"Tentando com ID: {client_id} e Code: {code[:10]}...") 
# code[:10] apenas para ver o início e não expor o código todo no log

payload = {
  "client_id": client_id,
  "client_secret": client_secret,
  "grant_type": "authorization_code",
  "code": code,
  "redirect_uri": "http://localhost:8080"
}

headers = {
    "accept": "application/json",
    "content-type": "application/json"
}


response = requests.post(url, json=payload, headers=headers)
token_data = response.json()

if "access_token" not in token_data:
    print("Erro ao obter token")
    exit()

token_limpo = token_data['access_token']
refresh_token = token_data['refresh_token']

headers_leads_list = {
    "accept": "application/json",
    "authorization": f"Bearer {token_limpo}",
    "Content-Type": "application/json"
}

url_leads = f"https://{subdomain}.kommo.com/api/v4/leads"

leads = requests.get(url=url_leads, headers=headers_leads_list)

print(leads.text)