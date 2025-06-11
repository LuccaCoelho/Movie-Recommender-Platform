from src.get_recommendations import top_5_movies
from src.load_data import extract_data
import streamlit as st

data = extract_data("Data/dataset/tmdb_5000_movies.csv")

st.title("Movie Recommender System")
movie_choice = st.selectbox("Select a Movie you liked!", data["title"])


if st.button("Recommendations"):
    recommendations, poster = top_5_movies(data, movie_choice)


    movie_1, movie_2, movie_3, movie_4, movie_5 = st.columns(5)


    with movie_1:
        st.text(recommendations[0])
        st.image(poster[0])
    with movie_2:
        st.text(recommendations[1])
        st.image(poster[1])
    with movie_3:
        st.text(recommendations[2])
        st.image(poster[2])
    with movie_4:
        st.text(recommendations[3])
        st.image(poster[3])
    with movie_5:
        st.text(recommendations[4])
        st.image(poster[4])
