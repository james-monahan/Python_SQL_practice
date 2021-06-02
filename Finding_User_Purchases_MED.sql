/*Write a query that'll identify returning active users. A returning active user is a user 
that has made a second purchase within 7 days of any other of their purchases. 
Output a list of user_ids of these returning active users.*/


WITH dd AS
(select at.*,
LAG(at.created_at) OVER(PARTITION BY user_id ORDER BY created_at)
from amazon_transactions at)

SELECT DISTINCT(user_id)
FROM
(SELECT *, created_at-lag AS is_active
from dd) t
WHERE is_active IS NOT NULL AND is_active <= 7

--alternate
select distinct(a.user_id)
from amazon_transactions a
inner join amazon_transactions b
on a.user_id = b.user_id
and a.id<> b.id
and b.created_at::date - a.created_at::date between 0 and 7
order by a.user_id

