# 📆 Day 2: Practical Examples of Functions in Action

Welcome back to **Day 2** of *Understanding Functions in Excel*! Now that you’ve got a solid grasp of how functions work theoretically, it’s time to explore **real-world applications** using some of the most commonly used Excel functions.

This hands-on section introduces you to powerful Excel functions across categories, using practical examples and sample use cases.

---

## 📌 Table of Contents

1. [Using the IF Function](#using-the-if-function)
2. [Working with Lookup Functions](#working-with-lookup-functions)
   - `VLOOKUP`
   - `INDEX` + `MATCH`
3. [Text Manipulation Functions](#text-manipulation-functions)
4. [Date & Time Functions](#date--time-functions)
5. [Math & Statistical Functions](#math--statistical-functions)
6. [Combining Functions in Real-Life Scenarios](#combining-functions-in-real-life-scenarios)

---

## ✅ Using the IF Function

The `IF` function allows conditional logic. It checks a condition and returns different values depending on the result.

### Syntax:
```excel
=IF(logical_test, value_if_true, value_if_false)
```

### Example:
```excel
=IF(A2 >= 60, "Pass", "Fail")
```

📌 Use case: Grade evaluation, payment status, approval flows.

---

## 🔎 Working with Lookup Functions

### 📘 VLOOKUP

Find a value in the first column of a table and return a value in the same row from another column.

### Syntax:
```excel
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

### Example:
```excel
=VLOOKUP("John", A2:C10, 2, FALSE)
```

📌 Use case: Looking up employee details, product pricing, etc.

---

### 🧩 INDEX + MATCH (More flexible)

- `INDEX` returns the value of a cell in a range.
- `MATCH` returns the relative position of a value in a range.

### Example:
```excel
=INDEX(B2:B10, MATCH("John", A2:A10, 0))
```

📌 Use case: More dynamic and robust than `VLOOKUP` when data layout changes.

---

## 🔤 Text Manipulation Functions

| Function | Purpose                        | Example |
|----------|--------------------------------|---------|
| `LEFT`   | Extract left-side characters   | `=LEFT(A1, 3)` |
| `RIGHT`  | Extract right-side characters  | `=RIGHT(A1, 4)` |
| `LEN`    | Count characters                | `=LEN(A1)` |
| `CONCAT` or `TEXTJOIN` | Combine text      | `=CONCAT(A1, " ", B1)` |

📌 Use case: Parsing product codes, formatting names, extracting email domains.

---

## 🗓 Date & Time Functions

| Function    | Description                          | Example                          |
|-------------|--------------------------------------|----------------------------------|
| `TODAY()`   | Returns current date                 | `=TODAY()`                       |
| `NOW()`     | Returns current date and time        | `=NOW()`                         |
| `DATEDIF`   | Calculates difference between dates   | `=DATEDIF(A1, B1, "Y")`          |
| `TEXT`      | Formats a date/time as text          | `=TEXT(TODAY(), "dd/mm/yyyy")`  |

📌 Use case: Age calculators, timelines, expiry dates.

---

## ➕ Math & Statistical Functions

| Function  | Description                     | Example                    |
|-----------|---------------------------------|----------------------------|
| `SUM`     | Adds numbers                    | `=SUM(A1:A5)`              |
| `AVERAGE` | Returns average                 | `=AVERAGE(B1:B5)`          |
| `ROUND`   | Rounds to specified decimals   | `=ROUND(C1, 2)`            |
| `COUNTIF` | Counts cells matching a criteria | `=COUNTIF(A1:A10, ">50")`  |

📌 Use case: Budget tracking, performance scoring, counting conditions.

---

## 🔁 Combining Functions in Real-Life Scenarios

### 📦 Scenario: Discount Calculator

| A | B        | C        |
|---|----------|----------|
| Product | Price   | Discount (%) |

```excel
=IF(C2>0, B2*(1-C2), B2)
```

---

### 📊 Scenario: Sales Dashboard Metric

```excel
=IF(AVERAGE(B2:B10) > 5000, "Above Target", "Below Target")
```

Combines `IF` and `AVERAGE` to assess performance.

---
