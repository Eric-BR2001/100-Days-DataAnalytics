# Understanding Search Interest with Google Trends

This project analyzes time series data from [Google Trends](https://trends.google.com/) to explore changes in public interest for various AI tools over time.

## 📊 Objective

Leverage Google Trends data to extract meaningful insights and answer key analytical questions regarding the popularity and growth of AI tools.

## 🧠 Key Questions Answered

1. **Consistent Growth:**
   Which AI tool has shown the most consistent growth in interest over the observed period?
   **Output variable:** `most_consistent_tool` *(string)*

2. **Interest Over Time:**
   Visualize the interest levels of **ChatGPT**, **Gemini**, and **Microsoft Copilot** over time.
   Identify when **ChatGPT** experienced its largest decline in interest.
   **Output variable:** `gpt_dip` *(string in the format "Month YYYY")*

3. **Seasonality Analysis:**
   Explore seasonality by calculating **monthly average interest** for each tool.
   Determine which month had the highest average interest across all tools.
   **Output variable:** `best_month` *(string)*

## 📁 Project Structure

* `notebook.ipynb`: Jupyter Notebook with data loading, cleaning, visualization, and insights.
* `data/`: Folder containing CSV or Excel files exported from Google Trends.
* `images/`: Plots generated during the analysis.
* `README.md`: Project overview and documentation.
