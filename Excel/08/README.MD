# 📊 Creating Dynamic Tables in Excel

This project demonstrates how to create and use **dynamic tables** in Microsoft Excel to better manage and analyze your data. Dynamic tables (also known as Excel Tables) are a powerful tool for working with structured data, allowing for easy sorting, filtering, and formula management.

## ✅ Features

- Create structured dynamic tables from raw data
- Auto-expand with new rows and columns
- Built-in filtering and sorting
- Use structured references in formulas
- Dynamic charts linked to table data
- Support for data validation and conditional formatting

## 🧰 Requirements

- Microsoft Excel 2013 or later
- Basic knowledge of Excel functions

## 🚀 Getting Started

1. **Open Excel** and create a new workbook or open your dataset.
2. **Insert a Table**:
   - Select your data range.
   - Go to the `Insert` tab and click on `Table`.
   - Make sure "My table has headers" is checked if applicable.
3. **Name Your Table**:
   - With the table selected, go to the `Table Design` tab.
   - Set a meaningful name in the "Table Name" field.

4. **Use Structured References**:
   - Instead of using `A2:A10`, use `[ColumnName]` in formulas.
   - Example: `=SUM(Table1[Sales])`

5. **Add Data and Watch It Grow**:
   - When you add new rows, the table auto-expands and includes them in calculations.

6. **Apply Filters & Sort**:
   - Use the dropdowns on headers to filter or sort data instantly.

7. **Create a Dynamic Chart** (Optional):
   - Insert a chart while the table is selected.
   - The chart will automatically update when new data is added.

## 📂 Example Files

| File Name | Description |
|----------|-------------|
| `dynamic-table-example.xlsx` | Sample Excel file with dynamic tables |
| `sales-dashboard.xlsx` | Example of using dynamic tables with a dashboard |

## 💡 Tips

- Use `Ctrl + T` shortcut to create a table quickly.
- Use Excel formulas like `SUMIFS`, `VLOOKUP`, and `INDEX` with structured references.
- Combine tables with PivotTables for advanced analysis.

## 📘 Resources

- [Microsoft Excel Tables Guide](https://support.microsoft.com/en-us/excel-tables)
- [ExcelJet - Structured References](https://exceljet.net/excel-table-structured-references)
- [How to Create Dynamic Charts in Excel](https://www.excel-easy.com/examples/dynamic-charts.html)

