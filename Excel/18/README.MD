# Sleep Health and Lifestyle Dataset Project

## Project Overview
This project analyzes the "Sleep Health and Lifestyle" dataset. The goal is to understand how sleep patterns, health conditions, and lifestyle choices are related.

We answered important research questions, performed data cleaning, generated descriptive statistics, explored relationships between variables, and visualized the results. The final analysis and visualizations are available in the accompanying Excel file.

## Basic Data Understanding
- **Columns/Features:**
  - Person ID
  - Gender
  - Age
  - Occupation
  - Sleep Duration
  - Quality of Sleep
  - Physical Activity Level
  - Stress Level
  - BMI Category
  - Blood Pressure
  - Heart Rate
  - Daily Steps
  - Sleep Disorder

- **Number of Records (Rows):** 374

- **Missing Values:**
  - Missing values were filled by:
    - Numerical columns: median value
    - Categorical columns: most frequent value (mode)

## Descriptive Statistics
- **Average Sleep Duration:** 7.04 hours

- **Distribution of Sleep Disorders:**
  - None: majority of participants
  - Insomnia and Sleep Apnea were the two main disorders

- **Sleep Habits by Age and Gender:**
  - Sleep duration tends to decrease slightly with age.
  - Females and males have similar average sleep durations.

## Data Insights
- **BMI and Sleep Disorder:**
  - Higher BMI categories (Overweight, Obese) show a greater percentage of sleep disorders compared to Normal BMI individuals.

- **Exercise Frequency and Sleep Duration:**
  - There is a mild positive correlation: people with higher physical activity levels tend to sleep slightly longer.

- **Stress Level and Sleep Quality:**
  - There is a negative correlation: higher stress levels are associated with lower quality of sleep.

## Visualization
- A histogram of sleep duration was created, showing most participants sleep between 6 and 8 hours.

## Data Cleaning Process
1. Checked for missing values.
2. Filled missing numerical values with the median.
3. Filled missing categorical values with the mode.
4. Created a binary column for Sleep Disorder analysis.
5. Ensured consistent data formatting.

## Files Provided
- **Sleep_Health_Analysis_Project.xlsx**: Contains cleaned data, summary statistics, and multiple sheets with analysis results.
- **sleep_duration_histogram.png**: Visualization of Sleep Duration distribution.