# 📊 Factors that Fuel Student Performance

Welcome to the **Student Performance Analysis** project! This project uses SQL to explore how various factors like study hours, extracurricular activities, sleep, and tutoring sessions influence students' academic success. You'll write and run SQL queries against a database of student data to uncover actionable insights.

## 🗂️ Project Overview

You'll answer the following questions using SQL:

1. **Do more study hours and extracurricular activities lead to better scores?**
2. **Is there a sweet spot for study hours that maximizes exam performance?**
3. **How can we rank students by performance without showing exact scores?**

---

## 📌 Objectives & Queries

### 1. Study Hours & Extracurricular Activities

**Goal:** Determine if studying more than 10 hours per week while participating in extracurricular activities improves exam performance.

**Query Requirements:**

* Columns: `hours_studied`, `avg_exam_score`
* Filters: `hours_studied > 10` and `participates_in_extracurriculars = TRUE`
* Grouped and ordered by `hours_studied DESC`
* **Save as:** `avg_exam_score_by_study_and_extracurricular`

---

### 2. Optimal Study Range

**Goal:** Identify which range of study hours results in the highest average exam scores.

**Study Hour Ranges:**

* 1–5 hours
* 6–10 hours
* 11–15 hours
* 16+ hours

**Query Requirements:**

* Columns: `hours_studied_range`, `avg_exam_score`
* Grouped by `hours_studied_range`
* Ordered by `avg_exam_score DESC`
* **Save as:** `avg_exam_score_by_hours_studied_range`

---

### 3. Anonymous Student Rankings

**Goal:** Rank students by exam score using window functions, keeping individual scores private.

**Query Requirements:**

* Columns: `attendance`, `hours_studied`, `sleep_hours`, `tutoring_sessions`, `exam_rank`
* Use a window function to rank by `exam_score`
* Tie scores get the same rank (no skipped ranks)
* Ordered by `exam_rank ASC`
* Limit to **30 students**
* **Save as:** `student_exam_rankings`