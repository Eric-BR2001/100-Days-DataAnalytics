# Employee Salaries Data - San Francisco (2011)

## Overview
This dataset contains information on employee salaries in San Francisco for the year 2011. It includes details about employees' names, job titles, base pay, overtime pay, other earnings, total pay, and total pay including benefits.

## Dataset Columns
- `id`: Unique identifier for each employee record
- `employeename`: Name of the employee
- `jobtitle`: Employee's job title
- `basepay`: Base salary of the employee
- `overtimepay`: Overtime pay received
- `otherpay`: Other additional earnings
- `benefits`: Benefits received (data may be missing for some employees)
- `totalpay`: Sum of base pay, overtime pay, and other pay
- `totalpaybenefits`: Total pay including benefits
- `year`: The year of the record (2011)
- `notes`: Additional notes (if any)
- `agency`: The agency or department where the employee works (San Francisco)
- `status`: Employment status (data not provided in the dataset)

## Data Insights
This dataset can be used to analyze:
- Salary distribution across different job roles
- The impact of overtime on total earnings
- Differences in total pay with and without benefits
- Identification of the highest-paid employees and their job roles

## Sample Data
| ID | Employee Name | Job Title | Base Pay | Overtime Pay | Other Pay | Total Pay | Total Pay & Benefits | Year | Agency |
|----|--------------|-----------|----------|--------------|-----------|-----------|---------------------|------|---------|
| 1  | Nathaniel Ford | General Manager-Metropolitan Transit Authority | 167411.18 | 0.0 | 400184.25 | 567595.43 | 567595.43 | 2011 | San Francisco |
| 2  | Gary Jimenez  | Captain III (Police Department) | 155966.02 | 245131.88 | 137811.38 | 538909.28 | 538909.28 | 2011 | San Francisco |
| 3  | Albert Pardini | Captain III (Police Department) | 212739.13 | 106088.18 | 16452.6 | 335279.91 | 335279.91 | 2011 | San Francisco |



## Queries
Below are some aggregation exercises that can be performed using the `san_francisco_salaries` table:

1. A table with the average (`AVG`) `totalpay` by `jobtitle`:
   ```sql
   SELECT jobtitle, ROUND(AVG(totalpay), 2) 
   FROM san_francisco_salaries 
   GROUP BY jobtitle;
   ```

2. A table with the sum of `totalpay` grouped by `jobtitle`:
   ```sql
   SELECT jobtitle, ROUND(SUM(totalpay), 2) AS SUM 
   FROM san_francisco_salaries 
   GROUP BY jobtitle;
   ```

3. A table showing the maximum (`MAX`) and minimum (`MIN`) salary (`totalpay`) with the corresponding employee name (`employeename`):
   ```sql
   SELECT employeename, MAX(totalpay), MIN(totalpay) 
   FROM san_francisco_salaries 
   GROUP BY jobtitle;
   ```

4. A table with the maximum (`MAX`) and minimum (`MIN`) `totalpay` grouped by `jobtitle`:
   ```sql
   SELECT jobtitle, MAX(totalpay), MIN(totalpay) 
   FROM san_francisco_salaries 
   GROUP BY jobtitle;
   ```

5. A table with the average (`AVG`) of `totalpaybenefits` per year (`year`), formatted as `year - avg_value`:
   ```sql
   SELECT year, CONCAT(year, ' - ', AVG(totalpaybenefits)) 
   FROM san_francisco_salaries 
   GROUP BY year;
   ```

6. A table with the number of employees (`id`) per `jobtitle`:
   ```sql
   SELECT COUNT(id), jobtitle 
   FROM san_francisco_salaries 
   GROUP BY jobtitle;
   ```

7. A table displaying all salary details with properly cast data types:
   ```sql
   SELECT id, employeename, jobtitle, 
          CAST(basepay AS DECIMAL), 
          CAST(overtimepay AS DECIMAL), 
          CAST(otherpay AS DECIMAL), 
          benefits, totalpay, totalpaybenefits, year, 
          notes, agency, status 
   FROM san_francisco_salaries;
   ```

