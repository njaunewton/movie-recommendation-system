MOVIE RECOMMENDATION SYSTEM (Collaborative Filtering)

PROJECT OVERVIEW

This project develops a movie recommendation system using the MovieLens Latest Small dataset.
The system leverages collaborative filtering techniques to generate personalized movie recommendations based on user–movie rating patterns.

The objectives of the project were to:

Perform exploratory data analysis (EDA)

Address dataset sparsity through preprocessing

Build a similarity-based recommendation engine

Deploy a working command-line interface (CLI) application

DATASET

Source: MovieLens Latest Small Dataset

The recommendation system primarily relies on the following variables:

userId

movieId

rating

These variables are used to construct a user–item rating matrix, which captures historical user preferences. Similarity between movies is computed based on rating patterns within this matrix. Other metadata such as movie titles and genres are used only for interpretation and presentation, not for modeling.

METHODOLOGY

The system implements item-based collaborative filtering using:

User–item rating matrix construction

Cosine similarity computation

Minimum interaction threshold filtering (20 ratings per user)

The recommendation engine identifies movies with similar rating behavior and suggests them based on the selected input movie.

COMMAND LINE INTERFACE (CLI)

A functional CLI application was developed to simulate practical system deployment.

To run the application:

Navigate to the src folder

Run: python movie_recommender_cli.py

Example session:

=== Movie Recommendation System ===
Enter a movie title: Toy Story

Because you liked 'Toy Story (1995)', you may also like:

Star Wars: Episode IV - A New Hope (1977)

Forrest Gump (1994)

Jurassic Park (1993)

Independence Day (1996)

Toy Story 2 (1999)

PROJECT STRUCTURE

ml-latest-small/
│
├── data/
│   └── raw/
│       ├── movies.csv
│       ├── ratings.csv
│       ├── tags.csv
│       └── links.csv
│
├── notebooks/
│   └── Newton_Capstone_Recommendation System.ipynb
│
├── reports/
│   ├── HTML.html
│   └── PDF.pdf
│
├── src/
│   └── movie_recommender_cli.py
│
└── README.md

KEY INSIGHTS

The dataset exhibits high sparsity (approximately 98 percent).

Movie rating distributions follow a long-tail pattern.

Collaborative filtering effectively captures user preference patterns without relying on content attributes.

Applying a 20-rating minimum threshold improves recommendation reliability while maintaining dataset coverage.

FUTURE IMPROVEMENTS

Implement matrix factorization techniques such as SVD

Add hybrid content-based filtering

Develop a web-based interface using Streamlit or Flask

Deploy the system as a cloud-hosted API

AUTHOR

Newton Mirang'a
North American College of Information Technology (NACIT)
Capstone Project – Recommendation Systems