# Employee Sales Data

## Overview
This dataset contains sales data for employees, including their unique ID, client names, revenue generated, total sales made, personal details, and management information.

## Table 1: Employee Sales Data

| Employee ID | Client Name        | Revenue (USD) | Sales |
|------------|------------------|--------------|-------|
| 1232122    | Page, Lisa       | 52,740.0     | 57    |
| 1232132    | Taylor, Hector   | 365,085.0    | 57    |
| 1232142    | Dawson, Jonathan | 235,350.0    | 32    |
| 1232152    | Duran, Brian     | 86,055.0     | 44    |
| 1232162    | Weber, Larry     | 447,840.0    | 38    |
| 1232172    | Pratt, Erik      | 195,540.0    | 84    |
| 1232182    | Oconnor, Kent    | 390,000.0    | 55    |
| 1232192    | Spencer, Boyd    | 288,540.0    | 50    |
| 1232202    | Wiggins, Frank   | 127,530.0    | 92    |
| 1232212    | Tanner, Timothy  | 308,610.0    | 38    |

## Table 2: Employee Personal Information

| Employee ID | First Name | Last Name  |
|------------|-----------|------------|
| 1232122    | Laila     | Friese     |
| 1232132    | Alden     | Puccio     |
| 1232142    | Dona      | Mccammon   |
| 1232152    | Leland    | Upton      |
| 1232162    | Ariane    | Belvin     |
| 1232172    | Regine    | Ellender   |
| 1232182    | Vincenza  | Petrus     |
| 1232192    | Maegan    | Sandusky   |
| 1232202    | Erma      | Vicini     |
| 1232212    | Laura     | Mcmakin    |

## Table 3: Employee Management Information

| Employee ID | State       | Manager             |
|------------|------------|---------------------|
| 1232122    | Alabama    | Rebbecca Tyree      |
| 1232132    | Alaska     | Sherron Gaumer     |
| 1232142    | Arizona    | Oralee Hilliker    |
| 1232152    | Arkansas   | Vita Tores         |
| 1232162    | California | Kate Dagenhart     |
| 1232172    | Colorado   | Inocencia Wiste    |
| 1232182    | Connecticut| Kassie Pertuit     |
| 1232192    | Delaware   | Winfred Yoon       |
| 1232202    | Florida    | Jerrell Baltazar   |
| 1232212    | Georgia    | Angelina Brakefield|

## SQL Queries and Questions

### 1. What is the average salary per employee status?
```sql
SELECT t1.status, AVG(t1.salary) 
FROM (SELECT ec.employee_id, ec.client, ec.revenue, ec.sales, en.first_name, en.last_name, es.salary, es.status, em.state 
      FROM employee_clients ec 
      JOIN employee_names en ON ec.employee_id = en.employee_id 
      JOIN employee_status es ON es.employee_id = ec.employee_id 
      JOIN employee_state_manager em ON em.employee_id = en.employee_id) t1 
GROUP BY t1.status;
```

### 2. How many employees are there in each state?
```sql
SELECT COUNT(t1.employee_id), t1.state 
FROM (SELECT ec.employee_id, ec.client, ec.revenue, ec.sales, en.first_name, en.last_name, es.salary, es.status, em.state 
      FROM employee_clients ec 
      JOIN employee_names en ON ec.employee_id = en.employee_id 
      JOIN employee_status es ON es.employee_id = ec.employee_id 
      JOIN employee_state_manager em ON em.employee_id = en.employee_id) t1 
GROUP BY t1.state;
```

### 3. What are the top 7 states with the highest total revenue?
```sql
SELECT t1.state, SUM(t1.revenue) 
FROM (SELECT ec.employee_id, ec.client, ec.revenue, ec.sales, en.first_name, en.last_name, es.salary, es.status, em.state 
      FROM employee_clients ec 
      JOIN employee_names en ON ec.employee_id = en.employee_id 
      JOIN employee_status es ON es.employee_id = ec.employee_id 
      JOIN employee_state_manager em ON em.employee_id = en.employee_id) t1 
GROUP BY t1.state 
ORDER BY SUM(t1.revenue) DESC 
LIMIT 7;
```

### 4. Which employees have revenue lower than their salary?
```sql
SELECT ec.employee_id, en.first_name, en.last_name, SUM(ec.revenue) - SUM(es.salary) AS difference_salary_revenue 
FROM employee_clients ec 
JOIN employee_names en ON ec.employee_id = en.employee_id 
JOIN employee_status es ON es.employee_id = en.employee_id 
JOIN employee_state_manager em ON em.employee_id = en.employee_id 
GROUP BY ec.employee_id, en.first_name, en.last_name 
HAVING SUM(ec.revenue) - SUM(es.salary) < 0;
```