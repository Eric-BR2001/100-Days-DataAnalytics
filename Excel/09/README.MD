# 📊 Excel Theory: How to Analyze Multiple Tables

This project provides a practical guide and theory on how to analyze multiple tables in Microsoft Excel. It's ideal for beginners to intermediate users who want to understand how to connect, clean, and analyze data from different sources using Excel tools like **Power Query**, **Pivot Tables**, **LOOKUP functions**, and **Data Models**.

## 🧠 What You’ll Learn

- How to prepare and structure multiple tables in Excel
- How to use **Power Query** to import and transform tables
- How to create **relationships** between tables using the **Data Model**
- How to analyze linked tables using **Pivot Tables**
- Examples using functions like `VLOOKUP`, `XLOOKUP`, `INDEX`, `MATCH`, and `SUMIFS`

## 📂 Files Included

- `excel-multi-table-analysis.xlsx`: Example workbook with multiple tables and analysis steps
- `README.md`: Documentation and explanation of the project

## 🧪 Example Scenario

Imagine a retail company with these separate tables:

1. **Products Table** - product ID, name, category, and price
2. **Sales Table** - sale ID, product ID, quantity, date
3. **Stores Table** - store ID, location, and manager
4. **Sales Summary** - analysis combining all tables

We use **Power Query** to clean and load each table. Then, we relate them via **Product ID** and **Store ID** in the **Data Model**.

Finally, we generate a Pivot Table to analyze:

- Total Sales by Product
- Sales per Region
- Best-selling Categories
- Performance by Store

## 📘 Tools Used

- Excel 2016 or later (Power Query + Data Model support)
- Pivot Tables
- Lookup Functions (XLOOKUP / VLOOKUP)
- Power Query Editor

## 🧩 How to Use

1. Open the file `excel-multi-table-analysis.xlsx`
2. Go to the **Power Query Editor** to view the loaded tables
3. Explore the relationships in the **Data tab > Manage Data Model**
4. Navigate to the Pivot Table sheet to explore insights
5. Follow inline comments for step-by-step guidance

