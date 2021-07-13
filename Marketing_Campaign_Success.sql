/*You have a table of in-app purchases by user. Users that make their first in-app purchase 
are placed in a marketing campaign where they see call-to-actions for more in-app purchases. 
Find the number of users that made additional in-app purchases due to the success of the marketing campaign.

The marketing campaign doesn't start until one day after the initial in-app purchase so users that 
make multiple purchases on the same day do not count, nor do we count users that make only the same purchases over time.*/

SELECT COUNT(DISTINCT(user_id)) FROM
(SELECT *,
RANK() OVER(PARTITION BY user_id ORDER BY created_at)
FROM
(SELECT user_id, MIN(created_at) AS created_at, product_id 
FROM marketing_campaign
GROUP BY user_id, product_id) t) j
WHERE rank >= 2
