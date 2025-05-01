# Identifying Common Data in Excel

This guide explains various methods to identify and work with common data (duplicates or matches) across Excel worksheets or columns.

## Methods to Identify Common Data

### 1. Conditional Formatting for Duplicates
Quickly highlight duplicate values:
1. Select the data range
2. Go to `Home` > `Conditional Formatting` > `Highlight Cells Rules` > `Duplicate Values`
3. Choose formatting style and click OK

### 2. Using the COUNTIF Function
Identify if a value exists in another list:
```excel
=COUNTIF(OtherRange, CurrentCell)>0
```
Returns TRUE if the value is found in the other range.

### 3. MATCH Function
Find position of a value in another range:
```excel
=MATCH(LookupValue, LookupRange, 0)
```
Returns #N/A if no match is found.

### 4. VLOOKUP Function
Check for common values between columns:
```excel
=VLOOKUP(LookupValue, TableRange, ColumnNumber, FALSE)
```
Returns #N/A if no match exists.

### 5. Using Power Query (Excel 2016+)
More advanced matching:
1. Go to `Data` > `Get & Transform` > `From Table/Range`
2. Use merge operations to find matching rows
3. Load results back to Excel

### 6. Pivot Tables
Identify common items by:
1. Create a pivot table from your data
2. Add the relevant fields to rows
3. Count occurrences to find duplicates

## Tips for Working with Common Data

- **Remove Duplicates**: Data tab > Remove Duplicates
- **Filter for Duplicates**: After conditional formatting, filter by color
- **Compare Two Sheets**: Use `=IF(ISNA(MATCH(A1,Sheet2!A:A,0)),"Unique","Duplicate")`
- **Exact vs. Fuzzy Matching**: Consider using TRIM() and CLEAN() for text data

