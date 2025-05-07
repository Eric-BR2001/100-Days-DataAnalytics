# 📅 Power Query Text Preparation in Excel

Welcome to **Day 3** of the Excel Text Interpretation Challenge!  
Today, we're shifting focus from formulas to **Power Query**, Excel's powerful data transformation tool.

---

## 🎯 Goal of the Day

- Learn to clean and prepare text using **Power Query**
- Automate transformations such as trimming, casing, and punctuation removal
- Build a clean dataset ready for analysis

---

## 🧪 What You'll Work With

The `Day3_PowerQuery_TextPrep.xlsx` file includes:

| Raw Feedback                                  | Cleaned Feedback (Power Query Target) | Lowercase (Example) | Trimmed (Example) | Notes                                 |
|----------------------------------------------|---------------------------------------|----------------------|-------------------|----------------------------------------|
| delivery was LATE and packaging damaged      |                                       | `=LOWER(A2)`         | `=TRIM(A2)`       | Use PQ to remove punctuation           |
| excellent SERVICE, very fast response!       |                                       | ...                  | ...               |                                        |
| item lost, waiting for support...            |                                       | ...                  | ...               |                                        |
| not bad, but could be better                 |                                       | ...                  | ...               |                                        |
| horrible delay, I want a refund ASAP         |                                       | ...                  | ...               |                                        |
| Love the product! Perfect condition.         |                                       | ...                  | ...               |                                        |

---

## 🧰 Power Query Tasks

Use Power Query to apply the following steps:

1. **Trim whitespace**  
   `Transform > Format > Trim`

2. **Convert to lowercase**  
   `Transform > Format > Lowercase`

3. **Remove punctuation**  
   `Transform > Replace Values`  
   Replace characters like `.`, `,`, `!`, `?` with nothing (`""`)

4. **Remove extra spaces**  
   Use `Clean` or `Text.Replace(Text, "  ", " ")` in Power Query formula bar

---

## 🧼 Output Example

After cleaning, the feedback:

```text
"   delivery was LATE and packaging damaged   "
````

becomes:

```text
"delivery was late and packaging damaged"
```

