#!/usr/bin/env python

"""

lastfm.py  --  Fetch last song played from the Last.fm API

Scott Schulz

v1.0  --  2016-02-09

"""

import os
import sys
import requests

#  Format for the output
#  Available: song, artist, album
output = 'Now Playing: {song} by {artist}'

#  Last FM username
username = os.environ.get('LASTFM_USER')

#  Last FM API Key
key = os.environ.get('LASTFM_KEY')

#  Final message for TE
message = ''

#  Last FM API endpoint
url = 'http://ws.audioscrobbler.com/2.0/'

payload = {
  'api_key': key, 
  'user': username, 
  'method': 'user.getRecentTracks', 
  'limit': 1, 
  'format': 'json'
}

r = requests.get(url, params=payload)

if r.status_code == 200:
  try:
    data = r.json()['recenttracks']['track'][0]
    song = data['name']
    artist = data['artist']['#text']
    album = data['album']['#text']
    message = output.format(song=song, artist=artist, album=album)
  except (KeyError, IndexError):
    message = 'Error Parsing Last Song'
else:
  message = 'Error Fetching API Data'

sys.stdout.write(message)
