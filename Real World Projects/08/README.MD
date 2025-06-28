# ✈️ Analyzing Flight Delays and Cancellations

This project analyzes flight delays and cancellations to identify patterns, high-impact routes and airlines, and the potential effects of wind on departure times. The focus is on deriving actionable insights from the data, using Python and Pandas for data processing and Matplotlib/Seaborn for visualization.

## 📊 Objective

To answer key questions related to:

* Which **airlines** and **routes** are most affected by **delays and cancellations**
* How **wind gusts** impact **departure delays** at major airports

---

## 📁 Dataset

The analysis uses two CSV files loaded into separate Pandas DataFrames:

* `flights.csv`: Contains flight-level data including delays and cancellation status.
* `weather.csv`: Contains weather data including wind gusts at airports like SEA and PDX.

---

## 🧠 Key Analyses

1. **Routes Analysis**

   * Compute average departure delays.
   * Count cancellations.
   * Create a DataFrame: `routes_delays_cancels`.

2. **Airlines Analysis**

   * Compute average departure delays.
   * Count cancellations.
   * Create a DataFrame: `airlines_delays_cancels`.

3. **Visualizations**

   * `top9_route_cancels_bar`: Bar chart of top 9 routes with the highest cancellations.
   * `top9_airline_delays_bar`: Bar chart of top 9 airlines with the highest average departure delays.

4. **Wind Impact Evaluation**

   * Evaluate whether wind gusts (≥10 mph) correlate with higher average departure delays at SEA and PDX.
   * Result stored as a boolean variable: `wind_response`.

