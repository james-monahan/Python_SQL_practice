/*What is the overall friend acceptance rate by date? 
Your output should have the rate of acceptances by 
the date the request was sent. Order by the earliest date to latest.

Assume that each friend request starts by a user sending 
(i.e., user_id_sender) a friend request to another user (i.e., user_id_receiver) 
that's logged in the table with action = 'sent'. If the request is accepted, 
the table logs action = 'accepted'. If the request is not accepted, no record of action = 'accepted' is logged.*/

WITH t1 AS
(select * from fb_friend_requests
WHERE action = 'sent'),

t2 AS
(select * from fb_friend_requests
WHERE action = 'accepted'),

t3 AS
(SELECT date, COUNT(*) AS accepted
FROM
(SELECT r.*
FROM t1 AS r
JOIN t2 as notr
ON r.user_id_sender=notr.user_id_sender
AND r.user_id_receiver=notr.user_id_receiver) z
GROUP BY date),

t4 AS 
(SELECT date, COUNT(*) AS day_total
FROM t1
GROUP BY date)

SELECT t4.date,  (accepted::FLOAT / day_total) AS percentage
FROM
t4
LEFT JOIN t3
ON t4.date=t3.date
ORDER BY 1

