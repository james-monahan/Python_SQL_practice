/*Write a query to calculate the distribution of comments by the count of users that joined 
Facebook between 2018 and 2020, for the month of January 2020. 

The output should contain a count of comments and the corresponding number of users that 
made that number of comments in Jan-2020. For example, you'll be counting how many users 
made 1 comment, 2 comments, 3 comments, 4 comments, etc in Jan-2020. Your left column in 
the output will be the number of comments while your right column in the output will be 
the number of users. Sort the output from the least number of comments to highest.

To add some complexity, there might be a bug where an user post is dated before the user join date. 
You'll want to remove these posts from the result.*/

WITH bt AS
(SELECT * 
FROM fb_comments fc
JOIN fb_users fu
ON fc.user_id = fu.id
AND fc.created_at > fu.joined_at
WHERE fu.joined_at >= '2018-01-01'
AND fu.joined_at < '2021-01-01'
AND fc.created_at::varchar LIKE '2020-01%'),

comment_counts AS
(SELECT user_id, COUNT(body) AS cc
FROM bt
GROUP BY user_id)

SELECT cc, COUNT(user_id) AS num_users
FROM comment_counts
GROUP BY cc
ORDER BY 1

--and date_trunc('month', fc.created_at) = '2020-01-01'::DATE 
