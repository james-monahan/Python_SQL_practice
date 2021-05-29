# We have a table with employees and their salaries, however, 
# some of the records are old and contain outdated salary information. 
# Find the current salary of each employee assuming that salaries increase each year. 
# Output their id, first name, last name, department ID, and current salary. 
# Order your list by employee ID in ascending order.

import pandas as pd
cols = [ 'id', 'first_name', 'last_name', 'department_id']
ms_employee_salary.groupby(cols, as_index=False)['salary'].max()\
.sort_values('id')
