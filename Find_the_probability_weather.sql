/*Find the probability of ordering a ride based on the weather and the hour.
Output the weather, hour along with the corresponding probability.
Sort records by the weather and the hour in ascending order.*/

WITH counts AS
(SELECT weather, hour, COUNT(hour) AS counts
FROM lyft_rides
GROUP BY weather, hour
ORDER BY 1,2)

SELECT weather, hour,
counts::DECIMAL/SUM(counts) OVER () AS total_per_hour
FROM counts
ORDER BY 1,2
