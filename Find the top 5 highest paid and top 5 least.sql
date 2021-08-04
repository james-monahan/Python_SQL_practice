/*Find the top 5 highest paid and top 5 least paid employees in 2012.
Output the employee name along with the corresponding total pay with benefits.
Sort records based on the total payment with benefits in ascending order.*/

SELECT *
FROM
  (SELECT employeename, totalpaybenefits
  FROM sf_public_salaries
  WHERE year = 2012
  ORDER BY 2
  LIMIT 5) t
UNION
SELECT *
FROM
  (SELECT employeename, totalpaybenefits
  FROM sf_public_salaries
  WHERE year = 2012
  ORDER BY 2 DESC
  LIMIT 5) j
ORDER BY 2
