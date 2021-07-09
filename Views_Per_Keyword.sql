/* Create a report showing how many views each keyword has. 
Output the keyword and the total views, and order records with highest view count first.*/

WITH keywords AS (SELECT post_id, unnest(string_to_array(BTRIM(post_keywords, '[##]'), ',')) AS key_word
FROM facebook_posts),

views AS
(SELECT post_id, COUNT(viewer_id) AS viewers
FROM facebook_post_views
GROUP BY post_id)

SELECT key_word, COALESCE(SUM(viewers),0) AS total_views
FROM keywords k
LEFT JOIN views as v
ON k.post_id = v.post_id
GROUP BY key_word
ORDER BY 2 DESC


