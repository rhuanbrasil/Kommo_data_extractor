import requests
import os
from dotenv import load_dotenv
import json
from Utils import Generator
load_dotenv()

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
code = os.environ.get('code')
subdomain = os.environ.get('subdomain')
url = f"https://{subdomain}.kommo.com/oauth2/access_token"

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

if os.path.exists("tokens.json") == False:
    Generator.generate_first_token(payload, url, headers)

with open('tokens.json', 'r', encoding='utf-8') as f:
    tokens_read = json.load(f)

token_limpo = tokens_read["access_token"]    
refresh_token = tokens_read["refresh_token"]    


headers_leads_list = {
    "accept": "application/json",
    "authorization": f"Bearer {token_limpo}",
    "Content-Type": "application/json"
}

url_leads = f"https://{subdomain}.kommo.com/api/v4/leads"

leads = requests.get(url=url_leads, headers=headers_leads_list)

if requests.status_codes == 401:
    print("token expirou, gerando outro...")
    payload_renew = {
  "client_id": client_id,
  "client_secret": client_secret,
  "grant_type": "refresh_token",
  "refresh_code": refresh_token,
  "redirect_uri": "http://localhost:8080"
  }
    leads = requests.get(url=url_leads, headers=headers_leads_list)
    
print(leads.json())


















print(leads.text)