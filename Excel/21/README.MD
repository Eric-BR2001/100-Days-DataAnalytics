# Advanced Text Interpretation in Excel

Welcome to **Day 2** of our Excel Text Analysis series!  
Today, we dive deeper into **text interpretation** using more refined and practical **Excel formulas**, including multiple keyword detection, text scoring, and priority tagging.

---

## 🎯 Goal of the Day

- Improve basic text analysis techniques from Day 1
- Introduce scoring logic to rank text entries
- Create automated labels like "High Priority" or "Low Sentiment"

---

## 🧩 Featured Formulas

### 1. **Score Text Based on Keywords**
Assigns a score by counting positive and negative words.

```excel
=SUM(COUNTIF(A1, {"*good*","*great*","*excellent*"})) - 
SUM(COUNTIF(A1, {"*bad*","*poor*","*terrible*"}))
````

> 🔍 *Result can be positive, negative, or zero to indicate overall tone.*

---

### 2. **Multi-Keyword Tagging**

Tags text with multiple relevant categories.

```excel
=TEXTJOIN(", ", TRUE, IF(ISNUMBER(SEARCH("delay",A1)), "Delayed", ""),
IF(ISNUMBER(SEARCH("refund",A1)), "Refund Request", ""),
IF(ISNUMBER(SEARCH("broken",A1)), "Product Issue", ""))
```

> 🏷️ *Returns tags like "Delayed, Refund Request".*

---

### 3. **Highlight Urgent Entries**

Marks cells as urgent if they contain critical keywords.

```excel
=IF(SUM(COUNTIF(A1, {"*urgent*","*asap*","*immediately*"}))>0, "🚨 Urgent", "—")
```

---

### 4. **Auto Sentiment Classification (Improved)**

Uses scores to classify text as Positive, Neutral, or Negative.

```excel
=IF(SUM(COUNTIF(A1, {"*good*","*great*","*excellent*"})) > 
SUM(COUNTIF(A1, {"*bad*","*poor*","*terrible*"})),"Positive",
IF(SUM(COUNTIF(A1, {"*good*","*great*","*excellent*"})) =
SUM(COUNTIF(A1, {"*bad*","*poor*","*terrible*"})),"Neutral","Negative"))
```

---

## 🧪 Challenge Task

Build an Excel sheet that:

* Accepts customer feedback
* Applies the above formulas to tag, score, and classify each entry
* Sorts or filters entries based on urgency or negative sentiment

---

## 📈 Bonus Idea

Use **Conditional Formatting** to color-code rows based on sentiment or urgency score.
For example, turn cells **red** when sentiment is "Negative" and "Urgent".

---

## 📁 Output Example

| Feedback                          | Sentiment | Tags                   | Urgent    |
| --------------------------------- | --------- | ---------------------- | --------- |
| "The item was broken and delayed" | Negative  | Product Issue, Delayed | —         |
| "Please refund me immediately!"   | Negative  | Refund Request         | 🚨 Urgent |
| "Great quality, thank you!"       | Positive  |                        | —         |

