# 🎤 SwiftieLyrics Explorer

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-blue?logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**SwiftieLyrics Explorer** is a fun, interactive Streamlit web app that allows you to enter the title of any Taylor Swift song, fetch its lyrics using the Genius API, and display a beautiful word cloud based on the lyrics.

Perfect for **Swifties** who love **Python**! 🎶🐍

---

## 🌟 Features

- 🎼 **Search Taylor Swift Songs**: Just type in the song title.
- 📜 **Lyrics Viewer**: Displays full lyrics of the song fetched from Genius.com.
- ☁️ **Word Cloud Generator**: Creates a visually stunning word cloud of the most common words in the lyrics.
- ⚙️ **Built with Python & Streamlit**: Easy to run, modify, and extend.

---

## 📸 Screenshots

> You can add screenshots after running the app

| Lyrics View | Word Cloud |
|-------------|------------|
| ![](screenshots/lyrics.png) | ![](screenshots/wordcloud.png) |

---

## 🚀 Live Demo

👉 **Coming Soon:** Deploy it on [Streamlit Cloud](https://streamlit.io/cloud) or Hugging Face Spaces.

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [Genius API](https://genius.com/developers) – For searching songs
- `requests` – For API and web calls
- `BeautifulSoup4` – To scrape lyrics from Genius
- `wordcloud` – To generate the word cloud
- `matplotlib` – To display the image in Streamlit

---

## 📦 Installation

### 🔧 Prerequisites
- Python 3.8 or higher
- A Genius API Token (free from [genius.com/developers](https://genius.com/developers))

### 🔌 1. Clone the Repository
```bash
git clone https://github.com/yourusername/swiftie-lyrics-explorer.git
cd swiftie-lyrics-explorer
