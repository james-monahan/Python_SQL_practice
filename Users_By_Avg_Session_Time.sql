/*Calculate each user's average session time. A session is defined as the 
time difference between a page_load and page_exit. For simplicity, assume 
an user has only 1 session per day and if there are multiple of the same 
events in that day, consider only the latest page_load and earliest page_exit. 
Output the user_id and their average session time.*/



WITH load AS (select user_id, 'page_load' AS action,
timestamp::DATE AS day, MAX(timestamp) AS time1 
from facebook_web_log
WHERE action IN ('page_load')
GROUP BY user_id, day),

exit AS (select user_id, 'page_exit' AS action,
timestamp::DATE AS day, MIN(timestamp) AS time2
from facebook_web_log
WHERE action IN ('page_exit')
GROUP BY user_id, day)

SELECT user_id, AVG(time_spent)
FROM
(SELECT l.user_id, l.day, time2-time1 AS time_spent 
FROM load AS l
JOIN exit AS e
ON l.user_id = e.user_id
AND l.day = e.day) t1
GROUP BY user_id
