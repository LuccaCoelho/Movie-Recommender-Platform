from sklearn.metrics.pairwise import cosine_similarity


def get_cos_sim(vector):
    cos_sim = cosine_similarity(vector)

    return cos_sim