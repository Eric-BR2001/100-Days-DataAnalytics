# Movie Data Analysis using Pandas

import pandas as pd

# Load dataset
df = pd.read_csv("movies.csv")
print("Initial Dataset Shape:", df.shape)
display(df.head())

# 1. Explore the Data
print("\n--- Dataset Info ---")
df.info()
print("\n--- Summary Statistics ---")
print(df.describe())
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 2. Questions to Answer
questions = [
    "1. Which director has the most movies in the dataset?",
    "2. What are the top 5 highest grossing movies?",
    "3. How does average rating vary by genre?",
    "4. How many movies are released per year?",
    "5. What's the correlation between budget and revenue?"
]
print("\n--- Questions ---")
for q in questions:
    print(q)

# 3. Clean the Data
print("\n--- Cleaning Data ---")
df = df.dropna(subset=['title', 'director', 'release_year', 'genre', 'rating', 'budget', 'revenue'])
df['release_year'] = df['release_year'].astype(int)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
print("Cleaned Dataset Shape:", df.shape)

# 4. Answer the Questions
print("\n--- Answers ---")

# Q1: Director with the most movies
most_movies_director = df['director'].value_counts().idxmax()
print("1. Director with most movies:", most_movies_director)

# Q2: Top 5 highest grossing movies
top_5_movies = df[['title', 'revenue']].sort_values(by='revenue', ascending=False).head(5)
print("\n2. Top 5 highest grossing movies:")
print(top_5_movies)

# Q3: Average rating by genre
genre_ratings = df.groupby('genre')['rating'].mean().sort_values(ascending=False)
print("\n3. Average rating by genre:")
print(genre_ratings.head())

# Q4: Movies released per year
movies_per_year = df['release_year'].value_counts().sort_index()
print("\n4. Movies released per year:")
print(movies_per_year.tail())

# Q5: Correlation between budget and revenue
correlation = df['budget'].corr(df['revenue'])
print("\n5. Correlation between Budget and Revenue:", round(correlation, 2))
