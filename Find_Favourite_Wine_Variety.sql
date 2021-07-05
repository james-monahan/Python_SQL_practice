/*Find each taster's favorite wine variety. 
Consider that favorite variety means the variety that has been tasted by most of the time.
Output the taster's name along with the wine variety.*/

WITH counts AS 
(SELECT taster_name, variety, COUNT(variety) AS num_reviews 
FROM winemag_p2
GROUP BY taster_name, variety),

rankings AS
(SELECT taster_name, variety, num_reviews, 
RANK() OVER(PARTITION BY taster_name ORDER BY num_reviews DESC)
FROM counts)

SELECT taster_name, variety
from rankings
WHERE rank = 1 and taster_name != ''

