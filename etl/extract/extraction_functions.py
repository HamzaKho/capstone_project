import pandas as pd
from requests import get
from .get_token import get_auth_header

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

def extract_data(token,region_playlists):
    all_data=[]
    for region in region_playlists:
        print(f"Fetching top 100 tracks for {region}...")
        tracks = get_playlist_tracks(region_playlists[region],token)
        for track in tracks:
            track["region"] = region
        all_data.extend(tracks)
    df = pd.DataFrame(all_data)
    return df

