/*Find the top 3 wineries in each country based on the average points earned. 
Output the country along with the best, second best, and third best wineries. 
If there is no second winery (NULL value) output 'No second winery' and if there is no third winery output 'No third winery'.*/



WITH base_q AS (SELECT winery, country, AVG(points) AS avg_pnt
FROM winemag_p1
GROUP BY country, winery),

ranked AS (SELECT *,
ROW_NUMBER() OVER (PARTITION BY country ORDER BY avg_pnt DESC) AS ranking
FROM base_q),

bests AS
(SELECT country,
CASE WHEN ranking=1 THEN winery || ' (' || ROUND(avg_pnt) || ')' ELSE NULL END best,
CASE WHEN ranking=2 THEN winery || ' (' || ROUND(avg_pnt) || ')' ELSE NULL END second_best,
CASE WHEN ranking=3 THEN winery || ' (' || ROUND(avg_pnt) || ')' ELSE NULL END third_best
FROM ranked)


SELECT country, 
MAX(best) one, 
COALESCE(MAX(second_best),'No second winery') two, 
COALESCE(MAX(third_best),'No third winery') three
FROM bests
GROUP BY 1
ORDER BY 1
