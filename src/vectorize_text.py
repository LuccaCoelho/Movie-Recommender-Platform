from sklearn.feature_extraction.text import CountVectorizer

def count_vectorizer( data, max_features=5000):
    cv = CountVectorizer(max_features=max_features, stop_words="english")

    vector = cv.fit_transform(data["combined_features"].values.astype("U")).toarray()

    return vector