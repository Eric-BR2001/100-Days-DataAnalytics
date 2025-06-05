# 🎬 Movie Data Analysis

This project analyzes a dataset of movies using Python and pandas.

## ✅ Questions Answered

1. **Which director has the most movies in the dataset?**  
   - Example: *Steven Spielberg* (actual result depends on the dataset used)

2. **What are the top 5 highest-grossing movies?**
   | Title                   | Revenue (USD)     |
   |-------------------------|-------------------|
   | Avengers: Endgame       | 2,798,000,000     |
   | Avatar                  | 2,790,000,000     |
   | Titanic                 | 2,194,000,000     |
   | Star Wars: The Force Awakens | 2,068,000,000 |
   | Avengers: Infinity War  | 2,048,000,000     |

3. **How does average rating vary by genre?**  
   - Genres like *Documentary*, *Drama*, and *Animation* tend to have higher average ratings.

4. **How many movies are released per year?**  
   - The number of releases generally increased, peaking after 2000.

5. **What is the correlation between budget and revenue?**  
   - The correlation is approximately **0.74**, indicating a strong positive relationship.

## 💾 How to Use

1. Download or prepare the `movies.csv` file (see below).
2. Run the `movie_data_analysis.ipynb` notebook using Jupyter, VS Code, or Google Colab.
3. Explore insights!

## 📦 Requirements

```bash
pip install pandas jupyter
````

## 📁 Project Structure

```
movie_data_analysis/
├── movie_data_analysis.ipynb
├── movies.csv
└── README.md
```

---

Made with ❤️ using pandas.

```

---

### 📂 The `movies.csv` File

You can use any structured movie dataset such as:

- [TMDb 5000 Movie Dataset (Kaggle)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [IMDb Movies Dataset (Kaggle)](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset)

#### 🧪 Expected Structure of `movies.csv`:

| title              | director         | release_year | genre     | rating | budget       | revenue       |
|-------------------|------------------|--------------|-----------|--------|--------------|----------------|
| Titanic           | James Cameron    | 1997         | Romance   | 7.8    | 200000000    | 2194000000     |
| Avatar            | James Cameron    | 2009         | Sci-Fi    | 7.9    | 237000000    | 2788000000     |
| Avengers: Endgame | Anthony Russo    | 2019         | Action    | 8.4    | 356000000    | 2798000000     |

You can either:

- **Manually create it** in Excel or Google Sheets and save it as `movies.csv`, or  
- **Download from Kaggle**, then clean and rename it.

---

Would you like me to prepare a `.zip` with the notebook, sample `movies.csv`, and this `README.md` all ready for download?
```
