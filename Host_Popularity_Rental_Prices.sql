/*You’re given a table of rental property searches by users. The table consists of search results and 
outputs host information for searchers. Find the minimum, average, maximum rental prices for each host’s 
popularity rating. The host’s popularity rating is defined as below:
    0 reviews: New
    1 to 5 reviews: Rising
    6 to 15 reviews: Trending Up
    16 to 40 reviews: Popular
    more than 40 reviews: Hot

Tip: The `id` column in the table refers to the search ID. You'll need to create your own host_id by concating price, 
room_type, host_since, zipcode, and number_of_reviews.*/


WITH base_table AS 
(SELECT DISTINCT(price||room_type||host_since||zipcode||number_of_reviews) AS id, 
price,
CASE
    WHEN number_of_reviews = 0 THEN 'New'
    WHEN number_of_reviews BETWEEN 1 AND 5 THEN 'Rising'
    WHEN number_of_reviews BETWEEN 6 AND 15 THEN 'Trending Up'
    WHEN number_of_reviews BETWEEN 16 AND 40 THEN 'Popular'
    ELSE 'Hot'
END AS pop_rating
FROM airbnb_host_searches)

SELECT pop_rating, MIN(price) min_p, AVG(price) avg_p, MAX(price) max_p
FROM base_table
GROUP BY pop_rating
