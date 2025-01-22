import requests
import hashlib
from dotenv import load_dotenv
import os
from requests import post, get

load_dotenv()
API_KEY = os.getenv("LASTFM_API_KEY")
SHARED_SECRET = os.getenv("SHARED_SECRET")
BASE_URL = os.getenv("BASE_URL")

def generate_signature(params):
    signature_string = "".join(f"{key}{value}" for key, value in sorted(params.items()))
    signature_string += SHARED_SECRET
    return hashlib.md5(signature_string.encode("utf-8")).hexdigest()

def get_lastfm_token():
    params = {
        "method": "auth.getToken",
        "api_key": API_KEY,
    }
    params["api_sig"] = generate_signature(params)
    params["format"] = "json" 
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["token"]
    else:
        raise Exception(f"Error getting token: {response.status_code}, {response.text}")