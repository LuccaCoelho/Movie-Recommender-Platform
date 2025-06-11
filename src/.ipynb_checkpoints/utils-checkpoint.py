from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def compute_indices(movies):
    indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


    return indices