/*Find the average time (in seconds), per product, that needed to progress between steps. 
You can ignore products that were never used. Output the feature id and the average time.*/

WITH base_table AS (SELECT *, timestamp-lag AS seconds 
FROM
(SELECT *,
LAG(timestamp,1) OVER(PARTITION BY feature_id, user_id ORDER BY step_reached)
FROM facebook_product_features_realizations) t)

SELECT feature_id, AVG(base_seconds)
FROM
  (SELECT feature_id, AVG(seconds) base_seconds
  FROM base_table
  WHERE seconds IS NOT NULL
  GROUP BY feature_id, user_id) j
GROUP BY feature_id
