import streamlit as st
import os
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/' + str(movie_id) + '?api_key=' + api_key)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + str(data['poster_path'])

def recommend(movie):
    # Find the index of the movie
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]

    # Sort by similarity score (the second element in the tuple)
    movie_list = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:6]

    recommend_movies = []
    recommend_movies_poster = []
    for i in movie_list:
        # fetch poster
        movies_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movies_id))

    return recommend_movies, recommend_movies_poster


# Load the data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "**Select a movie to get recommendations:**",
    movies['title'].values,
)

if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])


st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: black;
        color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 20px;
        z-index: 1000;
    }
    .footer a {
        margin: 0 15px;
        color: #333;
        text-decoration: none;
    }
    .footer .linkedin:hover {
        color: #0072b1;
        transform: scale(1.2);
    }.footer .github:hover {
        color: #f1f1f1;
        transform: scale(1.2);
    }.footer .mail:hover {
        color: red;
        transform: scale(1.2);
    }
    </style>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

    <div class="footer">
        <p>Connect with me:</p>
        <a href="https://www.linkedin.com/in/mittalhardik" target="_blank" class="linkedin"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/codewithmittalhardik" target="_blank" class="github"><i class="fab fa-github"></i></a>
        <a href="mailto:mittalhardik2007@gmail.com" class="mail"><i class="fas fa-envelope"></i></a>
    </div>
    """, unsafe_allow_html=True)