# 🌿 Sustainability Data Analysis Projects

Explore data-driven insights on sustainability through two projects:  
1. **EV Charging Behavior Analysis**  
2. **Industry Carbon Emissions Analysis**

---

## 🔌 Project 1: EV Charging Behavior Analysis

As electric vehicles (EVs) become more popular, apartment buildings are installing shared EV charging stations. With increased demand, building managers face a key question:  
**How can we optimize shared charging infrastructure to meet tenants’ needs?**

This project leverages data analysis and SQL on a PostgreSQL database to uncover charging habits and inform infrastructure planning.

<img src="charging_station.jpg" alt="EV Charging" width="500">

### 🧠 Objective

Analyze EV charging sessions to:
- Understand usage patterns
- Identify high-demand time slots
- Detect long-duration users
- Support decisions for scaling infrastructure

### 🗃️ Dataset Overview

Data is stored in a table called `charging_sessions` containing session logs.

#### Table: `charging_sessions`

| Column               | Description                                      | Data Type |
|----------------------|--------------------------------------------------|-----------|
| `garage_id`          | Unique ID for the garage                        | `VARCHAR` |
| `user_id`            | Unique ID for the user                          | `VARCHAR` |
| `user_type`          | Station type (`Shared` or `Private`)            | `VARCHAR` |
| `start_plugin`       | Start time of charging session                  | `DATETIME`|
| `start_plugin_hour`  | Hour the session started                        | `NUMERIC` |
| `end_plugout`        | End time of charging session                    | `DATETIME`|
| `end_plugout_hour`   | Hour the session ended                          | `NUMERIC` |
| `duration_hours`     | Duration of the session (hours)                 | `NUMERIC` |
| `el_kwh`             | Energy used (kWh)                               | `NUMERIC` |
| `month_plugin`       | Month the session started                       | `VARCHAR` |
| `weekdays_plugin`    | Weekday the session started                     | `VARCHAR` |

### 📊 Sample SQL Queries

#### 1. Unique Shared Station Users per Garage
```sql
SELECT garage_id, 
       COUNT(DISTINCT user_id) AS num_unique_users
FROM charging_sessions
WHERE user_type = 'Shared'
GROUP BY garage_id
ORDER BY num_unique_users DESC;
```

#### 2. Most Popular Charging Times (Shared)
```sql
SELECT weekdays_plugin,
       start_plugin_hour, 
       COUNT(*) AS num_charging_sessions
FROM charging_sessions
WHERE user_type = 'Shared'
GROUP BY weekdays_plugin, start_plugin_hour
ORDER BY num_charging_sessions DESC
LIMIT 10;
```

#### 3. Long Duration Shared Users
```sql
SELECT user_id, 
       AVG(duration_hours) as avg_charging_duration
FROM charging_sessions 
WHERE user_type = 'Shared' 
GROUP BY user_id
HAVING AVG(duration_hours) > 10
ORDER BY avg_charging_duration DESC;
```

### 📚 Sources
- Dataset: [Kaggle - Residential EV Charging](https://www.kaggle.com/datasets/anshtanwar/residential-ev-chargingfrom-apartment-buildings) [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)  
- Image: Julian Herzog, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Elektroauto_Lades%C3%A4ule_01.jpg) [CC BY 4.0](https://creativecommons.org/licenses/by/4.0)

---

## 🌍 Project 2: Industry Carbon Emissions Analysis

Product-related emissions—including manufacturing, transportation, and use—account for over **75% of global greenhouse gas emissions**. This project explores emissions at the product and industry level using SQL and a PostgreSQL database.

![Factories creating emissions](pollution.jpg)

### 🧠 Objective

- Analyze carbon footprints across products and industries  
- Identify high-emission sectors  
- Encourage data-driven sustainability practices

> _Source: [The Carbon Catalogue](https://www.nature.com/articles/s41597-022-01178-9)_

### 🗃️ Dataset Overview

Data is stored in the `product_emissions` table, detailing carbon metrics by product.

#### Table: `product_emissions`

| Column                          | Description                                      | Data Type |
|----------------------------------|--------------------------------------------------|-----------|
| `id`                             | Record ID                                       | `VARCHAR` |
| `year`                           | Reporting year                                  | `INT`     |
| `product_name`                   | Name of the product                             | `VARCHAR` |
| `company`                        | Reporting company                               | `VARCHAR` |
| `country`                        | Country of origin                               | `VARCHAR` |
| `industry_group`                 | Industry category                               | `VARCHAR` |
| `weight_kg`                      | Product weight (kg)                             | `NUMERIC` |
| `carbon_footprint_pcf`          | Total CO₂-equivalent emissions (PCF)            | `NUMERIC` |
| `upstream_percent_total_pcf`    | Upstream contribution to PCF (%)                | `VARCHAR` |
| `operations_percent_total_pcf`  | Operations contribution to PCF (%)              | `VARCHAR` |
| `downstream_percent_total_pcf`  | Downstream contribution to PCF (%)              | `VARCHAR` |

### 📊 Sample SQL Query

#### Total Emissions by Industry (Latest Year)
```sql
SELECT industry_group,
       COUNT(DISTINCT company) AS num_companies,
       ROUND(SUM(carbon_footprint_pcf), 1) AS total_industry_footprint
FROM product_emissions
WHERE year IN (SELECT MAX(year) FROM product_emissions)
GROUP BY industry_group
ORDER BY total_industry_footprint DESC;
```

---

## 🧭 Conclusion

These two analyses offer complementary insights into sustainability:
- **EV Charging Behavior** promotes smarter energy infrastructure in residential areas.
- **Product Carbon Emissions** helps identify industries that require focused sustainability efforts.

