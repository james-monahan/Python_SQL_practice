--Find the highest salary among salaries that appears only once.

WITH salary_counts AS
(SELECT *,
COUNT(*) OVER(PARTITION BY salary) AS s_counts
FROM employee)

SELECT MAX(salary)
FROM salary_counts
WHERE s_counts = 1

--alt select max(distinct(Salary)) from employee
