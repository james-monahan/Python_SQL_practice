/*Find the oldest survivor of each passenger class.
Output the name and the age of the survivor along with the corresponding passenger class.
Order records by passenger class in ascending order.*/

SELECT *
FROM
  (SELECT 
  pclass, name, age,
  MAX(age) OVER(PARTITION BY pclass) AS max_age
  FROM titanic
  WHERE survived = 1) t
WHERE pclass = pclass AND age = max_age
ORDER BY 1
