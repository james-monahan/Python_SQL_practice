/*You're given a table that contains search results. If the 'position' column represents the position of the search results, 
write a query to calculate the percentage of search results that were in the top 3 position.*/

select COUNT(*)::FLOAT / 
(SELECT COUNT(*) from fb_search_results) * 100 AS percentage
from fb_search_results
WHERE position in (1,2,3);
