from .get_token import get_token
from .get_last_fm_token import get_lastfm_token
from .extraction_functions import extract_data
import pandas as pd

#generate token and authorization header
token = get_token()
#lastfm_token = get_lastfm_token()

region_playlists = {
    "Global": "6UeSakyzhiEt4NB3UAd6NQ",
    "UK": "4OIVU71yO7SzyGrh0ils2i",
    "USA": "16wsvPYpJg1dmLhz0XTOmX",
    "Australia": "4eNlFzz2vIIYIGI3wzYMF0",
    "Spain": "2w90Jrb5nmYNzUYqv7DdBy"
}

def extract():
    try:
        df_tracks = extract_data(token,region_playlists)
        df_tracks.to_csv("etl/data/top_tracks.csv", index=False)
        print("Data saved to top_tracks.csv") 
        
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    