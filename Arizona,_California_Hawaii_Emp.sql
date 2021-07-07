/*Find employees from Arizona, California, and Hawaii while making sure to output all employees from each city. 
Output column headers should be Arizona, California, and Hawaii.*/

WITH empys AS (SELECT
CASE WHEN city = 'Arizona' THEN first_name END ariz,
CASE WHEN city = 'California' THEN first_name END cali,
CASE WHEN city = 'Hawaii' THEN first_name END hawaii,
ROW_NUMBER() OVER(PARTITION BY city ORDER BY first_name) AS rn
FROM employee),

AZ AS (SELECT ariz, rn
FROM empys
WHERE ariz IS NOT NULL),

CA AS (SELECT cali, rn
FROM empys
WHERE cali IS NOT NULL),

HI AS (SELECT hawaii, rn
FROM empys
WHERE hawaii IS NOT NULL)

SELECT ariz, cali, hawaii
FROM HI
FULL JOIN AZ
ON HI.rn = AZ.rn
FULL JOIN CA
ON HI.rn = CA.rn
