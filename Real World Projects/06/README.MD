# 🚀 Interstellar Delivery: Mastering Datetime in Python

A hands-on Python project to explore and manipulate date and time using built-in `datetime` functionalities. This project demonstrates formatting timestamps, calculating future dates, and computing date differences—perfect for space-themed logistics or Earth-based delivery systems.

---

## 📦 Features

### 1. `format_date(timestamp, datetime_format)`

Formats a Unix timestamp into a human-readable datetime string.

* **Parameters:**

  * `timestamp` (*int*): A Unix timestamp.
  * `datetime_format` (*str*): Desired format using Python's datetime directives.
* **Returns:** A formatted datetime string.

**Example:**

```python
format_date(1514665153, "%d-%m-%Y")
# Output: "30-12-2017"
```

---

### 2. `calculate_landing_time(rocket_launch_dt, travel_duration)`

Estimates the Mars landing date based on launch time and travel duration.

* **Parameters:**

  * `rocket_launch_dt` (*datetime.datetime*): Launch datetime.
  * `travel_duration` (*int*): Number of travel days.
* **Returns:** Landing date as a string in `"DD-MM-YYYY"` format.

**Example:**

```python
calculate_landing_time(datetime(2023, 2, 15), 20)
# Output: "07-03-2023"
```

---

### 3. `days_until_delivery(expected_delivery_dt, current_dt)`

Calculates how many days remain until a package is delivered.

* **Parameters:**

  * `expected_delivery_dt` (*datetime.datetime*): Target delivery date.
  * `current_dt` (*datetime.datetime*): The current date.
* **Returns:** Number of days remaining as an integer.

**Example:**

```python
days_until_delivery(datetime(2023, 2, 15), datetime(2023, 2, 5))
# Output: 10
```
