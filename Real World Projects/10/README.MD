Here’s a professional and clear `README.md` file based on your project description:

---

# Cleaning Bank Marketing Campaign Data

This project focuses on tidying and restructuring a bank marketing campaign dataset by splitting it into logical subsets, updating values, converting data types, and saving the results into separate CSV files.

## Project Description

The original dataset, `bank_marketing.csv`, contains information collected during a marketing campaign by a Portuguese banking institution. The goal is to clean and reformat the dataset by:

* Splitting it into three meaningful subsets: `client`, `campaign`, and `economics`
* Updating and cleaning values to ensure consistency and accuracy
* Converting columns to the appropriate data types
* Exporting the cleaned subsets into separate CSV files

## Output Files

The cleaned and structured data is saved into the following files:

* `client.csv` — contains client-related data
* `campaign.csv` — contains information about the marketing campaign and its outcome
* `economics.csv` — includes economic indicators relevant to the campaign period

Each file is saved **without an index** and contains only the necessary columns as specified in the project notebook.

## Requirements

To run this project, you will need:

* Python 3.x
* pandas

You can install the required library using:

```bash
pip install pandas
```

## Usage

Run the accompanying Jupyter notebook or Python script to:

1. Load the original `bank_marketing.csv` file
2. Process and clean the data
3. Split it into three DataFrames: `client`, `campaign`, and `economics`
4. Save each DataFrame as a separate CSV file

## Notes

* Make sure the original dataset `bank_marketing.csv` is in the same directory as the notebook or script before running.
* Data types and column names should be consistent with the cleaning rules outlined in the notebook.

## License

This project is for educational and non-commercial use.

---

Let me know if you want me to include example code or a data dictionary section too.
