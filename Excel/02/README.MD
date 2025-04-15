# 📆 Day 2: Advanced Use of Variables in Excel

Welcome back! On Day 1, we explored the basics of how Excel uses cell references and named ranges to simulate variables. Now, let’s dive into **practical use cases** and **dynamic techniques** that take these concepts to the next level.

---

## 📌 Table of Contents

1. [Recap of Day 1](#recap-of-day-1)
2. [Dynamic Named Ranges with OFFSET & INDEX](#dynamic-named-ranges-with-offset--index)
3. [Variables with Data Validation (Dropdowns)](#variables-with-data-validation-dropdowns)
4. [Using Variables with Conditional Logic (IF, SWITCH)](#using-variables-with-conditional-logic-if-switch)
5. [Scenario: Building a Simple Price Calculator](#scenario-building-a-simple-price-calculator)
6. [Bonus: Named Ranges with Tables](#bonus-named-ranges-with-tables)
7. [Wrap-up](#wrap-up)

---

## 🔁 Recap of Day 1

- Cell references = base level “variables”
- Named ranges = readable and reusable “labels” for cells or ranges
- Used in financial models, dashboards, and reusable formulas

---

## 🔄 Dynamic Named Ranges with OFFSET & INDEX

Named ranges don’t have to be static — they can adapt automatically as data grows.

### 🧠 Example: Dynamic List with `OFFSET`

```excel
=OFFSET(Sheet1!$A$1, 0, 0, COUNTA(Sheet1!$A:$A), 1)
```

Name this range `ProductList`, and it will grow as new products are added in column A.

### 📦 Using `INDEX` for Safer Dynamic Ranges

```excel
=Sheet1!$A$1:INDEX(Sheet1!$A:$A, COUNTA(Sheet1!$A:$A))
```

This is more stable than `OFFSET`, especially in large files.

---

## 🎛 Variables with Data Validation (Dropdowns)

Named ranges can be used as **sources** for dropdown lists via Data Validation:

1. Create a dynamic list and name it (e.g., `CategoryList`)
2. Go to **Data > Data Validation**
3. Set **Allow:** List and **Source:** `=CategoryList`

This lets users select a variable value, triggering calculations dynamically.

---

## 🧩 Using Variables with Conditional Logic (IF, SWITCH)

Named ranges can be used in formulas that act based on conditions.

### ✅ Example: IF Statement with Named Ranges

```excel
=IF(Status="Approved", Amount * DiscountRate, Amount)
```

### 🔁 SWITCH Function

```excel
=SWITCH(Plan, 
    "Basic", 10,
    "Pro", 20,
    "Enterprise", 50
)
```

Here, `Plan` could be a named range linked to a dropdown.

---

## 🧮 Scenario: Building a Simple Price Calculator

### Setup

| Cell | Value   | Name        |
|------|---------|-------------|
| A1   | 100     | UnitPrice   |
| A2   | 5       | Quantity    |
| A3   | 0.1     | DiscountRate|

### Formula in `B1`

```excel
=UnitPrice * Quantity * (1 - DiscountRate)
```

This simulates variable-based computation — readable and updatable.

---

## 🧾 Bonus: Named Ranges with Tables

When using **Excel Tables** (`Ctrl + T`):

- Columns are treated like dynamic named ranges.
- Example formula in a table: `=[@Quantity] * [@Price]`
- These automatically expand when you add rows.

### Benefits:

- Auto-expansion
- No need for manual updates
- Great for dashboards and reports

---

## ✅ Wrap-up

On Day 2, we learned how to:
- Create **dynamic named ranges** using `OFFSET` and `INDEX`
- Use named ranges with **data validation**
- Apply **logical formulas** with named references
- Combine all of the above in real-life scenarios and dynamic calculators

---
