/*Rank each host based on the number of beds they have listed. The host 
with the most beds should be ranked 1 and the host with the least number 
of beds should be ranked last. Hosts that have the same number of beds 
should have the same rank. A host can also own multiple properties. 
Output the host ID, number of beds, and rank from highest rank to lowest.*/

SELECT *,
DENSE_RANK() OVER(ORDER BY total_beds DESC)
FROM
(SELECT host_id, SUM(n_beds) AS total_beds
FROM airbnb_apartments
GROUP BY host_id
ORDER BY 2) t
