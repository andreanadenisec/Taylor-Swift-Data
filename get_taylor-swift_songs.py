import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
#import time

client_id = 'a2b49b0bb2ba408db319793151a131fd'
client_secret = 'f42cc390f08d46d683ded97ca22fca6d'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# function to get the IDs for each track of this playlist
def getTrackIDS(user, playlist_id):
    results = sp.user_playlist_tracks(user, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    # store track ids in ids list
    ids = []
    for item in tracks:
        track = item['track']
        ids.append(track['id'])

    return ids

ids = getTrackIDS('6qd0v42hemsqpa8ihn300ddk5', '48Bo7WsNTgjs61vsr4f8lU')
print(len(ids))
print(ids)


def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track

# loop over track ids
tracks = []
for i in range(len(ids)):
  #time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

# create dataset
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature'])
df.to_csv("spotify_taylor-swift_raw.csv", sep = ',')
