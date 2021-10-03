from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")

# date = "2019-03-30"
link = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(link)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

top_list = soup.find_all("span", {"class": "chart-element__information__song"})

song_list = []
for item in top_list:
    song_list.append(item.getText())


date_year = date.split("-")[0]
print(date_year)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "0caa57384b6c4e4b94a2a3b7704b85ac"
SPOTIPY_CLIENT_SECRET = "c631ff66d3954979a9e32d814be96466"



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog= True,
        cache_path="day46/token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{date_year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(song_list)
