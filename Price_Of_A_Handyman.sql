/*Find the price that a small handyman business is willing to pay per employee. 
Get the result based on the mode of the adword earnings per employee distribution. 
Small businesses are considered to have not more than ten employees.*/

SELECT earn_per_dist
FROM
  (SELECT *,
    COUNT(*) OVER(PARTITION BY earn_per_dist)
    FROM
    (SELECT business_type, adwords_earnings / n_employees AS earn_per_dist
    FROM google_adwords_earnings
    WHERE business_type = 'handyman' 
    AND n_employees <= 10) t
  ORDER BY 3 DESC, 2 DESC
  LIMIT 1) j

