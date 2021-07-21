/*Find the most profitable location. Write a query that calculates the average 
signup duration and average revenue for each location, and then compare these 
two measures together by taking the ratio of the average revenue and average 
duration for each location. 

Your output should include the location, average duration, average revenue, and ratio. 
Sort your results from highest ratio to lowest.*/

WITH avg_locations AS 
(SELECT location, AVG(signup_stop_date - signup_start_date) avg_duration
FROM signups
GROUP BY location),

avg_amounts AS
(SELECT s.location, AVG(t.amt) AS avg_amt
FROM signups s
JOIN transactions t
ON s.signup_id = t.signup_id
GROUP BY s.location)

SELECT aa.location, al.avg_duration, aa.avg_amt, 
aa.avg_amt/al.avg_duration AS ratio
FROM avg_amounts aa
JOIN avg_locations al
ON aa.location = al.location
ORDER BY 4 DESC
