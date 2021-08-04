/*Find the median total pay for each job. 
Output the job title and the corresponding total pay, 
and sort the results from highest total pay to lowest.*/

SELECT jobtitle,
PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY totalpay) AS median
FROM sf_public_salaries
GROUP BY jobtitle
ORDER BY 2 DESC;
