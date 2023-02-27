# import speech_recognition as  sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import pyttsx3
import os

# listener  = sr.Recognizer()

# sr.Microphone.list_microphone_names()

# def ouvir():
#     try:
#         with sr.Microphone(device_index=1) as source:
#             print('Listening...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             print(command)

#             return command
#     except:
#         return 'No sound'

os.environ['SPOTIPY_CLIENT_ID'] = 'd42fde4f8111483087e47122e353b9f2'
os.environ['SPOTIPY_CLIENT_SECRET'] = '0e56ae6b8c45442588a032688690732e'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.com/callback'

scope = 'user-read-playback-state, user-modify-playback-state'
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

query = 'Uptown Funk'
results = sp.search(query, 1, 0, "track")

# track_url = results['tracks']['items'][0]['uri']
# sp.start_playback(uris=[track_url])


# para colocar dentro da assistente virtual
# if 'spotify play' in comando.lower():
#     query = comamand.lower().replace('spotfy play', '').strip()

#     results = sp.search(query,1,0,"track")

#     nome_artista = results['tracks']['items'][0]['artists'][0]['name']
#     nome_musica = results['tracks']['items'][0]['name']

#     track_url = results['tracks']['items'][0]['uri']
#     engine.say(f'Playing {nome_musica} by {nome_artista}')
#     engine.runAndWait()

#     sp.start_playback(uris=[track_url])
