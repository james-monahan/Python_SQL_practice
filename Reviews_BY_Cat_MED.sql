Find the top business categories based on the total number of reviews. 
Output the category along with the total number of reviews. 
Order by total reviews in descending order.

--total num reviews by cat (array)
--out: cat, num rev
--order: desc by num

select  
unnest(string_to_array(categories, ';')) AS category,
SUM(review_count)
from yelp_business
GROUP BY category
ORDER BY 2 DESC;
