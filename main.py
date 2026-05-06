import requests
import os
from dotenv import load_dotenv
from Utils import Util
load_dotenv()

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
code = os.environ.get('code')
subdomain = os.environ.get('subdomain')
url = f"https://{subdomain}.kommo.com/oauth2/access_token"

if os.path.exists("tokens.json") == False:
    Util.write_tokens_from_code(client_id, client_secret, code, url)

tokens_dict = Util.get_tokens()   

leads = Util.get_leads(tokens_dict['access_token'], subdomain)

if leads.status_code == 401:
    print("Token expirou, gerando outro...")
    Util.write_tokens_from_refresh(client_id, client_secret, tokens_dict["refresh_token"], url)  

print(leads.json())
