import pandas as pd
from requests import get
from dotenv import load_dotenv
from .get_last_fm_token import generate_signature
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("LASTFM_API_KEY")

def get_chart_tracks(country_code,lastfm_token):
    params = {
        "method": "geo.getTopTracks",
        "country": country_code,
        "api_key": API_KEY,
        "token": lastfm_token,
        "limit": 50,
    }
    params["api_sig"] = generate_signature(params)
    params["format"] = "json"
    response = get(BASE_URL, params=params)
    if response.status_code != 200:
        raise RuntimeError(f'Failed to fetch data for country {country_code}: {response.status_code}')
    data = response.json()
    tracks = data["tracks"]["track"]
    return [{"name": track["name"], "artist": track["artist"]["name"]} for track in tracks]