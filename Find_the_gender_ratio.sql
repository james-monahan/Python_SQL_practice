/*Find the gender ratio between the number of men and women who participated in each Olympics.
Output the Olympics name along with the corresponding number of men, women, and the gender ratio.
Order records by the gender ratio in ascending order.*/

SELECT games, MAX(men) total_m, MAX(female) total_f,
MAX(men)::DECIMAL/(MAX(female)+1) ratio
FROM
  (SELECT games,
  CASE WHEN sex = 'M' THEN num ELSE 0 END as men,
  CASE WHEN sex = 'F' THEN num ELSE 0 END as female
  FROM
    (SELECT DISTINCT(games), sex, COUNT(sex) OVER(PARTITION BY games, sex) num
    FROM olympics_athletes_events
    ORDER BY 1) t) j
GROUP BY games
ORDER BY 4
