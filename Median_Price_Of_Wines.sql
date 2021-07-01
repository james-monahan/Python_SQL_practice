--Find the median price for each wine variety across both datasets. 
--Output distinct varieties along with the corresponding median price.

WITH all_wines AS
(SELECT id, price, variety 
FROM winemag_p1
UNION ALL
SELECT id, price, variety 
FROM winemag_p2)

SELECT DISTINCT(variety), 
PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) AS median
FROM all_wines
GROUP BY variety



