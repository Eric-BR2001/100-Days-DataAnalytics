# When-Was-the-Golden-Era-of-Video-Games-
Let's use SQL to figure out the golden era of video games!

## Project Description
According to Mordor Intelligence, video games are big business: the global gaming market is projected to be worth more than $300 billion by 2027. With so much money at stake, the major game publishers are hugely incentivized to create the next big hit. But are games getting better, or has the golden age of video games already passed?

In this project, you'll analyze video game critic and user scores, in addition to sales data for the top 400 video games released since 1977. You'll search for a golden age of video games by identifying release years that users and critics liked best, and you'll explore the business side of gaming by looking at game sales data.

# 🎮 Golden Age of Video Games

![Video Game](video_game.jpg)

Video games are big business: the global gaming market is projected to be worth more than **$300 billion by 2027**, according to *Mordor Intelligence*. With so much money at stake, major game publishers are racing to create the next big hit.

But that brings up an interesting question:  
**Are video games getting better, or has the golden age of gaming already passed?**

In this project, we dive into critic and user review scores, as well as game sales data, to uncover the golden years of gaming and examine the business side of the industry.

---

## 📊 Objective

- **Analyze** video game scores and sales for the top 400 games released since 1977.
- **Identify** the most loved years by critics and users.
- **Investigate** the correlation between high scores and high sales.
- **Uncover** the golden years of the video game industry.

---

## 🗃️ Dataset Overview

The project is based on a reduced dataset containing 400 of the top video games. The complete dataset is available on [Kaggle](https://www.kaggle.com/).

### `game_sales` table
| Column     | Definition                       | Type     |
|------------|----------------------------------|----------|
| name       | Name of the video game           | `varchar` |
| platform   | Gaming platform                  | `varchar` |
| publisher  | Game publisher                   | `varchar` |
| developer  | Game developer                   | `varchar` |
| games_sold | Number of copies sold (millions) | `float`   |
| year       | Release year                     | `int`     |

### `reviews` table
| Column       | Definition                             | Type     |
|--------------|----------------------------------------|----------|
| name         | Name of the video game                 | `varchar` |
| critic_score | Critic score (Metacritic)              | `float`   |
| user_score   | User score (Metacritic)                | `float`   |

### `users_avg_year_rating` table
| Column        | Definition                                  | Type   |
|---------------|---------------------------------------------|--------|
| year          | Release year                                | `int`  |
| num_games     | Number of games released that year          | `int`  |
| avg_user_score| Average user score that year                | `float`|

### `critics_avg_year_rating` table
| Column         | Definition                                 | Type   |
|----------------|--------------------------------------------|--------|
| year           | Release year                               | `int`  |
| num_games      | Number of games released that year         | `int`  |
| avg_critic_score| Average critic score that year           | `float`|

---

## 🧠 SQL Queries & Analysis

### 🔝 Best Selling Games
```sql
SELECT * 
FROM game_sales 
ORDER BY games_sold DESC 
LIMIT 10;
```

### 🏆 Critics' Top Ten Years
```sql
SELECT 
  g.year, 
  COUNT(g.name) AS num_games, 
  ROUND(AVG(r.critic_score), 2) AS avg_critic_score
FROM 
  game_sales g
INNER JOIN 
  reviews r ON g.name = r.name
GROUP BY 
  g.year
HAVING 
  COUNT(g.name) >= 4
ORDER BY 
  avg_critic_score DESC
LIMIT 10;
```

### ✨ Golden Years of Gaming
```sql
SELECT 
  u.year, 
  u.num_games, 
  c.avg_critic_score, 
  u.avg_user_score, 
  c.avg_critic_score - u.avg_user_score AS diff
FROM 
  critics_avg_year_rating c
INNER JOIN 
  users_avg_year_rating u ON c.year = u.year
WHERE 
  c.avg_critic_score > 9 OR u.avg_user_score > 9
ORDER BY 
  c.year ASC;
```

---

## 🧩 Skills Applied

- SQL Aggregation (`AVG`, `COUNT`, `ROUND`)
- Filtering with `WHERE` and `HAVING`
- Joining Tables (`INNER JOIN`)
- Grouping (`GROUP BY`)
- Sorting (`ORDER BY`)

---

## 📌 Conclusion

This analysis reveals which years were most loved by users and critics alike, and hints at whether the best days of gaming are behind us or still to come. By looking at both **sentiment** (scores) and **sales**, we gain insight into both the cultural and commercial success of video games through the decades.

---

## 🚀 Explore Further

🔗 Dataset source: [Kaggle - Video Game Sales with Ratings](https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings)

