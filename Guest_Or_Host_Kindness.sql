/*Find whether hosts or guests give higher review scores based on their 
average review scores. Output the higher of the average review score 
rounded to the 2nd decimal spot (e.g., 5.11).*/

SELECT from_type, maximum
FROM
(SELECT avg_review, from_type, MAX(avg_review) OVER() AS maximum
FROM
(select ROUND(AVG(review_score),2) AS avg_review, from_type
from airbnb_reviews
GROUP BY from_type) t) j
WHERE avg_review = maximum
