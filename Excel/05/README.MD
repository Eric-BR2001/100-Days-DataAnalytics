# 📆 Day 3: Modern Excel Functions & Dynamic Arrays

Welcome to **Day 3** of *Understanding Functions in Excel*! Today, we’ll explore Excel’s modern capabilities — **Dynamic Arrays**, powerful new functions like `XLOOKUP`, `UNIQUE`, and `FILTER`, and how they simplify and enhance what used to require complex formulas.

These functions are available in **Excel 365** and **Excel 2021+**.

---

## 📌 Table of Contents

1. [What Are Dynamic Arrays?](#what-are-dynamic-arrays)
2. [Introducing XLOOKUP – The VLOOKUP Killer](#introducing-xlookup--the-vlookup-killer)
3. [FILTER – Custom Views from Raw Data](#filter--custom-views-from-raw-data)
4. [UNIQUE – Remove Duplicates with a Formula](#unique--remove-duplicates-with-a-formula)
5. [SORT & SORTBY – Organize Your Data](#sort--sortby--organize-your-data)
6. [SEQUENCE & RANDARRAY](#sequence--randarray)
7. [Real-World Use Case – Dynamic Sales Report](#real-world-use-case--dynamic-sales-report)
8. [Wrap-up](#wrap-up)

---

## 🧬 What Are Dynamic Arrays?

Dynamic Arrays allow functions to return **multiple values** that automatically "spill" into adjacent cells.

Instead of writing the same formula over and over, one formula now fills the range.

### Example:

```excel
=A1:A5 * 2
```

This multiplies every value in the range A1:A5 by 2 and spills the result.

---

## 🔍 Introducing XLOOKUP – The VLOOKUP Killer

`XLOOKUP` replaces `VLOOKUP`, `HLOOKUP`, and even `INDEX` + `MATCH`.

### Syntax:

```excel
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found])
```

### Example:

```excel
=XLOOKUP("John", A2:A100, C2:C100, "Not Found")
```

📌 Benefits:
- Searches left OR right
- Exact match by default
- Cleaner syntax

---

## 🔎 FILTER – Custom Views from Raw Data

Extract rows that meet certain conditions.

### Syntax:

```excel
=FILTER(array, include, [if_empty])
```

### Example:

```excel
=FILTER(A2:C100, C2:C100="USA", "No results")
```

📌 Use case: Create filtered dashboards without manual sorting.

---

## 🧼 UNIQUE – Remove Duplicates with a Formula

### Syntax:

```excel
=UNIQUE(array)
```

### Example:

```excel
=UNIQUE(B2:B100)
```

Returns a list of distinct values.

📌 Use case: Create dropdown lists or summary reports from long data lists.

---

## 🔢 SORT & SORTBY – Organize Your Data

### SORT

```excel
=SORT(array, [sort_index], [sort_order])
```

Sorts a range based on one column.

### SORTBY

```excel
=SORTBY(array, sort_by_array, [sort_order])
```

More flexible — sort based on a different range.

---

## 🎲 SEQUENCE & RANDARRAY

### SEQUENCE

```excel
=SEQUENCE(rows, [columns], [start], [step])
```

Create lists without dragging formulas.

### Example:

```excel
=SEQUENCE(10,1,1,1) → 1 to 10
```

### RANDARRAY

```excel
=RANDARRAY([rows], [columns], [min], [max], [integer])
```

Generate a table of random numbers.

---

## 📈 Real-World Use Case – Dynamic Sales Report

Let’s say you have a list of sales records with:

- Date
- Region
- Product
- Revenue

### Use the following dynamic array combo:

1. **UNIQUE** to get all regions:
   ```excel
   =UNIQUE(RegionColumn)
   ```

2. **FILTER** to show sales for selected region:
   ```excel
   =FILTER(SalesTable, RegionColumn = SelectedRegion)
   ```

3. **SORT** to display top sellers:
   ```excel
   =SORT(FILTER(...), RevenueColumn, -1)
   ```

✨ Now you’ve got a mini dashboard with only formulas — no pivot tables required!

---

## ✅ Wrap-up

Today you learned about:
- Excel's new generation of **dynamic functions**
- How to build **interactive tools** using just formulas
- The power of **array formulas** to automate reports

---

