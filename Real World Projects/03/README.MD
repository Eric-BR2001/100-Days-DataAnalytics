# 📊 Analyzing Crime in Los Angeles

This project explores crime patterns in Los Angeles using the `crimes.csv` dataset. The goal is to uncover insights about when and where crimes are most likely to occur, and which demographics are most affected.

## 🔍 Objectives

- Identify the hour with the highest frequency of crimes.
- Determine which area experiences the most crimes at night (10:00 PM to 3:59 AM).
- Analyze the distribution of crimes across different victim age groups.

## 📁 Dataset

The project uses a dataset named `crimes.csv`, which contains records of reported crimes in Los Angeles. Each record includes details such as the time, location, and victim demographics.

## 📌 Questions Answered

1. **Peak Crime Hour:**  
   Determine the hour of the day with the highest number of reported crimes.  
   🧠 Stored in the variable: `peak_crime_hour` (type: `int`)

2. **Top Night Crime Area:**  
   Identify the area with the most crimes occurring between 10:00 PM and 3:59 AM.  
   🧠 Stored in the variable: `peak_night_crime_location` (type: `str`)

3. **Victim Age Analysis:**  
   Calculate the number of crimes committed against victims from various age groups.  
   🧠 Stored in a `pandas.Series` called `victim_ages` with age group labels as the index and frequencies as values:
   - "0-17"
   - "18-25"
   - "26-34"
   - "35-44"
   - "45-54"
   - "55-64"
   - "65+"

## 🛠 Tools & Libraries

- Python
- Pandas
- Jupyter Notebook (recommended)