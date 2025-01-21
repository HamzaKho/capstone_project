from get_token import get_token, get_auth_header
from requests import post, get

#generate token and authorization header
token = get_token()
print(token)

#retrieve top 100 tracks from each region

#Playlists Starting: 37i9dQZEVXb

region_playlists = {
    "Global": "6UeSakyzhiEt4NB3UAd6NQ",
    "UK": "4OIVU71yO7SzyGrh0ils2i",
    "USA": "16wsvPYpJg1dmLhz0XTOmX",
}
#retrieve top 100 tracks from each region
def get_top_tracks(region, token):
    url = "https://api.spotify.com/v1/playlists/{region}/tracks/"
    auth_header = get_auth_header(token)
    response = get(url, headers=auth_header)
    return response.content

print(get_top_tracks(region_playlists["Global"], token))
    