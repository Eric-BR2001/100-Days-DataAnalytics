SELECT ad_size, ad_type, (available_impressions - impressions) AS difference FROM clean_ads_data LIMIT 50;
SELECT ad_size, ad_type, MAX(available_impressions - impressions) AS max_difference FROM clean_ads_data GROUP BY ad_size, ad_type ORDER BY max_difference DESC LIMIT 1;
select date_2,SUM(available_impressions) as available_impressions from clean_ads_data where date_2 IN("Friday","Thursday","Monday","Tuesday","Wednesday") group by date_2;
select date_2,(SUM(available_impressions)-SUM(impressions)) as available_impressions from clean_ads_data group by date_2;
select date_2,(SUM(available_impressions)-SUM(impressions)) as available_impressions from clean_ads_data where hour_of_day BETWEEN 10 AND 17 group by date_2;