# 📊 Text Interpretation in Excel using Formulas

This project provides a collection of simple yet powerful **Excel formulas** designed to help users perform **basic text interpretation and analysis** directly within Excel — no VBA, Python, or external scripts required.

## 🔍 Features

- Word counting
- Keyword detection
- Sentiment analysis (basic)
- Text length classification
- Word frequency
- First word extraction

---

## 🧩 Included Formulas

### 1. **Word Count**
Counts the number of words in a cell.
```excel
=IF(LEN(A1)=0, 0, LEN(TRIM(A1)) - LEN(SUBSTITUTE(A1, " ", "")) + 1)
````

---

### 2. **Count Occurrences of a Word**

Counts how many times a specific word appears (case-insensitive).

```excel
=(LEN(A1)-LEN(SUBSTITUTE(LOWER(A1), "word", ""))) / LEN("word")
```

---

### 3. **Extract First Word**

Grabs the first word from a sentence.

```excel
=LEFT(A1, FIND(" ", A1 & " ") - 1)
```

---

### 4. **Basic Sentiment Detection**

Detects sentiment based on keyword presence.

```excel
=IF(SUM(COUNTIF(A1, {"*good*","*great*","*excellent*"}))>0,"Positive",
IF(SUM(COUNTIF(A1, {"*bad*","*terrible*","*awful*"}))>0,"Negative","Neutral"))
```

---

### 5. **Text Length Classification**

Classifies text as Short, Medium, or Long based on character length.

```excel
=IF(LEN(A1)<50,"Short",IF(LEN(A1)<150,"Medium","Long"))
```

---

### 6. **Keyword Presence (e.g., "urgent")**

Checks if the text contains a specific word.

```excel
=IF(ISNUMBER(SEARCH("urgent",A1)),"Contains 'urgent'","Does not contain")
```

---
