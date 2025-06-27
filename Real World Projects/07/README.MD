# 🧑‍💼 Consolidating Employee Data

This project demonstrates how to use **pandas DataFrames** to consolidate, clean, and merge employee data from multiple sources into a single structured dataset.

## 📌 Objective

Transform four separate datasets into one final pandas DataFrame named `employees_final` with clean and standardized employee information.

---

## 🧩 Features

* ✅ Read multiple data sources into pandas DataFrames
* ✅ Merge employee details with emergency contact and office assignment data
* ✅ Clean and standardize the final dataset
* ✅ Assign office information based on employee location
* ✅ Fill missing office data with `"Remote"`

---

## 🗂️ Final Output: `employees_final`

* **Index**: `employee_id`
* **Columns** (in exact order):

  1. `employee_first_name`
  2. `employee_last_name`
  3. `employee_country`
  4. `employee_city`
  5. `employee_street`
  6. `employee_street_number`
  7. `emergency_contact`
  8. `emergency_contact_number`
  9. `relationship`
  10. `monthly_salary`
  11. `team`
  12. `title`
  13. `office`
  14. `office_country`
  15. `office_city`
  16. `office_street`
  17. `office_street_number`

