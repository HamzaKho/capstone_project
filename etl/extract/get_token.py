from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#Function to get the Authorization token from Spotify using CLIENT_ID and CLIENT_SECRET
def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization":"Basic " + auth_base64,
        "Content-Type":"application/x-www-form-urlencoded",
    }
    data = {"grant_type":"client_credentials"}
    try:
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result['access_token']
        return token
    except Exception as e:
        raise RuntimeError(f'Failed fetching token: {e}')
    

def get_auth_header(token):
    auth_value= f'Bearer {token}'
    return {'Authorization': auth_value}