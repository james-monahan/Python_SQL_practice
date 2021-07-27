--Find the second highest salary of employees.

SELECT DISTINCT(salary)
FROM employee
ORDER BY salary DESC OFFSET 1
LIMIT 1
