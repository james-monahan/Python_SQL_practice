Write a query that identifies cities with higher than average home prices when compared to the national average. Output the city names.

--national avg
--city averages
--output city names

SELECT city 
FROM
(select *,
AVG(mkt_price) OVER () AS nat_avg
from zillow_transactions) t
GROUP BY city
HAVING AVG(mkt_price) > AVG(nat_avg)
