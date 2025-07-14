# 🎬 Movie Recommendation System

This project recommends similar movies based on your favorite title using a content-based filtering approach. It uses TMDB metadata like cast, crew, genres, and keywords to build similarity between films. The app is deployed using **Streamlit** on **Hugging Face Spaces**.

---

## 📌 Project Demo

🔗 **Live Hugging Face Demo**:  
[https://huggingface.co/spaces/itsmeaj18/movie-recommendation-system](https://huggingface.co/spaces/itsmeaj18/movie-recommendation-system)

![Demo](https://github.com/itsmeaj18/Movie-Recommendation-System/blob/55dee9fe2dc7bdd81f77423f944e812574e58c0c/Movie%20Recommendation%20System/Movie%20Recommendation%20S.gif)

---

## 📌 Project Highlights

- 🎞️ Movie metadata from TMDB (The Movie Database)
- 🧠 Content-based recommendation using:
  - Genres
  - Cast & Crew
  - Keywords
  - Overview (text vectorization)
- 🧮 Cosine Similarity between vectorized movie “tags”
- 🖼️ Movie posters fetched in real-time from the TMDB API
- ⚡ Fast and interactive UI using Streamlit

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests (for TMDB API)

---

## 📂 Project Files

- `app.py` — Streamlit app source code
- `movie_list.pkl` — Preprocessed movie metadata (title, id, tags, etc.)
- `similarity.pkl` — Cosine similarity matrix for fast recommendations
- `requirements.txt` — List of required Python packages
- `README.md` — Project overview file

---

## 📊 Dataset Source

This project uses the TMDB 5000 Movie Dataset available on Kaggle:  
🔗 [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

