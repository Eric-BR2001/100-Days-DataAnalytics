# Ad Size and Type Data

## Overview
This dataset contains information on different ad sizes, ad types, and their corresponding differences in impressions.

## Dataset Columns
- `ad_size`: The size of the advertisement (e.g., 728x90, 300x250, etc.)
- `ad_type`: The type of advertisement (e.g., Inter217, Inter218, etc.)
- `difference`: The calculated difference in impressions

## Data Insights
This dataset can be used to analyze:
- The impact of different ad sizes on impression differences
- Trends in impression differences across different ad types
- Performance analysis of various ad formats

## Sample Data
| Ad Size | Ad Type  | Difference  |
|---------|---------|------------|
| 728x90  | Inter217  | 10475675   |
| 728x90  | Inter218  | 1582222    |
| 480x70  | Inter218  | 141470     |
| 480x70  | Inter219  | 2811644    |
| 480x70  | Inter220  | 248296     |

---

**Question:** What is the difference in impressions for each ad size and ad type in the dataset?

1. Retrieve the ad size, ad type, and the difference between available impressions and actual impressions:
   ```sql
   SELECT ad_size, ad_type, (available_impressions - impressions) AS difference 
   FROM clean_ads_data 
   LIMIT 50;
   ```
   
**Question:** How do the total available impressions vary across different weekdays?

2. Retrieve the total available impressions for specific weekdays:
   ```sql
   SELECT date_2, SUM(available_impressions) AS available_impressions 
   FROM clean_ads_data 
   WHERE date_2 IN ("Friday", "Thursday", "Monday", "Tuesday", "Wednesday") 
   GROUP BY date_2;
   ```

**Question:** How much difference exists between available impressions and actual impressions for each day?

3. Retrieve the difference between total available impressions and total impressions for each day:
   ```sql
   SELECT date_2, (SUM(available_impressions) - SUM(impressions)) AS available_impressions 
   FROM clean_ads_data 
   GROUP BY date_2;
   ```

**Question:** What is the impression difference for each day when filtering by working hours (10 AM to 5 PM)?

4. Retrieve the difference between available impressions and impressions for specific hours of the day (between 10 AM and 5 PM):
   ```sql
   SELECT date_2, (SUM(available_impressions) - SUM(impressions)) AS available_impressions 
   FROM clean_ads_data 
   WHERE hour_of_day BETWEEN 10 AND 17 
   GROUP BY date_2;
   ```

**Question:** Which ad size and ad type combination has the highest difference in impressions?

5. Retrieve the ad size and ad type combination has the highest difference in impressions
  ```sql
  SELECT ad_size, ad_type, MAX(available_impressions - impressions) AS max_difference 
  FROM clean_ads_data 
  GROUP BY ad_size, ad_type 
  ORDER BY max_difference DESC 
  LIMIT 1;
   ```

---