import os
import pandas as pd
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

response = Util.get_leads(tokens_dict['access_token'], subdomain)
leads = response.json()

if response.status_code == 401:
    print("Token expirou, gerando outro...")
    Util.write_tokens_from_refresh(client_id, client_secret, tokens_dict["refresh_token"], url)
    response = Util.get_leads(tokens_dict['access_token'], subdomain)
    leads = response.json()
 
df = pd.DataFrame(leads["_embedded"]["leads"])

df['tags'] = ([", ".join([tag.get("name") for tag in lead.get("_embedded", {}).get("tags", [])])
               for lead in leads.get("_embedded").get("leads")
            ])


df = df[['id', 'responsible_user_id', 'pipeline_id', 'created_at', 'tags']]

print (df.head(10))

#Se quiser o resultado em csv
#df.to_csv("Leads.csv", index=False, encoding="utf-8")

