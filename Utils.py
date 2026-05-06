import requests
import json
class Util:

    @staticmethod
    def write_token(payload, url, headers):
        response = requests.post(url = url, headers = headers, json=payload)
        tokens = response.json()
        with open('tokens.json', 'w', encoding='utf-8') as f:
            json.dump(tokens, f, indent= 4, ensure_ascii=False)     
        
    
    @staticmethod
    def write_tokens_from_code(client_id, client_secret, code, url):
        dict = {}
        dict["headers"] = {
                "accept": "application/json",
                "content-type": "application/json"
            }
        dict["payload"] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://localhost:8080"
        }
        Util.write_token(dict["payload"], url, dict["headers"])

    @staticmethod
    def write_tokens_from_refresh(client_id, client_secret, refresh_token, url):
        dict = {}
        dict["headers"] = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        dict["payload"] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "redirect_uri": "http://localhost:8080"
        }
        Util.write_token(dict["payload"], url, dict["headers"])
    
    @staticmethod
    def get_tokens():
        dict= {}
        with open('tokens.json', 'r', encoding='utf-8') as f:
            tokens_read = json.load(f)
        dict['access_token'] = tokens_read["access_token"]  
        dict['refresh_token'] = tokens_read["refresh_token"]
        return dict
    @staticmethod
    def get_leads(token, subdomain):
        headers_leads_list = {
            "accept": "application/json",
            "authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        url_leads = f"https://{subdomain}.kommo.com/api/v4/leads"
        return requests.get(url=url_leads, headers=headers_leads_list)
    
    

