from sklearn.feature_extraction.text import TfidfVectorizer
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.models import Model

def compute_tfidf_embeddings(movies):
    tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = tfidf.fit_transform(movies["combined_features"])

    return tfidf_matrix.toarray(), tfidf

def nn_model_trained(movies, embedding_dim=128):
    X, tfidf = compute_tfidf_embeddings(movies)
    inputs = Input(shape=(X.shape[1],))
    x = Dense(512, activation='relu')(inputs)
    x = Dropout(0.2)(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.2)(x)
    outputs = Dense(embedding_dim, activation='linear')(x)

    model = Model(inputs=inputs, outputs=outputs)
    model = model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model = model.fit(X, X, epochs=20, batch_size=32)

    embeddings = model.predict(X)

    return embeddings  # <--- THIS LINE IS CRUCIAL