# 🛠️ Debugging a Sales Data Workflow

**Project Overview**

In real-world data pipelines, even well-functioning workflows can suddenly fail — due to schema changes, data quality issues, or logic errors. This project simulates one such situation using **sales data** where your task is to use **pandas** and your knowledge of **DataFrames** to find the root cause and fix the issue.

---

This project includes a `load_and_check()` function designed to validate the structure and integrity of a sales dataset (`sales.csv`). The goal is to ensure the data is properly formatted and consistent without modifying the raw CSV file directly.

## Instructions

1. Run the `load_and_check()` function first.
2. Look for any error messages in the output – these will indicate what needs to be fixed.
3. The function should return exactly two success messages:

   * `Data loaded successfully`
   * `Data integrity check was successful!`

## What to Review

Open the `load_and_check()` function and examine its logic. Focus on the two key integrity checks:

* **Column Count Check**: Validates that the dataset has the expected number of columns.
* **Data Integrity Check**: Includes two conditions:

  * **Condition 1**: Verifies that total values (e.g., Quantity × Unit Price) are correct.
  * **Condition 2**: Confirms that tax calculations are accurate at a 5% rate.

## Your Task

Identify and fix issues within the `load_and_check()` function **only**.
Do **not** modify the raw `sales.csv` dataset.
Make any necessary adjustments (e.g., column names, data types, calculations) inside the function.

The goal is to make the function return **only** the two success messages listed above.
