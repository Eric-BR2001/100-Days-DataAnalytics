# Video Game Sales Analysis using Pandas

import pandas as pd

# Load dataset
df = pd.read_csv("video_game_sales.csv")
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
    "1. Which publisher has the most games?",
    "2. What are the top 5 best-selling games globally?",
    "3. How do average sales differ by platform?",
    "4. How many games were released per year?",
    "5. What's the correlation between critic score and global sales?"
]
print("\n--- Questions ---")
for q in questions:
    print(q)

# 3. Clean the Data
print("\n--- Cleaning Data ---")
df = df.dropna(subset=['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'Global_Sales'])
df['Critic_Score'] = df['Critic_Score'].fillna(df['Critic_Score'].mean())
df['Year_of_Release'] = df['Year_of_Release'].astype(int)
print("Cleaned Dataset Shape:", df.shape)

# 4. Answer the Questions
print("\n--- Answers ---")

# Q1: Publisher with the most games
most_games_publisher = df['Publisher'].value_counts().idxmax()
print("1. Publisher with most games:", most_games_publisher)

# Q2: Top 5 best-selling games
top_5_games = df[['Name', 'Global_Sales']].sort_values(by='Global_Sales', ascending=False).head(5)
print("\n2. Top 5 best-selling games:")
print(top_5_games)

# Q3: Average global sales per platform
platform_sales = df.groupby('Platform')['Global_Sales'].mean().sort_values(ascending=False)
print("\n3. Average global sales by platform:")
print(platform_sales.head())

# Q4: Games released per year
games_per_year = df['Year_of_Release'].value_counts().sort_index()
print("\n4. Games released per year:")
print(games_per_year.tail())

# Q5: Correlation between critic score and global sales
correlation = df['Critic_Score'].corr(df['Global_Sales'])
print("\n5. Correlation between Critic Score and Global Sales:", round(correlation, 2))
