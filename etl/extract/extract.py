from .get_token import get_token, get_auth_header
from requests import post, get
import pandas as pd

#generate token and authorization header
token = get_token()

#retrieve top 100 tracks from each region

#Playlists Starting: 37i9dQZEVXb

region_playlists = {
    "Global": "6UeSakyzhiEt4NB3UAd6NQ",
    "UK": "4OIVU71yO7SzyGrh0ils2i",
    "USA": "16wsvPYpJg1dmLhz0XTOmX",
}
#retrieve top 100 tracks from each region

def get_playlist_tracks(playlist, token):
    url = f"https://api.spotify.com/v1/playlists/{playlist}/tracks/"
    auth_header = get_auth_header(token)
    response = get(url, headers=auth_header)
    if response.status_code != 200:
        raise RuntimeError(f'Failed to fetch data for playlist {playlist}: {response.status_code}')
    data = response.json()
    tracks = []  
    for i, item in enumerate(data.get("items", [])):
        track = item.get("track", {})
        track_info = {
            "track_name": track.get("name"),
            "artist_name": ", ".join(artist["name"] for artist in track.get("artists", [])),
            "album_name": track.get("album", {}).get("name"),
            "release_date": track.get("album", {}).get("release_date"),
            "popularity": track.get("popularity"),
            "track_id": track.get("id"),
        }
        tracks.append(track_info)
    
    return tracks

all_data = []
def extract_data(token):
    for region in region_playlists:
        print(f"Fetching top 100 tracks for {region}...")
        tracks = get_playlist_tracks(region_playlists[region],token)
        for track in tracks:
            track["region"] = region
        all_data.extend(tracks)
    df = pd.DataFrame(all_data)
    return df

def extract():
    try:
        df_tracks = extract_data(token)
        df_tracks.to_csv("etl/data/top_tracks.csv", index=False)
        print("Data saved to top_tracks.csv")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    