/*Make a pivot table to find the highest payment in each year for each employee.
Find payment details for 2011, 2012, 2013, and 2014. 
Output payment details along with the corresponding employee name.
Order records by the employee name in ascending order*/

WITH bt AS
(select employeename, year, MAX(totalpay) AS pay
from sf_public_salaries
GROUP BY year, employeename),

years AS
(SELECT employeename,
CASE WHEN year = 2011 THEN pay ELSE 0 END AS pay_2011,
CASE WHEN year = 2012 THEN pay ELSE 0 END AS pay_2012,
CASE WHEN year = 2013 THEN pay ELSE 0 END AS pay_2013,
CASE WHEN year = 2014 THEN pay ELSE 0 END AS pay_2014
FROM bt
ORDER BY 1)

SELECT employeename, MAX(pay_2011) _2011, MAX(pay_2012) _2012, 
MAX(pay_2013) _2013, MAX(pay_2014) _2014
FROM years
GROUP BY employeename


