import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_info(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        song_url = track["external_urls"]["spotify"]
        album_cover_url = track["album"]["images"][0]["url"]
        return song_url, album_cover_url
    else:
        return None, "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_info = []

    for i in distances[1:6]:
        # fetch the song URL and album cover
        artist = music.iloc[i[0]].artist
        song_name = music.iloc[i[0]].song
        song_url, album_cover_url = get_song_info(song_name, artist)
        
        if song_url:
            recommended_music_info.append((song_name, song_url, album_cover_url))

    return recommended_music_info

st.header('Music Recommender System')
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_info = recommend(selected_song)
    
    for i, (song_name, song_url, album_cover_url) in enumerate(recommended_music_info):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(f"{i + 1}.")
        with col2:
            st.write(f"[{song_name}]({song_url})")
            st.image(album_cover_url)
