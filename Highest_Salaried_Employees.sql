/*Find the employee with the highest salary in each department.
Output the department name, employee's first name, and the salary.*/

SELECT department, first_name, salary
FROM
(SELECT department, first_name, salary,
RANK() OVER(PARTITION BY department ORDER BY salary DESC) ranking
FROM worker) t
WHERE ranking = 1
