import numpy as np


def recommend_movies_nn(title, movies, embeddings, indices, n_recommendations=5):
    if title not in indices:
        return ["Movie not found!"]

    idx = indices[title]
    movie_embedding = embeddings[idx]

    # Compute cosine similarity in embedding space
    cosine_sim = np.dot(embeddings, movie_embedding) / (
            np.linalg.norm(embeddings, axis=1) * np.linalg.norm(movie_embedding) + 1e-10
    )

    sim_scores = list(enumerate(cosine_sim))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n_recommendations + 1]
    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices].tolist()