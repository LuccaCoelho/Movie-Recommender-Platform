from src.neural_model import compute_tfidf_embeddings, nn_model

def train_model(movies):
    X, tfidf = compute_tfidf_embeddings(movies)

    model = nn_model(input_dimension=X.shape[1])

    model = model.fit(X, X, epochs=20, batch_size=32)

    embeddings = model.predict(X)

    return model, embeddings, tfidf