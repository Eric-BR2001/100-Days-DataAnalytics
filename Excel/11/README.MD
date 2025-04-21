# 📊 Excel Exercises

Welcome to the **Excel Exercises** repository! This project is designed to help learners practice and master Excel skills through real-world examples and problem-solving.

## 🚀 What You'll Learn

- Basic formulas and functions
- Data formatting and validation
- Charts and graphs
- Logical functions (IF, AND, OR)
- Lookup functions (VLOOKUP, HLOOKUP, INDEX, MATCH)
- Pivot tables and summaries
- Data analysis and visualization

## 📁 Structure

- `exercises/`: Contains Excel files for each set of exercises.
- `solutions/`: Contains completed versions with answers and explanations.
- `README.md`: Overview and learning path.

## ✅ Requirements

- Microsoft Excel (or Google Sheets / LibreOffice Calc)
- Basic knowledge of spreadsheet usage

## 🧠 Example Exercises

### 1. Calculate Total Price
| Product | Price | Quantity | Total |
|---------|-------|----------|-------|
| Apple   | 2     | 5        | ?     |
| Banana  | 1.5   | 4        | ?     |

**Solution:**
```excel
= B2 * C2
```

---

### 2. Use IF Function
| Score | Result |
|-------|--------|
| 85    | ?      |
| 60    | ?      |

**Condition:** If score ≥ 70, return "Pass", else "Fail"

**Solution:**
```excel
= IF(A2 >= 70, "Pass", "Fail")
```

---

### 3. VLOOKUP Example
| ID | Name   |
|----|--------|
| 1  | Alice  |
| 2  | Bob    |

**Lookup ID:**
```excel
= VLOOKUP(2, A2:B3, 2, FALSE)
```
**Returns:** Bob

---

### 4. Create a Pie Chart
Given sales data per region:
| Region | Sales |
|--------|-------|
| North  | 5000  |
| South  | 3000  |
| East   | 2000  |

**Instructions:**
1. Select the data.
2. Go to **Insert** > **Chart** > **Pie Chart**.
3. Add labels and title.

---

### 5. Pivot Table
| Date       | Product | Sales |
|------------|---------|-------|
| 2024-01-01 | Apple   | 100   |
| 2024-01-01 | Banana  | 80    |
| 2024-01-02 | Apple   | 120   |

**Goal:** Summarize total sales by product.

**Steps:**
1. Select the table.
2. Insert PivotTable.
3. Rows: Product
4. Values: Sum of Sales

---

