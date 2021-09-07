/*Find the connection between the number of letters in the athlete's first 
name and the number of medals won for each type for medal, including no medals. 
Output the length of the name along with the corresponding number of no medals, 
bronze medals, silver medals, and gold medals.*/

SELECT name_length, 
SUM(no_medal) non, SUM(bronzes) bro,
SUM(silvers) sil, SUM(golds) gol
FROM
(SELECT
LENGTH(SPLIT_PART(name, ' ', 1)) AS name_length,
CASE WHEN medal = 'Gold' THEN 1 ELSE 0 END AS golds,
CASE WHEN medal = 'Silver' THEN 1 ELSE 0 END AS silvers,
CASE WHEN medal = 'Bronze' THEN 1 ELSE 0 END AS bronzes,
CASE WHEN medal IS NULL THEN 1 ELSE 0 END AS no_medal
FROM olympics_athletes_events) t
GROUP BY name_length
