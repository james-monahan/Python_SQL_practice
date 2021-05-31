/*Find the date with the highest total energy consumption from the 
Facebook data centers. Output the date along with the total energy 
consumption across all data centers.*/

WITH q1 AS (select *
from fb_eu_energy
UNION ALL
SELECT *
FROM fb_asia_energy
UNION ALL
select *
from fb_na_energy),
q2 AS
(SELECT date, SUM(consumption) AS total_energy
FROM q1
GROUP BY 1)

SELECT date, total_energy
FROM
(SELECT *, 
RANK() OVER(ORDER BY total_energy DESC)
FROM q2) t
WHERE rank = 1
