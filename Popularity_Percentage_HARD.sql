/*Find the popularity percentage for each user on Facebook. The popularity 
percentage is defined as the total number of friends the user has divided 
by the total number of users on the platform, then converted into a 
percentage by multiplying by 100. Output each user along with their 
popularity percentage. Order records in ascending order by user id.
The 'user1' and 'user2' column are pairs of friends.*/

WITH table2 AS
(select user2 AS user1, user1 AS user2
from facebook_friends),

combined_table AS
(SELECT *
FROM facebook_friends
UNION 
SELECT *
FROM table2)

SELECT user1, 
(COUNT(user2)::DECIMAL / (SELECT COUNT(DISTINCT(user1)) FROM combined_table))*100 AS pop_percentage
FROM
combined_table
GROUP BY user1
ORDER BY 1
