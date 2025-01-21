import requests
from bs4 import BeautifulSoup

def get_playlist_ids(url):
    # Send a GET request to get the page
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch the page: {response.status_code}")
    # Parse
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    #divs = soup.find_all("div")
    divs = soup.find_all("div", attrs={"aria-labelledby": True})
    print(divs)
    playlist_ids = []
    for div in divs:
        labelledby = div.get("aria-labelledby", "")
        if ":playlist:" in labelledby:
            playlist_id = labelledby.split("playlist:")[-1].split("-")[0]
            playlist_ids.append(playlist_id)
    return playlist_ids

def fetch_raw_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch the page: {response.status_code}")
    return response.text

url = "https://open.spotify.com/genre/section0JQ5DAzQHECxDlYNI6xD1i"
print(fetch_raw_html(url))
#playlist_ids = get_playlist_ids(url)
#print("Playlist IDs:", playlist_ids)
