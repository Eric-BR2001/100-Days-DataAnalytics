# 📅 Day 4 – Automated Categorization with Excel Formulas

In Day 4 of the Excel Text Interpretation Challenge, we’re going a step further by **automatically classifying cleaned feedback** into meaningful categories using Excel formulas.

---

## 🎯 Goal of the Day

- Use `SEARCH()` and `IF()` logic to assign feedback to a category.
- Classify issues like “Support Request,” “Delivery Issue,” and “Positive Feedback.”
- Build flexible, reusable formulas for automation.

---

## 🧪 Dataset Structure

The dataset contains:

| Cleaned Feedback                               | Category (Formula Applied)        |
|------------------------------------------------|-----------------------------------|
| delivery was late and packaging damaged        | Delivery Issue                    |
| excellent service very fast response           | Positive Feedback                 |
| item lost waiting for support                  | Support Request                   |
| not bad but could be better                    | Other                             |
| horrible delay i want a refund asap            | Support Request / Delivery Issue  |
| love the product perfect condition             | Positive Feedback                 |

---

## 🔧 Formula Logic (Example)

Here’s the logic behind the formula:

```excel
=IF(OR(ISNUMBER(SEARCH("refund", A2)), ISNUMBER(SEARCH("lost", A2))), "Support Request",
IF(OR(ISNUMBER(SEARCH("late", A2)), ISNUMBER(SEARCH("delay", A2))), "Delivery Issue",
IF(OR(ISNUMBER(SEARCH("excellent", A2)), ISNUMBER(SEARCH("love", A2))), "Positive Feedback", "Other")))
````

✅ **Flexible**
✅ **Scalable**
✅ **No Add-ins Required**

---

## 💡 Tips

* Expand the formula logic by adding more keywords.
* Use `IFERROR()` to catch and handle broken references or blanks.
* Consider using **Power Query** for more complex logic using custom columns.

---
