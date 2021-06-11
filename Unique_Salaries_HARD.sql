/*Find the top three unique salaries for each department. Output the department name and 
the top 3 unique salaries by each department. Order your results alphabetically by 
department and then by highest salary to lowest.*/

WITH inner_q AS
(select department, salary,
DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS ranking
from twitter_employee),
outer_q AS
(SELECT *
FROM inner_q
WHERE ranking IN (1,2,3))

SELECT department,salary
FROM outer_q
GROUP BY department,salary,ranking
ORDER BY 1 ASC, 2 DESC



