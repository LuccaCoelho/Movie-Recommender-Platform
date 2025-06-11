import pandas as pd
import ast

def extract_data(csv_path):
    df = pd.read_csv(csv_path)

    def parser(feature):
        try:
            features = ast.literal_eval(feature)
            return " ".join([column["name"] for column in features])
        except ValueError:
            return ""

    movies = df[["id", "title", "release_date", "genres", "overview", "keywords"]]

    movies["genres"] = movies["genres"].apply(parser)
    movies["keywords"] = movies["keywords"].apply(parser)
    movies['overview'] = movies['overview'].fillna('')

    movies["combined_features"] = movies["genres"] + movies["keywords"] + movies['overview']

    return movies