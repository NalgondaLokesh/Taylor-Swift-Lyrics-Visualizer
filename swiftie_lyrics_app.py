import streamlit as st
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Replace this with your actual Genius API token
GENIUS_API_TOKEN = 't9bGXdXmCjf0O8BIJQ7WVmnz7y8GiTuQcuIV6DeKnd-b1pcwDuoYRdRu9AE4tics'
GENIUS_API_BASE_URL = 'https://api.genius.com'

# --- Function to search for a song using Genius API ---
def search_song(song_title):
    headers = {'Authorization': f'Bearer {GENIUS_API_TOKEN}'}
    params = {'q': song_title}
    response = requests.get(f'{GENIUS_API_BASE_URL}/search', params=params, headers=headers)
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        print("API Error:", response.text)
        return None

    data = response.json()
    hits = data.get('response', {}).get('hits', [])
    if not hits:
        print("No hits found for:", song_title)
        return None

    # Log all results found
    for hit in hits:
        print("Found:", hit['result']['full_title'])

    # Just take the first hit (most relevant)
    return hits[0]['result']['url']

# --- Function to scrape lyrics from Genius page ---
def scrape_lyrics(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Try multiple containers for lyrics
    lyrics = ""
    for div in soup.find_all("div"):
        if div.get("data-lyrics-container") == "true":
            lyrics += div.get_text(separator="\n")

    return lyrics.strip() if lyrics else "Lyrics not found."

# --- Generate a word cloud from the lyrics text ---
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# --- Streamlit UI ---
st.set_page_config(page_title="🎤 SwiftieLyrics Explorer", layout="centered")
st.title("🎤 SwiftieLyrics Explorer")
st.subheader("Enter a Taylor Swift song title to see the lyrics & word cloud")

song_input = st.text_input("🎶 Song Title")

if song_input:
    with st.spinner("Searching Genius for lyrics..."):
        song_url = search_song(song_input)
        if song_url:
            lyrics = scrape_lyrics(song_url)
            if lyrics and lyrics != "Lyrics not found.":
                st.success("Lyrics found!")
                st.text_area("📝 Lyrics", lyrics, height=300)

                st.subheader("☁️ Word Cloud")
                wc = generate_wordcloud(lyrics)
                plt.imshow(wc, interpolation='bilinear')
                plt.axis("off")
                st.pyplot(plt.gcf())
            else:
                st.error("Lyrics could not be extracted from the Genius page.")
        else:
            st.error("❌ Song not found on Genius. Try a different title.")
