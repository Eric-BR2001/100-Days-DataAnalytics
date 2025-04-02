SELECT
    age_bucket,
    ROUND(
        SUM(CASE WHEN activity_type = 'send' THEN time_spent ELSE 0 END) * 100.0 / 
        SUM(time_spent), 
        2
    ) AS send_perc,
    ROUND(
        SUM(CASE WHEN activity_type = 'open' THEN time_spent ELSE 0 END) * 100.0 / 
        SUM(time_spent), 
        2
    ) AS open_perc
FROM activities
JOIN age_breakdown ON activities.user_id = age_breakdown.user_id
WHERE activity_type IN ('send', 'open')
GROUP BY age_bucket
ORDER BY age_bucket;