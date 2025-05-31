# TMDb Movie Analysis - Results via API

This document contains the **answers** to each of the 15 questions, along with the **HTTP method (`GET`)** and the **endpoint path** used for each query to the TMDb API.

---

1. **How many movies are registered in the database?**
   ➡️ GET `/movie/latest`
   🔎 **Answer:** Latest movie ID: `<id>` (represents an approximate total count of movies)

2. **What are the 10 oldest movies in the database?**
   ➡️ GET `/discover/movie?sort_by=release_date.asc`
   🔎 **Answer:** List of the 10 oldest movies by release date.

3. **How many movies were released by decade?**
   ➡️ GET `/discover/movie?sort_by=release_date.asc`
   🔎 **Answer:** Grouped count of movies by decade.

4. **What is the most common movie genre in the database?**
   ➡️ GET `/genre/movie/list` + `/discover/movie`
   🔎 **Answer:** Most frequent genre (e.g., Drama, Comedy, etc.)

5. **How many science fiction movies have a rating above 8.0?**
   ➡️ GET `/discover/movie?with_genres=<sci-fi_id>&sort_by=vote_average.desc`
   🔎 **Answer:** Number of sci-fi movies with rating > 8.0

6. **What are the 5 highest-grossing horror movies?**
   ➡️ GET `/discover/movie?with_genres=<horror_id>&sort_by=revenue.desc`
   🔎 **Answer:** List of top 5 horror films by revenue

7. **Which director has the most movies in the database?**
   ➡️ GET `/movie/{movie_id}/credits`
   🔎 **Answer:** Most frequent director across sampled movie credits

8. **Which actors/actresses appear in more than 10 movies?**
   ➡️ GET `/person/popular` + `/person/{person_id}/movie_credits`
   🔎 **Answer:** List of people with more than 10 movie appearances

9. **Which movie has the largest cast (most credited actors)?**
   ➡️ GET `/movie/{movie_id}/credits`
   🔎 **Answer:** Movie with the highest number of credited actors

10. **What are the top 3 movies with the highest average rating (e.g., IMDb/TMDb)?**
    ➡️ GET `/discover/movie?sort_by=vote_average.desc&vote_count.gte=1000`
    🔎 **Answer:** Top 3 movies by average rating

11. **Which movie has the largest difference between critic and audience ratings?**
    🚫 **Not available via public API.**
    🔎 **Answer:** Professional critic scores are not provided directly by the API.

12. **Is there a correlation between budget and movie ratings?**
    ➡️ GET `/movie/{movie_id}`
    🔎 **Answer:** Pearson correlation coefficient between `budget` and `vote_average`

13. **Which year had the highest number of movie releases?**
    ➡️ GET `/discover/movie?sort_by=release_date.asc`
    🔎 **Answer:** Year with the highest number of releases (based on release dates)

14. **Which movie had the highest financial return (box office vs. budget)?**
    ➡️ GET `/movie/{movie_id}`
    🔎 **Answer:** Movie with the highest positive difference between revenue and budget

15. **How did the average ratings evolve over the years (e.g., decade by decade)?**
    ➡️ GET `/discover/movie`
    🔎 **Answer:** Line graph showing the evolution of average ratings per year

---

