import pickle
import streamlit as st
import requests
import os

# =================== Add Background and Title Style =====================
import streamlit as st

st.set_page_config(layout="wide")

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1612036782180-6f0b6cd846fe?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# =================== Functions =====================

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/" + poster_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# =================== App =====================

st.markdown("<h1 style='text-align: center;'>🎬 MOVIE RECOMMENDATION SYSTEM 🎥</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: lightgray;'>Get instant recommendations based on your favorite movies 🎞️</h4>", unsafe_allow_html=True)




base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, "Models")

movies_path = os.path.join(model_dir, "movie_list.pkl")
similarity_path = os.path.join(model_dir, "similarity.pkl")

movies = pickle.load(open(movies_path, 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))



movie_list = movies['title'].values
selected_movie = st.selectbox(
    "🎞️ Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.markdown(f"**{names[i]}**")
