/*Find managers with at least 7 direct reporting employees.
Output first names of managers.*/

SELECT first_name 
FROM employee
WHERE id IN (select manager_id
from employee
GROUP BY manager_id
HAVING COUNT(*) >= 7)
AND employee_title = 'Manager'
