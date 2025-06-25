import streamlit as st
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Genius API Access Token (Replace with your token)
GENIUS_API_TOKEN = "i6d7KSSqY3qgW6kWV-QjS7EJY-WqGqrTk7X-24QFL783Di5elGF4lLLxMf9thD0gmP26ButTGSTdHhj1J0egXA"

# Function to search song on Genius
def search_song(song_title):
    base_url = "https://api.genius.com/search"
    headers = {"Authorization": f"Bearer {GENIUS_API_TOKEN}"}
    params = {"q": f"Taylor Swift {song_title}"}
    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        hits = data["response"]["hits"]
        if hits:
            return hits[0]["result"]["url"]
    return None

# Function to scrape lyrics from Genius URL
def get_lyrics(song_url):
    page = requests.get(song_url)
    soup = BeautifulSoup(page.text, "html.parser")
    lyrics_divs = soup.find_all("div", class_="Lyrics__Container-sc-1ynbvzw-6")
    if not lyrics_divs:
        lyrics_divs = soup.find_all("div", class_="lyrics")  # fallback for older pages
    lyrics = "\n".join([div.get_text(separator="\n") for div in lyrics_divs])
    return lyrics.strip()

# Function to generate word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

# Streamlit UI
st.set_page_config(page_title="Swiftie Lyrics & Word Cloud 🎶", layout="centered")

st.title("💖 Swiftie Lyrics Explorer")
st.write("Enter a **Taylor Swift** song title and see the lyrics and a magical word cloud!")

song_title = st.text_input("🎵 Song Title", placeholder="e.g., Love Story")

if st.button("Get Lyrics"):
    if not song_title.strip():
        st.warning("Please enter a song title.")
    else:
        st.info("Fetching lyrics from Genius...")
        url = search_song(song_title)
        if url:
            lyrics = get_lyrics(url)
            if lyrics:
                st.subheader("📝 Lyrics")
                st.text_area("Lyrics", lyrics, height=300)
                st.subheader("☁️ Word Cloud")
                generate_wordcloud(lyrics)
            else:
                st.error("Lyrics not found for the song.")
        else:
            st.error("Song not found on Genius.")

st.caption("Made with 💻 and 💗 by a Pythonista Swiftie!")
