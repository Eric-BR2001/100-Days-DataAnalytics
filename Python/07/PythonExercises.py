# Day 7: Python Exercises - Working with Pandas

import pandas as pd

# 1. Creating a DataFrame
def create_dataframe():
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40],
        "City": ["New York", "Los Angeles", "Chicago", "Houston"]
    }
    df = pd.DataFrame(data)
    return df

# 2. Reading from CSV
def read_csv_file(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        return "CSV file not found."

# 3. Basic DataFrame operations
def dataframe_operations(df):
    info = df.info()
    description = df.describe()
    head = df.head()
    return info, description, head

# 4. Filtering data
def filter_by_age(df, min_age):
    return df[df["Age"] > min_age]

# 5. Adding a new column
def add_salary_column(df):
    df["Salary"] = [50000, 60000, 70000, 80000]
    return df

# 6. Grouping data
def group_by_city(df):
    return df.groupby("City").mean(numeric_only=True)

# 7. Saving DataFrame to CSV
def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    return f"Data saved to {filename}"

# Example Tests
if __name__ == "__main__":
    df = create_dataframe()
    print("Original DataFrame:")
    print(df)

    df = add_salary_column(df)
    print("\nDataFrame with Salary column:")
    print(df)

    filtered_df = filter_by_age(df, 30)
    print("\nFiltered (Age > 30):")
    print(filtered_df)

    grouped = group_by_city(df)
    print("\nGrouped by City:")
    print(grouped)

    print(save_to_csv(df, "output_day7.csv"))
