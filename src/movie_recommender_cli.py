import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load Data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

movies_path = os.path.join(BASE_DIR, "data", "raw", "movies.csv")
ratings_path = os.path.join(BASE_DIR, "data", "raw", "ratings.csv")

movies = pd.read_csv(movies_path)
ratings = pd.read_csv(ratings_path)

# Create User-Item Matrix

user_movie_matrix = ratings.pivot_table(
    index="movieId",
    columns="userId",
    values="rating"
).fillna(0)

# Compute Cosine Similarity Between Movies

movie_similarity = cosine_similarity(user_movie_matrix)

similarity_df = pd.DataFrame(
    movie_similarity,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)

# Recommendation Function

def get_recommendations(movie_title, n_recommendations=5):
    movie_matches = movies[movies["title"].str.contains(movie_title, case=False)]

    if movie_matches.empty:
        return None, None

    movie_id = movie_matches.iloc[0]["movieId"]
    movie_name = movie_matches.iloc[0]["title"]

    similar_scores = similarity_df[movie_id].sort_values(ascending=False)
    similar_movies = similar_scores.iloc[1:n_recommendations+1]

    recommended_movies = movies[movies["movieId"].isin(similar_movies.index)][
        ["movieId", "title"]
    ].reset_index(drop=True)

    return movie_name, recommended_movies

# Command Line Interface

if __name__ == "__main__":
    print("\n=== Movie Recommendation System ===")

    user_input = input("Enter a movie title: ")

    movie_name, recommendations = get_recommendations(user_input)

    if recommendations is None:
        print("\nMovie not found. Please try again.\n")
    else:
        print(f"\nBecause you liked '{movie_name}', you may also like:\n")
        for title in recommendations["title"]:
            print(f"- {title}")

    print()
