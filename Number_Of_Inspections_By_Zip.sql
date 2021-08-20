--Find the number of inspections that happened in the municipality with postal code 94102 during January, May or November in each year.
--Output the count of each month separately.

WITH base AS (SELECT dt_year, dt_month, COUNT(*) counts
FROM
(SELECT business_postal_code, 
EXTRACT('year' FROM inspection_date) dt_year,
EXTRACT('month' FROM inspection_date) dt_month
FROM sf_restaurant_health_violations
WHERE EXTRACT('month' FROM inspection_date) IN (1, 5, 11)
AND business_postal_code = 94102) t
GROUP BY dt_year, dt_month)

SELECT dt_year,
MAX(CASE WHEN dt_month = 1 THEN counts ELSE 0 END) jan_counts,
MAX(CASE WHEN dt_month = 5 THEN counts ELSE 0 END) may_counts,
MAX(CASE WHEN dt_month = 11 THEN counts ELSE 0 END) nov_counts
FROM base
GROUP BY dt_year
