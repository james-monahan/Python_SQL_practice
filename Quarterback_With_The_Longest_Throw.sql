/*Find the quarterback who threw the longest throw in 2016. 
Output the quarterback name along with their corresponding longest throw. 

The 'lg' column contains the longest completion by the quarterback.*/

SELECT qb, REGEXP_REPLACE(lg, '[[:alpha:]]','')::INT AS lg_int
FROM qbstats_1996_2016
WHERE year = 2016
ORDER BY 2 DESC
LIMIT 1
