import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

day = input("Which date would like like to travel back into? (YYYY-MM-DD) ")

# Billboard
# day = "2000-08-12"
header = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

url = f"https://www.billboard.com/charts/hot-100/{day}/"

billboard_response = requests.get(url=url, headers=header)

print(billboard_response.status_code)
billboard_html = billboard_response.text

soup = BeautifulSoup(billboard_html, "html.parser")

divs = soup.find_all(name="li", class_="lrv-u-width-100p")
songs = [] # songs unsanitaised
# print(divs) DEBUG

for div in divs:
    song = div.find(name="h3", id="title-of-a-story")
    songs.append(song)


chart_songs = [s.get_text().strip() for s in songs if s is not None] #songs sanitaised
# print(chart_songs) # DEBUG

# SPOTIFY
# email: konrad.wrobel.tidal@gmail.com
# Spotify dashboard
SPOTIPY_CLIENT_ID=os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET=os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI=os.environ["SPOTIPY_REDIRECT_URI"]
OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'

scope = "user-library-read,playlist-modify-private,playlist-modify-public,playlist-read-private,playlist-read-collaborative,user-library-modify,user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,scope=scope))

results = sp.current_user_saved_tracks()
# print(results) # DEBUG
get_user = sp.current_user()
user_id = get_user["id"]
# print(user_id) DEBUG

spotify_songs_uri = []
spotify_songs_ids = []

for song in chart_songs:
    try:
        song_info = sp.search(q=f"track:{song} year:{day[0:4]}", type="track",limit=1)
        song_id = song_info["tracks"]["items"][0]["id"]
    except:
        with open("Songs-not-found.txt", "a") as f:
            f.write(f"No song {song} found in spotify for {day[0:4]} year\n") #TODO : make a simple log file and append to it
    else:
        # spotify_songs_uri.append(f"spotify:track:{song_id}") #NOT NEEDED
        spotify_songs_ids.append(song_id)

# pprint(spotify_songs_uri) #DEBUG
# print(len(spotify_songs_uri)) #DEBUG

# TODO: https://www.udemy.com/course/100-days-of-code/learn/lecture/21626886#overview
# CREATE playlist
# https://spotipy.readthedocs.io/en/2.25.1/#spotipy.client.Spotify.user_playlist_create
# user_playlist_create(user, name, public=True, collaborative=False, description='')
user_playlists = sp.current_user_playlists()["items"]
playlist_name = f"{day} Billboard 100"

# Added func: AVOID creating duplicates of playlists
current_playlist_names = []

for item in user_playlists:
    if playlist_name in item.values():
        current_playlist_names.append(playlist_name)

if playlist_name not in current_playlist_names:
    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name,
                                                   description=f"100 days of code, day 46 - Billboard 100 songs for {day}")
    # TODO: ADD items to playlist:
    # https://spotipy.readthedocs.io/en/2.25.1/#spotipy.client.Spotify.playlist_add_items
    sp.playlist_add_items(playlist_id=new_playlist["id"], items=spotify_songs_ids)
else:
    print(f"Playlist {playlist_name} already exists in your library")

# print(current_playlist_names) # DEBUG
