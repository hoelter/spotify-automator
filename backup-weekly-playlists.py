# Spotipy library reference: https://github.com/plamere/spotipy/tree/master/spotipy
# Spotify api reference: https://developer.spotify.com/documentation/web-api/reference/#/operations/create-playlist

import spotipy
import json
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

prefix = ''
target_playlist_name = ''

monday = 0
friday = 4

now = datetime.now()

if now.today().weekday() == monday:
    target_playlist_name = 'Discover Weekly'
    prefix = 'DW'
elif now.today().weekday() == friday:
    target_playlist_name = 'Release Radar'
    prefix = 'RR'
else:
    print("Shouldn't be backing up playlists right now, exiting.")
    quit()

curr_date = datetime.now().strftime('%m-%d-%y')
new_playlist_name = f'{prefix} {curr_date}' 

scope = "playlist-modify-public playlist-read-private playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))

playlists = sp.current_user_playlists()

target_playlist = None

while playlists:
    for i, playlist in enumerate(playlists['items']):
        name = playlist['name']

        if name == target_playlist_name:
            target_playlist = playlist

        elif name == new_playlist_name:
            print("Found matching new playlist already created, exiting")
            exit()

    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

if not target_playlist:
    print(f"{target_playlist_name} playlist not found.")
    exit()

target_playlist_tracks = sp.playlist_tracks(target_playlist['id'])

track_ids = [items['track']['id'] for items in target_playlist_tracks['items']]

my_id = sp.me()['id']

new_playlist = sp.user_playlist_create(user=my_id, name=new_playlist_name)

# with open('test-data-new_playlist.json', 'w', encoding='utf-8') as f:
#     json.dump(new_playlist, f, ensure_ascii=False, indent=4)

sp.playlist_add_items(new_playlist['id'], track_ids)

print(f"Created {new_playlist_name} and added {len(track_ids)} tracks to it.")

