/*Find how the number of `likes` are increasing by building a `like` score based on `like` propensities. 
A `like` propensity is defined as the probability of giving a like amongst all reactions, per friend 
(i.e., number of likes / number of all reactions).
Output the total propensity alongside the corresponding date and poster. 
Sort the result based on the liking score in descending order.
In `facebook_reactions` table `poster` is user who posted a content, `friend` is a user who saw the content and reacted. 
The `facebook_friends` table stores pairs of connected friends.*/

WITH liked_percent AS 
(SELECT friend, (SUM(c_reaction)::DECIMAL / COUNT(*)) AS percent_liked
FROM
(SELECT *,
(CASE WHEN reaction = 'like' THEN 1 ELSE 0 END) AS c_reaction
FROM facebook_reactions) t
GROUP BY friend)

SELECT date_day, poster, AVG(percent_liked)
FROM facebook_reactions fr
JOIN liked_percent lp
ON fr.friend = lp.friend
WHERE reaction = 'like'
GROUP BY poster, date_day
ORDER BY 3 DESC

