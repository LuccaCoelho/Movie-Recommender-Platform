from src.vectorize_text import count_vectorizer
from src.calculate_cosine_similarity import get_cos_sim
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(
        movie_id)
    poster = requests.get(url)
    poster = poster.json()
    poster_path = poster['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def top_5_movies(data, movie_title):
    vector = count_vectorizer(data)
    similarity = get_cos_sim(vector)

    idx = data[data["title"] == movie_title].index[0]

    distance = sorted(list(enumerate(similarity[idx])), reverse=True, key = lambda vector: vector[1])

    recommendation_list = []
    poster_list = []

    for i in distance[1:6]:
        recommendation_list.append(data.iloc[i[0]].title)
        poster_list.append(fetch_poster(data.iloc[i[0]].id))

    return recommendation_list, poster_list