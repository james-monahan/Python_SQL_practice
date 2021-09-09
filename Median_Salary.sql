/*Find the median employee salary of each department.
Output the department name along with the corresponding salary rounded to the nearest whole dollar.*/

SELECT department,
PERCENTILE_CONT(.5) WITHIN GROUP (ORDER BY salary)
FROM employee
GROUP BY department
